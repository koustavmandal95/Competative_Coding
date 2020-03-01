import math as m
def Zero_groups(arr,X,Y):
    cost=0
    toggle=0
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            toggle=toggle+1
    if toggle in (1,0):
        if arr[0]==1:
            return 0
        else:
            cost=Y
            return cost
    elif toggle==2:
        Zeros=2
    elif toggle%2==0:
        Zeros=toggle//2
    elif toggle%2==1:
        Zeros=toggle//2+1
    else:
        return 0
    return ((Zeros-1)*min(X,Y)+Y)
if __name__=="__main__":
    N,X,Y=list(map(int,input().rstrip().split()))
    arr=[int(i) for i in  input()]
    print(Zero_groups(arr,X,Y))
'''
8 2 3
10101010
7 2 3
1111111
'''