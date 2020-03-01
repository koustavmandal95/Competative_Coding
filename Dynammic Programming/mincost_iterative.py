def mincost(matrix,m,n):
    dp=[[0 for i in range(n)]for j in range(m)]
    dp[m-1][n-1]=matrix[m-1][n-1]
    for i in range(n-2,-1,-1):
        dp[m-1][i]=dp[m-1][i+1]+matrix[m-1][i]
    for i in range(m-2,-1,-1):
        dp[i][n-1]=dp[i+1][n-1]+matrix[i][n-1]
    for i in range(m-2,-1,-1):
        for j in range(n-2,-1,-1):
            dp[i][j]=matrix[i][j]+min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
    return dp[0][0]
if __name__=="__main__":
    matrix=[]
    m=int(input())
    n=int(input())
    for i in range(m):
         arr = list(map(int,input().rstrip().split()))
         matrix.append(arr)
    answer=mincost(matrix,m,n)
    print(answer)