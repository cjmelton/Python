import random as r
import time as t
import sys as s 

#This program simulation was configured by C.J. Melton
#This program is to show if you have what it takes to win the Powerball. Good luck!

the_list = [0,0,0,0,0,0]
the_num = [1,2,3,4,5,6]

print('\nWelcome to the "Powerball" Simulation!\n')
print('You must be feeling lucky!\n')

print('WARNING: This application does not advertise nor support gambling. If you win, you will not win real currency. This ' \
        'program is just made for fun and to show the odds of winning the powerball_lottery.')

def powerball():
    def instructions():
        print("\nInstructions:")
        print('Select six numbers to be on your ticket. The first five numbers can not be duplicated ranging from 1-69. The last number,' \
        ' the powerball, ranges from 1-26. If you want the machine to select the first five numbers, select easy pick ("EP").' \
        ' If you want the machine to select the number for the powerball, select easy pick ("EP").')

    def ticket_fillout():
        print("\nEnter in the first five numbers. After entering each number, click enter.")
        print('If you would like the machine to pick numbers, type "EP" and click enter.\n')

    def numbers():
        the_num[0] = r.randint(1,69)
        the_num[1] = r.randint(1,69)
        the_num[2] = r.randint(1,69)
        the_num[3] = r.randint(1,69)
        the_num[4] = r.randint(1,69)
        the_num[5] = r.randint(1,29)
        if the_num[0] == the_num[1]:
            the_num[1] = r.randint(1,69)
        elif the_num[0] or the_num[1] == the_num[2]:
            the_num[2] = r.randint(1,69)
        elif the_num[0] or the_num[1] or the_num[2] == the_num[3]:
            the_num[3] = r.randint(1,69)
        elif the_num[0] or the_num[1] or the_num[2] or the_num[3] == the_num[4]:
            the_num[4] = r.randint(1,69)

    numbers()

    def automated_option():
        t.sleep(0.5)
        print("\nHere are your first five numbers:\n")
        the_list[0] = r.randint(1,69)
        the_list[1] = r.randint(1,69)
        the_list[2] = r.randint(1,69)
        the_list[3] = r.randint(1,69)
        the_list[4] = r.randint(1,69)
        if the_list[0] == the_list[1]:
            the_list[1] = r.randint(1,69)
        elif the_list[0] or the_list[1] == the_list[2]:
            the_list[2] = r.randint(1,69)
        elif the_list[0] or the_list[1] or the_list[2] == the_list[3]:
            the_list[3] = r.randint(1,69)
        elif the_list[0] or the_list[1] or the_list[2] or the_list[3] == the_list[4]:
            the_list[4] = r.randint(1,69) 
        automated_num()

    def automated_num():
        print(the_list[0], the_list[1], the_list[2], the_list[3], the_list[4], end = '  ')
        print(" ")
            
    def powerball_num():
        print("\nEnter in your powerball number. After entering your powerball's number, click enter.")
        print('If you want to select the automated option, type "EP" and click enter.')
        while True:
            input_powerballnum = input("\nEnter in your powerball number: ")
            if input_powerballnum.lower() == "ep":
                print("\nYou have selected the automated option.")
                the_list[5] = r.randint(1,29)
                print("\nYour powerball number is: " + str(the_list[5]))
                print(" ")
                print("You have completed your ticket.")
                break
            try:
                input_powerballnum_int = int(input_powerballnum)
                if input_powerballnum_int >= 1 and input_powerballnum_int <= 29:
                    the_list[5] = input_powerballnum_int
                    print("\nYour powerball number is: " + str(the_list[5]))
                    print(" ")
                    print("You have completed your ticket.")
                    break
                else:
                    print("\nPlease select a number between 1-29 as your powerball number.")
            except ValueError:
                print("\nPlease select a number between 1-29 as your powerball number.")  
                
    def fifth_num():
        while True:
            print(" ")
            print(" ")
            input_fifthnum = int(input("Enter in your fifth number: "))
            print(' ')
            if input_fifthnum in the_list:
                print(" ")
                print("Invalid entry.")
                print(" ")
                print("Choose a different number than your first four numbers.\n")
                print("Your first four numbers are:")
                print(the_list[0], the_list[1], the_list[2], the_list[3], end = "")
            elif input_fifthnum >= 1 and input_fifthnum <= 69:
                the_list[4] = input_fifthnum
                print("Your first five numbers are:")
                print(the_list[0], the_list[1], the_list[2], the_list[3], the_list[4], end = " ")
                print(" ")
                powerball_num()
                break
            else:
                print(" ")
                print("This is not a valid entry.\nPlease enter a number between 1-69.")
            
    def fourth_num():
        while True:
            print(" ")
            print(" ")
            input_fourthnum = int(input("Enter in your fourth number: "))
            print(' ')
            if input_fourthnum in the_list:
                print(" ")
                print("Invalid entry.")
                print(" ")
                print("Choose a different number than your first three numbers.\n")
                print("Your first three numbers are:")
                print(the_list[0], the_list[1], the_list[2], end = "")
            elif input_fourthnum >= 1 and input_fourthnum <= 69:
                the_list[3] = input_fourthnum
                print("Your first four numbers are:")
                print(the_list[0], the_list[1], the_list[2], the_list[3], end = " ")
                fifth_num()
                break
            else:
                print(" ")
                print("This is not a valid entry.\nPlease enter a number between 1-69.")
            
    def third_num():
        while True:
            print(" ")
            print(" ")
            input_thirdnum = int(input("Enter in your third number: "))
            print(' ')
            if input_thirdnum in the_list:
                print(" ")
                print("Invalid entry.")
                print(" ")
                print("Choose a different number than your first two numbers.\n")
                print("Your first two numbers are:")
                print(the_list[0], the_list[1], end = "")
            elif input_thirdnum >= 1 and input_thirdnum <= 69:
                the_list[2] = input_thirdnum
                print("Your first three numbers are:")
                print(the_list[0], the_list[1], the_list[2], end = " ")
                fourth_num()
                break
            else:
                print(" ")
                print("This is not a valid entry.\nPlease enter a number between 1-69.")

    def second_num():
        while True:
            print(" ")
            print(" ")
            input_secondnum = int(input("Enter in your second number: "))
            print(' ')
            if input_secondnum in the_list:
                print(" ")
                print("Invalid entry.")
                print(" ")
                print("Choose a different number than your first number.\n")
                print("Your first number is:")
                print(the_list[0], end = "")
            elif input_secondnum >= 1 and input_secondnum <= 69:
                the_list[1] = input_secondnum
                print("Your first two numbers are:")
                print(the_list[0], the_list[1], end = " ")
                third_num()
                break
            else:
                print(" ")
                print("This is not a valid entry.\nPlease enter a number between 1-69.")

    def first_num():
        while True:
            input_firstnum = input("Enter in your first number: ")
            print(' ')
            if input_firstnum.lower() == 'ep':
                print("You have selected the automated option.")
                automated_option()
                powerball_num()
                break
            try: 
                input_firstnum_int = int(input_firstnum)
                if input_firstnum_int >= 1 and input_firstnum_int <= 69:
                    the_list[0] = input_firstnum_int
                    print("Your first number on the ticket is:")
                    print(the_list[0], end = "")
                    second_num()
                    break
                else:
                    print('\nThis is a invalid entry. Please choose a number between 1 - 69.\n')
            except ValueError:
                print("This is not a valid entry. Please choose a number between 1 - 69 or choose the EP (automated) option.\n")     

    instructions()
    ticket_fillout()
    first_num()

    print("\nPOWERBALL NUMBERS:\n")

    print(the_num[0], the_num[1], the_num[2], the_num[3], the_num[4], the_num[5])

    print("\nHere is your ticket for this Powerball simulation:\n")
    print(the_list[0], the_list[1], the_list[2], the_list[3], the_list[4],the_list[5])

    your_ticket = [the_list[0], the_list[1], the_list[2], the_list[3], the_list[4]]
    private_list = []

    for x in your_ticket:
        if x in the_num:
            private_list.append(x)

    print("\nAccording to the Powerball numbers,\n")

    if len(private_list) == 3 and the_list[5] != the_num[5]:
        print('you have won...\n') 
        print("$7!")
    elif len(private_list) == 4 and the_list[5] != the_num[5]:
        print('you have won...\n') 
        print("$100!")
    elif len(private_list) == 5 and the_list[5] != the_num[5]:
        print('you have won...\n') 
        print("$1,000,000!")
    elif len(private_list) == 0 and the_list[5] == the_num[5]:
        print('you have won...\n') 
        print("$4!")
    elif len(private_list) == 1 and the_list[5] == the_num[5]:
        print('you have won...\n') 
        print("$4!")
    elif len(private_list) == 2 and the_list[5] == the_num[5]:
        print('you have won...\n') 
        print("$7!")
    elif len(private_list) == 3 and the_list[5] == the_num[5]:
        print('you have won...\n') 
        print("$100!")
    elif len(private_list) == 4 and the_list[5] == the_num[5]:
        print('you have won...\n') 
        print("$50,000!")
    elif len(private_list) == 5 and the_list[5] == the_num[5]:
        print("you have won the Powerball Lottery! The odds you beat were 1 in 292,201,338! Congratulations!")
    else:
        print("your ticket was not lucky enough.")
        
powerball()

while True:
    print("\nWould you like to play again?")
    print("If yes, type yes and click enter.")
    print("If no, type no and click enter.\n")
    user_input = input()
    if user_input.lower() == "yes":
        the_list = [0,0,0,0,0,0]
        powerball()
    elif user_input.lower() == "no":
        print("\nThank you for playing the Powerball simulation configured by C.J. Melton!\nHope you come back to play once again!\n")
        s.exit()
        break
    else:
        print("\nInvalid option.")
    




    
