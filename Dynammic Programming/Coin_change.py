def coin_change(arr,N_Dim,V,output):
    if V==0:
        return 1
    if V<0:
        return 0
    if N_Dim<=0:
        return 0
    if output[V][N_Dim]>-1:
        return output[V][N_Dim]
    first=coin_change(arr,N_Dim,V-arr[0],output)
    second=coin_change(arr[1:],N_Dim-1,V,output)
    output[V][N_Dim]=first+second
    return first+second
if __name__=="__main__":
    N_Dim=int(input())
    arr=list(map(int,input().rstrip().split()))
    V=int(input())
    output=[[-1 for i in range(N_Dim+1)] for j in range(V+1)]
    print(coin_change(arr,N_Dim,V,output))
