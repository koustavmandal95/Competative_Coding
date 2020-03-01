def magic_grid(matrix,row,col):
    dp=[[1 for i in range(col)]for j in range(row)]
    dp[row-2][col-1]=1
    dp[row-1][col-2]=1
    dp[row-1][col-1]=1
    for i in range(col-3,-1,-1):
        dp[row-1][i]=dp[row-1][i]-matrix[row-1][i+1]
    for i in range(row-3,-1,-1):
        dp[i][col-1]=dp[i][col-1]-matrix[i+1][col-1]
    print(dp)
if __name__=="__main__":
    T=int(input())
    for i in range(T):
        row,col=list(map(int,input().rstrip().split()))
        matrix=[]
        for j in range(row):
            matrix.append(list(map(int,input().rstrip().split())))
        magic_grid(matrix,row,col)
'''
1
2 3
0 1 -3
1 -2 0
'''