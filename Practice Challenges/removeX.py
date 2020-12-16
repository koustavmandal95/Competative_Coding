def removeX(S):
    if S[0:]==[]:
        return ''
    if S[0]!='x':
        return S[0]+removeX(S[1:])
    else:
        i=1
        for i in range(1,len(S)):
             S[i-1]=S[i]
        S[-1]=''
        return removeX(S)
def length(S):
    if S[0:]==[]:# when S is string S[0:]=='' works when it's an array S==[] works
        return 0
    return 1+length(S[1:])
if __name__=="__main__":
    S = str(input())
    S=[str(i) for i in S]
    #print(S)
    l=length(S)
    print(l)
    result=removeX(S)
    print(result)
    print(l)