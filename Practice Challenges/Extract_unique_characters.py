def uniqueChars(string):
    # Please add your code here
    new_list=[str(i) for i in string]
    non_duplicate=''
    for i in new_list:
        if (i in new_list) and (i not in non_duplicate):
            non_duplicate=non_duplicate+i
    print(non_duplicate)

# Main
string = input()
uniqueChars(string)
'''
ababacd

o&6nQ0DT$3
'''