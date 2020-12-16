def triplet(arr):
    count=0
    idx_arr=[]
    for i in  range(n):
        if arr[i]%3==0:
            count=count+1
            idx_arr.append(i+1)
    print(count)
    print(idx_arr)
if __name__=="__main__":
    n = int(input())
    arr=[]
    for i in range(n):
        k = int(input())
        arr.append(k)
    triplet(arr)