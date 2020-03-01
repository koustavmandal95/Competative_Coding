import sys
def mincost(matrix,si,sj,ei,ej,output):
    if ((si==ei) and (sj==ej)):
        return matrix[ei][ej]
    if (si>ei or sj>ej):
        return sys.maxsize
    if output[si][sj]>0:
        return output[si][sj]
    option1=mincost(matrix,si+1,sj,ei,ej,output)
    option2=mincost(matrix,si+1,si+1,ei,ej,output)
    option3=mincost(matrix,si,sj+1,ei,ej,output)
    ans=matrix[si][sj]+min(option1,min(option2,option3))
    output[si][sj]=ans
    return ans
if __name__=="__main__":
    matrix=[]
    n=int(input())
    col=int(input())
    output=[[0 for i in range(col)]for j in range(n)]
    for i in range(n):
         arr = list(map(int,input().rstrip().split()))
         matrix.append(arr)
    answer=mincost(matrix,0,0,n-1,n-1,output)
    print(answer)