import subprocess
from time import sleep
import math
board=['-','-','-','-','-','-','-','-','-']
def print_board(board):
    print("                   ")
    print("                   ")
    print("                   ")
    print("                   ")
    print("                   ")
    print("                   ")
    print("                   ")
    print("                     TIC-TAC-TOE GAME")
    print("                   ")
    print("                        "+"-------")
    print("                        "+"|" + board[0] + "|" + board[1] +"|" + board[2] +"|")
    print("                        "+"-------")
    print("                        "+"|" +board[3] + "|" + board[4] +"|" + board[5]+ "|")
    print("                        "+"-------")
    print("                        "+"|" +board[6] + "|" + board[7] +"|" + board[8]+ "|")
    print("                        "+"-------")
def get_position(Board):
    print_board(Board)
    print("Input your best move (0-8)")
    move=int(input("move = "))
    sleep(1)
    subprocess.call('cls',shell=True)
    return move
def play_game(Board,Player):
    if "-" in Board:
        if Player=="X":
            play=get_position(Board)
            if Board[play]=="-":
                board[play]="X"
            else:
                print("Invalid move") 
        else:
            play=get_position(Board)
            if Board[play]=="-":
                board[play]="O"
            else:
                print("Invalid move")
    print_board(Board)
    subprocess.call('cls',shell=True)
def switch_player(Player):
    if Player=="X":
        Player="O"
    else:
        Player="X"
    return Player
def check_horizontal(board):
    if board[0]==board[1]==board[2] and board[0]!="-":
        if board[0]=="X":
            print("Player X wins")
            return True
        if board[0]=="O":
            print("Player O wins")
            return True
    if board[3]==board[4]==board[5] and board[3]!="-":
        if board[3]=="X":
            print("Player X wins")
            return True
        if board[3]=="O":
            print("Player O wins")
            return True
    if board[6]==board[7]==board[8] and board[6]!="-":
        if board[6]=="X":
            print("Player X wins")
            return True
        if board[6]=="O":
            print("Player O wins")
            return True
    else:
        return False
def check_vertical(board):
    if board[0]==board[3]==board[6] and board[0]!="-":
        if board[0]=="X":
            print("Player X wins")
            return True
        if board[0]=="O":
            print("Player O wins")
            return True
    if board[1]==board[4]==board[7] and board[1]!="-":
        if board[1]=="X":
            print("Player X wins")
            return True
        if board[1]=="O":
            print("Player O wins")
            return True
    if board[2]==board[5]==board[8] and board[2]!="-":
        if board[2]=="X":
            print("Player X wins")
            return True
        if board[2]=="O":
            print("Player O wins")
            return True
    else:
        return False
def check_diagonal(board):
    if board[0]==board[4]==board[8] and board[0]!="-":
        if board[0]=="X":
            print("Player X wins")
            return True
        if board[0]=="O":
            print("Player O wins")
            return True
    if board[2]==board[4]==board[6] and board[2]!="-":
        if board[2]=="X":
            print("Player X wins")
            return True
        if board[2]=="O":
            print("Player O wins")
            return True
    else:
        return False

def evaluate_board(Board):
    check1=check_horizontal(Board)
    check2=check_vertical(Board)
    check3=check_diagonal(Board)
    if check1==False and check2==False and check3==False and "-" not in Board:
        print("It is a Tie")
        return True    
    if check1==True or check2==True or check3==True:
        return True
    else:
        return False
def check_horizontally(board,Player):
    if board[0]==board[1]==board[2] and board[0]!="-":
        if board[0]==Player:
            return True
    if board[3]==board[4]==board[5] and board[3]!="-":
        if board[3]==Player:
            return True
    if board[6]==board[7]==board[8] and board[6]!="-":
        if board[6]==Player:
            return True
    else:
        return False
def check_vertically(board,Player):
    if board[0]==board[3]==board[6] and board[0]!="-":
        if board[0]==Player:
            return True
    if board[1]==board[4]==board[7] and board[1]!="-":
        if board[1]==Player:
            return True
    if board[2]==board[5]==board[8] and board[2]!="-":
        if board[2]==Player:
            return True
    else:
        return False
