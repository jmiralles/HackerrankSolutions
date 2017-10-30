# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

“”””
Task
The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:

The number of repairs, X , that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating A is Ca = 160 + 40X^2.
The number of repairs, , that machine  needs is a Poisson random variable with mean 1.55. The daily cost of operating B is Cb = 128 + 40X^2.

Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.

“””

from math import factorial, e

input = map(float, raw_input().split())
a = input[0]
b = input[1]

def poisson(mean, value):
    return (mean**value * e**-mean) / factorial(value)

def cost_a(x):
    return 160 + 40 * x**2

def cost_b(y):
    return 128 + 40 * y**2

def avg_cost(rate, cost_func):
    avg = 0
    for repairs in range(11):
        avg += poisson(rate, repairs) * cost_func(repairs)
    return avg

print('{:0.3f}'.format(avg_cost(a, cost_a)))
print('{:0.3f}'.format(avg_cost(b, cost_b)))
