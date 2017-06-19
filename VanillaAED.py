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

__author__ = "Pau Riba, Anjan Dutta"
__email__ = "priba@cvc.uab.cat, adutta@cvc.uab.cat"


class VanillaAED(AproximatedEditDistance):

    def __init__(self, del_cost = 0.25, ins_cost = 0.5, metric = "euclidean"):
        self.del_cost = del_cost
        self.ins_cost = ins_cost
        self.metric = metric

    def substitution(self, values1, values2):
        v1 = [list(chain.from_iterable(l.values())) for l in values1]
        v2 = [list(chain.from_iterable(l.values())) for l in values2]

        dist = cdist(np.array(v1), np.array(v2), metric=self.metric)

        return dist

    def insertion(self, values):
        return [self.ins_cost]*len(values)

    def deletion(self, values):
        return [self.del_cost] * len(values)

if __name__ == '__main__':

    path_dataset = '../graph_db/dataset/'
    name_dataset = 'Letters'
    set = 'train'

    aed = VanillaAED()

    path_dataset = os.path.join(path_dataset, name_dataset)
    path_dataset = os.path.join(path_dataset, set)
    files = glob.glob(path_dataset + '/*.gml')
    for f1, f2 in itertools.combinations_with_replacement(files, 2):
        # Read graphs
        g1 = nx.read_gml(f1)
        g2 = nx.read_gml(f2)

        # Distance
        dist, assignment = aed.ged(g1, g2)

        print g1.graph['class'] + ' <-> ' + g2.graph['class'] + ' | Distance: ' + str(dist)

