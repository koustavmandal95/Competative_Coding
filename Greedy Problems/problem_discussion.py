def get_number(arr,k):
    arr=sorted(arr)
    small = arr[0]+k
    big = arr[len(arr)-1]-k
    if small > big:
        small,big=big,small
    for i in range(1,len(arr)-1):
        substract=arr[i]-k
        add=arr[i]+k
        if (substract>=small) or (add <=big):
            arr[i]=substract
            continue
        else:
            if (small-substract) <= (add-big):
                small=substract
            else:
                big=add
    return (big-small)
if __name__=="__main__":
    N,k=list(map(int,input().rstrip().split()))
    arr=list(map(int,input().rstrip().split()))
    print(get_number(arr,k))
'''
3 6
1 15 10
'''
