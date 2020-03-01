def LIS(arr):
    output=[1]*len(arr)
    for i in range(1,len(arr)):
        for j in range(0,i):
            if arr[i]>arr[j] and output[i]<output[j]+1:
                output[i]=output[j]+1
    print(output)
    return max(output)
if __name__=="__main__":
    arr=list(map(int,input().rstrip().split()))
    print(LIS(arr))
'''
10 22 9 33 21 50 41 60
'''