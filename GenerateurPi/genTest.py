from math import *
input = open("generated.txt","r")
content = input.read().splitlines()
myGen=[]
pythonGen = []
for a in content:
    a =a.split('\t')
    myGen.append(float(a[0]))
    pythonGen.append(float(a[1]))

def ni(gen):
    partition2 = []
    for i in range(0,20):
        partition2.append(0)


    for x in gen:
        i = 0.05
        pos = 0
        while (x > i):
            i = i+0.05
            pos +=1
        partition2[pos] += 1
    return partition2

partition1 = ni(myGen)
partition2 = ni(pythonGen)

def Kr(partition,N):
    res = 0
    for r in range(0,20):
        val = ((partition[r]-N*0.05)/sqrt(N*0.05))**2
        res += val
    return res


#print(Kr(partition1,1000000))
#print(Kr(partition2,1000000))
def fct_empirique(gen,x):
    res = 0.0
    for t in gen:
        if t <= x:
            res +=1
    return res/len(gen)
def Dmax(gen):
    maximum = 0
    x=0.0
    while (x <1):
        t = fct_empirique(gen,x)-x
        if  t> maximum:
            maximum = t
        x+= 0.01
    return maximum

def getNechantillion(gen,n):
    i = 0
    res = []
    while i < len(gen):
        res.append(gen[i])
        i+=int(len(gen)/n)
    return res

myGen2 = getNechantillion(myGen,100000)
pythonGen2 = getNechantillion(pythonGen,100000)
print(len(myGen2))
print(Dmax(myGen2))
print(Dmax(pythonGen2))
#print(Dmax(pythonGen))
#print(1.07/sqrt(1000000))
#print(1.63/sqrt(1000000))
