#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read two ints
    r a reader
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    q=1
    if j<i:
        j, i = i , j
    if j/2>i:
        i=j/2+1
    
    for v in range(i,j): 
        x=0
        b=v
        while b != 1:
            if b%2 == 0:
                b=b/2
                x += 1
            elif b%2 == 1:
                b=b + b/2 + 1
                x += 2
        if x>q:
            q=x
    return q+1

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
