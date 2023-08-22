# -*- codeing = utf-8 -*-
class queuerev:
    def __init__(self):
        self.item = []

    def enqueue(self,item):
        self.item.insert(0,item)

    def dequeue(self,item):
        return self.item.pop()