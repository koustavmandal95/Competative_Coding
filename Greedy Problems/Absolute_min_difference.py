def abs_min(arr):
    arr1=sorted(arr)
    min=arr1[1]-arr1[0]
    for i in range(1,len(arr1)-1):
        if arr1[i+1]-arr1[i]<min:
            min=arr1[i+1]-arr1[i]
    return min
if __name__=="__main__":
    N=int(input())
    arr=list(map(int,input().rstrip().split()))
    print(abs_min(arr))
# 5
# 2 9 0 4 5