def sumArray(arr,size,n,sum):
    # Please add your code here
    if size == 0:
        return sum
    else:
        sum=sum+arr[n-size-1]
        return sumArray(arr,size-1,n,sum)
if __name__=="__main__":
    N = int(input())
    sum=0
    for _ in range(N):
        #print(sum_rec(map(int, list(input().strip('\r'))),sum=0))
        array=list(map(int,list(input().strip('\r'))))
        n=len(array)
        size=n
        print(sumArray(array,size,n,sum=0))
'''
2
1547 
45876
10
2589079827616848659
8127150368270901392
4097029834046084078
6721479242603409196
4827652636861795532
7030965249904816878
36792244416222129
4025425973848197842
2846313811217792334
588590103798690546
'''