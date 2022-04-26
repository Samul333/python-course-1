import requests
import json

from constants import POKEMON_URL


def print_borders():
    print('==============Pokemon Information ================')


def get_pokemon_info():
    
    pokemon_id = input('Enter the pokemon id that you want to learn about ')
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/')
    pokemon_name = r.json()['name']
    pokemon_type = r.json()['types']
    print_borders()
    print('The name of the pokemon is ' + pokemon_name)
    for i in range(len(pokemon_type)):
        print(f'Type {pokemon_type[i]["type"]["name"]}')
    print_borders()
    



def main():
    
    run = True
    while run:
        get_pokemon_info()
        choice = input('Do you want to learn about another pokemon? (y/n) ').lower()
        
        if choice != 'y':
            run = False



if __name__ == '__main__':
    main()