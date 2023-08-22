# -*- codeing = utf-8 -*-
import time
def sumof2(n):
    start = time.time()
    thesum = 0
    for i in range(1,n+1):
        thesum = i +thesum

    end = time.time()
    return end-start

for i in range(5):
    print("%10.7f"%sumof2(10000))


def test1():
    l=[]
    for i in range(1000):
        l = l + [i]

def test2():
    l=[]
    for i in range(1000):
        l.append(i)
def test3():
    l =  [i for i in range(1000) ]

def test4():
    l = list(range(1000))
