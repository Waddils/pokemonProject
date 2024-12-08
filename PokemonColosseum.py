import math
import random
from Pokemon import pokemon_data
from Moves import get_moves_for_pokemon, mark_move_as_used, reset_moves

def damage_calc(M, A, B):
    '''
        M = Move user chose
        A = Attack of the attacking pokemon
        B = Defense of the defending pokemon
    '''
    
    STAB = 1
    if M.move_type == A.pokemon_type:
        STAB = 1.5
    
    damage = int((M.power * (A.attack / B.defense) * STAB * TE(M, B) * random.uniform(0.5, 1)))
    rounded_damage = math.ceil(damage)
    
    return rounded_damage

def TE(M, B):
    default_damage = 1
    pokeType = B.pokemon_type
    
    match M.move_type:
        case "Normal":
            return default_damage
        
        case "Fire":
            if (pokeType == "Fire") or (pokeType == "Water"):
                return 0.5
            elif pokeType == "Grass":
                return 2
            else:
                return default_damage
            
        case "Water":
            if (pokeType == "Water") or (pokeType == "Grass"):
                return 0.5
            elif pokeType == "Fire":
                return 2
            else:
                return default_damage
        
        case "Electric":
            if (pokeType == "Electric") or (pokeType == "Grass"):
                return 0.5
            elif pokeType == "Water":
                return 2
            else:
                return default_damage
        
        case "Grass":
            if (pokeType == "Grass") or (pokeType == "Fire"):
                return 0.5
            elif pokeType == "Water":
                return 2
            else:
                return default_damage
        
        case _:
            return default_damage


def isPokemonDead(currentPokemon, rocketCurrPokemon, playerCurrPokemon):
    # Checks if the current pokemon is dead
    if currentPokemon.hp <= 0:
        if currentPokemon == playerCurrPokemon:
            currentPlayer = rocketTeam
            otherPlayer = playerTeam
        else:
            currentPlayer = playerTeam
            otherPlayer = rocketTeam
    
        if otherPlayer:
            nextPokemon = otherPlayer.pop(0)
        
        # Logic if a pokemon dies on the player's/rocket's side
        # Team Rocket's Turn
        if currentPlayer == rocketTeam:
            print(f"Now {rocketCurrPokemon.name} has {rocketCurrPokemon.hp} HP, and {currentPokemon.name} faints back to poke ball.")
            print()
            
            if len(otherPlayer) == 0:
                return nextPokemon, True, True
            
            print(f"Next for Team {name}, {otherPlayer[0].name} enters battle!")
            print()
            return nextPokemon, True, False
        
        # Player's Turn
        elif currentPlayer == playerTeam:
            print(f"Now {currentPokemon.name} faints back to poke ball, and {playerCurrPokemon.name} has {playerCurrPokemon.hp} HP.")
            print()
            
            if len(otherPlayer) == 0:
                return nextPokemon, True, True
            
            print(f"Next for Team Rocket, {otherPlayer[0].name} enters the battle!")
            print()
            return nextPokemon, True, False
    else:
        return None, False, False



#############################################
#           Phase 1 - Introduction          #
#############################################

print("Welcome to the Pokemon Colosseum!")
print()

name = input("Enter your name: ")
print()

#-------------------------------------------#

rocketTeam = []
for i in range(3):
    new_pokemon = pokemon_data()
    
    # Ensures there are no duplicate pokemon in the battle
    while any(Pokemon.name == new_pokemon.name for Pokemon in rocketTeam):
        new_pokemon = pokemon_data()
           
    rocketTeam.append(new_pokemon)

# Print the names of Pokemon in Team Rocket
rocketPokemonNames = [Pokemon.name for Pokemon in rocketTeam]

if len(rocketPokemonNames) > 1:
    rocketPokemonNames[-1] = "and " + rocketPokemonNames[-1]
    
print("Team Rocket enters with " + ', '.join(rocketPokemonNames) + ".")
print()



playerTeam = []
for i in range(3):
    new_pokemon = pokemon_data()
    
    # Ensures there are no duplicate pokemon in the battle
    while any(Pokemon.name == new_pokemon.name for Pokemon in rocketTeam):
        new_pokemon = pokemon_data()
    while any(Pokemon.name == new_pokemon.name for Pokemon in playerTeam):
        new_pokemon = pokemon_data()
        
    playerTeam.append(new_pokemon)

playerPokemonNames = [Pokemon.name for Pokemon in playerTeam]

if len(playerPokemonNames) > 1:
    playerPokemonNames[-1] = "and " + playerPokemonNames[-1]
    
print("Team " + name + " enters with " + ', '.join(playerPokemonNames) + ".")
print()



#############################################
#           Phase 2 - Who Starts            #
#############################################

print("Let the battle begin!")

# Random coin toss to choose the starting player
turn = random.randint(0, 1)
startingTeam = name if turn == 0 else "Team Rocket"
    
print("Coin toss goes to ----- " + startingTeam + " to start the attack!")
print()



