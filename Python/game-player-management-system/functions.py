from Player import *
import json

def displayCommands(): 
    print('1. add new player')
    print('2. update a player')
    print('3. remove a player')
    print('4. find a player')
    
def createNewUser():
    # create the player object
    name = input('Enter your name: ')
    password = input('Enter your password: ')
    # password validation -> function
    # password2 = input('Enter your password again: ')
    
    newPlayer = Player(name, password) # object from class
    
    # confirm if the user wants to save player
    if input('Do you want to save: ').lower() == 'y':
        saveToJson(newPlayer)
        
    
    # if yes, save to json
    
    
def validatePassword(p1, p2):
    ...
    
def saveToJson(player):
    # file = open('file')
    playerList = None
    with open('./playerDB.json', 'r') as file:
        # content = file.read()
        # print(content)
        # json.loads(content)
        
        playerList = json.load(file)
        
        file.close() # make sure to close the file to avoid leaking memory
        
    if playerList != None:
        # playerList.append(player.__dict__)
        playerList.append(vars(player))
        print(playerList)
        
    with open('./playerDB.json', 'w') as file:
        # json.dump(playerList)
        ...
        # json.load
        json.dump(playerList, file, indent=4)
        file.close()
        
