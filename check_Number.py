def checkNumber(arr, x,n):
    # Please add your code here
    if x == arr[n-1]:
        return True
    elif n == 0:
        return False
    else:
        return checkNumber(arr,x,n-1)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr,x,n):
    print('true')
else:
    print('false')
'''
3
9 8 10
8
'''