#############################################
#         Phase 3 - Colosseum Fight         #
#############################################
hitpoints = 0      
hasFainted = False
end_battle = False
playerMoves = []
rocketMoves = []
playerCurrPokemon = playerTeam[0]        
rocketCurrPokemon = rocketTeam[0]

while True:
    
    # Player's Turn
    if turn == 0:
        # Lists all the moves of the selected pokemon
        if not playerMoves:
            playerMoves = get_moves_for_pokemon(playerCurrPokemon)
            
        print(f"Choose the move for {playerCurrPokemon.name}:")
        
        for i, move in enumerate(playerMoves, start = 1):
            print(f"{i}. {move.name}")
        
        print()

        while True:
            try:   
                choice = int(input(f"Team {name}'s choice: "))
                print()
                
                if not(0 < choice <= len(playerMoves)):
                    print("Please enter a valid move number")
                    print()
                    
                    print(f"Choose the move for {playerCurrPokemon.name}:")
                    for i, move in enumerate(playerMoves, start = 1):
                        print(f"{i}. {move.name}")
                    print()
                        
                else:
                    selectedMove = playerMoves[choice - 1]
                    
                    if selectedMove.used == True:
                        print("Choose a move you haven't used")
                        print()
                        
                        print(f"Choose the move for {playerCurrPokemon.name}:")
                        for i, move in enumerate(playerMoves, start = 1):
                            print(f"{i}. {move.name}")
                        print()
                        
                    elif 0 < choice <= len(playerMoves):
                        print(f"{playerCurrPokemon.name} used '{selectedMove.name}' on {rocketCurrPokemon.name}:")

                        # Disables the move(s) temporarily
                        mark_move_as_used(playerMoves, selectedMove)
                        break
    
            except ValueError:
                print()
                print("Please enter a numerical value")
                print()
        
        # Damage Calculator
        hitpoints = damage_calc(selectedMove, playerCurrPokemon, rocketCurrPokemon)
        
        print(f"Damage to {rocketCurrPokemon.name} is {hitpoints} points.")
        
        rocketCurrPokemon.hp -= hitpoints
        if rocketCurrPokemon.hp <= 0:
            rocketCurrPokemon.hp = 0
        
        rocketDefeatedPokemon, hasFainted, end_battle = isPokemonDead(rocketCurrPokemon, rocketCurrPokemon, playerCurrPokemon)
        if hasFainted and end_battle == False:
            reset_moves(rocketMoves)
            rocketCurrPokemon = rocketTeam[0]  
            rocketMoves = get_moves_for_pokemon(rocketCurrPokemon)
        elif end_battle == True:
            print(f"All of Team Rocket's Pokemon fainted, and Team {name} prevails!")
            break
        elif hasFainted == False:
            print(f"Now {rocketCurrPokemon.name} has {rocketCurrPokemon.hp} HP, and {playerCurrPokemon.name} has {playerCurrPokemon.hp} HP.")
            print()
        
        # Checks to see whether or not the player has used all moves
        if all(move.used for move in playerMoves):
            reset_moves(playerMoves)
        
        hasFainted = False
        hitpoints = 0
        turn = 1

############################################# 

    # Team Rocket's Turn
    if turn == 1:    
        # Logic for gathering moves for Team Rocket's pokemon
        if not rocketMoves:
            rocketMoves = get_moves_for_pokemon(rocketCurrPokemon)
        
        selectedMove = random.choice(rocketMoves)
        
        while True:
            if selectedMove.used == True:
                selectedMove = random.choice(rocketMoves)
            else:
                break
            
        print(f"Team Rocket's {rocketCurrPokemon.name} used '{selectedMove.name}' on {playerCurrPokemon.name}:")

        # Disables the move(s) temporarily
        mark_move_as_used(rocketMoves, selectedMove)

        # Damage Calculation
        hitpoints = damage_calc(selectedMove, rocketCurrPokemon, playerCurrPokemon)
        
        print(f"Damage to {playerCurrPokemon.name} is {hitpoints} points.")

        playerCurrPokemon.hp -= hitpoints
        if playerCurrPokemon.hp <= 0:
            playerCurrPokemon.hp = 0
        
        playerDefeatedPokemon, hasFainted, end_battle = isPokemonDead(playerCurrPokemon, rocketCurrPokemon, playerCurrPokemon)
        if hasFainted and end_battle == False:
            reset_moves(playerMoves)
            playerCurrPokemon = playerTeam[0] 
            playerMoves = get_moves_for_pokemon(playerCurrPokemon)
        elif end_battle == True:
            print(f"All of Team {name}'s Pokemon fainted, and Team Rocket prevails!")  
            break
        elif hasFainted == False:
            print(f"Now {rocketCurrPokemon.name} has {rocketCurrPokemon.hp} HP, and {playerCurrPokemon.name} has {playerCurrPokemon.hp} HP.")
            print()
        
        # Checks to see whether or not the player has used all moves
        if all(move.used for move in rocketMoves):
            reset_moves(rocketMoves)
        
        hasFainted = False
        hitpoints = 0
        turn = 0