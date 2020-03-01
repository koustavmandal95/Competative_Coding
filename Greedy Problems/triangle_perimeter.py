def triangle_perimeter(arr):
    arr=sorted(arr,reverse=True)
    max_side=arr[0]
    perimeter=[0]*3
    for i in range(1,len(arr)-1):
        if max_side<(arr[i]+arr[i+1]) and arr[i]<(arr[i+1]+max_side) and arr[i+1]<(arr[i]+max_side):
            perimeter=[arr[i+1],arr[i],max_side]
    if perimeter[0]==0:
        print(-1)
    else:
        print(*perimeter)
if __name__=="__main__":
    N=int(input())
    arr=list(map(int,input().rstrip().split()))
    triangle_perimeter(arr)
'''
5
1 1 1 3 3
3
2 2 4
'''