from pythonds.basic import Stack

def paraChecker(symbolString):
    index = 0
    balanced = True
    stack = Stack()

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]

        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balanced = False
            else:
                top = stack.pop()
                balanced = matches(top, symbol)
        index = index + 1

    if stack.isEmpty() and balanced:
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

if __name__ == "__main__":
    result = paraChecker("[{{}}]")
    print(result)