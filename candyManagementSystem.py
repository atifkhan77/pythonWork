print("\t\t\t\t      ~~CANDY MANAGEMENT SYSTEM~~")#Program title
print("--"*50) #Formatting
candy_dic = {} #Empty dictionary for candy
customer_dic = {} #Empty dictionary for customer
sale_dic = {} #Empty dictionary for sale
def candy_add(): #Adding detail function
     print("\n**************ADD PRODUCT RECORD**************")#Formatting 
     a_confirmation = "y" #confirmation
     option = True #checks whether the ID Already exists or not in True case
     while a_confirmation =="y" or a_confirmation =="Y": #confirmation loop
         while True: #while loop
             try: #checking if there is any error in input
                 ID = eval(input ("\nEnter the product ID: ")) #Enter unique product ID to proceed
                 break #if user enters correct input loop will break
             except: #checks error type
                print("Wrong input.You have to enter digits only") #indicates error
         if option ==False: #False option
             if ID in candy_dic.keys(): #condition checks whether ID is in candy dictionay or not
                   print("ID already exist.Try another one") #already exist
             else: #condition
                 while True: #while loop
                     name=input( "\nEnter name of the product: ") #Enter product name
                     if name.isalpha() or (" " in name) ==True: #condition
                         break #if user enters correct input loop will break
                     else: #condition
                         print("Wrong input.You have to enter Alphabets only") #indicates error
                         
                 while True: #while loop
                     try: #checking if there is any error in input
                         quantity=eval(input("\nEnter the quantity of product: ")) #Enter product quantity
                         break #if user enters correct input loop will break
                     except: #checks error type
                         print("Wrong input.You have to enter digits only") #indicates error
                 while True: #while loop
                     try: #checking if there is any error in input
                         price=eval(input("\nEnter the price of product: ")) #Enter product price
                         break #if user enters correct input loop will break
                     except: #checks error type
                         print("Wrong input.You have to enter digits only") #indicates error
                 while True: #while loop
                     a_confirmation = input("\nEnter y to continue or any alphabet to end adding process: ")  #confirmation
                     if a_confirmation.isalpha() or (" " in a_confirmation) ==True: #condition
                         break #if user enters correct input loop will break
                     else: #condition
                         print("Wrong input.You have to enter Alphabets only") #indicates error
                     
                 candy_dic[ID]=[name,quantity,price] #input storing in dic
         else: #condition
             while True: #while loop
                 name=input( "\nEnter name of the product: ") #Enter product name
                 if name.isalpha() or (" " in name) ==True:  #condition
                     break #if user enters correct input loop will break
                 else: #condition
                     print("Wrong input.You have to enter Alphabets only") #indicates error
             while True: #while loop
                 try: #checking if there is any error in input
                     quantity=eval(input("\nEnter the quantity of product: ")) #Enter product quantity
                     break #if user enters correct input loop will break
                 except: #checks error type
                     print("Wrong input.You have to enter digits only") #indicates error
             while True: #while loop
                 try: #checking if there is any error in input
                     price=eval(input("\nEnter the price of product: ")) #Enter product price
                     break #if user enters correct input loop will break
                 except: #checks error type
                     print("Wrong input.You have to enter digits only") #indicates error
             while True: #while loop
                 a_confirmation = input("\nEnter y to continue or any alphabet to end adding process: ") #confirmation
                 if a_confirmation.isalpha() or (" " in a_confirmation) ==True: #condition
                     break #if user enters correct input loop will break
                 else: #condition
                     print("Wrong input.You have to enter Alphabets only") #indicates error
                     
             candy_dic[ID]=[name,quantity,price] #Adding in Dictionary
         option =False #condition
         
def candy_view(): #viewing detail function
    print("\n**************VIEW PRODUCT RECORD**************") #Formatting
    print("\t\t\nCANDY_ID\t\tCANDY_NAME\t\tCANDY_QUANTITY\t\tCANDY_PRICE") #view
    for ID in candy_dic.keys(): #checking ID
        index = candy_dic[ID] 
        print("\n\n  ",ID, "\t\t\t " ,index[0], "\t\t     " ,index[1], "\t\t    " ,index[2])#displaying
             
