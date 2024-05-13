def winGame(arr):
    # rows
    for i in range(3):
        count = 0
        # check for non-default chars
        if arr[i][0] != ' ':
            letter = arr[i][0]
            for j in range(3):
                if arr[i][j] == letter:
                    count = count + 1
            if count == 3:
                if letter == 'X':
                    print("Player 1 wins!")
                else:
                    print("Player 2 wins!")
                return True
        
    # cols
    for i in range(3):
        count = 0
        # check for non-default chars
        if arr[0][i] != ' ':
            letter = arr[0][i]
            for j in range(3):
                if arr[j][i] == letter:
                    count = count + 1
            if count == 3:
                if letter == 'X':
                    print("Player 1 wins!")
                else:
                    print("Player 2 wins!")
                return True


    # manually check diags
    letter = arr[1][1]
    if letter != ' ':
        if (letter == arr[0][0] and letter == arr[2][2]):
            if letter == 'X':
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return True
        if (letter == arr[0][2] and letter == arr[2][0]):
            if letter == 'X':
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return True
    return False
'''
  1 2 3
1 X X O
2 X O X
3 X X X


'''
def displayBoard(arr):
    print("  1 2 3")
    print("1", arr[0][0], arr[0][1], arr[0][2])
    print("2", arr[1][0], arr[1][1], arr[1][2])
    print("3", arr[2][0], arr[2][1], arr[2][2])

def updateBoard(arr, row, col, letter):
    arr[int(row) - 1][int(col) - 1] = letter

arr = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def isValidInput(arr, str):
    # invalid input syntax
    if (len(str) != 2):
        return False
    
    # 
    row = int(str[0]) - 1
    col = int(str[1]) - 1
    # out of bounds
    if row not in range(3) or col not in range(3):
        return False

    # square already taken
    if arr[row][col] != ' ':
        return False
    return True
    
# turn variable checks whether the turn is P1 or P2
turn = 1

while winGame(arr) == False:    
    displayBoard(arr)
    if turn == 1:
        print("Player 1, choose square using RC (row/column) coords (i.e. \"13\" for row 1, column 3):")
        p1_input = input()
        while (isValidInput(arr, p1_input) == False):
            print("Invalid input/Square already taken.\n")
            print("Player 1, choose square using RC (row/column) coords (i.e. \"13\" for row 1, column 3):\n")
            p1_input = input()
        updateBoard(arr, p1_input[0], p1_input[1], 'X')
    elif turn == 0:
        print("Player 2, choose square using RC (row/column) coords (i.e. \"13\" for row 1, column 3):")
        p2_input = input()
        while (isValidInput(arr, p2_input) == False):
            print("Invalid input/Square already taken.\n")
            print("Player 2, choose square using RC (row/column) coords (i.e. \"13\" for row 1, column 3):\n")
            p2_input = input()
        updateBoard(arr, p2_input[0], p2_input[1], 'O')
    
    turn = (turn + 1) % 2