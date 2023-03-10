Palindrome: the string is mirroed from the middle

abba

class vs objects

OOP: object-oriented programming?

Write a Game player management system using OOP:
    - add a new player to a JSON file
    - look for a player
    - delete a player
    - update a player
    
Player:
    - id: string/int (unique)
    - realName: string
    - userName: string
    - email: string (has to conform to "something[@]something[.]something") -> check if email is valid
    - password: string (level 1: store the plain password => Level 2: store the HASHED password)
    
    
import json
with open('./path/file.json', 'w') as file:
    json.dump(players, file)
    
    
Paradigm: pattern of programming that a project/lang tends to follow


client-sided (frontend): CLI command-lined interface (vs GUI graphical user interface)
server-sided (backend): Python as the prog lang, JSON as DB
    
    
List = ['']
    
    
    
    
    
    
    
class Player:
    ...
    
    # getters/setters