import csv
import random

pokemon_filename = 'pokemon-data.csv'
header = []

class Pokemon:
    def __init__(self, name, pokemon_type, hp, attack, defense, moves):
        self.name = name
        self.pokemon_type = pokemon_type
        self.hp = int(hp)
        self.attack = int(attack)
        self.defense = int(defense)
        self.moves = moves

def pokemon_data():
    with open(pokemon_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        pokemon_list = list(reader)
        
        # Picks a random row and gathers all the data about the pokemon
        rand = random.randint(0, len(pokemon_list) - 1)
        pokemon_info = pokemon_list[rand]
        name, pokemon_type, hp, attack, defense, _, _, moves = pokemon_info        
    return Pokemon(name, pokemon_type, hp, attack, defense, eval(moves))
