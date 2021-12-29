import os
def clear():
    os.system('cls')
    
def display_board(board):
    clear()
    print(board[7]+'    |    '+board[8]+'    |    '+board[9])
    print('----- --------- ------')
    print(board[4]+'    |    '+board[5]+'    |    '+board[6])
    print('----- --------- ------')
    print(board[1]+'    |    '+board[2]+'    |    '+board[3])

def play_input():
    '''
    OUTPUT= (Player 1 input, Player 2 input)
    '''
    inp=' '
    while inp!='X' and inp!='O':
        inp=input("PLAYER 1: CHOOSE X or O").upper()
    
    if inp=='X':
        return ('X','O')
    else:
        return ('O','X')
        
def place_inp(board, inp, position):
    board[position]=  inp  

def check_win(board,inp):
   return((board[1]==board[2]==board[3]==inp) or (board[4]==board[5]==board[6]==inp) or (board[7]==board[8]==board[9]==inp) or (board[7]==board[4]==board[1]==inp) or (board[8]==board[5]==board[2]==inp) or (board[9]==board[6]==board[3]==inp) or (board[7]==board[5]==board[3]==inp) or (board[9]==board[5]==board[1]==inp))
    

import random

def choose_player():
    flip = random.randint(0,1)
    
    if flip == 0:
        return "PLAYER 1"
    else:
        return "PLAYER 2"

def check_space(board,position):
    return  board[position] == ' '

def full_board(board):
    for i in range(1,10):
        if check_space(board,i):
            return False
    return True

def player_choice(board):
    position =0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not check_space(board,position):
        position=int(input('Choose the position you want to enter : [1-9]'))
    
    return position

def replay():
    choice= input("DO YOU WANT TO PLAY AGAIN? IF YES ENTER Yes")
    
    return choice=='Yes'

print("WELCOME TO TIC-TAC-TOE")

while True:
    the_board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',]
    player1_inp,player2_inp = play_input()
    
    turn=choose_player()
    print(turn + " WILL CHOOSE FIRST")
     
    ready= input("ARE YOU READY TO PLAY? Y or N")
    
    if ready == 'y':
        game_on=True
    
    else:
        game_on=False
        
    while game_on:
        if turn=='PLAYER 1':
            display_board(the_board) 
            pos=player_choice(the_board)
            place_inp(the_board,player1_inp,pos)
            
            if check_win(the_board,player1_inp):
                display_board(the_board)
                print('!! PLAYER 1 WON THE GAME !!') 
                game_on=False
            else:
                if full_board(the_board):
                    display_board(the_board)
                    print("!! GAME TIED !!")
                    game_on=False
                else:
                    turn = 'PLAYER 2'
        
        elif turn=='PLAYER 2':
            display_board(the_board)
            pos=player_choice(the_board)
            place_inp(the_board,player2_inp,pos)
            
            if check_win(the_board,player2_inp):
                display_board(the_board)
                print('!! PLAYER 2 WON THE GAME !!') 
                game_on=False
            else:
                if full_board(the_board):
                    display_board(the_board)
                    print("!! GAME TIED !!")
                    game_on=False
                else:
                    turn = 'PLAYER 1'
            
                    
    if not replay():
          break
    