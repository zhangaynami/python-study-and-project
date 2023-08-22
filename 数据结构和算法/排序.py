# -*- codeing = utf-8 -*-
def bubblesrt(alist):
    for passnum in range(len(alist)-1,0,-1):
        for x in range(passnum):
            if alist[x] > alist[x+1]:
                temp = alist[x]
                alist[x] = alist[x+1]
                alist[x + 1] = temp
# 短冒泡
def shortbubblesrt(alist):
    changenum = len(alist) - 1
    change = True

    while changenum > 0 and change:
        change = False
        for x in range(changenum):
            if alist[x] > alist[x + 1]:
                change = True
                temp = alist[x]
                alist[x] = alist[x + 1]
                alist[x + 1] = temp
        changenum -= 1

# 选择排序
def selectionsort(alist):
    for changenum in range(len(alist)-1,0,-1):
        posmax = 0
        for location in range(1,changenum + 1):
            if alist[location] > alist[posmax]:
                posmax = location

        temp = alist[changenum]
        alist[changenum] = alist[posmax]
        alist[posmax] = temp
# 插入排序

def insertionsort(alist):
    for index in range(1,len(alist)):
        concurrentvalue = alist[index]
        pos = index

        while pos > 0 and alist[pos - 1] > concurrentvalue:
            alist[pos] = alist[pos] - 1
            pos -= 1

        alist[pos] = concurrentvalue

# 希尔排序
# def shellsort(alist):
#     sublistcount = len(alist) // 2 #排序的数量
#     while sublistcount > 0:
#         for startposition in range(sublistcount):
#             gapinsertionsort(alist,startposition,sublistcount)
#         print(sublistcount,alist)
#         sublistcount = sublistcount // 2
#
# def gapinsertionsort(alist,start,gap):
#     for i in range(start + gap,len(alist),gap):
#         currentvalue = alist[i]
#         pos = i
#         while pos >= gap and alist[pos-gap] > currentvalue:
#             alist[pos] = alist[pos-gap]
#             pos -= gap
#         alist[pos] = currentvalue
def shellsort(alist):
    subliscount = alist // 2
    while subliscount > 0:
        for start in range(subliscount):
            gapinsertionsort(alist, start, subliscount)

        print(subliscount)
        subliscount = alist // 2
def gapinsertionsort(alist, start, gap):
    for index in range(start + gap,len(alist),gap):
        concurrentvalue = alist[index]
        pos = index

        while pos >= gap and alist[pos - gap] > concurrentvalue:
            alist[pos] = alist[pos - gap]
            pos -= gap
        alist[pos] = concurrentvalue

# def mergesort(alist):
#     print("S:",alist)
#     if len(alist) > 1:
#         mid = len(alist) // 2
#         left = alist[:mid]
#         right = alist[mid:]
#         mergesort(left)
#         mergesort(right)
#
#         i = 0
#         j = 0
#         k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 alist[k] = left[i]
#                 i += 1
#             else:
#                 alist[k] = right[j]
#                 j += 1
#             k += 1
#
#         while i < len(left):
#             alist[k] = left[i]
#             i += 1
#             k += 1
#         while j <len(right):
#             alist[k] = right[j]
#             j += 1
#             k += 1
#     print(alist)
#
# b=[23,4,56,21,3,7,324]
# print(mergesort(b))


def mergesort(alist):
    print("s",alist)

    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]
        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            alist[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            alist[k] = right[j]
            k += 1
            j += 1

    print(alist)
# b=[23,4,56,21,3,7,324]
# print(mergesort(b))
#快速排序

def quicksort(alist):
    quicksorthelp(alist,0,len(alist)-1)
def quicksorthelp(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quicksorthelp(alist,first,splitpoint -1 )
        quicksorthelp(alist,splitpoint+1,last)
def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmarket = first + 1
    rightmarket = last

    done = False
    while not done:
        while leftmarket <= rightmarket and alist[leftmarket] <= pivotvalue:
            leftmarket += 1

        while alist[rightmarket] >=pivotvalue and rightmarket >= leftmarket:
            rightmarket -= 1

        if leftmarket < rightmarket:
            done = True
        else:
            temp = alist[leftmarket]
            alist[leftmarket] = alist[rightmarket]
            alist[rightmarket] = temp

        temp = alist[first]
        alist[first] = alist[rightmarket]
        alist[rightmarket] = temp

        return rightmarket