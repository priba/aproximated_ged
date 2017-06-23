#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    evaluate.py

    Computes the distance between .
"""

from VanillaAED import VanillaAED
from VanillaHED import VanillaHED

import os
import glob
import itertools

import networkx as nx

import argparse

__author__ = "Pau Riba, Anjan Dutta"
__email__ = "priba@cvc.uab.cat, adutta@cvc.uab.cat"

# Argument parser
parser = argparse.ArgumentParser(description='Computes the distance all vs all between two folders.')

# Prototypes
parser.add_argument('--folder1', help='Input graphs', default='./data/Letters/test/')
parser.add_argument('--folder2', help='Graphs agains whose computes the distance', default='./data/Letters/train/')

args = parser.parse_args()


def main(fold1, fold2, ged):
    # TODO
    for f1, f2 in itertools.combinations_with_replacement(files, 2):
        # Read graphs
        g1 = nx.read_gml(f1)
        g2 = nx.read_gml(f2)

        # Distance
        dist, assignment = ged.ged(g1, g2)
    pass

if __name__ == '__main__':
    ged = VanillaHED()
    main(args.folder1, args.folder2, ged)