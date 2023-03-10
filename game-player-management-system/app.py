# dictionary = {}

# app should only contain the main runninng code (interface)
# functions/implementations shoud be splitted into module

from functions import *
# import functions


def main():
    displayCommands()
    command = input('Enter your command: ')
    
    if command == '1':
        createNewUser()

    
    # userChoice = getUserInput()
    # operation()
    
    
    
    
if __name__ == '__main__':
    main()