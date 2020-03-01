import math as m
def Interesting_sequence(arr,K,L):
    arr=sorted(arr)
    cost_array=[]
    for mid in range(min(arr),max(arr)+1):
        decrease=0
        increase=0
        for num in arr:
            if num<=mid:
                increase=increase+mid-num
            else:
                decrease=decrease+num-mid
        if increase>=decrease:
            cost=decrease*K
            cost = cost + (increase-decrease)*L
            cost_array.append(cost)
        elif decrease>increase:
            continue
    return min(cost_array)
if __name__=="__main__":
    N,K,L=list(map(int,input().rstrip().split()))
    arr=list(map(int,input().rstrip().split()))
    print(Interesting_sequence(arr,K,L))    
'''

4 10 1
3 3 7 6
4 1 2
3 4 2 2
3 2 1
5 5 5
'''