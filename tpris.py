names = ["Apple", "Bread", "Milk", "Eggs"]
prices = [1.0, 2.50, 3.00, 4.50]
stock = [100, 20, 50, 4]

cont=True
while cont:
    print("View Inventory", "Purchase Item", "Restock Item", "Exit")
    print("To View item Press 1")
    print("To Purchase Item Press 2")
    print("To Restock Item Press 3")
    print("To Exit Press 4")
    x=int(input("Enter Your Choice: "))
    print(" ")
    if(x==1):
        print("Names\tprices\tstock")
        for i in range(len(names)):
            if(stock[i]< 5):
                print(names[i],"\t",prices[i],"\t",stock[i],"\t","-----> Stock Low Restock Needed")
            else:
                print(names[i],"\t",prices[i],"\t",stock[i])
    elif(x==4):
        break
    elif(x==2):
        pername=input("Enter the Item You want to perchase:  ")
        perqn=int(input("Enter The Number Of Item You Want to Buy:  "))
        p=0
        Flag=False
        price=0
        for i in range(len(names)):
            if(pername==names[i]):
                if(stock[i]>=perqn):
                    p=i
                    flag=True
                else:
                    print("Stock insufficient")
                    flag=False
                    break
        if(flag):
            price=prices[p]*perqn
            stock[p]=stock[p]-perqn
            print(f"Dear Customer You Need To Pay ₹{price} At The Counter")
        else:
            print(f"Dear Customer The Item {pername} You Are Trying To Find Is Unavailable At The Moment")
    elif(x==3):
        resname=input("Enter the Item You Want To Restock:  ")
        resqn=int(input("Enter The Number Of Item You Want To Restock:  "))
        if(resname in names):
            ind=names.index(resname)
            stock[ind]=stock[ind]+resqn
        else:
            resprice=float(input("Enter The Price Of Item You Want To Restock:  "))
            names.append(resname)
            stock.append(resqn)
            prices.append(resprice)
    print(" ")
        


          