def candy_search(): #searching detail function
     print("\n**************SEARCH PRODUCT RECORD**************") #Formatting
     s_confirmation = "y" # confirmation
     while s_confirmation =="y" or s_confirmation =="Y": #confirmation loop
         while True: #while loop
             try: #checking if there is any error in input
                 ID= eval(input ("\nEnter the product ID to SEARCH: ")) #Enter unique Product ID to search
                 break #if user enters correct input loop will break
             except: #checks error type
                print("Wrong input.You have to enter digits only") #indicates error
         print("\nCANDY_ID\tCANDY_NAME\tCANDY_QUANTITY\tCANDY_PRICE") #Formating
         if ID in candy_dic.keys(): #if product ID found then proceed
             search=candy_dic[ID]  #varriable confirmation
             print(ID,"\t\t" ,search[0], "\t\t" ,search[1], "\t\t" ,search[2])    #displaying                    
         else: #condition
             print("Invalid ID") #indicates error
             print("candy not found try another ID") #indicates error
         while True: #while loop
                 s_confirmation = input("\nEnter y to continue or any alphabet to end searching process: ") #confirmation
                 if s_confirmation.isalpha() or (" " in s_confirmation) ==True: #condition
                     break #if user enters correct input loop will break
                 else: #condition
                     print("Wrong input.You have to enter Alphabets only") #indicates error
                     
def candy_edit(): #editing detail function
    print("\n**************EDIT PRODUCT RECORD**************") #Formatting
    e_confirmation = "y" #confirmation 
    while e_confirmation =="y" or e_confirmation =="Y": #confirmation loop
         while True: #while loop
             try: #checking if there is any error in input
                 ID= eval(input ("\nEnter the product ID to Edit: ")) #Enter unique Product ID to Edit
                 break #if user enters correct input loop will break
             except: #checks error type
                print("Wrong input.You have to enter digits only") #indicates error
                
         if ID in candy_dic.keys():#check whether the Id is in candy dictionary or not
            while True: #while loop
                    try: #checking if there is any error in input
                        edit=eval(input("\n1) To edit name:\n\n2) To edit quantity:\n\n3) To edit price:\n\n4) To edit the whole product record:\n\nEnter your choice:"))
                        break #if user enters correct input loop will break
                    except: #checks error type
                          print("Wrong input.You have to enter digits only") #indicates error
        
            if edit ==1: #when user enter 1
             while True: #while loop
                 name=input( "\nEnter name of the product: ") #Enter the product name
                 if name.isalpha() or (" " in name) ==True: #condition
                     break #if user enters correct input loop will break
                 else: #condition
                     print("Wrong input.You have to enter Alphabets only") #indicates error
             candy_dic[ID][0] = name
             print("Name Edited") #display
            elif edit ==2: #when user enter 2
                while True: #while loop
                    try: #checking if there is any error in input
                        quantity=eval(input("\nEnter the quantity of product: ")) #Enter the product quantity
                        break #if user enters correct input loop will break
                    except: #checks error type
                     print("Wrong input.You have to enter digits only") #indicates error
                candy_dic[ID][1] = quantity
                print("Quantity Edited") #display
            elif edit ==3: #when user enter 3
                while True: #while loop
                    try: #checking if there is any error in input
                        price=eval(input("\nEnter the price of product: ")) #Enter the product price
                        break #if user enters correct input loop will break
                    except: #checks error type
                        print("Wrong input.You have to enter digits only") #indicates error
                candy_dic[ID][2] = price
                print("Price Edited") #display
            elif edit ==4: #when user enter 4
                while True: #while loop
                    name=input( "\nEnter name of the product: ") #Enter the product name
                    if name.isalpha() or (" " in name) ==True: #condition
                        break #if user enters correct input loop will break
                    else: #condition
                        print("Wrong input.You have to enter Alphabets only") #indicates error
                while True: #while loop
                    try: #checking if there is any error in input
                        quantity=eval(input("\nEnter the quantity of product: ")) #Enter the product quantity
                        break #if user enters correct input loop will break
                    except: #checks error type
                        print("Wrong input.You have to enter digits only") #indicates error
                while True: #while loop
                    try: #checking if there is any error in input
                        price=eval(input("\nEnter the price of product: ")) #Enter the product price
                        break #if user enters correct input loop will break
                    except: #checks error type
                        print("Wrong input.You have to enter digits only") #indicates error
                candy_dic[ID]=[name,quantity,price] #updating product record in candy dictionary 
         else: #condition
            print("Invalid ID") #indicates error
            print("candy not found try another ID") #indicates error
         while True: #while loop
             e_confirmation = input("\nEnter y to continue or any alphabet to end editing process: ") #user choice
             if e_confirmation.isalpha() or (" " in e_confirmation) ==True: #condition
                 break #if user enters correct input loop will break
             else: #condition
                 print("Wrong input.You have to enter Alphabets only") #indicates error

