def Activity_max(arr):
    arr=sorted(arr,key=lambda t:t[1])
    task_counter=1
    activity_selected=arr[0][1]
    for i in range(1,len(arr)):
        if arr[i][0]>=activity_selected:
            activity_selected=arr[i][1]
            print(arr[i])
            task_counter+=1
    return task_counter
if __name__=="__main__":
    d=int(input())
    arr=[]
    for i in range(d):
        s,f=list(input().rstrip().split())
        arr.append([int(s),int(f)])
    print(Activity_max(arr))
'''
16
24010 43531
53618 78750
18901 27061
28374 47320
62980 90727
16758 61710
8739 36915
21947 46698
22523 70367
40840 77256
24135 43993
23864 74931
35779 97355
23197 44902
31258 66308
37892 67279
'''