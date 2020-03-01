def Miles_walk(arr):
    new_arr=sorted(arr,reverse=True)
    Miles=0
    for i in range(0,len(new_arr)):
        Miles=Miles+pow(2,i)*new_arr[i]
    return Miles
if __name__=="__main__":
    N=int(input())
    arr=list(map(int,input().rstrip().split()))
    print(Miles_walk(arr))