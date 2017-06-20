#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    VanillaAED.py
    Riesen, Kaspar, and Horst Bunke. "Approximate graph edit distance computation by means of bipartite graph matching."
    Image and Vision computing 27.7 (2009): 950-959.
"""

from AproximatedEditDistance import AproximatedEditDistance

import os
import glob
import itertools

from itertools import chain
from scipy.spatial.distance import cdist
import numpy as np
import networkx as nx

from Plotter import plot_assignment

__author__ = "Pau Riba, Anjan Dutta"
__email__ = "priba@cvc.uab.cat, adutta@cvc.uab.cat"


class VanillaAED(AproximatedEditDistance):

    def __init__(self, del_node = 0.25, ins_node = 0.5, del_edge = 0.1, ins_edge = 0.1, metric = "euclidean"):
        self.del_node = del_node
        self.ins_node = ins_node
        self.del_edge = del_edge
        self.ins_edge = ins_edge

        self.metric = metric

    def node_substitution(self, g1, g2):
        values1 = [v for k, v in g1.nodes(data=True)]
        v1 = [list(chain.from_iterable(l.values())) for l in values1]

        values2 = [v for k, v in g2.nodes(data=True)]
        v2 = [list(chain.from_iterable(l.values())) for l in values2]

        node_dist = cdist(np.array(v1), np.array(v2), metric=self.metric)

        i1 = 0
        for k1 in g1.nodes():
            i2=0
            for k2 in g2.nodes():

                node_dist[i1,i2] += self.edge_ed(g1[k1], g2[k2])
                i2 += 1
            i1 += 1

        return node_dist

    def node_insertion(self, g):
        values = [v for k, v in g.nodes(data=True)]
        return [self.ins_node]*len(values) + self.edge_insertion(g.edge.values())

    def node_deletion(self, g):
        values = [v for k, v in g.nodes(data=True)]
        return [self.del_node] * len(values) + self.edge_deletion(g.edge.values())

    def edge_substitution(self, g1, g2):
        edge_dist = cdist(np.array([l.values() for l in g1]), np.array([l.values() for l in g2]), metric=self.metric)
        return edge_dist

    def edge_insertion(self, g):
        insert_edges = [len(e) for e in g]
        return np.array([self.ins_edge] * len(insert_edges)) * insert_edges

    def edge_deletion(self, g):
        delete_edges = [len(e) for e in g]
        return np.array([self.del_edge] * len(delete_edges)) * delete_edges

if __name__ == '__main__':

    path_dataset = './data/'
    name_dataset = 'Letters'

    aed = VanillaAED()

    path_dataset = os.path.join(path_dataset, name_dataset)
    files = glob.glob(path_dataset + '/*.gml')
    for f1, f2 in itertools.combinations_with_replacement(files, 2):
        # Read graphs
        g1 = nx.read_gml(f1)
        g2 = nx.read_gml(f2)

        # Distance
        dist, assignment = aed.ged(g1, g2)

        plot_assignment(g1, g2, assignment)
        print g1.graph['class'] + ' <-> ' + g2.graph['class'] + ' | Distance: ' + str(dist)
