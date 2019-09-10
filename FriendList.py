def friendlist(arr):
    a={}
    for i in arr:
        if i in a.keys():
            a[i]+=1
        else:
            a[i]=1
    #max_friend=[a[i] for i in a.keys()]
    value_arr=[i for i in a.values()]
    max_friend=max(value_arr)
    print(max_friend,a)
    for i in a.keys():
        if a[i]==max_friend:
            print(i,end=' ')
if __name__=="__main__":
    N=int(input())
    arr=[]
    for i in range(N):
        a,b=[int(i) for i in input().split()]
        arr=arr+[a,b]
    arr.sort()
    friendlist(arr)
'''
6
5 6
0 1
1 4
5 4
1 2
4 0
'''