def candy_delete(): #deleting detail function
    print("\n**************DELETE PRODUCT RECORD**************") #Formatting
    d_confirmation = "y" #confirmation 
    while d_confirmation =="y" or d_confirmation =="Y": #confirmation loop
         while True: #while loop
             try: #checking if there is any error in input
                 ID= eval(input ("\nEnter the product ID to delete: ")) #Enter unique Product ID to delete
                 break #if user enters correct input loop will break
             except: #checks error type
                print("Wrong input.You have to enter digits only") #indicates error
         if ID in candy_dic.keys():
             del candy_dic[ID]
             print("Record Deleted")
         else: #condition
             print("Invalid ID") #indicates error
             print("candy not found try another ID") #indicates error
         while True: #while loop
                 d_confirmation = input("\nEnter y to continue or any alphabet to end deleting process: ") #user choice
                 if d_confirmation.isalpha() or (" " in d_confirmation) ==True: #condition
                     break #if user enters correct input loop will break
                 else: #condition
                     print("Wrong input.You have to enter Alphabets only") #indicates error
             
             
def candy_menu() : #Main function for Product details
    print("\n**************WELCOME TO CANDY MENU**************") #Formatting
    candy_confirmation = "y" #confirmation 
    while candy_confirmation =="y" or candy_confirmation =="Y": #confirmation loop
         while True: #while loop
             try: #checking if there is any error in input
                 num = eval(input("\n1) To add candy product:\n\n2) To view candy product:\n\n3) To search candy product:\n\n4) To edit candy product:\n\n5) To delete candy product:\n\nEnter a number from the given  indexes:"))
                 break #if user enters correct input loop will break
             except: #checks error type
                 print("Wrong input.You have to enter digits only") #indicates error
         delete =True
         if len(candy_dic)>=1:
             delete =False
         if num == 1 : #for adding Product detail
             candy_add()
         elif num == 2 : #for viewing Product detail
             if delete ==False:
                 candy_view()
             else: #condition
                print("Add record First")
                
         elif num == 3 : #for searching Product detail
            if delete ==False:
                candy_search()
            else: #condition
                print("Add record First")
                
         elif num == 4 : #for eiditing Product detail
            if delete ==False:
                candy_edit()
            else: #condition
                print("Add record First")
                
         elif num == 5 : #for deleting Product detail
            if delete ==False:
                candy_delete()
            else: #condition
                print("Add record First")
                
         else: #condition
            print("Invalid input.Try again") #indicates error
         while True: #while loop
             candy_confirmation = input("\nEnter y to BACK to candy Menu or any Alphabet to exit this process:") #user choice
             if candy_confirmation.isalpha() or (" " in candy_confirmation) ==True: #condition
                 break #if user enters correct input loop will break
             else: #condition
                 print("Wrong input.You have to enter Alphabets only") #indicates error
            

