def patternA(N):
    a=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(N+1):
        for j in range(0,i):
            print(a[i-1],end='')
        print('\r')
def patternE(N):
    a=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(N+1,0,-1):
        for j in range(i,N+1):
            print(a[j-1],end='')
        print('\r')
def triAngle(N):
    for i in range(0,N):
        for k in range(i):
            print(" ",end="")
        for j in range(N,i,-1):
            print("*",end="")
        print("\r")
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
def Numpattern(N):
    for i in range(N,0,-1):
        for k in range(i,N):
            print(k,end='')
        for j in range(i,0,-1):
            print(N,end="")
        print("\r")
if __name__=="__main__":
    N=int(input())
    Numpattern(N)

