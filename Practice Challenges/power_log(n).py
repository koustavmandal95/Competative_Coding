def power(base,N):
    if N==0:
        return 1
    #print("calling before base case is evaluated ",N)
    partial_sum=power(base,N//2)
    result=partial_sum*partial_sum
    if N%2==1:
        result = result*base
    #print("---------------/////\\\\\\\----------")
    #print("retriving after base case is evaluated ",N)
    return result
if __name__=="__main__":
    base,N= input().split()
    print(power(int(base),int(N)))