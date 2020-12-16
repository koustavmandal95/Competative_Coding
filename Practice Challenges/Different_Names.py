def differentNames(l):
    # Please add your code here
    name_counter={}
    for name in l:
        if name in name_counter.keys():
            name_counter[name]=name_counter[name]+1
        else:
            name_counter[name]=1
    k = [int(i) for i in name_counter.values() if i>1]
    repeated_name=[i for i in name_counter.keys() if name_counter[i]>1]
    return name_counter


# Main
names=input().strip().split()
m=differentNames(names)
counter=0
if m:
    for name in m:
        if m[name]>1:
            print(name, m[name])
    if counter == 0:
        print(-1)
#Abhishek harshit Ayush harshit Ayush Iti Deepak Ayush Iti
#Abhishek Harshit Ayush Iti