import requests 
url =  'https://pokeapi.co/api/v2/pokemon/'
def get_info (poke):
    pokemon = str(poke).strip().lower()
    if pokemon == '':
        print('Error: Enter a speciifc pokemon name')
        return
    print(f'Getting information for{poke}...', end='')
    p_url= 'https://pokeapi.co/api/v2/pokemon/' + pokemon
    msg = requests.get(p_url)

    if msg.status_code == requests.codes.ok:
        print('successfully completed')
        return msg.json()
    else:
        print('not completed')
        print(f'Response: {msg.status_code} ({msg.reason})')
    return
