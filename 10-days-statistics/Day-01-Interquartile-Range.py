# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

“”””
Task
The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3-Q1).

Given an array, X, of n integers and an array, F, representing the respective frequencies of X's elements,
 construct a data set, S, where each x1  occurs at frequency fi.
Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place (i.e., 12.3 format).
“””
n = int(raw_input())
x = map(int, raw_input().split())
f = map(int, raw_input().split())

s = []

for i, val in enumerate(x):
    for i in range(f[i]):
        s.append(val)

sorted_s = sorted(s)

def get_quartile(n_elem, col):
    lower_half = []
    upper_half = []
    median = 0

    if n_elem % 2 == 0:
        x = n_elem/2
        lower_half = col[:x]
        upper_half = col[x:]
        median = (upper_half[0] + lower_half[-1]) /2
    else:
        lower_half = col[:(n_elem-1)/2]
        upper_half = col[(n_elem-1)/2 + 1:]
        median = col[(n_elem-1)/2]

    return median, lower_half, upper_half


q2, lh, uh = get_quartile (len(sorted_s), sorted_s)
q1, q1_lh, q1_uh = get_quartile (len(lh), lh)
q3, q2_lh, q3_uh = get_quartile (len(uh), uh)

print float(q3 - q1)
