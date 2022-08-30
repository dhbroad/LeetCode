#  Valid Sudoku

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.


def isValidSudokuDict(board):
    # First Check: Rows
    for row in board:
        row_dict = {}
        for num in row:
            if num == ".":
                continue
            elif num in row_dict:
                return False
            else:
                row_dict[num] = 1
                
    # Second Check: Boxes
    for third_of_rows in range(0,len(board),3):
        for third_of_cols in range(0,len(board),3):
            tor = third_of_rows
            toc = third_of_cols
            box_dict = {}
            for column in range(0,3):
                for row in range(0,3):
                    if board[tor+row][toc+column] == ".":
                        continue
                    elif board[tor+row][toc+column] in box_dict:
                        return False
                    else:
                        box_dict[board[tor+row][toc+column]] = 1
                
    # Third Check: Columns
    for column in range(0,len(board)):
        column_dict = {}
        for row in range(0,len(board)):
            if board[row][column] == ".":
                continue
            elif board[row][column] in column_dict:
                return False
            else:
                column_dict[board[row][column]] = 1                    
    return True

def isValidSudokuSet(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # First Check: Rows
    for row in board:
        row_set = set()
        for num in row:
            if num == ".":
                continue
            elif num in row_set:
                return False
            else:
                row_set.add(num)
                
    # Second Check: Boxes
    for third_of_rows in range(0,len(board),3):
        for third_of_cols in range(0,len(board),3):
            tor = third_of_rows
            toc = third_of_cols
            box_set = set()
            for column in range(0,3):
                for row in range(0,3):
                    if board[tor+row][toc+column] == ".":
                        continue
                    elif board[tor+row][toc+column] in box_set:
                        return False
                    else:
                        box_set.add(board[tor+row][toc+column])
                
    # Third Check: Columns
    for column in range(0,len(board)):
        column_set = set()
        for row in range(0,len(board)):
            if board[row][column] == ".":
                continue
            elif board[row][column] in column_set:
                return False
            else:
                column_set.add(board[row][column])                   
    return True
               

board1 = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudokuDict(board1))
print(isValidSudokuSet(board1))