# -----------------------------------------------------------
# Record Items for a shopping chart
# (C) 2020 Mahmudul Alam
# Released under Colorado State University-Global Campus
# email mahmudul.alam@csuglobal.edu
# -----------------------------------------------------------

#make a list to hold to new items
shopping_list = []
shopping_Price = []
#How to use the app

print("You can add items to your list")

while True:
    print("Type DONE when finished")
    #User will be asked for new input
    new_item = input("Enter item name > ")
    #Quit the app
    if new_item == 'DONE':
        break
    new_item1 = input("Enter item price > ")
    #add items to the list
    shopping_list.append(new_item)
    shopping_Price.append(new_item1)
#tells you your list
print("Items you have added to your list are:")

#prints out the items
for item in shopping_list:
    for price in shopping_Price:
        print(item,price)
# ----------------------END-----------------------#


