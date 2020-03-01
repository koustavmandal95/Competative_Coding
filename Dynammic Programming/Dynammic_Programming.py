def fib(n,arr):
    if n==0 or n==1:
        return 1
    if arr[n]>0:
        return arr[n]
    output=fib(n-1,arr)+fib(n-2,arr)
    arr[n]=output
    return output
def fib3(n):
    if n==0 or n==1:
        return 1
    return fib3(n-1)+fib3(n-2)
def fibi(n):
    arr2=[0]*(n+1)
    arr2[0]=1
    arr2[1]=1
    for i in range(2,len(arr2)):
        arr2[i]=arr2[i-1]+arr2[i-2]
    res=arr2[n]
    del arr2
    return res
if __name__=="__main__":
    n=int(input())
    arr=[0]*(n+1)
    print(fib(n,arr))
    print(fibi(n))
    print(fib3(n))