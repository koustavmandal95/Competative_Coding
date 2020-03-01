def lps(S):
    m=0
    for i in range(0,len(S)):
        l=i
        r=i
        while l>=0 and r<len(S) and S[l]==S[r]:
            cur_len=(r-l)+1
            if cur_len>m:
                m=cur_len
            l=l-1
            r=r+1
        l=i
        r=i+1
        while l>=0 and r<len(S) and S[l]==S[r]:
            cur_len=(r-l)+1
            if cur_len>m:
                m=cur_len
            l=l-1
            r=r+1
    return m
if __name__=="__main__":
    S=input()
    print(lps(S))
# oyvvlkbcpkjxldxwsejw
