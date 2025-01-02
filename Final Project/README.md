# Tic-Tac-Toe: Battle Against the Computer
    #### Video Demo:  https://youtu.be/lKFL4nzzxk8
    #### Description:

Things to do later In Sha ALLAH:

    1. I had found that in some cases the minimax doesn't seem to do what it should do, like when there is a chance that one might lose only if he misses the line of 3 forming, but not if he is an excellent player as assumed by minimax. For it I would need to store a variable corresponding to  possibility to win as well. Perhaps even a bar representing possibilities could be added.

    2. I could have used gifs and PIL libs to make gui type things and keyboard lib to automate enter or simply used the pygame lib

    3. I also could have added a feature to UNDO in the game, storing each move of the player and going one back if UNDO is entered instead of x or o, and remapped it if needed in GUI.

    4. Also could have added storing and displaying the highscores with names. Though they would have been negative. And used binary searches to operate through the scores.

    5. Timer for the user to play

    6. If the gui was used or ascii art, the cells could have been marked in every move at the bottom right corner, this approach would have been more user-friendly.

    7. This board could be extended from 3*3 to n*n with a fixed number of consecutive lines required to win.

    8. Gaming slangs and loser gifs could be added later.

    9. Though I have already corrected this in my github versions of this, this program repetitively goes through the whole minimax tree.

    10. The game can be stopped much before the all nine moves if a win by fork or a draw is destined.

The program starts by importing os and random. The os line is used at first which clears the screen and the marked grid is printed telling the user the keys to correspond to.

x or o is entered by the user, giving him the upper edge to choose if he wants to go first or second.

A list named grid always exists:
    The grid contains 9+1 elements which store the elements in the table of tic-tac-toe, with the last one storing the corresponding minimax value of the grid.

The Game loop ensures that the game functions till check_who_won() isn't 2:
    the check_who_won() returns:
        -1: if o won
         0: if draw
         1: if x won
         2: if the game still continues

The conditionals for choice for x or o ensures that if choice was o then computer goes first, otherwise player goes first.

The repetitive checking of check_who_won() ensures that the game ends and the while loop breaks at a point where check_who_won(grid) gives a value otehr than 2

Again, the os lib was used to clear the previous screen.


Before going into the complex nature and implementation of the mininax,

    1. The print_grid() function pretty prints the table of game through ascii art and to maintain equal spaces lowercase and spaces are used as list elements.

    2. Player_move takes the choice for what the player is supposed to play on the grid onto which the comp has played or is the starting grid. It ensures that the input is not corresponding to any filled space.

    3. The program only runs when run directly. as __name__ must be "__main__" to call the main() function.



To understand minimax and its implementation:

    1. Lets understand minimax:
        We should imagine ourselves in the shoes of the computer, if we had the time and resouces to find ways and form decision game trees, to play the game smartly. What would we do?
        We would play every possible game and navigate to the wins of what is assigned to us from x or o. While considering that what best can be played by nemesis and pushing towards ways that ensure are win, or draw atleast again whie considering the best move for our nemesis.
    2. Making the algorithm into coding and simple maths
        Let us say that win of x is 1 and of o is -1 and draw is 0 and mark the leaf nodes of the games to the corresponding states.
        And start by back tracing the decision-tree of every possible game of tic-tac-toe, by assigning the minimax value: max value of the branches for x's chance and min for the o's chance.
        Thus we have:

        1. minimax(l):
            It takes a list item that is a grid and returns d a list with all possible "next moves" after l also marking the values(we'll see how).
            It marks the last games and sperates them, so that they don't pass through minimax() again
            It goes through l checking for an empty space, making a shallow copy and playing x or o at the empty spot determining the chance by finding that no of moves is even or odd.
            If the game ends at that spot the tree should have an end there and hence check_who_won is used.
            else if the game doesn't end there it uses recursion and calls minimax to get the "next to next move" list within a list and stores it in e. Then min_ll or max__ll is used to get the randomised result within the min value of "next to next move" list or max value respectively. As the move is next to next min_ll is called for x and max_ll for o.
            Then all t(next move with marked values) are stored in d one by one in the same loop and finally d is returned.
        2. min_ll and max_ll
            As mentioned before these take in a list of list of marked grids and first gets the min or max marked values, however there could be many with the same value hence randomly chooses between them to make the game a little less repetitive.
