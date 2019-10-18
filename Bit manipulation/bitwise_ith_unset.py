def bit_set(N,i):
    z=0
    if N&(1<<i)!=0:
        z=N^(1<<i)
    else:
         z=N^(0<<i)
    return z
if __name__=="__main__":
    N,i=list(map(int,input().rstrip().split()))
    print(bit_set(N,i))
# def bit_set(N,i):
#     z=N^(1<<i)
#     return z