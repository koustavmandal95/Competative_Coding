def revnum(N):
    for i in range(1,N+1):
            for j in range(((i*(i+1))//2)-i+1,((i*(i+1))//2)+1):
                print(j,end='')
                if j>=9:
                    for k in range()
            print("\r")
if __name__=="__main__":
    N=int(input())
    revnum(N)