def bit_set(N):
    z=0
    for i in range(N//2):
        if N&(1<<i)!=0:
            z= N&(1<<i)
            return z
        else:
            z=N^(0<<i)
if __name__=="__main__":
    N=int(input())
    print(bit_set(N))