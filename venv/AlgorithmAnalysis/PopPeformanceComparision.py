from timeit import Timer

# prove pop is O(1) operation and pop(index) is O(n) operation.

for i in range(1000000, 100000001, 1000000):
    pz = list(range(i))
    pzt = Timer("pz.pop(0)", "from __main__ import pz")
    print("pop(0)", pzt.timeit(number=1000))

    x = list(range(i))
    pt = Timer("x.pop", "from __main__ import x")
    print("pop", pt.timeit(number=1000))