'''
Princess Peach is trapped in one of the four corners of a square grid. You are in the center of the grid and can
move one step at a time in any of the four directions. Can you rescue the princess?

Input format:

The first line contains an odd integer (3<= N <= 100) denoting the size of the grid. This is followed by an
N X N grid. Each cell is denoted by '-'. The bot position is denoted by 'm' and the princess position is denoted
by 'p'.

Grid is indexed using Matrix Convention

Output format:

Print out the moves you will take to rescue the princess in one go. The moves must be separated by '\n', a new line.
The valid moves are LEFT, RIGHT, UP or DOWN.

Sample input:

3
---
-m-
p--

Sample output:
DOWN
LEFT

Task:

Complete the function displayPathtoPrincess() which takes in two parameters. The integer N and the character array
grid. The grid will be formatted exactly as you see it in the input, so for the sample input, the princess is at
grid[2][0]. The function shall output moves (LEFT, RIGHT, UP or DOWN) on consecutive lines to rescue/reach the princess.
The goal is to reach the princess in as few moves as possible.

The princess 'p' can be in any one of the four corners.
'''

def displayPathtoPrincess(N, grid):

    '''
    First thing first: We need to stablish the size of the grid, and the grid itself.

    Then, we need to locate the positions of the bot ('m') and the princess ('p')
    '''

    bot_pos = (0,0)

    princess_pos = (0, 0)

    # Find the positions of m and p

    for i in range(N):

        for j in range(N):

            if grid[i][j] == 'm':

                bot_pos = (i,j)
            
            elif grid[i][j] == 'p':

                princess_pos = (i,j)

    # Calculate the moves

    moves = []

    row_diff = princess_pos[0] - bot_pos[0]

    col_diff = princess_pos[1] - bot_pos[1]

    if row_diff > 0:

        moves.extend(['DOWN'] * row_diff)

    else:

        moves.extend(['UP'] * (-row_diff))

    if col_diff > 0:

        moves.extend(['RIGHT'] * col_diff)

    else:

        moves.extend(['LEFT'] * (-col_diff))

    return moves


N = int(input())

grid = []

for _ in range(N):

    grid.append(input().strip())

moves = displayPathtoPrincess(N, grid)

print("\n".join(moves))