def customer_add(): #Adding detail function
     print("\n**************ADD CUSTOMER RECORD**************") #Formatting
     a_confirmation = "y" #confirmation 
     option = True
     while a_confirmation =="y" or a_confirmation =="Y": #confirmation loop
         while True: #while loop
             try: #checking if there is any error in input
                 ID = eval(input ("\nEnter the Customer's ID: ")) #Enter unique product ID to proceed
                 break #if user enters correct input loop will break
             except: #checks error type
                 print("Wrong input.You have to enter digits only") #indicates error
         if option ==False:
             if ID in customer_dic.keys():
                 print("ID already exist.Try another one") #already exist
             else: #condition
                 while True: #while loop
                     name = input( "\nEnter the customer's name: ")
                     if name.isalpha() or (" " in name) ==True:
                         break #if user enters correct input loop will break
                     else:
                         print("Wrong input.You have to enter Alphabets only") #indicates error
                 while True: #while loop
                     try: #checking if there is any error in input
                         Age = eval(input("\nEnter the customer's age: "))
                         break #if user enters correct input loop will break
                     except: #checks error type
                         print("Wrong input.You have to enter digits only") #indicates error
                 while True: #while loop
                     try: #checking if there is any error in input
                         contact = eval(input("\nEnter the customer's contact: "))
                         break #if user enters correct input loop will break
                     except: #checks error type
                         print("Wrong input.You have to enter digits only") #indicates error
                 while True: #while loop
                     a_confirmation = input("\nEnter y to continue or any alphabet to end adding process: ") #user choice
                     if a_confirmation.isalpha() or (" " in a_confirmation) ==True: #condition
                         break #if user enters correct input loop will break
                     else: #condition
                         print("Wrong input.You have to enter Alphabets only") #indicates error
                 customer_dic[ID]=[name,Age,contact]
         else: #condition
             while True: #while loop
                     name = input( "\nEnter the customer's name: ")
                     if name.isalpha() or (" " in name) ==True:
                         break #if user enters correct input loop will break
                     else:
                         print("Wrong input.You have to enter Alphabets only") #indicates error
             while True: #while loop
                 try: #checking if there is any error in input
                     Age = eval(input("\nEnter the customer's age: "))
                     break #if user enters correct input loop will break
                 except: #checks error type
                     print("Wrong input.You have to enter digits only") #indicates error
                 
             while True: #while loop
                 try: #checking if there is any error in input
                     contact = eval(input("\nEnter the customer's contact: "))
                     break #if user enters correct input loop will break
                 except: #checks error type
                     print("Wrong input.You have to enter digits only") #indicates error
             while True: #while loop
                     a_confirmation = input("\nEnter y to continue or any alphabet to end adding process: ") #user choice
                     if a_confirmation.isalpha() or (" " in a_confirmation) ==True: #condition
                         break #if user enters correct input loop will break
                     else: #condition
                         print("Wrong input.You have to enter Alphabets only") #indicates error
             customer_dic[ID]=[name,Age,contact]
         option =False

def customer_view(): #viewing detail function
    print("\n**************VIEW CUSTOMER RECORD**************") #Formatting
    print("\t\t\nCUSTOMER_ID\t\tCUSTOMER_NAME\t\tCUSTOMER_AGE\t\tCUSTOMER_CONTACT") #display
    for ID in customer_dic.keys(): #checking ID
        index = customer_dic[ID]
        print("\n\n   ",ID, "\t\t\t   " ,index[0], "\t\t    " ,index[1], "\t\t     " ,index[2])#display

def customer_search(): #searching detail function
     print("\n**************SEARCH CUSTOMER RECORD**************") #Formatting
     s_confirmation = "y" #confirmation 
     while s_confirmation =="y" or s_confirmation =="Y": #confirmation loop
         while True: #while loop
             try: #checking if there is any error in input
                 ID= eval(input ("\nEnter the Customer's ID to SEARCH: ")) #Enter unique Product ID to search
                 break #if user enters correct input loop will break
             except: #checks error type
                 print("Wrong input.You have to enter digits only") #indicates error
     print("\nCUSTOMER_ID\tCUSTOMER_NAME\tCUSTOMER_AGE\tCUSTOMER_CONTACT") #display
     if ID in customer_dic.keys(): #if customer ID found then proceed
         search=customer_dic[ID] 
         print(ID,"\t\t" ,search[0], "\t\t" ,search[1], "\t\t" ,search[2]) #display                      
     else: #condition
         print("Invalid ID") #indicates error
         print("customer not found try another ID") #indicates error
     while True: #while loop
         s_confirmation = input("\nEnter y to continue or any alphabet to end searching process: ") #user choice
         if s_confirmation.isalpha() or (" " in s_confirmation) ==True: #condition
             break #if user enters correct input loop will break
         else: #condition
             print("Wrong input.You have to enter Alphabets only") #indicates error

