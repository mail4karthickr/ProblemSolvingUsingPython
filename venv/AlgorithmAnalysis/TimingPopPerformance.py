from timeit import Timer

# Measure Pop operation

popzero = Timer("popZeroList.pop(0)", "from __main__ import popZeroList")
popend = Timer("popEndList.pop()", "from __main__ import popEndList")

popZeroList = list(range(2000000))
print ("popZeroList ", popzero.timeit(number=1000))

popEndList = list(range(2000000))
print ("popEndList ", popend.timeit(number=1000))