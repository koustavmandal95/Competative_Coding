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
'''

7 --> Input 
O/P below-
7777777

6777777

5677777

4567777

3456777

2345677

1234567
