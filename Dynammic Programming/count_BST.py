prime=1000000007
def count_Bst(N):
    arr=[0 for i in range(N+1)]
    bst_arr=[i for i in range(0,N+1)]
    arr[0]=1
    arr[1]=1
    for i in range(2,len(bst_arr)):
        for k in range(0,i):
            arr[i]=arr[i]+arr[k]*arr[i-k-1]
    print(bst_arr)
    print(arr)
    print(arr[N]%prime)
if __name__=="__main__":
    N=int(input())
    count_Bst(N)