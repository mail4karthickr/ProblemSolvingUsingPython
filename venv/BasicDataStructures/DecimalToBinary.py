from pythonds.basic import Stack

def decimalToBinary(decNumber):

    stack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        decNumber = decNumber // 2
        stack.push(rem)

    binString = ""
    while not stack.isEmpty():
        binString = binString + str(stack.pop())

    return binString

if __name__ == "__main__":
   print(decimalToBinary(10))
