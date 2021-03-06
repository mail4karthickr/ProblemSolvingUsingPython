from pythonds.basic import Stack

def postFixEvaluation(postfixExpr):

    tokenList = postfixExpr.split()
    operandStack = Stack()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(token)
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()

            result = doMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()


def doMath(op, op1, op2):

    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return  op1 + op2
    else:
        return op1 - op2

if __name__ == "__main__":
    result = postFixEvaluation("123*+")
    print(result)