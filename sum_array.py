def sumArray(sum,arr,size,n):
    # Please add your code here
    if size == 0:
        return sum
    else:
        sum=sum+arr[n-size-1]
        return sumArray(sum,arr,size-1,n)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
size=n
arr=list(int(i) for i in input().strip().split(' '))
sum=0
print(sumArray(sum,arr,size,n=len(arr)))