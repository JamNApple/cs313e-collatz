

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
    cache ={1 : 1,
2 : 2,
3 : 8,
4 : 3,
5 : 6,
6 : 9,
7 : 17,
8 : 4,
9 : 20,
10 : 7,
11 : 15,
12 : 10,
13 : 10,
14 : 18,
15 : 18,
16 : 5,
17 : 13,
18 : 21,
19 : 21,
20 : 8,
21 : 8,
22 : 16,
23 : 16,
24 : 11,
25 : 24,
26 : 11,
27 : 112,
28 : 19,
29 : 19,
30 : 19,
31 : 107,
32 : 6,
33 : 27,
34 : 14,
35 : 14,
36 : 22,
37 : 22,
38 : 22,
39 : 35,
40 : 9,
41 : 110,
42 : 9,
43 : 30,
44 : 17,
45 : 17,
46 : 17,
47 : 105,
48 : 12,
49 : 25,
50 : 25,
51 : 25,
52 : 12,
53 : 12,
54 : 113,
55 : 113,
56 : 20,
57 : 33,
58 : 20,
59 : 33,
60 : 20,
61 : 20,
62 : 108,
63 : 108,
64 : 7,
65 : 28,
66 : 28,
67 : 28,
68 : 15,
69 : 15,
70 : 15,
71 : 103,
72 : 23,
73 : 116,
74 : 23,
75 : 15,
76 : 23,
77 : 23,
78 : 36,
79 : 36,
80 : 10,
81 : 23,
82 : 111,
83 : 111,
84 : 10,
85 : 10,
86 : 31,
87 : 31,
88 : 18,
89 : 31,
90 : 18,
91 : 93,
92 : 18,
93 : 18,
94 : 106,
95 : 106,
96 : 13,
97 : 119,
98 : 26,
99 : 26,
100 : 26}
    if j<i:
        i, j = j, i
    if j//2>=i:
        i=j//2+1
    for b in range(i,j+1): 
        x=1
        while b != 1:
            if b in cache:
                x+=cache[b]-2
                b=2
            if b%2 == 0:
                b=b/2
                x += 1
            elif b%2 == 1:
                b=b + b//2 + 1
                x += 2
        if x>q:
            q=x
    return q

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
#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys


# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)

"""
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 20
100 200 125
201 210 89
900 1000 174



% pydoc3 -w Collatz
"""
#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------
