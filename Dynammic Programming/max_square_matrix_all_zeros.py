def square(matrix,row,col):
    exp_matrix=[[0 for i in range(col)] for j in range(row)]
    for i in range(0,col):
        if matrix[0][i]==0:
            exp_matrix[0][i]=1
    for i in range(1,row):
        if matrix[i][0]==0:
            exp_matrix[i][0]=1
    # print(exp_matrix)
    for r in range(1,row):
        for c in range(1,col):
            if matrix[r][c]==1:
                continue
            exp_matrix[r][c]=min(exp_matrix[r-1][c-1],exp_matrix[r][c-1],exp_matrix[r-1][c])+1
            # print(min(matrix[0][0],matrix[1][0],matrix[0][1]))
    # print(exp_matrix)
    maximum=exp_matrix[0][0]
    for r in range(0,row):
        for c in range(0,col):
           if maximum<exp_matrix[r][c]:
                maximum=exp_matrix[r][c]
    print(maximum)
if __name__=="__main__":
    row,col=list(map(int,input().rstrip().split()))
    matrix=[]
    for i in range(row):
        matrix.append(list(map(int,input().rstrip().split())))
    square(matrix,row,col)
'''
3 3
1 1 0
1 1 1
1 1 1
'''