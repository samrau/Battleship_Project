#Final Project Pyladies Vienna Python Beginners Course - Battleship

#Project sample steps and phases
# Following steps 1-7 depend on each other, and provide the final solution gradually. If you
# complete them, you should be able to play the game!

#Step 1. Write a function that creates a grid (map) where ships will be placed. The function
# should take a list of coordinate pairs as an input, which represents the position of the
# ship. The grid should be 10 spaces by 10 spaces big and for simplicity at the
# beginning consider ships only one space big.
import random 

def draw_battleship_map(ship_positions):
    grid = [['.' for _ in range(10)] for _ in range(10)]
    for x, y in ship_positions:
        grid[y][x] = 'X'
    
    for row in grid:
        print(' '.join(row))

##example -> draw_battleship_map([(0,0),(1,0),(2,2),(8,9),(8,9)])
        
#1.Create a function that allows the user to select positions for their ships. Store this in
# a format that your draw function from Step 1 can accept as an argument. Limit the
# number of ships and verify that a position is not already taken or not outside of a
# map. After the user selects their ships, draw a map using the function from point 1.

def user_selection():
    ship_positions = []
    number_ships = 3 #limits the number of ships 
    
    while len(ship_positions) < number_ships:
        try:
            x = int(input(f"Enter x position for ship {len(ship_positions) + 1}: "))
            y = int(input(f"Enter y position for ship {len(ship_positions) + 1}: "))
            if 0 <= x < 10 and 0 <= y < 10:
                if (x,y) not in ship_positions:
                    ship_positions.append((x,y))
                else: 
                    print("Position is already taken. Please try again.")
            else: 
                print("Position is outside of the map. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return ship_positions

user_ship_positions = user_selection()
draw_battleship_map(user_ship_positions)

#2. Create a function that randomly places computer ships (also check that nothing exists on target position), but does not display the board to the player.

def computer_ship_position(number_ships):
    computer_ships = []
    while len(computer_ships) < number_ships:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if (x, y) not in computer_ships:
            computer_ships.append((x, y))
    return computer_ships
    
#3. Write a function where after asking for input, you check if the opponent's ship was
# destroyed. If yes, remove the ship from the list of coordinates. create either two
# functions (one for the player, second for the computer) or try setting default
# arguments to a single function to play randomly for the computer.

def player_turn(opponent_ships):
    while True:
        try:
            x = int(input("Enter x position for attack: "))
            y = int(input("Enter y position for attack: "))
            if 0 <= x < 10 and 0 <= y < 10:
                target = (x, y)
                if target in opponent_ships:
                    opponent_ships.remove(target)
                    print("You've destroyed the ship!")
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
        print("You've destroyed the ship!")
        if not opponent_ships:
            print("Computer wins!")
            return True
    else:
        print("You've missed!")
    return False
#4. Let's put it together: write a main function where the player and computer (after
# placing their ships) iterate in guessing the opponent's ship location. Keep score and
# let players know their successes or misses. The game ends when one of the player's
# lists of ships is empty. Congratulations! You have a game!

def main():
    num_computer_ships = 3 

    print("Player, place your ships:")
    player_ship_positions = user_selection() 

    print("\nComputer is placing its ships...")
    computer_ship_positions = computer_ship_position(num_computer_ships)

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
