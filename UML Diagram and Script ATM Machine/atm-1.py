# --------------------------------------------------------------------
# Automated teller machine (ATM)
# (C) 2020 Mahmudul Alam
# Released under Colorado State University-Global Campus
# email mahmudul.alam@csuglobal.edu
# --------------------------------------------------------------------


##############################
## @def will keep count and validate the difference between total balance vs the withdraw amount.
## @returns total balance and the difference in balance
##############################
def withdraw(withdrawal_amount,Balance):
    if withdrawal_amount > Balance:
        return -1 # returning -1 if the withdrawal isn't possible.
    else:
        return (Balance - withdrawal_amount) # returning Mathematical calculation result value.

##############################
## @def will display thank you message
## @prints "Thank you for using this ATM"
##############################
def quit():
    print('-----------------------------------')
    print('***********************************')
    print("   Thank you for using the ATM") 
    print('***********************************')
    print('-----------------------------------')
    exit()

# myBalance variable will store the total amount
myBalance = float(500.25)

# count will make sure there is only three tries for the pin
count=0

# while loop will make sure the user can only try three times
while count < 3:
    print('')
    password = input('Enter Pin: ')
    if password=='1234':
        print('-----------------------------------')
        print('***********************************')
        print("  Welcome Mamudul Alam to the ATM")
        print('***********************************')
        print('-----------------------------------')
        if (password == "1234"):
            print(' ')
            print("Your account balance is:",myBalance)
            withdrawal_amount = float(input("How much would you like to withdraw today: "))
            myResult = withdraw(withdrawal_amount,myBalance)
        if (myResult == -1): # checking the return value if it is -1 then it is not posible to withdraw with the given withdrawal_amount
            print("$%.2f is greater than your account balance of $%.2f" % (withdrawal_amount,myBalance))
        else:
            myBalance = myResult # Updating the myBalance
            print("Withdrawal amount was $%.2f, current balance is $%.2f" % (withdrawal_amount, myBalance)) # Prints to two decimal places
            print('')
            quit()
        break

    else: # When the user input the wrong pin, else will execute
        print('-------------------------')
        print('Access denied, Try again')
        print('-------------------------')
        count += 1
        if count == 3:
            print('')
            print('           Access denied')
            quit()

# -------------------------------------------------------END--------------------------------------------------------#