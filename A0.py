# -*- coding: utf-8 -*-
"""
Assignment 0 template

For submission, rename this file to "A0.py" 

Answer each question in the corresponding method definition stub below
"""


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
    for x in E.values():
        if n == x[0]:
            n_successors.append(x[1])

    return set(n_successors)


def Q5(inFile, outFile, remove):
    arr = []
    str = ""
    maxDiff = None
    with open(inFile) as f:
        contents = f.read()
        print(contents)

    for ch in contents:
        if ch != remove:
            arr.append(ch)
            str += ch
        else:
            arr.append("_")

    f = open(outFile, "a")
    f.write(str)
    f.close()
    print(arr)
    print(
        f" +---+---+---+\n | {arr[0]} | {arr[1]} | {arr[2]} | \n +---+---+---+ \n | {arr[3]} | {arr[4]} | {arr[5]} | \n +---+---+---+ \n | {arr[6]} | {arr[7]} | {arr[8]} | \n +---+---+---+")


def Q6(state1, state2):
    print(state1)
    counter1 = 0
    counter2 = 0
    for ch in state1:
        if ch == "_":
            for chars in state2:
                if chars == "_":
                    if abs(counter1 - counter2) != 1 or abs(counter1 - counter2) != 3:
                        print('IMPOSSIBLE')
                    else:
                        if(counter1 - counter2 == 1):
                            print('L')
                        if(counter1 - counter2 == -1):
                            print('R')
                        if(counter1 - counter2 == -1):
                            print('U')
                        if(counter1 - counter2 == -1):
                            print('D')
                counter2 += 1
        counter1 += 1
