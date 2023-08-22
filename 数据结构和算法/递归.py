# -*- codeing = utf-8 -*-
# def tostr(n,base):
#     num = "0123456789"
#     if n < base:
#         return num[n]
#     else:
#         return tostr(n//base,base) + num[n %base]

def tostr(n,base):
    numlist = "0123456789"
    if n < base:
        return numlist[n]
    else:
        return tostr(n // base,base) + numlist[n % base]
from pythonds.basic import Stack
rstack = Stack()
def tostrpro(n,base):
    numlist = "0123456789"
    if n < base:
        rstack.push(numlist[n])
    else:
        rstack.push(numlist[n % base])
        tostr(n // base,base)