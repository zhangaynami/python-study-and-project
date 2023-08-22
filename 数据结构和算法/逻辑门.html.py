# -*- codeing = utf-8 -*-

#与门
class AndGate1:

    # 初始化，包含逻辑门的名字、输入、输出
    def __init__(self,name):
        self.name = name
        self.pin = [None,None]
        self.output = None

    # 接口，数据来源
    def setPin(self,source,pin_num):
        self.pin[pin_num] = source
    # 如果逻辑值存在就输出，否则手动输入
    def getPin(self,pin):
        if pin == None:
            return input("输入逻辑"+self.name)
        else:
            return self.getOutput()

    def performGateLogic(self):
        # 利用逻辑门输入判断结果
        self.pin[0] = self.getPin(self.pin[0])
        self.pin[1] = self.getPin(self.pin[1])
        if self.pin[0] == 1 and self.pin[1] == 1:
            return 1
        else:
            return 0
    # 输出
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

# g = AndGate1("G1")
# # print(g.getOutput())


class OrGate1:
    def __init__(self,name):
        self.name = name
        self.pin = [None,None]
        self.output = None
    def setpin(self,source,pin_num):
        self.pin[pin_num] = source
    def getpin(self,pin):
        if pin  == None:
            return int(input("输入逻辑"+self.name))
        else:
            return self.getoutput()

    def performGateLogic(self):
        self.pin[0] = self.getpin(self.pin[0])
        self.pin[1] = self.getpin(self.pin[1])
        if self.pin[0] == 1 or self.pin[1] == 1:
            return 1
        else:
            return 0
    def getoutput(self):
        self.output = self.performGateLogic()
        return self.output
# g = OrGate1("or")
# print(g.getoutput())
# 与非门（NOT-AND gate）
class NOT_AND:
    def __init__(self,name):
        self.name = name
        self.pin = None
        self.outpin = None

    def setpin(self,source):
        self.pin = source

    def getpin(self,pin):
        if pin == None:
            return int(input("输入逻辑"+self.name))
        else:
            return self.output()
    def performGateLogic(self):
        self.pin = self.getpin(self.pin)
        if self.pin == 1:
            return 0
        else:
            return 1

    def output(self):
        self.outpin = self.performGateLogic()
        return self.outpin
# 非门
class Or_not:
    def __init__(self,name):
        self.name = name
        self.pin = [None,None]
        self.output = None
    def setpin(self,source,pin_num):
        self.pin[pin_num] = source
    def getpin(self,pin):
        if pin  == None:
            return int(input("输入逻辑"+self.name))
        else:
            return self.getoutput()

    def performGateLogic(self):
        self.pin[0] = self.getpin(self.pin[0])
        self.pin[1] = self.getpin(self.pin[1])
        if self.pin[0] == 1 or self.pin[1] == 1:
            return 0
        else:
            return 1
    def getoutput(self):
        self.output = self.performGateLogic()
        return self.output

# 异或门（XOR gate）

class XOR_gate:
    def __init__(self,name):
        self.name = name
        self.pin = [None,None]
        self.output = None
    def setpin(self,source,pin_num):
        self.pin[pin_num] = source
    def getpin(self,pin):
        if pin  == None:
            return int(input("输入逻辑"+self.name))
        else:
            return self.getoutput()

    def performGateLogic(self):
        self.pin[0] = self.getpin(self.pin[0])
        self.pin[1] = self.getpin(self.pin[1])
        if self.pin[0] == self.pin[1]:
            return 0
        else:
            return 1
    def getoutput(self):
        self.output = self.performGateLogic()
        return self.output

# 半加器
class XOR_gate:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.sum()
        self.carrybit()

    def sum(self):
        if self.a == self.b:
            print("s=0")
        else:
            print("s=1")
    def carrybit(self):
        if self.a == 1 and self.b == 1:
            print("c=1")
        else:
            print("C=0")
# 全加器（Full Adder）
class Full_Adder:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.sum()
        self.carrybit()


    def sum(self):
        if self.a == self.b:
            if self.c == 0:
                print("s=0")
            else:
                print("s=1")
        else:
            if self.c == 1:
                print("s=0")
            else:
                print("s=1")
    def carrybit(self):
        if self.a == self.b :
            print("c=1")
        else:
            print("C=0")

class AndGate2:
    def cal(self,a,b):
        self.pin = [a,b]
        if self.pin[0] == 1 and self.pin[1] == 1:
            return 1
        else:
            return 0

class OrGate2:
    def cal(self,a,b):
        self.pin = [a, b]
        if self.pin[0] == 1 or self.pin[1] == 1:
            return 1
        else:
            return 0
class NoGate2:
    def cal(self,a):
        self.pin = a
        if self.pin == 1 :
            return 0
        else:
            return 1

g1 = AndGate2()
g2 = OrGate2()
g3 = NoGate2()



# 半加器
# carry = g1.cal(1,1)
#
# print(carry)
# sum = g2.cal(g1.cal(1,1),g3.cal(g1.cal(1,1)))
# print(sum)

# print(g2.cal(g1.cal(1,0),g1.cal(1,1)))

