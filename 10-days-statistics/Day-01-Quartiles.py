
# https://www.hackerrank.com/challenges/s10-quartiles/problem

“”””
Task
Given an array, X, of  integers, calculate the respective first quartile (Q1), second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.

“””
n_elem = int(raw_input())
col = sorted(map(int, raw_input().split()))

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

q2, lh, uh = get_quartile (n_elem, col)
q1, q1_lh, q1_uh = get_quartile (len(lh), lh)
q3, q2_lh, q3_uh = get_quartile (len(uh), uh)

print q1
print q2
print q3
