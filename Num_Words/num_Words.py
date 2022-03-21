# -----------------------------------------------------------
# Given a numeric dollar amount, will print the amount in words
# (C) 2020 Mahmudul Alam
# Released under Colorado State University-Global Campus
# email mahmudul.alam@csuglobal.edu
# -----------------------------------------------------------

"""""""""""""""""
@des num_Words function, identifies interpretation of the user input 
@prints validates user input and prints corresponding words 
"""""""""""""""""
def num_Words(num):
    a = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty',
         30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety'}

    r = 1000
    o = r * 1000
    n = o * 1000
    y = n * 1000

    assert (0 <= num)

    # conditional statement to find numbers smaller than 20
    if (num < 20):
        return a[num]

    # conditional statement to find numbers smaller than 100
    if (num < 100):
        if num % 10 == 0:
            return a[num]
        else:
            return a[num // 10 * 10] + ' ' + a[num % 10]

    # conditional statement to evaluate numbers larger than 100 and translate them to ten figures
    if (num < r):
        if num % 100 == 0:
            return a[num // 100] + ' hundred'
        else:
            return a[num // 100] + ' hundred ' + num_Words(num % 100)

    if (num < o):
        if num % o == 0:
            return num_Words(num // r) + ' thousand'
        else:
            return num_Words(num // r) + ' thousand, ' + num_Words(num % r)

# Amount takes user input
amount = input('What is the doller amount in number: ')
arr = amount.split('.')

# When the user input is in thousand figure the number will be translated in to value of tens and hundreds
if len(arr) == 2:
    print(num_Words(int(arr[0])).upper(), "AND", arr[1], "/", 10 ** (len(arr[1])))
else:
    print('Your total is ', end = '')
    print(num_Words(int(arr[0])).upper())

# ----------------------END-----------------------#
