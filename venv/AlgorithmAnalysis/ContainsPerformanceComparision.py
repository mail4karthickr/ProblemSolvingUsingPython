from timeit import Timer
import random

# Prove list's contains operation is O(n) and Dictionary's contains operation is O(1)
for i in range(10000, 1000001, 20000):
    x = list(range(i))
    t = Timer("random.randrange(%d) in x"%i, "from __main__ import random,x")
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))