def make_same(a,b):
    cost=0
    i=0
    arr1=[int(i) for i in a]
    arr2=[int(i) for i in b]
    while i < len(arr1):
        if arr1[i]==arr2[i]:
            i=i+1
            continue
        elif arr1[i]!=arr2[i]:
            if i+1 < len(arr1) and arr1[i+1]!=arr1[i] and arr1[i+1]!=arr2[i+1]:
                arr2[i],arr2[i+1]=arr2[i+1],arr2[i]
                cost = cost+1
                i=i+2
            else:
                arr2[i]=arr2[i]^1
                cost=cost+1
                i=i+1
    print(arr1,arr2,cost)
if __name__=="__main__":
    num1=[i for i in input().split(' ')]
    num2=[i for i in input().split(' ')]
    a,b=num1[0],num2[0]
    make_same(a,b)
'''
10001
00110
'''