from pythonds.basic import Stack
import string

def infixToPostfix(infixexpr):

    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    tokenList = infixexpr.split()
    postfixList = []
    operatorsList = Stack()

    for token in tokenList:
        if token in string.ascii_uppercase:
            postfixList.append(token)
        elif token == '(':
            operatorsList.push(token)
        elif token == ')':
            topToken = operatorsList.pop()
            while topToken != '(':
                topToken = operatorsList.pop()
                postfixList.append(topToken)
        else:
            while not operatorsList.isEmpty() and prec[operatorsList.peek()] >= prec[token]:
                postfixList.append(operatorsList.pop())
            operatorsList.push(token)

    while not operatorsList.isEmpty():
        postfixList.append(operatorsList.pop())

    return " ".join(postfixList)

if __name__ == "__main__":
    result = infixToPostfix("A + B * C")
    print(result)






