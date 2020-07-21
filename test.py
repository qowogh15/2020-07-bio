#!/usr/bin/python
print("test")





n=5
a=1

while n > 0:
    a*=n
    n-=1


print(a)


def greet():
    b =print("hello bioinfomatics")
     
greet()
greet()
greet()

def mysum(a:int,b:int):
    print(f"{a}+{b}={a+b}")
    return a+b
res = mysum(2,3)

print(res)


nam = input("aa:")

if nam.isalpha()==True:
    print("str")
elif nam.isnumeric()==True:
    print("int")
else:
    print("also not")


import sys

print(f"sys.argv{1}")
#print(f"run -> sample{sys.argv[1]}")



#dna1 = "ACGTACGTAAAA"
#dna2 = "TTTAAAGGAAAA"

d = {}
#for s in dna1.strip():
#    if s in d:
#        d[s]+=1
#    else:
#        d[s]= 1

#print(d)

import sys
f = sys.argv[1]

"""

with open(f,'r') as ha:
    for line in ha:
        if line.startswith(">"):
            continue
        for s in line.strip():
            if s in d:
                d[s]+=1
            else:
                d[s] =1
print(d)
total = 0
for k,v in d.items():
    total+=v
print(total)

"""

with open(f,'r') as s:
   v= s.readlines()
print(v)    
