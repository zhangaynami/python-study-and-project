# -*- codeing = utf-8 -*-
# 1-9
class Fraction:
    #初始化
    def __init__(self,top,botton):
        if int(top) != float(top) or int(botton) != float(botton):
            raise RuntimeError("你不能使用小数")
        self.top = top
        self.botton = botton

    def __str__(self):
        common = self.gcd(self.top,self.botton)
        return str(self.top//common) + "/" + str(self.botton//common)
    # 返回分子
    def getNum(self):
        return self.top

    # 返回分母
    def getDem(self):
        return self.botton
    #最大公因私
    def gcd(self,m,n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn

        return n

    #最简加法
    def __add__(self, other):
        newtop = self.top*other.botton + self.botton*other.top
        newbotton = self.botton * other.botton

        common = self.gcd(newtop,newbotton)
        return Fraction(newtop//common,newbotton//common)

    #减法运算
    def __sub__(self, other):
        newtop = self.top*other.botton - self.botton*other.top
        newbotton = self.botton * other.botton

        common = self.gcd(newtop,newbotton)
        return Fraction(newtop//common,newbotton//common)
    # 乘法运算
    def __mul__(self, other):
        newtop = self.top * other.top
        newbotton = self.botton * other.botton
        common = self.gcd(newtop, newbotton)
        return Fraction(newtop // common, newbotton // common)
    # 除法运算
    def __truediv__(self, other):
        newtop = self.top * other.botton
        newbotton = self.botton * other.top
        common = self.gcd(newtop, newbotton)
        return Fraction(newtop // common, newbotton // common)

    # 判断原本的参数是否大于新的参数
    def __gt__(self,other):
        if  self.top * other.botton * self.botton * other.botton >= 0:
            if self.top * other.botton > self.botton * other.botton:
                return True
            else:
                return False
        else:
            if self.top * self.botton > 0:
                return True
            else:
                return False
    def __ge__(self,other):
        if self.top * other.botton * self.botton * other.botton >= 0:
            if self.top * other.botton > self.botton * other.botton:
                return True
            else:
                return False
        else:
            if self.top * self.botton > 0:
                return True
            else:
                return False
    def __lt__(self,other):
        if self.top * other.botton * self.botton * other.botton >= 0:
            if self.top * other.botton  < self.botton * other.botton:
                return True
            else:
                return False
        else:
            if self.top * self.botton < 0:
                return True
            else:
                return False
    def __le__(self,other):
        if self.top * other.botton * self.botton * other.botton >= 0:
            if self.top * other.botton <= self.botton * other.botton:
                return True
            else:
                return False
        else:
            if self.top * self.botton <= 0:
                return True
            else:
                return False

    #     不等式判别
    def __ne__(self,other):
        if self.top * other.botton != self.botton * other.botton:
            return True
        else:
            return False

    def __radd__(self, other):
        newtop = self.top*other.botton +self.botton*other.top
        newbotton = self.botton*other.botton

        return Fraction(newtop,newbotton)

    def __iadd__(self, other):
        newtop = self.top * other.botton + self.botton * other.top
        newbotton = self.botton * other.botton

        self.top = newtop
        self.botton = newbotton

    def __repr__(self):
        return "这是分数"




a = Fraction(3,6)

print(a)






