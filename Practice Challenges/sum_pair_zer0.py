def pairSum0(l):
#Implement Your Code Here
    negative_array=[]
    positive_array=[]
    for i in range(len(l)):
        if l[i]<0:
            negative_array.append(l[i])
            #l.remove(l[i])
        else:
            positive_array.append(l[i])
    print(negative_array,positive_array)
    for i in range(0,len(positive_array)):
            if abs(negative_array[i]) in positive_array:
                print(negative_array[i],positive_array[i])

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
pairSum0(l)
'''
5
2 1 -2 2 3
'''