import sys

"""

def fib(n:int):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

"""

n = int(sys.argv[1])

#print(fib(n))

ls1 = ["A","C","T","G"]
ls2 = ["A","C","T","G"]

def kmer(ls1,ls2,n):
    ls3= []
    if  n ==1:
        return ls2 #for 문으로 가지않고 여기서 리턴됨.
    for i in ls1:
        for j in ls2:
            ls3.append(i+j)
    return kmer(ls1,ls3,n-1)

a = kmer(ls1,ls2,n)
print(a)

    
