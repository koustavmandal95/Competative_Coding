def FindUnique(arr):
    # Please add your code here
    arr=[str(i) for i in arr]
    repeat={}
    for i in arr:
        if i in repeat.keys():
            repeat[i]=repeat[i]+1
        else:
            repeat[i]=1
    for i in repeat.keys():
        if repeat[i]==1:
            k=int(i)
    return k
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
unique=FindUnique(arr)
print(unique)
'''
7
2 3 1 6 3 6 2
'''