def mex(arr):
    arr.sort(reverse=False)
    print(arr)
    if arr[0]==0:
        for i in range(0,len(arr)-1):
            if arr[i+1]-arr[i]!=1:
                return arr[i+1]
        return arr[len(arr)-1]+1
    else:
        return 0
def grundey(n,arr):
    if n<=0:
        return 0
    if n==1:
        return 1
    if arr[n]!=-1:
        return arr[n]
    elif n==1:
        ans=mex([grundey(n-1,arr)])
        arr[n]=ans
    elif n==2:
        ans=mex([grundey(n-1,arr),grundey(n-2,arr)])
        arr[n]=ans
    if n>2:
        ans=[grundey(n-1,arr),grundey(n-2,arr),grundey(n-3,arr)]
        print("here is :",ans)
        return
        arr[n]=ans
if __name__=="__main__":
    N = int(input())
    arr = [-1]*(N+1)
    grundey(N,arr)