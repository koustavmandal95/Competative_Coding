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
 O/p
 Please give a number:-7
1 

3 2 

4 5 6 

10 9 8 7 

11 12 13 14 15 

21 20 19 18 17 16 

22 23 24 25 26 27 28 
