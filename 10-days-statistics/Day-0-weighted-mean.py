# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

“””” This would be a multiline comment
Task
Given an array, , of  integers and an array, , representing the respective weights of 's elements, calculate and print the weighted mean of 's elements. Your answer should be rounded to a scale of  decimal place (i.e.,  format).

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
