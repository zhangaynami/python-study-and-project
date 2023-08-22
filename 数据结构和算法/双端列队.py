# -*- codeing = utf-8 -*-
# class Deque:
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def addfront(self,item):
#         self.items.append(item)
#     def addrear(self,item):
#         self.items.insert(0,item)
#
#     def removefront(self):
#         self.items.pop()
#     def removerear(self):
#         self.items.pop(0)
#
#     def size(self):
#         return len(self.items)

from pythonds.basic import Deque
def palchecker(astring):
    chardeque = Deque()
    for i in astring:
        chardeque.addfront(i)

    hw = True
    while hw and chardeque.size() > 1:

        f = chardeque.removefront()
        r = chardeque.removerear()
        if f != r:
            return False
    return hw

# 回文检测升级

def palcheckerpro(astring):
    chardeque = Deque()
    for i in astring:
        if i == " ":
            continue
        chardeque.addRear(i)

    hw = True

    while hw and chardeque.size() > 1:

        f = chardeque.removeFront()
        r = chardeque.removeRear()



        if f != r :
            return False
    return hw
print(palcheckerpro("r  o r"))