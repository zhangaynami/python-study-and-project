

# from pythonds.basic import Queue
# import random
# class Printer:
#     def __init__(self,ppm):
#         self.pagerate = ppm
#         self.currenttas = None
#         self.timeremaining = 0
#
#     def busy(self):
#         if self.currenttas != None:
#             return True
#         else:
#             return False
#
#     def startnext(self,newtask):
#         self.currenttas = newtask
#         self.timeremaining  = newtask.getpage()*60/self.pagerate
#
#     def tick(self):
#         if self.currenttas != None:
#             self.timeremaining -= 1
#             if self.timeremaining <= 0:
#                 self.currenttas = None
#
# class Task:
#     def __init__(self,time):
#         self.starttime = time
#         self.pages = random.randrange(1,21)
#     def getstamp(self):
#         return self.starttime
#     def getpage(self):
#         return self.pages
#     def waittime(self,currenttime):
#         return currenttime - self.starttime
#
# def simulation(numseconds,pagesperminute):
#     labprinter = Printer(pagesperminute)
#     taskqueue = Queue()
#     tasklist = []
#
#     for currentsecond in range(numseconds):
#         if newprinter():
#             task = Task(currentsecond)
#             taskqueue.enqueue(task)
#
#         if (not taskqueue.isEmpty()) and not labprinter.busy():
#             nexttask = taskqueue.dequeue()
#
#             tasklist.append(nexttask.waittime(currentsecond))
#             labprinter.startnext(nexttask)
#         labprinter.tick()
#     ave = sum(tasklist)/len(tasklist)
#     print("平均时间%6.2f,执行任务%2d"%(ave,taskqueue.size()))
#
# def newprinter():
#     num = random.randrange(1,181)
#     if num == 180:
#         return True
#     else:
#         return False
#
#
# print(simulation(3600,5))


import random

from pythonds.basic import Queue


class Printer:
    def __init__(self,pagepernumber):
        self.pagerate = pagepernumber
        self.currenttask = None
        self.timeremaining = 0

    def tick(self):
        if self.currenttask != None:
            self.startnext -= 1
            if self.startnext <= 0:
                self.currenttask = None

    def busy(self):
        if self.currenttask != None:
            return True
        else:
            return False
    def startnexttime(self,currenttask):
        self.currenttask = currenttask
        self.startnext = currenttask.getpage() * 60 / self.pagerate

class tasks:
    def __init__(self,time):
        self.starttime = time
        self.pages = random.randrange(1,21)
    def gettime(self):
        return self.starttime
    def getpage(self):
        return self.pages

    def waittime(self,currenttime):
        return currenttime - self.gettime()

def simulate(numsecond,pagepernumber):
    Q = Queue()
    waittime = []
    labprinter = Printer(pagepernumber)


    for i in range(numsecond):
        if iftask():
            Task = tasks(i)
            Q.enqueue(Task)

        if not Q.isEmpty() and not labprinter.busy():
            nexttask = Q.dequeue()
            waittime.append(nexttask.waittime(i))
            labprinter.startnexttime(nexttask)
        labprinter.tick()
    avg = sum(waittime) / len(waittime)
    return avg

def iftask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

print(simulate(3600,10))