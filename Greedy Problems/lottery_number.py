def lottery(s,d):
    arr=[0]*d
    arr[0]=1
    rem=s-1
    for i in range(d-1,-1,-1):
        if rem<=9 and i==0:
            arr[i]=arr[0]+rem
            rem=0
        elif rem<=9:
            arr[i]=rem
            rem=0
        else:
            arr[i]=9
            rem=rem-9
    return arr
if __name__=="__main__":
    s,d=list(map(int,input().rstrip().split()))
    arr=lottery(s,d)
    s=[""+str(i) for i in arr]
    print("".join(s))
'''
9 2
18
'''