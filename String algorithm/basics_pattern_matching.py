def pattern_match(seq,pat):
    seq=[str(i) for i in seq]
    pat=[str(i) for i in pat]
    print(seq,pat)
    for i in range(0,len(seq)-len(pat)):
        count=0
        for j in range(0,len(pat)):
            
            if pat[j]==seq[i+j]:
                count=count+1
                if count==len(pat):
                    print(i)
                    return 
    print(-1)
if __name__=="__main__":
    seq=input()
    pat=input()
    pattern_match(seq,pat)