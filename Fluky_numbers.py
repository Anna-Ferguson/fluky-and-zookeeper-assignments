import random
import math 


fl = 0
iterations = 0
for i in range(1,10000):
    sum = 0 
    #factors - 
    for j in range(1,i-1):
        if i % j == 0:
            random.seed(j)
            sum += random.randint(1,i)
    if sum == i:
        print(str(i) + " is a fluky number")
        fl += 1
    if fl == 7:
        break
