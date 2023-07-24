import os

def exit_or_not(exit_code):
 
   while exit_code !=0:

        # 1-yes to exit the program
        # 0-no  to return to log in page
        exit_number=int(input("Do you want to exit? (1=yes,0=no)>> ")) 

        if exit_number !=0: 
  
            exit() 

        elif exit_number==0: 

            exit_code=0

            print()



def login_identity():
    
    os.system("cls") 

    print("Welcome to Crazy Mamak !\n") 

    print("Login to your account\n") 

    #Key in "0" is owner
    #Key in any numbers (expect 0) is customer
    
    username = int(input("Username ID:"))

    print ()

    password = input("Password   :")

    print()

    return (username)


def owner_menu(): 

    os.system("cls")
    
    print("\t\tMain Menu\n") 

    print("\t\t1 - add a new food") 

    print("\t\t2 - delete a food") 

    print("\t\t3 - display all food\n") 

    print("\t\t0 - exit\n") 

    print() 


def option_owner_1(): 

    new_food = input("Please key in the name of food >> ") 

    print() 

    food_list.append(new_food) 

    new_food_price = float(input("Price for new food >> RM ")) 

    print() 

    price_list.append(new_food_price) 

    price_order_food_list.append(0) 

    number_order_food_list.append(0)



def owner_add_food_or_not(repeat_owner_add_food):

    repeat_owner_add_food = int(input("Do you want to add a new food again (1=yes,0=no) >> "))

    print()
 
    while repeat_owner_add_food != 1 and repeat_owner_add_food != 0:         

            print("Invalid Selection. Please key in (1=yes,0=no).\n ") 

            repeat_owner_add_food = int(input("Do you want to add a new food again (1=yes,0=no) >> ")) 
             
            print("\n")

    return repeat_owner_add_food


def option_owner_2(): 

    name_delete = input("Please key in the name of food >> ") 

    print() 

    index_delete = food_list.index(name_delete) 

    food_list.pop(index_delete) 

    price_list.pop(index_delete) 

    price_order_food_list.pop(index_delete) 

    number_order_food_list.pop(index_delete)



def owner_delete_food_or_not(repeat_owner_delete_food) :
    
    repeat_owner_delete_food = int(input("Do you want to delete food again (1=yes,0=no) >> "))

    print()

    while repeat_owner_delete_food != 1 and repeat_owner_delete_food != 0: 

        print("Invalid Selection. Please key in (1=yes,0=no).\n ")  

        repeat_owner_delete_food = int(input("Do you want to delete food again (1=yes,0=no) >> ")) 

        print()
        
    return repeat_owner_delete_food


def option_owner_3():
    
   print("\t\tCode |        Food        |   Price(RM)\n") 

   for counter in range(1, len(food_list) + 1, 1): 

       print("\t\t ", counter, " | ","%15s"%food_list[counter - 1], "  | ", "%.2f"%price_list[counter - 1]) 


   input("\nPress ENTER to continue...\n") 
 

 
def customer_menu(): 

    os.system("cls") 

    print("\t\tMenu\n")
    
    print("\t\t1 - Place order") 

    print("\t\t2 - Check order") 

    print("\t\t3 - Make Payment\n") 

    print("\t\t0 - Quit") 

    print()



def option_customer_1():
 
               
    print("\t\t           Code  |  ","%15s"%"      Food           |   Price(RM)") 

    print() 


    for counter in range(1, len(food_list) + 1, 1): 
 
        print("\t\t ","%12s"%  counter, "  | "," %16s   "%food_list[counter - 1],  " |   ", "%.2f"%price_list[counter - 1]) 

    print() 


def calculation_food_order(others): 

    order = int(input("Please key in the code for food >> ")) 

    while order not in range (1,len(food_list)+1): 

        print("Invalid Selection .Please key in the code from the table above only .\n") 

        order = int(input("Please key in the code for food >> ")) 

    unit = int(input("\nPlease key in unit for food ordered >> ")) 

    unit=unit+number_order_food_list[order-1] 

    number_order_food_list.insert(order - 1, unit) 

    number_order_food_list.pop(order) 

    price_order_food = (price_list[order - 1]) * unit 

    price_order_food_list.insert(order - 1, price_order_food) 

    price_order_food_list.pop(order) 

    total_price_order_food = sum(price_order_food_list)
    
    others: int = int(input("\nDo you want to continue order ? [1-Yes / 0-No] >> ")) 

    while others != 1 and others != 0 : 

        print("\nInvalid Selection. Please key in ( 1 - 2 ).\n ") 
  
        others: int = int(input("\nDo you want to continue order ? [1-Yes / 0-No] >> ")) 

    print() 

    return [others, total_price_order_food] 


def check_order(total_price_order_food): 

    print() 

    os.system("cls") 

    print("Your current order :") 

    print() 

    for count in range(len(food_list)): 
 
        print("\t\t"," %16s   "%food_list[count],"|","%3s"%number_order_food_list[count], " |  ","%.2f"% price_order_food_list[count]) 

    print() 

    print("Total price now :RM","%.2f"%total_price_order_food,"\n") 

    input("Press ENTER to continue...\n") 
 

