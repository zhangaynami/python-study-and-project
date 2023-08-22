# -*- codeing = utf-8 -*-
# 无序列表的搜索
def sequentialsearch(alist,item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if item == alist[pos]:
            found = True
        else:
            pos += 1
    return found
# 有序列表的搜索
def ordersequentialsearch(alist,item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if item == alist[pos]:
            found = True
        else:
            if alist[pos] < item:
                stop = True
            else:
                pos += 1
    return found
# 二分查找
def binarysearch(alist,item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if item == alist[midpoint]:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found
# 二分查找的递归

def binarysearchpro(alist,item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if item == alist[midpoint]:
            return True
        else:
            if item < alist[midpoint]:
                return binarysearchpro(alist[:midpoint],item)
            else:
                return binarysearchpro(alist[midpoint+1:],item)

# 散列
def hash(astring,tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum += ord(astring[pos])

    return sum % tablesize

# class HashTable:
#     def __init__(self):
#         self.size = 11 #散列表初始值
#         self.slots = [None] * self.size #储存栈
#         self.data = [None] * self.size #储存值
#
#     def put(self,key,data):
#         hashvalue = self.hashfunction(key,len(self.slots))
#
#         if self.slots[hashvalue] == None:
#             self.slots[hashvalue] = key
#             self.data[hashvalue] = data
#         else:
#             if self.slots[hashvalue] == key:
#                 self.data[hashvalue] = data #替换
#
#             else:
#                 nextslots =  self.rehash(hashvalue,len(self.slots))
#                 while self.slots[nextslots] != None and  self.slots[nextslots] != key:
#                     nextslots = self.rehash(nextslots,len(self.slots))
#                 if self.slots[nextslots] == None:
#                     self.slots[nextslots] = key
#                     self.data[nextslots] = data
#                 else:
#                     self.data[nextslots] = data
#
#
#     def hashfunction(self,key,size):
#         return key*size
#     def rehash(self,oldhash,size):
#         return (oldhash+1) % size
class Hashtable:
    def __init__(self):
        self.size = 11
        self.slot = [None] * self.size
        self.data = [None] * self.size


    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slot))
        if self.slot[hashvalue] == None:
            self.slot[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slot[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.reshash(hashvalue,len(self.slot))
                while self.slot[nextslot] != None and self.slot[nextslot] != key:
                    nextslot = self.reshash(hashvalue, len(self.slot))

                if self.slot[nextslot] == None:
                    self.slot[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data


    def get(self,key):
        startslot = self.hashfunction(key,len(self.slot))
        found = False
        stop = False
        data = None
        pos = startslot
        while self.slot[pos] != None and not stop and not found:

            if self.slot[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self.reshash(pos,len(self.slot))
                if pos == startslot:
                    stop = True
        return data
    def hashfunction(self,key,size):
        return key % size
    def reshash(self,oldhash,size):
        return (oldhash + 1) % size
    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, data):
        self.put(key,data)
H = Hashtable()
H[54] = "cat"
H[26] = "dog"
H[93] ="lion"
print(H.slot)







