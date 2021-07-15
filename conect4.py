import numpy as np
jogadas = 0 
board = [7*[0],7*[0],7*[0],7*[0],7*[0],7*[0],7*[0]]
def fall_chip(board,pos,player):
    try:
        if board[0][pos-1] !=0 :
            return False
        j = 0 
        while j<6:
            if board[j+1][pos-1] == 0 :
                j+=1
            else:
                break 
        board[j][pos-1] = player
        return True
    except:
        return False
def find_diagonais(board):
    diagonais = []
    parcial,parcial1 = [],[]
    for i in range(len(board[0])-1,-1,-1):
        for j in range(len(board)):
            if (i+j)<len(board[0]):
                parcial.append(board[j][i])
            else:
                break
        if len(parcial)>=4:
            diagonais.append(parcial)
        parcial = []
    for i in range(1,len(board)):
        for j,k in zip(range(i,len(board[0])),range(0,len(board))):
            parcial.append(board[j][k])
        if len(parcial)>=4:
            diagonais.append(parcial)
        parcial = []
    for i in range(len(board[0])):
        parcial.append(board[i][i])

    diagonais.append(parcial)

    return diagonais

            

        
def check_win_or_tie(board):
    
    board = list(board)
    somas = []
    d = find_diagonais(board)
    for i in range(len(board)):
        colunas = [row[i] for row in board]
        linhas  = board[i]
        for k in range(len(linhas)-3):
            parc = colunas[k:k+4]
            parl = linhas[k:k+4]
            somas.append(sum(parc))
            somas.append(sum(parl))
            if parc.count(-1)==4 or parl.count(-1)==4:
                return True,'O ganhou'
            elif parc.count(1)==4 or parl.count(1)==4:
                return True,'X ganhou'
    for i in range(len(d)):
        for j in range(len(d[i])-3):
            parc1  = d[i][j:j+4]
            somas.append(sum(parc1))
            if parc1.count(-1)==4 :
                return True,"O ganhou"
            elif parc1.count(1)==4:
                return True,'X ganhou'
    if (np.array(board) == 0).sum() < 3 and (somas.count(3)==0 or somas.count(-3)==0):
        return True,'Empate'
    return False,'_'

while not(check_win_or_tie(board)[0]):
    if jogadas%2==0:
        print('è a vez de O')
        posA = int(input('Digite um valor de 1 a 7 que representa a posição da esquerda para a direita'))
        is_possible = fall_chip(board,posA,-1)
        if not(is_possible):
            print('Movimento invalido')
            continue
        string = ''
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==1:
                  string = string + ' X '
                elif board[i][j]==-1:
                    string = string+ ' O '
                else:
                    string = string +' . '
            string = string + '\n' 
        print(string) 
        jogadas+=1
    else:
        print('è a vez de X')
        posB = int(input('Digite um valor de 1 a 7 que representa a posição da esquerda para a direita'))
        is_possible = fall_chip(board,posB,1)
        if not(is_possible):
            print('Movimento invalido')
            continue
        string = ''
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==1:
                  string = string + ' X '
                elif board[i][j]==-1:
                    string = string+ ' O '
                else:
                    string = string +' . '
            string = string + '\n'
        print(string) 
        jogadas+=1
print(check_win_or_tie(board)[1])