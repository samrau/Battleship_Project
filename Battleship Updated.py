#Final Project Pyladies Vienna Python Beginners Course - Battleship

#Project sample steps and phases
# Following steps 1-7 depend on each other, and provide the final solution gradually. If you
# complete them, you should be able to play the game!
#Includes task 5: Now the game is working, but it is time to make it slightly more interesting. Let's put
# bigger ships into the place. Ships are no longer only single spaces, but create 1x five
# space big ships, 2x three space big ships, and 3x two space ones. If a player or
# computer hits a ship, tell them the size of their target.

#Step 1. 
import random 

def draw_battleship_map(ship_positions):
    grid = [['.' for _ in range(10)] for _ in range(10)]
    for x, y in ship_positions:
        grid[y][x] = 'X'
    
    for row in grid:
        print(' '.join(row))

##example -> draw_battleship_map([(0,0),(1,0),(2,2),(8,9),(8,9)])
        
#1.

def user_selection():
    ship_positions = []
    ship_sizes = [5, 3, 3, 2, 2, 2]  # Sizes of ships
    for size in ship_sizes:
        while True:
            try:
                print(f"Place a ship of size {size}")
                x = int(input(f"Enter x position for the ship (size {size}): "))
                y = int(input(f"Enter y position for the ship (size {size}): "))
                orientation = input("Enter orientation (h for horizontal, v for vertical): ").lower()
                
                if orientation == 'h':
                    positions = [(x+i, y) for i in range(size)]
                elif orientation == 'v':
                    positions = [(x, y+i) for i in range(size)]
                else:
                    print("Invalid orientation! Please enter 'h' for horizontal or 'v' for vertical.")
                    continue
                
                valid = all(0 <= pos[0] < 10 and 0 <= pos[1] < 10 and pos not in ship_positions for pos in positions)
                if valid:
                    ship_positions.extend(positions)
                    break
                else:
                    print("Invalid position! Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return ship_positions

#2. 

def computer_ship_position():
    ship_sizes = [5, 3, 3, 2, 2, 2]  # Sizes of ships
    computer_ships = []
    for size in ship_sizes:
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            orientation = random.choice(['h', 'v'])
            
            if orientation == 'h':
                positions = [(x+i, y) for i in range(size)]
            elif orientation == 'v':
                positions = [(x, y+i) for i in range(size)]
                
            if all(0 <= pos[0] < 10 and 0 <= pos[1] < 10 and pos not in computer_ships for pos in positions):
                computer_ships.extend(positions)
                break
    return computer_ships
    
#3. 
def player_turn(opponent_ships):
    while True:
        try:
            x = int(input("Enter x position for attack: "))
            y = int(input("Enter y position for attack: "))
            if 0 <= x < 10 and 0 <= y < 10:
                target = (x, y)
                if target in opponent_ships:
                    opponent_ships.remove(target)
                    print(f"You've hit a ship of size {len(opponent_ships)+1}!")
                    if not opponent_ships:
                        print("Player wins!")
                        return True
                else:
                    print("You've missed!")
                return False
            else:
                print("Position is outside of the map. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def computer_turn(opponent_ships):
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    target = (x, y)
    if target in opponent_ships:
        opponent_ships.remove(target)
        print(f"Computer hit your ship of size {len(opponent_ships)+1}!")
        if not opponent_ships:
            print("Computer wins!")
            return True
    else:
        print("Computer missed!")
    return False

#4. 

def main():
    print("Player, place your ships:")
    player_ship_positions = user_selection() 

    print("\nComputer is placing its ships...")
    computer_ship_positions = computer_ship_position()

    player_score = 0
    computer_score = 0

    while player_ship_positions and computer_ship_positions:
        print("\nPlayer's Turn:")
        if player_turn(computer_ship_positions):
            player_score += 1
            if not computer_ship_positions:
                print("Congratulations, Player wins!")
                break
        print("\nComputer's Turn:")
        if computer_turn(player_ship_positions):
            computer_score += 1
            if not player_ship_positions:
                print("Congratulations, Computer wins!")
                break
            
    print("\nGame over!")

    if not player_ship_positions:
        print("Gameover, computer won.")
        print(f"Your score: {player_score}")
    else:
        print("Congratulations!")
        print(f"Computer's score: {computer_score}")

    # Display both player's and computer's ship positions at the end
    print("\nPlayer's Ship Positions:")
    draw_battleship_map(player_ship_positions)
    
    print("\nComputer's Ship Positions:")
    draw_battleship_map(computer_ship_positions)

if __name__ == "__main__":
    main()

# 6. Think about a better strategy for a computer than random and implement it - maybe next to the previous hit?
#Something that would improve the game is if I added in case the computer manages to successfully destroy a ship, automatically next steps would be to target the cells surrounding the destroyed one.
