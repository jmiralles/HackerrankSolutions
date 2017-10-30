# https://www.hackerrank.com/challenges/s10-mcq-7/problem

“”””
Task

Andrea has a simple equation:
    Y = a + b1 * f1 + b1 * f2 + ... + bm * fm

for (m + 1) real constants (a, f1, f2, ..., fm).
We can say that the value of Y depends on m features.
 Andrea studies this equation for  different feature sets (f1, f2, f3, ..., fm)
 and records each respective value of Y.
  If she has q new feature sets, can you help
  Andrea find the value of Y for each of the sets?
“””

from sklearn import linear_model

m,n = raw_input().split()
inputs = []
for i in range(int(n)):
    inputs.append([float(j) for j in raw_input().split()])

y = [x.pop() for x in inputs]
f = input() # Record the number of 'features' that you will apply the linear model to!
x = []
for k in range(f): # The next series of inputs are the values of x1, x2 to be used later
    x.append([float(l) for l in raw_input().split()])

lm = linear_model.LinearRegression()
lm.fit(inputs, y)
a = lm.intercept_
b = lm.coef_

for m in range(0, len(x)):
    out = a + x[m][0] * b[0] + x[m][1] * b[1]
    print out
