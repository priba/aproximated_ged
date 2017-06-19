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

    def edge_cost_matrix(self, g1, g2):
        cost_matrix = np.zeros([len(g1)+len(g2),len(g1)+len(g2)])

        # Insertion
        cost_matrix[len(g1):, 0:len(g2)] = np.inf
        np.fill_diagonal(cost_matrix[len(g1):, 0:len(g2)], self.edge_insertion(g1.values()))

        # Deletion
        cost_matrix[0:len(g1), len(g2):] = np.inf
        np.fill_diagonal(cost_matrix[0:len(g1), len(g2):], self.edge_deletion(g2.values()))

        # Substitution
        cost_matrix[0:len(g1), 0:len(g2)] = self.edge_substitution(g1.values(), g2.values())

        return cost_matrix

    def edge_ed(self, g1, g2):

        # Compute cost matrix
        cost_matrix = self.edge_cost_matrix(g1, g2)

        # Munkres algorithm
        row_ind, col_ind = linear_sum_assignment(cost_matrix)

        # Graph edit distance
        dist = cost_matrix[row_ind, col_ind].sum()

        return dist

    def cost_matrix(self, g1, g2):
        cost_matrix = np.zeros([len(g1)+len(g2),len(g1)+len(g2)])

        # Insertion
        cost_matrix[len(g1):, 0:len(g2)] = np.inf
        np.fill_diagonal(cost_matrix[len(g1):, 0:len(g2)], self.node_insertion(g1))

        # Deletion
        cost_matrix[0:len(g1), len(g2):] = np.inf
        np.fill_diagonal(cost_matrix[0:len(g1), len(g2):], self.node_deletion(g2))

        # Substitution
        cost_matrix[0:len(g1), 0:len(g2)] = self.node_substitution(g1, g2)

        return cost_matrix

    def ged(self, g1, g2):

        # Compute cost matrix
        cost_matrix = self.cost_matrix(g1, g2)

        # Munkres algorithm
        row_ind, col_ind = linear_sum_assignment(cost_matrix)

        # Graph edit distance
        dist = cost_matrix[row_ind, col_ind].sum()

        return dist, (row_ind, col_ind)
