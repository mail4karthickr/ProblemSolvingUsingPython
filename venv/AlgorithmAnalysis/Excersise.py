import timeit
import random

# 1. Devise an experiment to verify that the list index operator is O(1)

# x = list(range(1000))
# for i in range(100):
#     print(timeit.timeit("x[random.choice(x)]", setup="from __main__ import x, random",number=1000))
#
# # 2. Devise an experiment to verify that get item and set item are O(1) for dictionaries.
# dic = {j:None for j in range(1000)}
# for i in range(100):
#     print(timeit.timeit("dic[i]", setup="from __main__ import dic, i", number=1000))
#
# for i in range(100):
#     val = "value"
#     print(timeit.timeit("dic[i]=val", setup="from __main__ import dic, i, val", number=1000))

# 3. Devise an experiment that compares the performance of the del operator on lists and dictionaries.
# Lists del operator's time complexity is O(n)
def proveListsDelOperator():
    index = 0
    for i in range(1000, 100000, 1000):
        myList = list(range(i))
        timeTaken = timeit.timeit("del myList[index]", setup="from __main__ import myList, index", number=i)
        print(f'Timetaken {timeTaken} for list size {i}')

# Dictionary's del operator is O(1) time complexity
def proveDicDelOperator():
    for x in range(1000, 100000, 1000):
        dic = {j:None for j in range(x)}
        TEST_CODE = '''
find = randint(0, sizeOfTheDic)
del dic[find]'''

        SETUP_CODE = '''
from __main__ import x, dic
from random import randint'''
        timeit.timeit(lambda: delOperatorTestCode(x, di))
        times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, number=1000)
        print('del operator time : {}'.format(min(times)))

def delOperatorTestCode(size, dic):
    find = randint(0, size)
    del dic[find]

if __name__ == "__main__":
    # proveDicDelOperator()
    # proveListsDelOperator()
    findSmallestNumber([2, 5, 3, 0, 1])

# Find the kth smallest number in the list.

def findSmallestNumber(list, k):
    stillOK = True
    smallestNo = list[0]
    x = 0
    while i < len(list) and stillOK:
        if list[i] < smallestNo:
            smallestNo = list[i]
            x = x + 1

        if x == k:
            stillOK = False

        return smallestNo


