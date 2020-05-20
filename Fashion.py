dress=[{"id":1001,"Name":"Tops","Available":10,"Price":250,"Original_Price":200},
       {"id":1002,"Name":"Pants","Available":12,"Price":500,"Original_Price":450},
       {"id":1003,"Name":"Sarees","Available":100,"Price":750,"Original_Price":700},
       {"id":1004,"Name":"Shorts","Available":20,"Price":350,"Original_Price":300},
       {"id":1005,"Name":"Kurtas","Available":15,"Price":400,"Original_Price":300}]
dress1=dress
temp=[]
order=""


def adminLogin():
    print("*********************")
    print("1.Display Menu")
    print("2.Add item")
    print("3.Remove item")
    print("4.Total goods available")
    print("5.Income and Loss")
    print("6.Logout")
    print("*********************")
    

def adminDisplayMenu():
    print("Id\tName\tAvailable\tPrice\tOriginal Price")
    print("***************************************************")
    for d in dress:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}\t{d["Original_Price"]}')
        
                       
def addItem():
    n=int(input("Enter the no.of.items need to be added : "))
    for i in range(n):
        new_id=int(input("Enter id : "))
        new_Name=input("Enter Name : ")
        new_Available=int(input("Enter Available : "))
        new_Price=int(input("Enter Price : "))
        new_original=int(input("Enter the original price : "))
        d=[{"id":new_id,"Name":new_Name,"Available":new_Available,"Price":new_Price,"Original_Price":new_original}]
        dress.extend(d)
        adminDisplayMenu()
        
def removeItem():
    
    dressId=int(input("Enter the id need to be deleted : "))
    found=False
    for d in dress1:
        found=d["id"]==dressId
        if found !=True:
            temp.append(d)
            continue
        if found==True:
            d["Available"]-=1
    print("Deleting item....")
    if len(temp)==d:
        print(f"{dressId} not found")
    else:
        print(f"{dressId}'s one available is removed from the list")
    adminDisplayMenu()
def goods():
    Total=0
    print("\n")
    for d in dress:
        print(f'{d["Name"]} = {d["Available"]}')
        Total+=(d["Available"])
    print("\nTotal available goods is : ",Total)
def incomeLoss():
    total=0
    for d in dress:
        total+=((d["Available"]*d["Price"])-(d["Available"]*d["Original_Price"]))
    print("\nTotal income or loss is : ",total)
    
def logout():
    login()

    

def adminChoice():
    choice=int(input("Please enter user choice : "))
    if choice==1:
        adminDisplayMenu()
        print("\n***************************************************\n")
        adminLogin()
        print("\n***************************************************\n")
        adminChoice()
    elif choice==2:
        adminDisplayMenu()
        print("\n***************************************************\n")
        addItem()
        print("\n***************************************************\n")
        adminLogin()
        print("\n***************************************************\n")
        adminChoice()
    elif choice==3:
        adminDisplayMenu()
        print("\n***************************************************\n")
        removeItem()
        print("\n***************************************************\n")
        adminLogin()
        print("\n***************************************************\n")
        adminChoice()
    elif choice==4:
        goods()
        print("\n***************************************************\n")
        adminLogin()
        print("\n***************************************************\n")
        adminChoice()
    elif choice==5:
        incomeLoss()
        print("\n***************************************************\n")
        adminLogin()
        print("\n***************************************************\n")
        adminChoice()
    elif choice==6:
        logout()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n***************************************************\n")
        adminLogin()
        print("\n***************************************************\n")
        adminChoice()


    


def userLogin():
    print("*********************\n")
    print("1.Display Menu")
    print("2.Place order")
    print("3.Cancel order")
    print("4.Logout")
    print("\n*********************")
def userDisplayMenu():
                print("Id\tName\tAvailable\tPrice")
                print("***************************************************")
                for d in dress:
                    print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
def user_id():
    userDisplayMenu()
    p_id=int(input("\nEnter the id : "))
def placeOrder():
    order_number=10
    userDisplayMenu()
    p_id=int(input("\nEnter the id : "))
    
    for d in dress:
        if d["id"]==p_id:
            print("\nId\tName\tAvailable\tPrice")
            print("***************************************************")
            print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
            order='{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}'
            conform=input("\nDo you want to place an order on the above shown product : Y/N ")
            
            if conform=='Y' or conform=='y':
                print("\nSuccessfully placed the order on the product {} {}".format(d["id"],d["Name"]))
                order_number+=1
                print("Your order number is : ",order_number)
                d["Available"]-=1
                break
                
            elif conform=='N' or conform=='n' :
                print("The order is not placed. You can carry on with you purchase. Happy shopping!!!!")
                break
            else:
                print("\nYou have entered wrong option. Please enter again\n")
                conform=input("\nDo you want to place an order on the above shown product : Y/N ")
                break
            
        
    if d["id"]!=p_id:
        print("\nYou have entered invalid id. Please enter valid id\n")
        user_id()            
    print("\nAvailable products : \n")    
    userDisplayMenu()
    
def cancelOrder():
    found=False
    temp=[]
    order_id=input("Enter the order id : ")
    for d in dress:
        found=d["id"]==order_id
        if found!=True:
            temp.append(d)
    if len(temp)==d:
        print(f'{order_id} is not found')
    else:
        print(f'{order_id} is removed from the placed order')
    
def userChoice():
    choice=int(input("Please enter user choice : "))
    if choice==1:
        userDisplayMenu()
        print("\n***************************************************\n")
        userLogin()
        print("\n***************************************************\n")
        userChoice()
    elif choice==2:
        placeOrder()
        print("\n***************************************************\n")
        userLogin()
        print("\n***************************************************\n")
        userChoice()
    elif choice==3:
        cancelOrder()
        print("\n***************************************************\n")
        userLogin()
        print("\n***************************************************\n")
        userChoice()
    elif choice==4:
        logout()
    else:
        print("Invalid Choice. Please enter valid choice")
            

def login():
    tp=input("Admin/User [A/U] : ")
    if tp=='A' or tp=='a' :
        password=input("Enter the password : ")
        if password=="abc":
            adminLogin()
            adminChoice()    
        else:
            print("Invalid password. Please enter valid password")

    elif tp=='U' or tp=='u':
        password=input("Enter the password : ")
        if(password=="123"):
            userLogin()
            userChoice()
        else:
            print("Invalid password. Please enter valid password")
    else:
        print("Invalid user type. Enter valid user type")
login()

    


        




