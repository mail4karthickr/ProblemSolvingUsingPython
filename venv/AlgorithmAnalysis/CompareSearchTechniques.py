import timeit

# binary search function
def binary_search(myList, find):
    while len(myList) > 0:
        mid = len(myList) // 2
        if find == mid:
            return True
        elif find < mid:
            myList = myList[:mid]
        else:
            myList = myList[mid + 1:]
    return False

# linear search function
def linear_search(myList, find):
    for i in myList:
        if i == find:
            return True
    return False

# compute binary search time
def binary_time():
    SETUP_CODE = '''
from __main__ import binary_search
from random import randint'''

    TEST_CODE = '''
myList = [x for x in range(10000)]
find = randint(0, len(myList))
binary_search(myList, find)'''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=1000)
    print('Binary search time: {}'.format(min(times)))

def linear_time():
    SETUP_CODE = '''
from __main__ import linear_search
from random import randint'''

    TEST_CODE = '''
myList = [x for x in range(10000)]
find = randint(0, len(myList))
linear_search(myList, find)'''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=1000)
    print('Linear search time: {}'.format(min(times)))

if __name__ == "__main__":
    linear_time()
    binary_time()