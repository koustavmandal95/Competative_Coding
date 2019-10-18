import math as m
def bit_set(N):
    z=0
    for i in range(N//2+1):
        if N&(1<<i)!=0:
            z= N^(1<<i)
            return z
if __name__=="__main__":
    N=int(input())
    print(bit_set(N))