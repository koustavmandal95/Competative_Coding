import math as m
def prime(N):
    count=0
    for i in range(1,N):
        if isPrime(i)==True:
            count=count+1
    return count
def isPrime(N):
    count=0
    checkRange=m.floor((m.sqrt(N)))
    for j in range(1,checkRange+1):
        if N%j==0:
            count=count+2
    if count==2:
        return True
    else:
        return False
if __name__=="__main__":
    N=int(input())
    print(prime(N))