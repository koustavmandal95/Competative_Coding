def galaxystar(N):
    N_new=N
    N_mid=m.ceil(N/2)
    if N%2==0:
        N_new=N+1
        N_mid=m.ceil(N_new/2)
    for i in range(1,N_new+1):
        if i<=N_mid:
            for c in range(0,i):
                print("*",end='')
            print("\r")
        if i>N_mid:
            for c1 in range(i-N_mid,N_mid):
                print("*",end='')
            print("\r")
if __name__=="__main__":
    N=int(input("Please give a number:-"))
    galaxystar(N)     
'''
Please give a number:-4
*

**

***

**

*

>>> 
 RESTART: C:/Users/koustavx/Downloads/training materials/Python_work/pattern2.py 
Please give a number:-3
*

**

*

>>> 
 RESTART: C:/Users/koustavx/Downloads/training materials/Python_work/pattern2.py 
Please give a number:-2
*

**

*

>>> 
 RESTART: C:/Users/koustavx/Downloads/training materials/Python_work/pattern2.py 
Please give a number:-5
*

**

***

**

*

'''
