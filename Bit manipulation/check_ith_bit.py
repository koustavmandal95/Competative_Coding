def bit_set(N,i):
    if N&(1<<i)!=0:
        return 1
    else:
        return 0
if __name__=="__main__":
    N,i=list(map(int,input().rstrip().split()))
    print(bit_set(N,i))