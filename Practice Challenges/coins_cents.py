def dimoninsations(coins,cents):
    no_coins=0
    my_dict={}
    for i in range(len(coins)): # 1quater 25 cent , 1 dime = 10 cents , 1 Nickel =5 cents , 1 Penny = 1cent
        while cents//coins[i]!=0:
            no_coins+=cents//coins[i]
            my_dict[coins[i]]=cents//coins[i]
            cents=cents%coins[i]
        if cents==0:
            break
    print(my_dict)
    return no_coins
if __name__=="__main__":
    N=int(input("Enter the cents--> "))
    coins=[2000,500,200,100,50,20,10,5,2,1]
    print("Is any coin emptied in th cash ? (Press -1 if everything is full)")
    empty_coin=int(input())
    if empty_coin==-1:
        print(dimoninsations(coins,N))
    else:
        coins.remove(empty_coin)
        print("the minimum coins",dimoninsations(coins,N))
    