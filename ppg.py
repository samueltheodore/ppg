import random, time
from random import randint

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
        [10] secure+ (utf-8)

          +---------------------------------Powerful Password Generator-----------------------------------+             
 
''')

choice = input("choose a type of password from above: ")

if choice == "1":
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
        password += random.choice(loweronly)
    print("+--------------------------------------+")
    print('Your password: ' +password)
    print("+--------------------------------------+")
    print("Thanks for using my password generator!")
    input()

if choice == "2":
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

if choice == "3":
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

if choice == "4":
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

if choice == "5":
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

if choice == "6":
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

if choice == "7":
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

if choice == "8":
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

if choice == "9":

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

if choice == "10":    
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
    print("Thanks for using my password generator!")
    input()
