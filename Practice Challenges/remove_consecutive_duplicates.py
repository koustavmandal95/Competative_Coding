def remove_duplicates(S):
    if len(S)==1:
        return S[0]
    if S[0]!=S[1]:
       return  S[0]+remove_duplicates(S[1:])
    else:
        return remove_duplicates(S[1:])
if __name__=="__main__":
    S=str(input())
    print(remove_duplicates(S))