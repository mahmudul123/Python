# -----------------------------------------------------------
# prompts a user to input their specification and returns the object of their input.
# (C) 2020 Mahmudul Alam
# Released under Colorado State University-Global Campus
# email mahmudul.alam@csuglobal.edu
# -----------------------------------------------------------

def userInput():

    # Calls for an infinite loop that keeps executing
    # until an exception occurs
    while True:
        name = input("What's your name? ")
        describe=input('Describe the specification you want to look into: ')

        try:
            rate = int(input("From 0 to 4, how important would you rate it: " ))

        # If something else that is not the string
        # version of a number is introduced, the
        # ValueError exception will be called.
        except ValueError:
            # The cycle will go on until validation
            print("Error! This is not a number. Try again.")
        # the loop will end.
        else:
            rate_all=['Easy','Medium','Hard','Difficult','Extremely Difficult']

            print("Impressive,", name, "You have mentioned:",describe,".We will further take a look into this request.---", rate_all [rate] )
            break
userInput()

# ----------------------END-----------------------#
