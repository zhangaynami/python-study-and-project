# -*- codeing = utf-8 -*-
# 后续表达式

import string

from pythonds.basic import Stack


# 后序表达式
def infixToPostfix(x):
    s = Stack()
    finlist = []
    prec = {
        "*":3,
        "/":3,
        "+":2,
        "-":2,
        "(":1
        }

    for token in x.split():
        if token in string.ascii_uppercase:
            finlist.append(token)
        elif token == "(":
            s.push(token)
        elif token == ")":
            las = s.pop()
            while las != "(":
                finlist.append(las)
                las = s.pop()
        elif token in "+-*/":
            while not s.isEmpty() and prec[s.peek()] >= prec[token]:
                finlist.append(s.pop())
            s.push(token)
        else:
            return "请输入正确的数字、符号"

    while not s.isEmpty():
        finlist.append(s.pop())
    return "".join(finlist)
# print(infixToPostfix("A + B"))
def postfixEval(formal):
    s = Stack()
    tokenlist = formal.split()

    for i in tokenlist:
        if i in "0123456789":
            s.push(int(i))
        else:
            num2 = s.pop()
            num1 = s.pop()
            newnum = domath(i,num1,num2)
            s.push(newnum)

    return s.pop()
def domath(way,num1,num2):
    if way == "+":
        return num1 + num2
    elif way == "-":
        return num1 - num2
    elif way == "*":
        return num1*num2
    elif way == "/":
        return num1 / num2

# print(postfixEval("1 1 +"))
#

# 直接计算
def infixToPostfixnum(x):
    s = Stack()
    finlist = []
    prec = {
        "*":3,
        "/":3,
        "+":2,
        "-":2,
        "(":1
        }

    for token in x.split():
        if token in "0123456789":
            finlist.append(token)
        elif token == "(":
            s.push(token)
        elif token == ")":
            las = s.pop()
            while las != "(":
                finlist.append(las)
                las = s.pop()
        elif token in "+-*/":
            while not s.isEmpty() and prec[s.peek()] >= prec[token]:
                finlist.append(s.pop())
            s.push(token)
        else:
            return "请输入正确的数字、符号"

    while not s.isEmpty():
        finlist.append(s.pop())
    numlist =  " ".join(finlist)
    # print(infixToPostfixnum("3 + 4"))
    s = Stack()
    tokenlist = numlist.split()

    for i in tokenlist:
        if i in "0123456789":
            s.push(int(i))
        else:
            num2 = s.pop()
            num1 = s.pop()
            newnum = domath(i,num1,num2)
            s.push(newnum)

    return s.pop()

print(infixToPostfixnum("3 * 5"))