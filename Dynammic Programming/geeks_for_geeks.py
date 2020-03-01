'''
lis[i] ==> Longest Increasing subsequence ending with arr[i] 
lds[i] ==> Longest decreasing subsequence starting with arr[i] 
'''
def bitonic(arr, n): 
      
    # Length of increasing subarray ending at all indexes 
    inc = [0] * n  
      
    # Length of decreasing subarray starting at all indexes 
    dec = [0] * n 
      
    # length of increasing sequence ending at first index is 1 
    inc[0] = 1
      
    # length of increasing sequence starting at first index is 1 
    dec[0] = 1
  
    # Step 1) Construct increasing sequence array 
    for i in range(1,n): 
        if arr[i] >arr[i-1]: 
            inc[i] = inc[i-1] + 1
        else: 
            inc[i] = 1
  
    # Step 2) Construct decreasing sequence array 
    for i in range(0,n-1): 
        if arr[i] > arr[i+1]: 
            dec[i] = dec[i+1] + 1
        else: 
            dec[i] = 1
  
    # Step 3) Find the length of maximum length bitonic sequence 
    print(inc,dec)
    maxi = inc[0] + dec[0] - 1
    for i in range(n): 
        if inc[i] + dec[i] - 1 > maxi: 
            maxi = inc[i] + dec[i] - 1
  
    return maxi
  
# Driver program to test above function 
if __name__=="__main__":
    arr=list(map(int,input().rstrip().split()))
    n = len(arr) 
    print(bitonic(arr, n))
'''
6 17 12 30 7 5 4
15 20 20 6 4 2
10 22 9 33 21 50 41 60
6 17 12 30 7 5 4
2 -1 4 3 5 -1 3 2
'''