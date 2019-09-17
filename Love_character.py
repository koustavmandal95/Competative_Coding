def Occur(S):
    count_a=0
    count_s=0
    count_p=0
    k=[str(i) for i in S]
    for i in k :
        if i=='a':
            count_a=count_a+1
        elif i=='s':
            count_s=count_s+1
        elif i=='p':
            count_p=count_p+1
    print(count_a,count_s,count_p)
if __name__=="__main__":
    n=int(input())
    S=input()
    Occur(S)
    '''
    Ayush loves the characters ‘a’, ‘s’, and ‘p’. 
    He got a string of lowercase letters and he wants to find out how many times characters ‘a’, ‘s’, and ‘p’ 
    occurs in the string respectively.
    Help him find it out.
    '''
