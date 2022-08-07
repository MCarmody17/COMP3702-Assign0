# -*- coding: utf-8 -*-
"""
Assignment 0 template

For submission, rename this file to "A0.py" 

Answer each question in the corresponding method definition stub below
"""
import unittest


def Q1(A, B):
    union = set(A | B)
    intersection = set(A & B)
    return union, intersection


def Q2(A, B):
    intersection = set(A & B)
    if(len(intersection) == 0):
        return 'DISJOINT'

    return 'INTERSECTING'


def Q3(a, b):
    X = set()
    Y = set()
    G = set()
    for x in range(0, a):
        X.add(x)

    for y in range(0, b):
        Y.add(y)

    G = list(zip(x, y))

    return X, Y, G


def Q4(E, n):
    n_successors = []
    for item in E.items():
        if item.contains(n):
            n_item = item.value().split(',')
            n_successors.add(n_item(1))

    return n_successors


def Q5(inFile, outFile, remove):
    print('Character '+remove+' removed from '+inFile)
    print('Output written to '+outFile)


def Q6(state1, state2):
    print('IMPOSSIBLE')
