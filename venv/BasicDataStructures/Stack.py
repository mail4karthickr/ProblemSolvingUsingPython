# Solution1
# Stack implementation
# Time complexity of push and pop is O(1) in this implementation.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

# Solution2
# Stack implementation
# Time complexity of push and pop operation in this implementation is O(n)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        self.items.pop(0)

    def peek(self):
        return self.items[0]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


# Simple Balanced Parentheses
