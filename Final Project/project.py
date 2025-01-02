import random
import os

def main():
    
    
    os.system("cls" if os.name == "nt" else "clear")
    
    # Just to show the user the grid marking
    printing_grid=[]
    for i in range(3):
        for j in range(3):
            printing_grid.append(i*3+j+1)

    print_grid(printing_grid)
    
    print("\nWelcome to TicTacToe!")
    
    
    # Asking the user to choose between x and o
    while True:
        choice=input("Would you like to play enter x or o: ")
        if choice in ["x", "o"]:
            break
    
    # The default grid with extra element for value (len(l))=10 and not 9
    grid=[" "]*(9+1)
    
    
    
    # Performing the actual grid loop till the game ends, (game-loop)
    while True:
        if choice=="o":
            # Getting the best move for x
            grid=max_ll(minimax(grid))
            #Printing the grid to the user again and again
            print_grid(grid)
            
            state=check_who_won(grid)
            if state!=2:
                break
        
        
        if player_move(choice,grid)=="undo":
            grid=prev_grid
        else:
            prev_grid=list(grid)
        os.system("cls" if os.name == "nt" else "clear")
        
          
          
        # Ending the game if win/lose/draw
        state=check_who_won(grid)
        if state!=2:
            break
          
          
            
        if choice=="x":
        # Storing the optimal move for o in l
            grid=min_ll(minimax(grid))
        
        #Printing the grid to the user again and again
            print_grid(grid)
            # Ending the game if win/lose/draw
            state=check_who_won(grid)
            if state!=2:
                break 
        
    # The player will never win, In Sha ALLAH 
    if state!=0:
        print("Computer Wins!!")
    else:
        print("It's Draw!, you'll never win against me!")
   
    
    
def print_grid(grid):
    # Printing the grid using ASCII, Fomating may not make sense till printed again and again
    for i in range(3):
        for j in range(3):
            print(f"| {grid[j+i*3]} ", end="")
        print("|")
        if i!=2:   
            print(" ___"*3+"\n")

    

        




def check_who_won(l):
    # Checking 3 consecutive horizontally, vertically and diagonally respectively

    if (l[0]==l[1] and l[1]==l[2] and l[2]=="x")| (l[3]==l[4] and l[4]==l[5] and l[5]=="x")|( l[6]==l[7] and l[7]==l[8] and l[8]=="x"):
        return 1 # 1 for win of x
    elif (l[0]==l[3] and l[3]==l[6] and l[6]=="x")|(l[1]==l[4] and l[4]==l[7] and l[7]=="x")|(l[2]==l[5] and l[5]==l[8] and l[8]=="x"):
        return 1
    elif (l[0]==l[4] and l[4]==l[8] and l[8]=="x")|(l[2]==l[4]and l[4]==l[6] and l[6]=="x"):
        return 1
    elif (l[0]==l[1] and l[1]==l[2] and l[2]=="o")|(l[3]==l[4] and l[4]==l[5] and l[5]=="o")|(l[6]==l[7] and l[7]==l[8] and l[8]=="o"):
        return -1 # -1 for win of o
    elif (l[0]==l[3] and l[3]==l[6] and l[6]=="o")|(l[1]==l[4] and l[4]==l[7] and l[7]=="o")|(l[2]==l[5] and l[5]==l[8] and l[8]=="o"):
        return -1
    elif (l[0]==l[4] and l[4]==l[8] and l[8]=="o")|(l[2]==l[4] and l[4]==l[6] and l[6]=="o"):
        return -1
    # Checking if all chances are exhausted: 0 corresponds to draw
    elif l.count("x")+l.count("o")==9:
        return 0
    # If more chances can be played: 2
    else:
        return 2
        









        

# Try to construct a minimax that returns choices of move at position l and their corresponding values
# It automatically detects whose chance it is by counting x and o in l
def minimax(l):
    
    # d should store the choices for the one move after l and their values as the last element of each element in d
    d=[]
    
    # To process every possible move and get its value
    for i in range(len(l)-1):
        
        # Move has to be played at an empty spot
        if l[i]==" ":
            
            # Making a shallow copy of l
            t=list(l)
            
            # Imaginarily playing x or o
            if (l.count("x")+l.count("o"))%2==0:
                t[i]="x"
            else:
                t[i]="o"
                
            # If this move ends the game: marking value directly
            if check_who_won(t)!=2:
                t[-1]=check_who_won(t)
                
            # If this move doesn't end the game: using recursion
            else:
                e=minimax(t)
                
                # Is it the chance of x or o
                if (l.count("x")+l.count("o"))%2==0:
                    t[-1]=min_ll(e)[-1] # if l was x then e must be o
                else:
                    t[-1]=max_ll(e)[-1] # if o was x then e must be x
             
             # Storing this move in d   
            d=d+[t]
    return d

# returns list from list of list with the greatest last element (value)
def min_ll(e):
    index=0 # index for e
    value=e[0][-1]
    randomised=[]
    for i in range(len(e)):
        if e[i][-1]<value:
            value=e[i][-1]
            index=i
            
    # Randomly choosing between the same but min values
    for i in range(len(e)):
        if e[index][-1]==e[i][-1]:
            randomised.append(i)
    rand_index=randomised[random.randrange(0,len(randomised))]
    return e[rand_index]


# Returns list from list of list with the smallest last element (value)
def max_ll(e):
    index=0 # index for e
    value=e[0][-1]
    
    for i in range(len(e)):
        if e[i][-1]>value:
            value=e[i][-1]
            index=i
            
            
    # Randomly choosing between the same but max values
    randomised=[]
    for i in range(len(e)):
        if e[index][-1]==e[i][-1]:
            randomised.append(i)
    rand_index=randomised[random.randrange(0,len(randomised))]
    return e[rand_index]


        
def player_move(chance, grid):
    # Preventing the user form entering into a filled block
    while True:
        
        inp=int(input(f"Enter from 1 to 9: "))
        if str(inp).lower()=="undo":
            return "undo"
        else:
            inp=inp-1
        
        if grid[inp]==" " and chance=="x":
            grid[inp]="x"
            break
        if grid[inp]==" " and chance=="o":
            grid[inp]="o"
            break

if __name__=="__main__":
    main()
    
