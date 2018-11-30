#Draw the board of play
def boards(board):
    print(board[0],'|',board[1],'|',board[2])
    print(' ','|',' ','|',' ')
    print('---------')
    print(board[3],'|',board[4],'|',board[5])
    print(' ','|',' ','|',' ')
    print('---------')
    print(board[6],'|',board[7],'|',board[8])
    print(' ','|',' ','|',' ')
#accept the move from the players
def move():
    position=' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not check(board,int(position)-1):
        print('Enter your move(as number 1-9)\n\n')
        position=input()
    return position

#check the move not immposible
def check(board,position):
    p=' '
    return p==board[position] 


#check the game is tie
def full_board_check(board):
    for i in range(0,9):
        if check(board, i):
            return False
    return True

#determine the winner

def win_check(board,mark):
    
    return ((board[6] == mark and board[7] == mark and board[8] == mark) or # across the top
    (board[3] == mark and board[4] == mark and board[5] == mark) or # across the middle
    (board[0] == mark and board[1] == mark and board[2] == mark) or # across the bottom
    (board[6] == mark and board[3] == mark and board[0] == mark) or # down the middle
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the right side
    (board[6] == mark and board[4] == mark and board[2] == mark) or # diagonal
    (board[8] == mark and board[4] == mark and board[0] == mark)) # diagonal

#main code of Tic Tac toe

board=[' ']*9
#Draw the empty board
boards(board)
turn=0
while True:
    #player1
    if turn==0 :
        #form player1 give the move
        position=int(move())
        board[position-1]='X'
        #print(board)
        boards(board)
        turn=1
        #check the move is winner?
        if win_check(board,'X'):
            print('congelation player1 you win!!')
            break
        else:
            pass
        
        
        
        #check is loop full?
        if full_board_check(board):
            print('The game is tie')
            break
        else:
            continue
    
        
    
    #player2
    else:
        position=int(move())
        board[position-1]='O'
        #print(board)
        full_board_check(board)
        boards(board)
        turn=0
        #check the move is winner?
        if win_check(board,'O'):
            print('congelation player2 you win سوت سووت!!')
            break
        else:
            continue
      
            
        
#print(board)
