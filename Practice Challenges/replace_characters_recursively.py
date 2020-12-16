def replace_char(S,front,back,lookup,replace):
    if front>back:
        S="".join(S)
        return S
    if S[front]==lookup:
        S[front]=replace
    if S[back]==lookup:
        S[back]=replace
    return replace_char(S,front+1,back-1,lookup,replace)
if __name__=="__main__":
    S=str(input())
    S=[str(i) for i in S]
    char=input().split(' ')
    lookup=char[0]
    replace=char[1]
    front=0
    back=len(S)-1
    print(replace_char(S,front,back,lookup,replace))
'''
abacd
a x
import string
if __name__=="__main__":
    S=str(input())
    char=input().split(' ')
    lookup=char[0]
    replace=char[1]
    print(S.replace(lookup,replace))
if S[0]==lookup:
    S[0]=replace
size=size+1
'''