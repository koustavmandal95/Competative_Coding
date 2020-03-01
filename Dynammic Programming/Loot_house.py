def Loot(arr,N):
    loot=[0]*N
    loot[0]=arr[0]
    if N>1:
        loot[1]=max(arr[0],arr[1])
    for i in range(2,N):
        loot[i]=max(arr[i]+loot[i-2],loot[i-1])
    return max(loot)
if __name__=="__main__":
    N=int(input())
    arr=list(map(int,input().rstrip().split()))
    print(Loot(arr,N)))
'''
6
5 5 10 100 10 5
'''