def customer_edit(): #editing detail function
    print("\n**************EDIT CUSTOMER RECORD**************") #Formatting
    e_confirmation = "y" #confirmation 
    while e_confirmation =="y" or e_confirmation =="Y": #confirmation loop
        while True: #while loop
            try: #checking if there is any error in input
                ID = eval(input ("\nEnter the Customer's ID: ")) #Enter unique customer ID to proceed
                break #if user enters correct input loop will break
            except: #checks error type
                print("Wrong input.You have to enter digits only") #indicates error
                
        if ID in customer_dic.keys(): #checks whether the ID is in candy dictionary or not
                while True: #while loop
                    try: #checking if there is any error in input
                        edit=eval(input("\n1) To edit name:\n\n2) To edit Age:\n\n3) To edit contact:\n\n4) To edit the whole customer record:\n\nEnter your choice:"))
                        break #if user enters correct input loop will break
                    except: #checks error type
                        print("Wrong input.You have to enter digits only") #indicates error
                if edit ==1:
                    while True: #while loop
                        name = input( "Enter the customer's name: ") #Enter the customer name
                        if name.isalpha() or (" " in name) ==True:
                            break #if user enters correct input loop will break
                        else: #condition
                            print("Wrong input.You have to enter Alphabets only") #indicates error
                    customer_dic[ID][0] = name
                    print("Name Edited") #display
                elif edit ==2:
                    while True: #while loop
                        try: #checking if there is any error in input
                            Age = eval(input("Enter the customer's age: ")) #Enter the customer age
                            break #if user enters correct input loop will break
                        except: #checks error type
                            print("Wrong input.You have to enter digits only") #indicates error
                    customer_dic[ID][1] = Age #display
                    print("Age Edited")
                elif edit ==3:
                    while True: #while loop
                        try: #checking if there is any error in input
                            contact=eval(input("\nEnter the customer's contact: ")) #Enter the customer contact
                            break #if user enters correct input loop will break
                        except: #checks error type
                            print("Wrong input.You have to enter digits only") #indicates error
                    customer_dic[ID][2] = contact
                    print("contact Edited") #display
                elif edit ==4:
                    while True: #while loop
                        name = input( "Enter the customer's name: ") #Enter the customer contact
                        if name.isalpha() or (" " in name) ==True: #condition
                            break #if user enters correct input loop will break
                        else: #condition
                            print("Wrong input.You have to enter Alphabets only") #indicates error
                    while True: #while loop
                        try: #checking if there is any error in input
                            Age = eval(input("Enter the customer's age: ")) #Enter the customer age
                            break #if user enters correct input loop will break
                        except: #checks error type
                            print("Wrong input.You have to enter digits only") #indicates error
                    while True: #while loop
                        try: #checking if there is any error in input
                            contact = eval(input("Enter the customer's contact: ")) #Enter the customer contact
                            break #if user enters correct input loop will break
                        except: #checks error type
                            print("Wrong input.You have to enter digits only") #indicates error
                    while True: #while loop
                        update = input("\nEnter y to continue or any alphabet to end editing process: ") #user choice
                        if update.isalpha() or (" " in update) ==True: #condition
                            break #if user enters correct input loop will break
                        else: #condition
                            print("Wrong input.You have to enter Alphabets only") #indicates error
                    customer_dic[ID]=[name,Age,contact]
        else: #condition
            print("Invalid ID") #indicates error
            print("customer not found try another ID") #indicates error
        while True: #while loop
            e_confirmation = input("\nEnter y to continue or any alphabet to end editing process: ") #user choice 
            if e_confirmation.isalpha() or (" " in e_confirmation) ==True: #condition
                break #if user enters correct input loop will break
            else: #condition
                print("Wrong input.You have to enter Alphabets only") #indicates error

def customer_delete(): #deleting detail function
    print("\n**************DELETE CUSTOMER RECORD**************") #Formatting
    d_confirmation = "y" #confirmation 
    while d_confirmation =="y" or d_confirmation =="Y": #confirmation loop
         while True: #while loop
             try: #checking if there is any error in input
                 ID = eval(input ("\nEnter the Customer's ID: ")) #Enter unique product ID to proceed
                 break #if user enters correct input loop will break
             except: #checks error type
                 print("Wrong input.You have to enter digits only") #indicates error
         if ID in customer_dic.keys(): #checks whether the ID is in customer dictionary or not
             del customer_dic[ID]
         else: #condition
             print("Invalid ID") #indicates error
             print("customer not found try another ID") #indicates error
         while True: #while loop
                 d_confirmation = input("\nEnter y to continue or any alphabet to end deleting process: ") #user choice
                 if d_confirmation.isalpha() or (" " in d_confirmation) ==True: #condition
                     break #if user enters correct input loop will break
                 else: #condition
                     print("Wrong input.You have to enter Alphabets only") #indicates error
             
