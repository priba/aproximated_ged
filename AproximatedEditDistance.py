#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    AproximatedEditDistance.py
    Riesen, Kaspar, and Horst Bunke. "Approximate graph edit distance computation by means of bipartite graph matching."
    Image and Vision computing 27.7 (2009): 950-959.
"""

from GraphEditDistance import GraphEditDistance

import os
import glob
import itertools

from scipy.optimize import linear_sum_assignment
import networkx as nx
import numpy as np

__author__ = "Pau Riba, Anjan Dutta"
__email__ = "priba@cvc.uab.cat, adutta@cvc.uab.cat"


class AproximatedEditDistance(GraphEditDistance):

    def __init__(self):
        super(GraphEditDistance, self).__init__()

    def __substitution(self):
        pass

    def __insertion(self):
        pass

    def __deletion(self):
        pass

    def __cost_matrix__(self, g1, g2):
        cost_matrix = np.zeros([len(g1)+len(g2),len(g1)+len(g2)])

        # Insertion
        cost_matrix[len(g1):, 0:len(g2)] = np.inf

        # Deletion
        cost_matrix[0:len(g1), len(g2):] = np.inf

        return cost_matrix

    def ged(self, g1, g2):
        # Compute cost matrix
        cost_matrix = self.__cost_matrix__(g1,g2)

        # Munkres algorithm
        row_ind, col_ind = linear_sum_assignment(cost_matrix)

        # Graph edit distance
        dist = cost_matrix[row_ind, col_ind].sum()

        return dist, (row_ind, col_ind)

if __name__ == '__main__':

    path_dataset = '../graph_db/dataset/'
    name_dataset = 'Letters'
    set = 'train'

    aed = AproximatedEditDistance()

    path_dataset = os.path.join(path_dataset, name_dataset)
    path_dataset = os.path.join(path_dataset, set)
    files = glob.glob(path_dataset + '/*.gml')
    for f1, f2 in itertools.combinations_with_replacement(files, 2):
        # Read graphs
        g1 = nx.read_gml(f1)
        g2 = nx.read_gml(f2)

        # Distance
        dist, assignment = aed.ged(g1, g2)

        print g1.graph['class'] + ' <-> ' + g2.graph['class'] + ' Distance ' + dist

