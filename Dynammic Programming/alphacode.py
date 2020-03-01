prime=1000000009
def alphacode(arr):
    output=[0]*(len(arr)+1)
    output[0]=1
    output[1]=1
    for i in range(2,len(arr)+1):
        output[i]=output[i-1]
        if (arr[i-2]*10+arr[i-1])<=26:
            output[i]=output[i]+output[i-2]
    return output[len(arr)]%prime
if __name__=="__main__":
    while 1:
        S=str(input())
        if S!="0":
            arr=[int(i) for i in S]
            print(alphacode(arr))
        elif int(S)==0:
            exit(0)
'''
25114
1111111111
333333333
0
'''