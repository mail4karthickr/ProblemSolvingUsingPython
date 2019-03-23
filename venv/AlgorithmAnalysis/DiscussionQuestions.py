import timeit



def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

# Time complexity is O(n^2)
def problem1(n):
    for i in range(n):
        for j in range(n):
            k = 2 + 2

# Time complexity is O(n)
def problem2(n):
    for i in range(n):
        k = 2+2

# Time complexity is O(log n) because for every iteration n is getting reduced by half.
def problem3(n):
    i = n
    while i > 0:
        k = 2 + 2
        i = i // 2
        print(i)




# for size in range(10, 100, 10):
    # wrapped = wrapper(problem1, size)
    # print("problem1 - ist size",size, timeit.timeit(wrapped, number=1000))

    # wrapped = wrapper(problem2, size)
    # print("problem2 - lst size", size, timeit.timeit(wrapped, number=1000))

    # wrapped = wrapper(problem3, size)
    # print("problem3 - lst size", size, timeit.timeit(wrapped, number=1000))

problem3(20)

