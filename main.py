sudoku = [[5,1,7,6,0,0,0,3,4],
          [2,8,9,0,0,4,0,0,0],
          [3,4,6,2,0,5,0,9,0],
          [6,0,2,0,0,0,0,1,0],
          [0,3,8,0,0,6,0,4,7],
          [0,0,0,0,0,0,0,0,0],
          [0,9,0,0,0,0,0,7,8],
          [7,0,3,4,0,0,5,6,0],
          [0,0,0,0,0,0,0,0,0]]

def main(sudoku):
  valid=empty(sudoku)
  if not valid:#if it is not empty
    return True
  else:#if empty
    row,col=find
  for num in range(1,10):
    if row_col(row,col,num,sudoku):#if it is valid
      sudoku[row][col]=num
      if main(sudoku):
        return True
      sudoku[row][col]=0#if value not correct, we initialise it to 0
  return False#back-tracking

def empty(sudoku):#to check which row and column is empty
  for row in range(9):
    for col in range(9):
      if sudoku[row][col]==0:
        return (row,col)
  return None

def row_col(row,col,num,sudoku):
  for r in range(9):#to check for the number in the row
      if num == sudoku[row][r]:
        return False
  for c in range(9):#to check for the number in the column
      if num == sudoku[c][col]:
        return False
  '''we divide the whole 9*9 grid into 9 boxes of size 3*3'''
  x=(row//3)*3
  y=(col//3)*3
  for i in range(0,3):
    for j in range(0,3):
      if sudoku[x+i][y+j]==num:
        return False
  return True
  
def display(sudoku):#to display the final sudoku
  for r in range(9):
    for c in range(9):
      print(sudoku[r][c],end=" ")
    print()

main(sudoku)
display(sudoku)
