import random, time
from random import randint

# what the characters of the passwords being used 
everything = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
loweronly = 'abcdefghijklmnopqrstuvwxyz'
upperonly = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
upperandlower = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
upperandlowerwithnumbers = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
onlyupperwithnumbers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
onlylowerwithnumbers = 'abcdefghijklmnopqrstuvwxyz0123456789'
numbersonly = '0123456789'
secure = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
utf8 = '!"#$%&*+,-./0123456789:;<=>? ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~€‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜™š›œžŸ ¡¢£¤¥¦§¨©ª«¬ ®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞş'

# displays this to terminal
print('''

     /$$$$$$$  /$$$$$$$   /$$$$$$                       /$$$$$$                                              /$$
    | $$__  $$| $$__  $$ /$$__  $$                     /$$__  $$                                            | $$
    | $$  \ $$| $$  \ $$| $$  \__/                    | $$  \__/  /$$$$$$  /$$$$$$/$$$$  /$$   /$$  /$$$$$$ | $$
    | $$$$$$$/| $$$$$$$/| $$ /$$$$       /$$$$$$      |  $$$$$$  |____  $$| $$_  $$_  $$| $$  | $$ /$$__  $$| $$
    | $$____/ | $$____/ | $$|_  $$      |______/       \____  $$  /$$$$$$$| $$ \ $$ \ $$| $$  | $$| $$$$$$$$| $$
    | $$      | $$      | $$  \ $$                     /$$  \ $$ /$$__  $$| $$ | $$ | $$| $$  | $$| $$_____/| $$
    | $$      | $$      |  $$$$$$/                    |  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$/|  $$$$$$$| $$
    |__/      |__/       \______/                      \______/  \_______/|__/ |__/ |__/ \______/  \_______/|__/
                                                                                                                
          +---------------------------------Powerful Password Generator-----------------------------------+                                                                                                       
                                                                                                            
        [1]  lower characters only
        [2]  upper characters only
        [3]  lower and upper characters only
        [4]  all types of characters
        [5]  lower and upper characters with numbers
        [6]  only upper with numbers
        [7]  only lower with numbers
        [8]  numbers only
        [9]  secure
        [10] secure+ (utf-8, unstable on windows)

          +---------------------------------Powerful Password Generator-----------------------------------+    
          // disclaimer: this script does not remeber passwords for you!         
 
''')

choice = input("choose a type of password from above: ") # asks what type of password user wants

if choice == "1": # if choise is value; do the following.
    number = 1 # not a necessity but useful

    length = input('number of characters: ') # asks user how many charaters he/she wants in there password.
    length = int(length) # tels the code to make the password the amount of charaters the user said.
    if length < 8: # if the user choose to have less than 8 characters, a waring will apper. 
        print("Warning: a password with 8 charaters or less is not reccomended!") # makes the warning display
        time.sleep(1) # a timer so the user reads the the warning. 
    else: # if the users chooses to have more than 8 characters the error won't apper.
        print("please wait..") # makes the program more natural.
        time.sleep(0.3) # wait 0.3 secconds.

    for pwd in range(number): # how many passwords to make, this is disabeld because number = 1.
      password = '' 
    for c in range(length): # makes the password length the length the user said.
        password += random.choice(loweronly) # makes the password, what type of password.
    print("+--------------------------------------+") # to help user see their password
    print('Your password: ' +password)
    print("+--------------------------------------+")
    print("Thanks for using my password generator!") # a thank you note <3
    input()

if choice == "2": # if choise is value; do the following.
    number = 1

    length = input('number of characters: ')
    length = int(length)
    if length < 8:
        print("Warning: a password with 8 charaters or less is not reccomended!")
        time.sleep(1) 
    else:  
        print("please wait..")
        time.sleep(0.3)

    for pwd in range(number):
      password = ''
    for c in range(length):
        password += random.choice(upperonly)
    print("+--------------------------------------+")
    print('Your password: ' +password)
    print("+--------------------------------------+")
    print("Thanks for using my password generator!")
    input()

