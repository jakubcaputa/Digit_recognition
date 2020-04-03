import numpy

a=numpy.zeros((5,5))
a[(1,1)] = 5
for q in range(5):
    for w in range(5):
        if a[(q,w)] < 6:
            a[(q,w)] = 1
print(a)