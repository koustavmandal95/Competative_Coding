def group_ppl():
    for i in range(n//2):
        for j in range(i,i+1):
            sum=arr[j]+arr[n-j-1]
            print(sum//10,sum%10)
if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().rstrip().split()))
    group_ppl()

'''
---------------Input---------------
10
26 96 18 24 87 51 44 86 75 32
---------------Output--------------
5 8
17 1
10 4
6 8
13 8
------------------------------------
'''