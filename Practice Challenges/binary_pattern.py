def binpattern(N):
    bit=N%2
    for i in range(N,0,-1):
        if i%2==bit:
            for j in range(0,i):
                print("1",end='')
            print("\r")
        elif i%2!=bit:
            for k in range(0,i):
                print("0",end='')
            print("\r")
if __name__=="__main__":
    N=int(input())
    binpattern(N)
 -----------------
.../...Output.../..
10
1111111111

000000000

11111111

0000000

111111

00000

1111

000

11

0
