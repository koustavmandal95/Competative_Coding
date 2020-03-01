def staircaseDP(n,arr):
    ''' Return possible no of ways to climb n staircase using using Dynamic Prog'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    if arr[n]>0:
        return arr[n]
    ans = staircaseDP(n-3,arr)+staircaseDP(n-2,arr)+staircaseDP(n-1,arr)
    arr[n]=ans
    return ans

# Main
n=int(input())
arr=[0]*(n+1)
print(staircaseDP(n,arr))