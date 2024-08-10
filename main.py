# Mini-Project: Tic-Tac-Toe Game

from time import sleep

def gameloop(): # Creating loop for continuity of game

    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    oState = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    turn = 1 # 1 for X and 0 for O

    print("\n----------------------------")      
    print("        * New Game *        ")
    print("----------------------------")

    while True:
            
        printBoard(xState, oState)
                    
        if turn == 1:
            print(f"\nX's Turn (Player-1)")
            position = int(input("Enter a position number to draw 'X': "))
            if position<0 or position>8:
                print("\nInvalid choice, enter a number between 0 and 8\n")
                break
            else:
                xState[position] = 1
                    
        else:
            print(f"\nO's Turn (Player-2)")
            position = int(input("Enter a position number to draw 'O': "))
            if position<0 or position>8:
                print("\nInvalid choice, enter a number between 0 and 8\n")
                break
            else:
                oState[position] = 1
                    
        res = result(xState, oState)

        if res != -1:
            print("Game Over...\n")
            break
                    
        turn = 1 - turn

def custom_sum(x, y, z): # Custom sum function to add the contents on list
    return x + y + z

def printBoard(x, o): # Printing the Game Board

    zero = ("X" if x[0] else ("O" if o[0] else 0))
    one = ("X" if x[1] else ("O" if o[1] else 1))
    two = ("X" if x[2] else ("O" if o[2] else 2))
    three = ("X" if x[3] else ("O" if o[3] else 3))
    four = ("X" if x[4] else ("O" if o[4] else 4))
    five = ("X" if x[5] else ("O" if o[5] else 5))
    six = ("X" if x[6] else ("O" if o[6] else 6))
    seven = ("X" if x[7] else ("O" if o[7] else 7))
    eight = ("X" if x[8] else ("O" if o[8] else 8))

    print(f"\n\t {zero} | {one} | {two} ")
    print("\t---|---|---")
    print(f"\t {three} | {four} | {five} ")
    print("\t---|---|---")
    print(f"\t {six} | {seven} | {eight} ")

def result(x, o): # Logic of Game

    winning_chances = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    for chance in winning_chances:
        
        if custom_sum(x[chance[0]], x[chance[1]], x[chance[2]])==3:
            print("\nX Wins 🎉")
            return 1
        elif custom_sum(o[chance[0]], o[chance[1]], o[chance[2]])==3:
            print("\nO Wins 🎉")
            return 0
    if sum(x) + sum(o) == 9:
        print("\nIt's a Draw!")
        return 2
    return -1
        

if __name__=="__main__":

    # Game menu using loop

    print("\n------------------------------")
    print("|    *** Tic-Tac-Toe ***     |")
    print("------------------------------")

    while True:

        print("\nDo you want to play?")
        choice = int(input("Press 1 - Yes\nPress 2 - Quit\nEnter your choice: "))

        if choice<1 or choice>2:
            print("\nInvalid choice, enter 1 or 2")
        elif choice==1:
            gameloop()
        else:
            print("\nQuitting the game...\n")
            sleep(2) # adding 2 second delay before quitting the program
            break