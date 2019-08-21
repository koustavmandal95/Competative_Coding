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
if __name__=="__main__":
    N=int(input("Please give a number:-"))
    Butterfly(N)
Please give a number:-10
*                  *

**                **

***              ***

****            ****

*****          *****

******        ******

*******      *******

********    ********

*********  *********

********************

*********  *********

********    ********

*******      *******

******        ******

*****          *****

****            ****

***              ***

**                **

*                  *
