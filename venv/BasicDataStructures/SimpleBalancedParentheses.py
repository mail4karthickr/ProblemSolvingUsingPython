from pythonds.basic import Stack

def paraChecker(symbolString):
    stack = Stack()
    while i < len(symbolString):
        i = symbolString[i]
        if i == "(":
            stack.push(i)

        if i == ")":
            stack.pop()