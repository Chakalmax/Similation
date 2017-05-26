import time
import random

x = time.time()
def linear_congruence():
    global x
    a = 3
    c = 5
    m = 1000000
    y = (a*x + c) % m
    value = []
    for i in range(0,6):
        x = y
        y = (a*x + c) % m
        value.append((int(y)))
    return value

lo = []

fichier = open("piDecimal.txt", "r")
decimal = fichier.read()
pi = []
for line in decimal:
    line = line.strip()
    line = line.splitlines()
    for i in line:
        pi.append(i)
def gen_random(x):
    value = linear_congruence()
    result = 0
    for t in value:
        result = result + int(pi[t])
        result *= 10
    result /= 10000000
    return result

output = open("generated.txt","w")

for a in range (0, 1000000):
    lo.append(x)
    result= gen_random(x)
    #print(str(result))
    
    output.write(str(result))
    output.write("\t")
    r= random.random()
    output.write(str(r))
    output.write("\n")
output.close()

