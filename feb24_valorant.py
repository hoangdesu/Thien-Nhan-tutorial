import requests

def help(data):
    print()
    for i in range(len(data)):
        agent = data[i]
        print(f"{i+1}. {agent.get('displayName')}")
    print()
    
def getAgent(userInput, data):
    print()
    
    # linear search
    foundAgent = None
    
    for agent in data:
        if userInput == agent.get('displayName').lower():
            foundAgent = agent
            break
        
    # display info if found
    if foundAgent == None:
        print('No agent found')
    else:
        displayName = foundAgent.get('displayName')
        description = foundAgent.get('description')
        developerName = foundAgent.get('developerName')
        abilities = foundAgent.get('abilities')
        
        print(f'Display name: {displayName}')
        print(f'Description: {description}')
        print(f'Developer name: {developerName}')
        
        print('Abilities:')
        for i in range(len(abilities)):
            ability = abilities[i]
            print(f"{i+1}. {ability.get('displayName')}")
    print()


def main():
    langs = ['en-US', 'vi-VN', 'ko-KR']
    for index, lang in enumerate(langs):
        print(index+1, lang)
    language = input('Enter a number for your language: ')
    
    if language == '':
        language = 1
    else:
        language = int(language)
    
    URL = f'https://valorant-api.com/v1/agents?language={langs[language-1]}&isPlayableCharacter=true'
    response = requests.get(URL)
    if not response.ok:
        print('Error')
        exit()
    contentJson = response.json()
    data = contentJson['data']

    while True:
        userInput = input('Enter an agent name or type "help" to display all agents: ').lower()

        if userInput == 'help':
            help(data)
        elif userInput in ['q', 'quit', 'exit', '0']:
            exit()
        else:
            getAgent(userInput, data)
      

if __name__ == '__main__':        
    main()
    


