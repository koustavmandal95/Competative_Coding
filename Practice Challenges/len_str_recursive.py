def length(S,size):
    if S[size:] == '':
        return size
    return length(S,size+1)
if __name__=="__main__":
    S=str(input())
    print(length(S,size=0))