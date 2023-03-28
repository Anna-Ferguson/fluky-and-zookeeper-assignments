import random
e1 = 0
e2 = 0
n = 0
while n < 100000:
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    if num1 == 1 or num1 == 2 or num2 == 1 or num2 == 2:
        e1 += 1
    elif num1 == num2:
        e2 += 1
    n += 1


pen1 = (e1/100000) * 100
pen2 = (e2/100000) * 100
a= ("{0:.2f}".format(pen1))
b = ("{0:.2f}".format(pen2))
if 0.31 <= pen1 <= 0.35:
    msg = "The zookeeper was correct"
else:
    msg = "The Custodian was correct"

if .14 <= pen2 <= .18:
    msg = "The zookeeper was correct"
else:
    msg = "The Custodian was correct"

print(str(a) + "% of the time there was at least one elephant in the pen")
print(str(b) + "% of the time there was two elephants in the pen")
print(msg)
print(" ")






