

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
50 : 25
}
    if j<i:
        i, j = j, i
    if j//2>=i:
        i=j//2+1
    for b in range(i,j+1): 
        x=1
        while b != 1:
            if b <= 50:
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