def customer_menu() : #Main function for customer details
    print("\n**************WELCOME TO CUSTOMER MENU**************") #Formatting
    customer_confirmation = "y" #confirmation 
    delete =True
    while customer_confirmation =="y" or customer_confirmation =="Y": #confirmation loop
        while True: #while loop
            try: #checking if there is any error in input
                num = eval(input("\n\n1) To add Customer's Record:\n\n2) To view Customer's Record :\n\n3) To search Customer's Record:\n\n4) To edit Customer's Record:\n\n5) To delete Customer's Record:\n\nEnter a number from the given  indexes:"))
                break #if user enters correct input loop will break
            except: #checks error type
                print("Wrong input.You have to enter digits only") #indicates error
        delete =True
        if len (customer_dic)>=1: #checks lenght of dictionary
            delete =False
        if num == 1 : #for adding customer detail
            customer_add() #calls function
            delete =False
        elif num == 2 : #for viewing customer detail
            if delete ==False:
                customer_view() #calls function
            else: #condition
                print("Add record First")
        elif num == 3 : #for searching customer detail
            if delete ==False:
                customer_search() #calls function
            else: #condition
                print("Add record First")
        elif num == 4 : #for eiditing customer detail
            if delete ==False:
                customer_edit() #calls function
            else: #condition
                print("Add record First")
        elif num == 5 : #for deleting customer detail
            if delete ==False:
                customer_delete() #calls function
            else: #condition
                print("Add record First")
        else:
            print("Invalid input.Try again") #indicates error
        while True: #while loop
            customer_confirmation = input("\nEnter y to BACK to customer Menu or any Alphabet to exit this process:") #user choice
            if customer_confirmation.isalpha() or (" " in customer_confirmation) ==True: #condition
                break #if user enters correct input loop will break
            else: #condition
                print("Wrong input.You have to enter Alphabets only") #indicates error
                       

def sale_add(): #adding detail function
    print("\n**************ADD SALE RECORD**************") #Formatting
    Order_confirmation ="y" #confirmation 
    while Order_confirmation =="y" or Order_confirmation =="Y": #confirmation loop
        while True: #while loop
            while True: #while loop
                try: #checking if there is any error in input
                    order_ID = eval(input ("\nEnter your Unique product ID to add sale: ")) #Enter unique product ID to proceed
                    break #if user enters correct input loop will break
                except: #checks error type
                    print("Wrong input.You have to enter digits only") #indicates error
            if order_ID in candy_dic.keys(): #checks whether the ID is in candy dictionary or not
                order= candy_dic[order_ID]
                break #if user enters correct input loop will break
            else: #condition
                print("Invalid ID") #indicates error
                print("candy not found try another ID") #indicates error
        while True: #while loop
            while True: #while loop
                try: #checking if there is any error in input
                    Unique_ID = eval(input("Enter your Unique customer's ID to place order: ")) #Enter the unique customer ID to proceed
                    break #if user enters correct input loop will break
                except: #checks error type
                    print("Wrong input.You have to enter digits only") #indicates error
            if Unique_ID in customer_dic.keys(): #checks whether the ID is in customer dictionary or not
                order1= customer_dic[Unique_ID]
                break #if user enters correct input loop will break
            else: #condition
                print("Invalid ID") #indicates error
                print("customer not found try another ID") #indicates error
        while True: #while loop
            try: #checking if there is any error in input
                Quantity = eval(input("Enter the Quantity of candy to order: ")) #enter the quantity
                break #if user enters correct input loop will break
            except: #checks error type
                print("Wrong input.You have to enter digits only") #indicates error
        
        if order_ID in candy_dic.keys(): #checks whether the ID is in candy dictionary or not
            
            order= candy_dic[order_ID]
            
            
            if Unique_ID in customer_dic.keys(): #checks whether the ID is in customer dictionary or not
                
                
                order_price= Quantity * order[2]
                sale_dic.update({1:[order_price]})
            else: #condition
                print("Invalid ID") #indicates error
                print("customer not found try another ID") #indicates error
        else: #condition
            print("Invalid ID") #indicates error
            print("candy not found try another ID") #indicates error
        while True: #while loop
                Order_confirmation=input("Enter y to Re_enter or any Alphabet to end Order: ") #user choice
                if Order_confirmation.isalpha() or (" " in Order_confirmation) ==True: #condition
                    break #if user enters correct input loop will break
                else: #condition
                    print("Wrong input.You have to enter Alphabets only") #indicates error

