def bit_set(N,i):
    z=N|(1<<i)
    return z
if __name__=="__main__":
    N,i=list(map(int,input().rstrip().split()))
    print(bit_set(N,i))