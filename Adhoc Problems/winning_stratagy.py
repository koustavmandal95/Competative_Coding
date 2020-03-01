def Stratagy(arr):
    cost=0
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==i+1:
            continue
        elif abs((i+1)-arr[i])>2:
            return ["NO"]
        elif abs((i+1)-arr[i])<=2:
            if arr[i-1]==i+1:
                arr[i],arr[i-1]=arr[i-1],arr[i]
                cost=cost+1
            elif arr[i-2]==i+1:
                arr[i-2],arr[i-1]=arr[i-1],arr[i-2]
                arr[i],arr[i-1]=arr[i-1],arr[i]  
                cost=cost+2
    return ["YES",cost]
if __name__=="__main__":
    N=int(input())
    arr=list(map(int,input().rstrip().split()))
    output=Stratagy(arr)
    for i in output:
        print(i)
'''
5
2 1 5 3 4
5
2 5 1 3 4
'''