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
def revnutri(N):
    a=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(0,N):
        for j in range(0,i):
            print(" ",end='')
        for c in range(0,N-i):
            print(a[c],end='')
        for c1 in range(N-i-1,-1,-1):
            print(a[c1],end='')
        for k in range(0,i):
            print(" ",end='')
        print("\r")
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
def Butterfly(N):
    for i in range(0,2*N):
        if i<N:
            for j in range(0,i+1):
                print("*",end='')
            for s in range((i+1),(2*N-(i+1))):
                print(" ",end='')
            for k in range(0,i+1):
                print("*",end='')
            print("\r")
        elif i>N:
            for j1 in range(i,2*N):
                print("*",end='')
            for s1 in range(2*N-i,i):
                print(" ",end='')
            for k1 in range(i,2*N):
                print("*",end='')
            print("\r")
def revnum(N):
    for i in range(1,N+1): # Hint what is the summation of n elements ?
        if i%2==1:
            for j in range(((i*(i+1))//2)-i+1,((i*(i+1))//2)+1):
                print(j,end=' ')
        if i%2==0:
            for j in range(((i*(i+1))//2),((i*(i+1))//2)-i,-1):
                print(j,end=' ')
        print("\r")
if __name__=="__main__":
    N=int(input("Please give a number:-"))
    revnum(N)



