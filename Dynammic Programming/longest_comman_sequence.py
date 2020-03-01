def LCS(i,j):
    if i==len(A) or j==len(B):
        return 0
    elif A[i]==B[j]:
        return 1+LCS(i+1,j+1)
    else:
        return max(LCS(i+1,j),LCS(i,j+1))
if __name__=="__main__":
    A=input()
    B=input()
    print(LCS(i=0,j=0))