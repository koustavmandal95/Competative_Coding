def lcsHelper(A,B,m,n,dp):
    if m==0 or n==0:
        return 0
    if dp[m][n]>-1:
        return dp[m][n]
    if A[0]==B[0]:
        ans=1+lcsHelper(A[1:],B[1:],m-1,n-1,dp)
    else:
        option1 = lcsHelper(A,B[1:],m,n-1,dp)
        option2 = lcsHelper(A[1:],B,m-1,n,dp)
        ans=max(option1,option2)
    dp[m][n]=ans
    return ans
def LCS(A,B):
    m=len(A)
    n=len(B)
    dp=[[-1 for i in range(n+1)]for j in range(m+1)]
    print(lcsHelper(A,B,m,n,dp))
if __name__=="__main__":
    A=input()
    B=input()
    LCS(A,B)