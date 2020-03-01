def LIS(arr):
    inc=[1]*len(arr)
    dec=[1]*len(arr)
    for i in range(1,len(arr)):
        for j in range(0,i):
            if arr[i]>arr[j] and inc[i]<inc[j]+1:
                inc[i]=inc[j]+1
    for i in range(len(arr)-2,-1,-1):
        for cur in range(len(arr)-1,i-1,-1):
            if arr[i]>arr[cur] and dec[i]<dec[cur]+1:
                dec[i]=dec[cur]+1
    maximum = inc[0] + dec[0] - 1
    for i in range(1 ,len(arr)): 
        maximum = max((inc[i] + dec[i]-1), maximum) 
      
    return maximum 
if __name__=="__main__":
    arr=list(map(int,input().rstrip().split()))
    print(LIS(arr))
'''
6
15 20 20 6 4 2
10 22 9 33 21 50 41 60
6 17 12 30 7 5 4
2 -1 4 3 5 -1 3 2
'''