def sale_view(): #viewing detail function
    print("\n**************VIEW SALE RECORD**************") #Formatting
    print("\nThe price of your order is",sale_dic[1])
    while True: #while loop
        order_bill=input("\nEnter y to print BILL or N to not print the bill :  ")
        if order_bill.isalpha() or (" " in order_bill) == True: #condition
            break #if user enters correct input loop will break
        print("You have to enter Alphabats here. Try again :  ") #indicates error
    if order_bill=="yes" or "Yes": #condition
        while True: #while loop
            name = input("\nPlease enter customer's name here: ") #Enter customer name
            if name.isalpha() or (" " in name) == True: #condition
                break #if user enters correct input loop will break
            print("Wrong input.You have to enter Alphabats only") #indicates error
        while True: #while loop
            gender = input("\nPlease enter customer's gender here: ") #Enter customer gender
            if name.isalpha() or (" " in name) == True: #condition
                break #if user enters correct input loop will break
            print("Wrong input.You have to enter Alphabats only") #indicates error
        while True: #while loop
            try: #checking if there is any error in input
                contact= eval(input("\nEnter customer's contact number here: ")) #Enter customer contact
                break #if user enters correct input loop will break
            except: #checks error type
                print("Wrong input.You have to enter digits only") #indicates error
        print("----------------Order Bill------------------------")
        u="""  *******Thanks For******
*********Visting Us******"""
        print(u)
        print("Name \t\t  Contact number \t\t Gender \t\t Total Amount") #display
        print(name,"\t\t",contact,"\t\t\t ",gender,"\t\t\t   ",sale_dic[1]) #display
        print(" ")
        f="""                        (Complaint or Home Deivery)
                For any complaint or Free home delivery contact us::
                            Contact#0311-5043556 and 0333-6669356
                            
                            email address zafarmehmood1609@gmail.com
                                         hassanbasharat167@gmail.com"""
        print(f)
        print("---------------------------------------------------------------------------------------------------------")

def sale_menu():  #Main function for sale details
    print("\n**************WELCOME TO SALE MENU**************") #Formatting
    sale_confirmation = "y" #confirmation
    delete =True
    while sale_confirmation =="y" or sale_confirmation =="Y": #confirmation loop
        while True: #while loop
            try: #checking if there is any error in input
                choice = eval(input("\n1) To add sale:\n\n2) To view sale:\n\nEnter your choice:")) #user choice
                break #if user enters correct input loop will break
            except: #checks error type
                print("Wrong input.You have to enter digits only") #indicates error
        
        if choice ==1: #if user enter 1
            sale_add() #calls function
            delete =False
        elif choice ==2: #if user enter 2
            if len(sale_dic)>=1: #check length of dictionary
                sale_view() #calls function
            else: #condition
                print("Place order first.")
        else: #condition
            print("Invalid Input.Try again") #indicates error
            
        while True: #while loop
            sale_confirmation = input("\nEnter y to BACK to SALE Menu or any Alphabet to exit this process:") #user choice 
            if sale_confirmation.isalpha() or (" " in sale_confirmation) ==True: #condition
                break #if user enters correct input loop will break
            else: #condition
                print("Wrong input.You have to enter Alphabets only") #indicates error
def control_menu():#Main Controling function
    print("\n**************WELCOME TO CONTROL MENU**************") #Formatting
    delete =False #check
    
    choise=7#variable initialization
    while choise!=4:#condition to Exit the program
        while True:#while loop
           try: #checking if there is any error in input
               choise=eval(input("\n 1) To Access candy menu:\n\n 2) To Access customer menu:\n\n 3) To Access sale menu:\n\n 4) For exit:\n\nEnter number here : "))#prints menu
               break #if user enters correct input loop will break
           except:#checks error type
               print("Wrong input.You have to enter digits only")#prompts user that there's an error
        if choise==1:#condition
           candy_menu()#calls function
        elif choise==2:#condition
           customer_menu()#calls function
        elif choise==3:#condition
           sale_menu()#calls function
        elif choise==4:#condition
            print("PROGRAM TERMINATED") #display
            print("Created by:\nMuhammd Hassan Basharat(FA19-BSE-104)\nZafar Mehmood(SP19-BSE-045)") #display
        else: #condition
            print("Invalid input.Try again") #indicates error
control_menu() #calls function