def payment(total_price_order_food,cash): 

    os.system("cls") 

    for i in range(len(food_list)): 

        if number_order_food_list[i] != 0: 

            print("\t\t ", " %16s   "%food_list[i], "|", " %3s   "%number_order_food_list[i], " |  ", "%.2f"% price_order_food_list[i]) 

        else: 

            print()
            

    print("\nTotal bill : RM", "%.2f" % total_price_order_food, "\n") 

    print("\t\t1 - 10% discount when using cash to pay.\n") 

    print("\t\t2 -  5% discount when using credit card to pay.\n")
    
    method=input("Which payment method do you want ? (1=cash,2=credit card) >> ")
    
    print()
    

    while method not in ("1","2"):  

        print("Invalid Selection. Please key in 1/2 !") 

        method=input(" Which payment method do you want ?(1=cash,2=credit card) >> ") 

        print()
        

    if method=="1":  

         discount=total_price_order_food*0.1  

         total_price_order_food= total_price_order_food-discount  

         print("Your total bill is>> RM ","%.2f"%total_price_order_food,"\n")

         cash = float(input("Cash paid : RM "))
         

         while cash<total_price_order_food:

             print( "Cash paid is less than total price of your food order \n")

             cash = float(input("Cash paid : RM ")) 
 
         give_change = cash - total_price_order_food 

         print("\nChange : RM ","%.2f"%give_change,"\n") 


    elif method=="2":  

         discount=total_price_order_food*0.05  

         total_price_order_food=total_price_order_food-discount 

         print("Your total bill is >> RM","%.2f"%total_price_order_food,"\n") 

         credit_card = int(input("Please key in your credit card number >> ")) 

         print()            
 
    print("\tThx for your support!\n")  

    print("\tHope you have the good day and see you soon !")   

    input("\nPress ENTER to continue...\n")
    

    return cash


def option_customer_0(cash , total_price_order_food) :

    proceed=1

    if cash ==0 and total_price_order_food!=0:

        proceed=int(input("You not yet do the payment , do you still want to exit ? (1=yes,0=no)>> "))

        if proceed!=0:

           print("Hope you have the good day and see you soon !") 

           
                    
    exit()




# settings---------------------------------------------------------------------- 

option_owner_menu=0 

others = 1  

total_price_order_food=0 

exit_code=0

cash=0

proceed=0


# --------------------------------------Main Program------------------------------------- 

 
# --food list----------------------------------------------------------------------------  


food_list = ["Roti Canai","Roti Telur", "Curry Mee","Maggi Goreng", "Nasi Lemak"] 

price_list = [1.20, 1.50, 5.50, 6.00, 2.00] 

price_order_food_list = [0, 0, 0, 0, 0] 

number_order_food_list = [0, 0, 0, 0, 0] 

 
# ---------------------------------------------------------------------------------------- 

while option_owner_menu==0 or option_customer==0:
    
    exit_or_not(exit_code)

    option_owner_menu=1 


# login identity----------------------------------------------------------------------

    username=login_identity()


# ---Owner part----------------------------------------------------------------------------------  

 
    if username  == 0: 

        while option_owner_menu !=0: 

            owner_menu() 

            option_owner_menu = int(input("Choose your option >> ")) 

            print()  

            if option_owner_menu == 1:
                
                repeat_owner_add_food=1

                while repeat_owner_add_food != 0:

                    option_owner_1()

                    repeat_owner_add_food=owner_add_food_or_not(repeat_owner_add_food)

             
            elif option_owner_menu == 2:

                repeat_owner_delete_food = 1            

                while repeat_owner_delete_food != 0: 

                    option_owner_2()

                    repeat_owner_delete_food=owner_delete_food_or_not(repeat_owner_delete_food)

                    

            elif option_owner_menu == 3: 

                os.system("cls")

                option_owner_3()

                
 
            elif option_owner_menu==0: 

                exit_code=1 

                                 
            else: 
 
                print("Invalid Selection. Please key in ( 0 - 3 ).\n")
                input()


# -------Customer part ------------------------------------------------------------------------------                                


    else: 


# -------program start (Choose option)----------------------------- 

        option_customer=1

        while option_customer != 0 or proceed ==0: 

            customer_menu() 
 
            option_customer = int(input("Choose your option >> ")) 

 

# ----------Place order------------------------------------------- 

 

            if option_customer == 1:

                os.system("cls") 

                option_customer_1()

 
                others = 1 


                while others != 0: 

                   a,b=calculation_food_order(others) 

                   others = a 

                   total_price_order_food = b 


# ----------Check Order--------------------------------------------------------------------- 

 

            elif option_customer == 2: 

                check_order(total_price_order_food) 

 

# ----------Make payment--------------------------------------------------------------------- 

 

            elif option_customer == 3:

                if total_price_order_food > 0: 

                    cash=payment(total_price_order_food,cash) 

                    price_order_food_list = [0, 0, 0, 0, 0] 

                    number_order_food_list = [0, 0, 0, 0, 0] 

                    total_price_order_food=0 

 
                else:
                                
                    print("\nYou have no order.") 

                    input("\nPress ENTER to continue...\n") 


            elif option_customer==0:

                option_customer_0(cash , total_price_order_food)


            else: 

                print("Invalid Selection. Please key in (1 - 3).\n")
                input("\nPress ENTER to continue...\n")


