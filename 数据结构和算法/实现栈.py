# -*- codeing = utf-8 -*-
class stack:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def push(self,item):
        self.item.append(item)

    def pop(self):
       return self.item.pop()

    def peek(self):
        return self.item[-1]

    def size(self):
        return len(self.item)

# s = stack()
# print(s.isEmpty())
# print(s.push(4))
# print(s.push("dog"))
# print(s.pop())
# print(s.peek())
# print(s.size())

class stackreverse:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def push(self,item):
        self.item.insert(0,item)

    def pop(self):
       return self.item.pop(0)

    def peek(self):
        return self.item[0]

    def size(self):
        return len(self.item)


from pythonds.basic import Stack
# 匹配括号
def parChecker(symbolstring):
    s = Stack()
    index = 0
    balanced = True

    while index < len(symbolstring) and balanced:
        symbol = symbolstring[index]

        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

# a = "()"
# print(parChecker(a))

def parChecker1(symbolstring):

    s = stack()
    for i in symbolstring:
        if i == "(":
            s.push(i)
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()

    if s.isEmpty():
        return True
    else:

       return False
# x = "()"
# a = parChecker1(x)
# print(a)


# 匹配括号
def parChecker3(symbolstring):
    s = Stack()
    index = 0
    balanced = True

    while index < len(symbolstring) and balanced:
        symbol = symbolstring[index]

        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                if symbol == ")" and s.peek() == "(":
                    s.pop()
                elif symbol == "}" and s.peek() == "{":
                    s.pop()
                elif symbol == "]" and s.peek() == "[":
                    s.pop()

                else:
                    balanced = False

        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

# print(parChecker3("({)})"))

def dividedby3(number):
    s = Stack()

    while number > 0 :
        ys = number % 2
        s.push(ys)
        number = number // 2

    num = ""
    while not s.isEmpty():
        num += str(s.pop())
    return num
a = dividedby3(2)

print(a)




