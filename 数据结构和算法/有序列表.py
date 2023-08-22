# -*- codeing = utf-8 -*-
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getdata(self):
        return self.data
    def getnext(self):
        return self.next
    def setdata(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next =newnext
class orderlist:
    def __init__(self):
        self.head = None


    def length(self):
        current = self.head
        count = 0
        while count != None:
            count += 1
            current = current.getNext()
        return count

    def remove(self,item):
        current = self.head
        pronode = None
        find = False
        while current != None and find == False:
            if current == item:
                find = True
            else:
                pronode = current
                current = current.getNext()
        if pronode == None:
            self.head = current.getNext()
        else:
            current.setNext(current.getNext())

    def isEmpty(self):
        return self.head == None

    def search(self,item):
        current = self.head
        find = False
        stop = False
        while current != None and not find and not stop:
            if current == item:
                find = True
            else:
                if item < current.getDate():
                    stop = False
                else:
                    current = current.getNext()
        return find
    def add(self,item):
        current = self.head
        pronode = None
        find = False
        while current != None and find == False:
            if current == item:
                find = True
            else:
                pronode = current
                current = current.getNext()
        temp = Node(item)
        if pronode == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(self.head)
            pronode.setNext(temp)