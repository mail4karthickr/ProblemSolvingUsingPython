from pythonds.basic import Stack

def paraChecker(symbolString):
    stack = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balanced = False
            else:
                stack.pop()

        index = index + 1

    if balanced and stack.isEmpty():
        return True
    else:
        return False



if __name__ == "__main__":
    result = paraChecker("((()))")
    print(result)
