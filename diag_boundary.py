def sum_all():
    sum_diag_left=0
    sum_diag_right=0
    sum_boundary=0
    mid=size//2
    sub=0
    if size%2==1:
        sub=arr[mid][mid]
    for i in range(size):
        for j in range(size):
            if i==j:
                sum_diag_left=sum_diag_left+arr[i][j]
    for i in range(size-1,-1,-1):
        for j in range(size-i-1,(size-i)):
            sum_diag_right=sum_diag_right+arr[j][i]
    for i in range(size):
        if i>0 and i<size-1:
            sum_boundary=sum_boundary+arr[i][0]+arr[i][size-1]
    for i in range(size):
        if i>0 and i<size-1:
            sum_boundary=sum_boundary+arr[0][i]+arr[size-1][i]
    print(sum_diag_left+sum_diag_right+sum_boundary-sub)
if __name__=="__main__":
    size=int(input())
    arr=[]
    for i in range(size):
        arr.append(list(map(int, input().rstrip().split())))
    sum_all()
'''
5
8 18 18 1 10
12 3 13 6 19
17 11 18 10 19
10 13 12 11 14
3 1 19 11 1
0/p 232
'''