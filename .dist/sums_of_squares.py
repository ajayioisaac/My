#! /usr/bin/python
def sums_of_squares(y):
    #Note that y is a list
    sum = 0
    for i in y:
        sum += i*i
    result = sum
    return result
print(sums_of_squares([2, 10, 5, 3]))
