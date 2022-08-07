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

    for x in range(0, a):
        X.add(x)

    for y in range(0, b):
        Y.add(y)

    G = set(zip(X, Y))

    return X, Y, G


def Q4(E, n):
    n_successors = []
    vals = E.values()
    for x in E.values():
        if n in x:
            n_successors.append(x[1])

    print(n_successors)
    return n_successors


def Q5(inFile, outFile, remove):
    print('Character '+remove+' removed from '+inFile)
    print('Output written to '+outFile)


def Q6(state1, state2):
    print('IMPOSSIBLE')


E = {'e1': (1, 3),
     'e2': (2, 3, {'weight': 3.1415}),
     'e3': (2, 4),
     'e4': (3, 4)
     }
Q4(E, 2)
