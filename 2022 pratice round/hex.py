def clockWise(row,col,color,insertpt):
    #print('here2')
    global firstPath,otherPath
    if havePass[row][col] != 1 and board[row][col] == color:
        havePass[row][col] = 1
        #print(havePass)
        if color == 'B' and col == board_size-1:
            firstPath = 1
        elif color == 'R' and row == board_size-1:
            otherPath = 1
            
        for i in range(0,5):
            if firstPath == 1 and color == 'B':
                break
            if otherPath == 1 and color == 'R':
                break
            nxtpt = (i+1+insertpt+6)%6
            nxtinsert = (nxtpt+3)%6
            #print(nxtpt,row,col)
            if nxtpt == 0 :
                if row != 0:
                    clockWise(row-1,col,color,nxtinsert)
            elif nxtpt == 1 :
                if col != board_size-1 and row != 0:
                    clockWise(row-1,col+1,color,nxtinsert)
            elif nxtpt == 2 :
                if col != board_size-1:
                    clockWise(row,col+1,color,nxtinsert)
            elif nxtpt == 3 :
                if row != board_size-1:
                    clockWise(row+1,col,color,nxtinsert)
            elif nxtpt == 4 :
                if row != board_size-1 and col != 0:
                    clockWise(row+1,col-1,color,nxtinsert)
            elif nxtpt == 5 :
                if col != 0:
                    clockWise(row,col-1,color,nxtinsert)
                    

def antiClockWise(row,col,color,insertpt):
    #print('here')
    global firstPath,otherPath
    if havePass[row][col] != 1 and board[row][col] == color:
        havePass[row][col] = 1
        if color == 'B' and col == board_size-1:
            otherPath = 1
        elif color == 'R' and row == board_size-1:
            firstPath = 1
            
        for i in range(5,0,-1):
            if firstPath == 1 and color == 'R':
                break
            if otherPath == 1 and color == 'B':
                break
            nxtpt = (i-1+insertpt+6)%6
            nxtinsert = (nxtpt+3)%6
            if nxtpt == 0 :
                if row != 0:
                    antiClockWise(row-1,col,color,nxtinsert)
            elif nxtpt == 1 :
                if col != board_size-1 and row != 0:
                    antiClockWise(row-1,col+1,color,nxtinsert)
            elif nxtpt == 2 :
                if col != board_size-1:
                    antiClockWise(row,col+1,color,nxtinsert)
            elif nxtpt == 3 :
                if row != board_size-1:
                    antiClockWise(row+1,col,color,nxtinsert)
            elif nxtpt == 4 :
                if row != board_size-1 and col != 0:
                    antiClockWise(row+1,col-1,color,nxtinsert)
            elif nxtpt == 5 :
                if col != 0:
                    antiClockWise(row,col-1,color,nxtinsert)

    
def game_status(board_size, board):
    # TODO: implement this method to determine the status of the game board
    #check if diff of num of chess >= 2
    n_Red = 0
    n_Blue = 0
    for row in range(0,board_size):
      for col in range(0,board_size):
          if board[row][col] == 'B':
              n_Blue += 1
          if board[row][col] == 'R':
              n_Red += 1
    if n_Blue-n_Red > 1 or n_Red-n_Blue > 1:
        return 'Impossible'
    
    global havePass
    global firstPath
    global otherPath
    havePass = [[0 for j in range(0,board_size)] for j in range(0,board_size)]
    #check red
    firstPath = 0
    otherPath = 0
    for col in range(0,board_size):
        if firstPath != 1:
            antiClockWise(0,col,'R',1)
        else:
            clockWise(0,col,'R',1)
            if otherPath == 1:
                return 'Impossible'
    if firstPath == 1:
        if n_Red >= n_Blue:
            return 'Red wins'
        else:
            return 'Impossible'
    
    
    #check blue
    havePass = [[0 for j in range(0,board_size)] for j in range(0,board_size)]
    firstPath = 0
    otherPath = 0
    for row in range(0,board_size):
        #print(row,firstPath)
        if firstPath == 0:
            clockWise(row,0,'B',5)
        else:
            antiClockWise(row,0,'B',5)
            if otherPath == 1:
                return 'Impossible'
    if firstPath == 1:
        if n_Red <= n_Blue:
            return 'Blue wins'
        else:
            return 'Impossible'
    else:
        return 'Nobody wins'

def main():
  test_cases = int(input())
  global board_size
  for test_case in range(1, test_cases + 1, 1):
    board_size = int(input())
    global board,havePass
    board = []
    for _ in range(board_size):
      board.append(list(input().strip()))

    ans = game_status(board_size, board)

    print("Case #{}: {}".format(test_case, ans))
    #print(board)
if __name__ == "__main__":
  main()