def check_diagonally(board,Player):
    if board[0]==board[4]==board[8] and board[0]!="-":
        if board[0]==Player:
            return True
    if board[2]==board[4]==board[6] and board[2]!="-":
        if board[2]==Player:
            return True
    else:
        return False
def is_draw(Board):
    check10=check_horizontal(Board)
    check11=check_vertical(Board)
    check12=check_diagonal(Board)
    if check10==False and check11==False and check12==False and "-" not in Board:
        return True
    else:
        return False
    
def is_winner(Board,player):
    if player=="X":
        check4=check_horizontally(Board,"X")
        check5=check_vertically(Board,"X")
        check6=check_diagonally(Board,"X")
        if check4 or check5 or check6==True:
            return True
        else:
            return False
    else:
        check7=check_horizontally(Board,"O")
        check8=check_vertically(Board,"O")
        check9=check_diagonally(Board,"O")
        if check7 or check8 or check9==True:
            return True
        else:
            return False
        
def minimax(board,Depth,is_maximising):
    if Depth == 0 or is_winner(board, "X") or is_winner(board, "O") or is_draw(board):
        if is_winner(board, "X"):
            return 1
        elif is_winner(board, "O"):
            return -1
        elif is_draw(board):
            return 0
    if is_maximising==True:
        best_score=-math.inf
        for i in range(len(board)):
            if board[i]=="-":
                board[i]="X"
                score=minimax(board,Depth-1,False)
                board[i]="-"
                best_score=max(score,best_score)
        return best_score
    else:
        best_score=math.inf
        for i in range(len(board)):
            if board[i]=="-":
                board[i]="O"
                score=minimax(board,Depth-1,True)
                board[i]="-"
                best_score=min(score,best_score)
        return best_score


def gameplay(Board,Player1):
    if Player1=="X":
        play=get_position(Board)
        if Board[play]=="-":
            board[play]="X"
        else:
            print("Invalid move") 
    else:
        depth=1000
        bestmove=None
        optimal_score=math.inf
        for j in range(len(Board)):
            if Board[j]=="-":
                Board[j]="O"
                opt_score=minimax(Board,depth,True)
                Board[j]="-"
                if opt_score<optimal_score:
                    optimal_score=opt_score
                    bestmove=j
        if Board[bestmove] == "-":
            board[bestmove]="O"
        else:
            print("Invalid move by the AI") 
            sleep(1)
    print_board(Board)
    subprocess.call('cls',shell=True)

gamerunning=True
option=0
print("                                                           ")
print("                                                           ")
print("                                                           ")
print("                                                           ")
print("                                                           ")
print("                                                           ")
print("                                           TIC-TAC-TOE GAME")
print("                                            CHOOSE OPPONENT")
print("                                            1.TWO PLAYERS")
print("                                            2.AGAINST AI")
print("                                            Input an option(1 or 2)")
option=int(input("                                            option = "))
if option==1:
    print("Player 1-Which symbol do you want(X or O)-Uppercase")
    player=input("Player = ")
    if player=='X':
        print("Player 2-your symbol is O")
    else:
        print("Player 2-your symbol is X")
    while gamerunning==True:
        print(f"Player {player}'s turn")
        play_game(board,player)
        check=evaluate_board(board)
        if check==True:
            gamerunning==False
            print("GAME OVER")
            print_board(board)
            break
        else:
            player=switch_player(player)

elif option==2:
    gamerunning2=True
    player1="X"
    print("You are the maximizer(X)")
    print("AI is the minimizer(O)")
    while gamerunning2==True:
        gameplay(board,player1)
        check13=evaluate_board(board)
        if check13==True:
            gamerunning2==False
            print("GAME OVER")
            print_board(board)
            break
        else:
            player1=switch_player(player1)
else:
    print("Invalid input")

    

