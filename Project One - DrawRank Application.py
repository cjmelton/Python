import random as r
import time as t
import sys as s 

#Application that contains both ranking and drawing participants
#Configured by C.J. Melton

#If you would like to host a drawing, start this program to do so.
#If you would like to randomly rank a group of people or objects, start this program to do so.

def drawrank_application():
    list = []

    def new_list():
        list.clear()
        enter_participants()
        main_menu()
    
    def quit():
        print("\nThank you for using this application configured by C.J. Melton!\nI hope you visit again!\n")
        s.exit()

    def enter_participants():
        print('\nAdd each participant to the list and click enter.\n'\
        'To stop adding names, type "STOP" and click enter.')
        print('To quit, enter: QUIT\n')

        while True:
            user_input = str(input())
            if user_input.lower() == "stop":
                t.sleep(1)
                print("\nParticipants have been entered.")
                break
            list.append(user_input)
            if user_input.lower() == 'quit':
                quit()
        return list
    
    def adjusted_list():
            number = 1
            print('\nThe list:\n')
            for x in list:
                print(str(number) + ". " + str(x))
                number += 1

    def app_selection():
        adjusted_list()        
        t.sleep(0.5)
        while True:
            print('\nSelect the following options:')
            t.sleep(0.25)
            print('To proceed with the drawing of the list entered, enter: DRAW')
            t.sleep(0.25)
            print('To proceed with a ranking of the list entered, enter: RANK')
            t.sleep(0.25)
            print('To make modifications to the list, enter: MODIFY')
            t.sleep(0.25)
            print("To reenter a new list, enter: REENTER")
            t.sleep(0.25)
            print('To quit the application, enter: QUIT')
            print("Click enter after typing request.\n")
            user_choice = input()
            if user_choice.lower() == 'draw':
                winning_participant()
            elif user_choice.lower() == 'rank':
                ranking()
            elif user_choice.lower() == 'modify':
                mod_options()
            elif user_choice.lower() == 'reenter':
                new_list()
            elif user_choice.lower() == 'quit':
                quit()
                break
            else:
                print("\nInvalid option.")

    def mod_options():
        adjusted_list()

        t.sleep(0.5)
        print('\nSelect the following options:')
        t.sleep(0.25)
        print('To continue with the list above, enter: CONTINUE')
        t.sleep(0.25)
        print('To add to the list, enter: ADD')
        t.sleep(0.25)
        print('To edit an participant in the list, enter: EDIT')
        t.sleep(0.25)
        print('To remove a participant in the list, enter: REMOVE')
        t.sleep(0.25)
        print('To quit the application, enter: QUIT')
        print("Click enter after typing request.\n")

        while True:
            user_choice = input()
            if user_choice.lower() == "continue":
                app_selection()
            elif user_choice.lower() == 'add':
                add()
            elif user_choice.lower() == 'edit':
                edit()
            elif user_choice.lower() == 'remove':
                remove()
            elif user_choice.lower() == "continue":
                app_selection()
            elif user_choice.lower() == 'quit':
                quit()
            else:
                print("\nInvalid option")
            return mod_options()

    def main_menu():

        t.sleep(0.25)
        print("\nHere is your list:\n")
        t.sleep(0.25)
        for x in list:
            print(x, end = " \n")
        t.sleep(0.5)
        print("\nWould you like to proceed with the application?")

        
        while True:
            t.sleep(0.5)
            print("Choose an option:")
            print("If yes, enter: YES")
            print("If no, enter: NO")
            print("Click enter after typing request.\n")
            user_input = input()
            if user_input.lower() == 'yes':
                app_selection()
                break
            elif user_input.lower() == 'no':
                while True:
                    t.sleep(0.25)
                    print("\nSelect an option.")
                    print("To go back, enter: BACK")
                    print("To reenter a new list, enter: REENTER")
                    print("To quit, enter: QUIT")
                    user_choice = input('\n')
                    if user_choice.lower() == 'back':
                        main_menu()
                    if user_choice.lower() == 'reenter':
                        return new_list()
                    elif user_choice.lower() == 'quit':
                        quit()
                    else:
                        t.sleep(0.25)
                        print('\nInvalid option.')
            else:
                    print('\nInvalid option. Please enter "YES" for yes or "NO" for no.')   
 
    def edit():
        adjusted_list()
        while True:
            user_input = input('\nSelect the number of the participant, you would like to edit:\n\n')
            try:
                integer_value = int(user_input)
                list_data_point = integer_value - 1
                while True:
                    if list_data_point <= 0:
                        print("\nPlease select a option presented in the list.")
                        print("The number entered is not within the list.")
                        t.sleep(0.25)
                        return edit()
                    elif list_data_point > len(list):
                        print("\nPlease select a option presented in the list.")
                        print("The number entered is not within the list.")
                        t.sleep(0.25)
                        return edit()
                    else:
                        selected_option = list[list_data_point]                         
                        user_choice = input("\nEnter your participant replacement for " + str(selected_option) + ":\n\n")
                        list[list_data_point] = user_choice
                        t.sleep(0.25)
                        print("\nList has been modified.")
                        return mod_options()
            except ValueError:
                    t.sleep(0.25)
                    print('\nInvalid option.')
                    t.sleep(0.25)
        
    def add():
        adjusted_list()
        print("\nAdd each additional participant, click enter when completed.")
        print('To stop adding participants, type "STOP" and click enter.\n')
        while True:
            user_input = input()
            if user_input.lower() == 'stop':
                print('\nParticipants have been added.')
                break
            list.append(user_input)
        return mod_options()
            
    def remove():
        while True:
            adjusted_list()
            t.sleep(0.25)
            user_input = input('\nSelect the number of the participant, you would like to remove:\n\n')
            try:
                integer_value = int(user_input)
                list_data_point = integer_value - 1
                while True:
                    if list_data_point <= 0:
                        print("\nPlease select a option presented in the list.")
                        print("The number entered is not within the list.")
                        return remove()
                    elif list_data_point > len(list):
                        print("\nPlease select a option presented in the list.")
                        print("The number entered is not within the list.")
                        return remove()
                    else:
                        list.remove(list[list_data_point])                         
                        t.sleep(0.25)
                        print("\nList has been modified.")
                        return mod_options()
            except ValueError:
                t.sleep(0.25)
                print('\nInvalid option. Please enter a number on the list.')
                t.sleep(0.25)
            return remove()

    def winning_participant():
        print("\nAnd the winner is...\n")
        t.sleep(2)
        winner = r.choice(list)
        print(winner)

        t.sleep(0.25)
        while True:
            print('\nWould you like to execute another drawing?')
            print('Select the following options:')
            print('To continue, enter: YES')
            print('To go back to the main menu, enter: BACK')
            print("To reenter a new list, enter: REENTER")
            print('To quit the application, enter: QUIT')
            print("Click enter after typing request.\n")
            user_input = input()
            if user_input.lower() == 'yes':
                return winning_participant()
            elif user_input.lower() == 'back':
                app_selection()
            elif user_input.lower() == 'reenter':
                new_list()
            elif user_input.lower() == 'quit':
                quit()
                break
            else:
                print("\nInvalid option.")

    def ranking():
        number = 1
        rankings = r.shuffle(list)
        print("\nAnd here are your rankings: \n")
        t.sleep(2)
        for x in list:
            print(str(number) + ". " + str(x))
            number += 1

        t.sleep(0.25)
        while True:
            print('\nWould you like to execute another ranking?')
            print('Select the following options:')
            print('To continue, enter: YES')
            print('To go back to the main menu, enter: BACK')
            print("To reenter a new list, enter: REENTER")
            print('To quit the application, enter: QUIT')
            print("Click enter after typing request.\n")
            user_input = input()
            if user_input.lower() == 'yes':
                return ranking()
            elif user_input.lower() == 'back':
                app_selection()
            elif user_input.lower() == 'reenter':
                new_list()
            elif user_input.lower() == 'quit':
                quit()
                break
            else:
                print("\nInvalid option.")
        
    enter_participants()
    main_menu()

drawrank_application()


