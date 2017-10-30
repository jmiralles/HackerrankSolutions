# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

“”””
Task
Given an array, , of  integers, calculate and print the respective mean, median, and mode on separate lines.
 If your array contains more than one modal value, choose the numerically smallest one.
“””
import numpy as np
from scipy import stats

a = raw_input()
b = map(int, raw_input().split())
c = np.array(b)

print np.mean(c)
print np.median(c)
print stats.mode(c)[0][0]
