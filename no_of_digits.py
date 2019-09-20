def digits(N,digit):
    if N==0:
        return digit
    else:
        digit=digit+1
    return digits(N//10,digit)

if __name__=="__main__":
    N=int(input())
    print(digits(N,digit=0))