def isPalindrome(S,N_sub):
    mid=len(S)//2
    start=0 
    end=len(S)-1
    pal=False
    if len(S)==0:
        return 0
    if len(S)==1:
        return 1
    while start<end and S[start]==S[end]:
        start=start+1
        end=end-1
        if start==mid:
            pal=True
    if pal==True:
        return 1
    else:
        return 0
def palindromic_sub(S,N_sub):
    N_sum=0
    N=0
    for i in range(len(S)):
        for j in range(i,len(S)):
            N=isPalindrome(S[i:j+1],N_sub)
            N_sum=N_sum+N
    return N_sum
if __name__=="__main__":
    S=input()
    N_sub=0
    print(palindromic_sub(S,N_sub))