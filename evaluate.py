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

if __name__ == '__main__':
