#Expense Tracker project

ExpensesList = [] #list of expenses in form of dict.
print("Welcome to expense tracker")

while True:
    print("====MENU====")
    print("Press 1 For add expenses")
    print("press 2 to see all expenses")
    print("press 3 for exit")
    choice = int(input("Enter your choice: "))
    
    #add expenses

    if (choice ==1):
        date = input("Enter a date (YYYY-MM-DD): ")
        whatyoubuy = input( "Name what you buy: ")
        amount = input("Write the amount: ")
        
        expenses={
            "date":date,
            "whatyoubuy":whatyoubuy,
            "amount":amount

        }
        
        ExpensesList.append(expenses)
        print("Expenses add succesfully")

     #show expenses   

    elif (choice==2):
        if(len(ExpensesList)==0):
            print("No expenses found")
        else:
            print("ALL YOUR EXPENSES")
            count=1
            for eachexp in ExpensesList:
                print(f"Expense No {count} -- {eachexp['date']}, {eachexp['whatyoubuy']}, {eachexp['amount']}")
                count = count+1
        total = 0
        for eachexp in ExpensesList:
            total = total + int(eachexp["amount"])
            print("Total Expense:", total)
    
    
    #exit
    elif(choice==3):
        print("Thanks for using our system")
        break
    else:
        print("Invalid choice")
        



