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
if __name__=="__main__":
    N=int(input("Enter the number:--> "))
    revnutri(N)
'''
=================== RESTART: K:/python files/revnumtri.py ===================
Enter the number:--> 3
ABCCBA

 ABBA 

  AA  

=================== RESTART: K:/python files/revnumtri.py ===================
Enter the number:--> 4
ABCDDCBA

 ABCCBA 

  ABBA  

   AA   

'''
