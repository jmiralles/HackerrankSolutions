# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

“”””
Task
Given an array, X, of N integers and an array, W, representing the respective weights of X's elements,
 calculate and print the weighted mean of X's elements.
Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).

“””
a = raw_input()
b = map(float, raw_input().split())
c = map(float, raw_input().split())
den = 0
num = 0

# d = reduce(lambda a, b :  a + b ,c) # importing reduce from functools

# no importing reduce
for val in c:
    den = den + val

for i, val in enumerate(b):
    num = num + val * c[i]

print round(num/den,1)
