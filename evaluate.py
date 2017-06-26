#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    evaluate.py

    Computes the distance between .
"""

from VanillaAED import VanillaAED
from VanillaHED import VanillaHED

import glob
from sklearn.metrics import average_precision_score

import networkx as nx
import numpy as np
from scipy import stats

import argparse

__author__ = "Pau Riba, Anjan Dutta"
__email__ = "priba@cvc.uab.cat, adutta@cvc.uab.cat"

# Argument parser
parser = argparse.ArgumentParser(description='Computes the distance all vs all between two folders.')

# Prototypes
parser.add_argument('--folder1', help='Input graphs.', default='./data/Letters/test/')
parser.add_argument('--folder2', help='Graphs against whose computes the distance.', default='./data/Letters/train/')

# Edit Distance
parser.add_argument('--ged', help='Graph edit distance algorithm.', default='vanillaAED')
parser.add_argument('--edit-operations', help='Graph edit distance parameters.', default={})

args = parser.parse_args()


def dist_matrix(fold1, fold2, ged):
    # Find graph files
    files1 = glob.glob(fold1 + '/*.gml')
    files2 = glob.glob(fold2 + '/*.gml')

    # Distance matrix
    d = np.zeros([len(files1), len(files2)])

    l1 = []
    l2 = []

    for f1 in range(d.shape[0]):
        # Read graph
        g1 = nx.read_gml(files1[f1])
        l1 += g1.graph['class']

        for f2 in range(d.shape[1]):
            # Read graph
            g2 = nx.read_gml(files2[f2])

            if not f1:
                l2 += g2.graph['class']

            # Distance
            dist, _ = ged.ged(g1, g2)

            d[f1, f2] = dist

    return d, l1, l2



def evaluation(folder1, folder2, ged):
    # Distance matrix computation
    d, l1, l2 = dist_matrix(folder1, folder2, ged)

    # Evaluation
    ind = np.argsort(d, axis=1)
    d_sort = np.sort(d, axis=1)
    k=5
    l2_matrix = np.array([np.array(l2)[ind[i,0:k]] for i in range(len(l1))])
    stats.mode(l2_matrix, axis=1)

    comparison = np.array([[i == j for j in l2] for i in l1])
    ind_sort = comparison[:,ind][np.eye(ind.shape[0],ind.shape[1], dtype=bool)]


    mAP = average_precision_score(comparison, np.exp(-d))

if __name__ == '__main__':
    ged = {
        'vanillaaed': VanillaAED(**args.edit_operations),
        'vanillahed': VanillaHED(**args.edit_operations)
    }.get(args.ged.lower(), None)

    if ged is not None:
        evaluation(args.folder1, args.folder2, ged)
    else:
        raise NameError('GED argument not implemented')