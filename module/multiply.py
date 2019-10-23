import sys
import emb

def multiply(a, b):
    print("{} x {}".format(a,b))
    c = 0
    for i in range(0,a):
        c = c + b
    return c

def divide(a, b):
    print("{} / {}".format(a,b))
    c = 0
    while a > 0:
        c = c + 1
        a = a - b

    return c

def getargs(a, b):
    print('Number of arguments {}'.format(emb.numargs()))

def dohelp(a,b):
    help(emb)

def callstat(a,b):
    r = emb.status()
    print(r)
    return r
    