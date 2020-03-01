def get_student(elem,traversal,list1):
    idx=list1.index(elem)
    if idx+traversal>=len(list1):
        rem_traveral=traversal-(len(list1)-len(list1[:idx]))
        print(list1[rem_traveral])
    else:
        print(list1[idx+traversal])
if __name__=="__main__":
    list1=[0,1,2,3,4,5,6,7,8,9,10,11]
    N=int(input())
    for i in range(N):
        elem,traversal=list(map(int,input().rstrip().split()))
        get_student(elem,traversal,list1)
'''
2
2 3
5 8
10
9 4
3 7
9 5
0 5
2 1
2 8
4 11
6 4
1 12
6 6
'''
