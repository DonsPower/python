#Juego del gatO
#IniciamosDIbujando la plataforma

board= ["-","-","-",
        "-","-","-",
        "-","-","-"]

def plataforma():
    print(board[0] +" | " +board[1]+" | "+board[2])
    print(board[3] +" | " +board[4]+" | "+board[5])
    print(board[6] +" | " +board[7]+" | "+board[8])
def decision():
    # xwin=1 ywin=2 empate=0
    decision_game=0
    #HOrizontal
    if board[0]=="Y" and board[1]=="Y" and board[2]=="Y":
        decision_game=2
    if board[3]=="Y" and board[4]=="Y" and board[5]=="Y":
        decision_game=2
    if board[6]=="Y" and board[7]=="Y" and board[8]=="Y":
        decision_game=2
    if board[0]=="X" and board[1]=="X" and board[2]=="X":
        decision_game=1
    if board[3]=="X" and board[4]=="X" and board[5]=="X":
        decision_game=1
    if board[6]=="X" and board[7]=="X" and board[8]=="X":
        decision_game=1
    #Vertical
    if board[0]=="X" and board[3]=="X" and board[6]=="X":
        decision_game=1
    if board[1]=="X" and board[4]=="X" and board[7]=="X":
        decision_game=1
    if board[2]=="X" and board[5]=="X" and board[8]=="X":
        decision_game=1
    if board[0]=="Y" and board[3]=="Y" and board[6]=="Y":
        decision_game=2
    if board[1]=="Y" and board[4]=="Y" and board[7]=="Y":
        decision_game=2
    if board[2]=="Y" and board[5]=="Y" and board[8]=="Y":
        decision_game=2
    #INclinado
    if board[0]=="Y" and board[4]=="Y" and board[8]=="Y":
        decision_game=2
    if board[2]=="Y" and board[4]=="Y" and board[6]=="Y":
        decision_game=2
    if board[0]=="X" and board[4]=="X" and board[8]=="X":
        decision_game=1
    if board[2]=="X" and board[4]=="X" and board[6]=="X":
        decision_game=1
    return decision_game

def gameControl():
    for x in range(10):
        print
        print
        if x==9:
            print("Empate")
        else:
            if (x%2)!=0:
                #SEtea A
                xgame=input("InsertaX :" )
                while board[xgame-1]!="-":
                    xgame=input("Introduce en otra posicion o numero x :" )
                board.pop(xgame-1)
                board.insert(xgame-1,"X")
                plataforma()
            else:
                #Setea b
                ygame=input("InsertaY :" )
                while board[ygame-1]!="-":    
                    ygame=input("InsertaY en otra posicion o numero: y" )
                board.pop(ygame-1)
                board.insert(ygame-1,"Y")
                plataforma()
            resu=decision()
            # xwin=1 ywin=2 empate=0
            if resu==1:
                print("Gano X")
                break
            elif resu==2:
                print("GanoY")
                break

plataforma()
gameControl()
