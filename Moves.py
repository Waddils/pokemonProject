import csv

move_filename = 'moves-data.csv'
header = []

class Moves:
    def __init__(self, name, move_type, power):
        self.name = name
        self.move_type = move_type
        self.power = int(power)
        self.used = False


def get_moves_for_pokemon(pokemon):
    skills = []
    with open(move_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        
        # Parses through and finds each move of the desired Pokemon
        for row in reader:
            name, move_type, _, _, _, power, _ = row
            
            if name in pokemon.moves:
                skills.append(Moves(name, move_type, power))
    
    return skills

def mark_move_as_used(moves, selected_move):
    for move in moves:
        if move.name == selected_move.name:
            move.used = True
            move.name += " (N/A)"
            break
        
def reset_moves(moves):
    for move in moves:
        move.used = False
        move.name = move.name.replace(" (N/A)", "")