if choice == "3": # if choise is value; do the following.
    number = 1

    length = input('number of characters: ')
    length = int(length)
    if length < 8:
        print("Warning: a password with 8 charaters or less is not reccomended!")
        time.sleep(1) 
    else:  
        print("please wait..")
        time.sleep(0.3)

    for pwd in range(number):
      password = ''
    for c in range(length):
        password += random.choice(upperandlower)
    print("+--------------------------------------+")
    print('Your password: ' +password)
    print("+--------------------------------------+")
    print("Thanks for using my password generator!")
    input()

if choice == "4": # if choise is value; do the following.
    number = 1

    length = input('number of characters: ')
    length = int(length)
    if length < 8:
        print("Warning: a password with 8 charaters or less is not reccomended!")
        time.sleep(1) 
    else:  
        print("please wait..")
        time.sleep(0.3)

    for pwd in range(number):
      password = ''
    for c in range(length):
        password += random.choice(everything)
    print("+--------------------------------------+")
    print('Your password: ' +password)
    print("+--------------------------------------+")
    print("Thanks for using my password generator!")
    input()

if choice == "5": # if choise is value; do the following.
    number = 1

    length = input('number of characters: ')
    length = int(length)
    if length < 8:
        print("Warning: a password with 8 charaters or less is not reccomended!")
        time.sleep(1) 
    else:  
        print("please wait..")
        time.sleep(0.3)

    for pwd in range(number):
      password = ''
    for c in range(length):
        password += random.choice(upperandlowerwithnumbers)
    print("+--------------------------------------+")
    print('Your password: ' +password)
    print("+--------------------------------------+")
    print("Thanks for using my password generator!")
    input()

if choice == "6": # if choise is value; do the following.
    number = 1

    length = input('number of characters: ')
    length = int(length)
    if length < 8:
        print("Warning: a password with 8 charaters or less is not reccomended!")
        time.sleep(1) 
    else:  
        print("please wait..")
        time.sleep(0.3)

    for pwd in range(number):
      password = ''
    for c in range(length):
        password += random.choice(onlyupperwithnumbers)
    print("+--------------------------------------+")
    print('Your password: ' +password)
    print("+--------------------------------------+")
    print("Thanks for using my password generator!")
    input()

if choice == "7": # if choise is value; do the following.
    number = 1

    length = input('number of characters: ')
    length = int(length)
    if length < 8:
        print("Warning: a password with 8 charaters or less is not reccomended!")
        time.sleep(1) 
    else:  
        print("please wait..")
        time.sleep(0.3)

    for pwd in range(number):
      password = ''
    for c in range(length):
        password += random.choice(onlylowerwithnumbers)
    print("+--------------------------------------+")
    print('Your password: ' +password)
    print("+--------------------------------------+")
    print("Thanks for using my password generator!")
    input()

if choice == "8": # if choise is value; do the following.
    number = 1

    length = input('number of characters: ')
    length = int(length)
    if length < 8:
        print("Warning: a password with 8 charaters or less is not reccomended!")
        time.sleep(1) 
    else:  
        print("please wait..")
        time.sleep(0.3)

    for pwd in range(number):
      password = ''
    for c in range(length):
        password += random.choice(numbersonly)
    print("+--------------------------------------+")
    print('Your password: ' +password)
    print("+--------------------------------------+")
    print("Thanks for using my password generator!")
    input()

if choice == "9": # if choise is value; do the following.

    number = 1
    
    length = (randint(20, 99))

    for pwd in range(number):
      password = ''
    for c in range(length):
        password += random.choice(secure)
    print("+--------------------------------------+")
    print('Your password: ' +password)
    print("+--------------------------------------+")
    print("password length : %d" % len (password)) 
    print("Thanks for using my password generator!")
    input()

if choice == "10": # if choise is value; do the following.
    length = (randint(20, 99))

    number = 1

    for pwd in range(number):
      password = ''
    for c in range(length):
        password += random.choice(utf8)
    print("+--------------------------------------+")
    print('Your password: ' +password)
    print("+--------------------------------------+")
    print("password length : %d" % len (password)) 
    print("Thanks for using my password generator! you have 20 secconds to copy password.")
    time.sleep(20)
    exit()
