from tkinter import *
from tkinter import messagebox
import numpy as np
import time
class App(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master = master
        self.jogada = -1 
        self.w = 49
        self.h = 49
        self.board = [7*[0],7*[0],7*[0],7*[0],7*[0],7*[0],7*[0]]
        self.canvas_board = []
        temporario  = []
        #Criando frame para a matriz de valores 
        self.container = Frame(master)
        self.zero_frame = Frame(master)
        self.zero_frame.pack()
        self.primeiro_frame = Frame(master)
        self.primeiro_frame.pack()
        self.frame1 = Frame(master)
        self.frame1.pack()
        self.frame2 = Frame(master)
        self.frame2.pack()
        self.frame3 = Frame(master)
        self.frame3.pack()
        self.frame4 = Frame(master)
        self.frame4.pack()
        self.frame5 = Frame(master)
        self.frame5.pack()
        self.frame6 = Frame(master)
        self.frame6.pack()
        self.frame7 = Frame(master)
        self.frame7.pack()
        self.frames = [self.frame1,self.frame2,self.frame3,self.frame4,self.frame5,self.frame6,self.frame7]
        #------------------------------
        
        # criando a matriz de canvas 
        for i in range(7):
            for j in range(7):
                temporario.append(Canvas(self.frames[i],width=self.w,height=self.h,highlightthickness=0.5,highlightbackground="white",background='black'))
            self.canvas_board.append(temporario)
            temporario = [] 
        for i in self.canvas_board:
            for j in i :
                j.pack(side=LEFT)
        #----------------------------
        # criando botoes
        self.butao_limpe = Button(self.zero_frame,command = self.clean,text = 'Limpe',bg  ='black',fg = 'white',height = self.h//16,width = self.w//7-1)
        self.butao_limpe.pack(side = RIGHT)
        self.butao1 = Button(self.primeiro_frame,command = lambda  : self.on_button_pressed(1),width = self.w//7-1,height = self.h//16,text = '1',background= 'black',fg = 'white')
        self.butao1.pack(side = LEFT)
        self.butao2 = Button(self.primeiro_frame,command = lambda  : self.on_button_pressed(2),width = self.w//7-1,height = self.h//16,text = '2',background = 'black',fg = 'white')
        self.butao2.pack(side = LEFT)
        self.butao3 = Button(self.primeiro_frame,command = lambda  : self.on_button_pressed(3),width = self.w//7-1,height = self.h//16,text = '3',background = 'black',fg = 'white')
        self.butao3.pack(side = LEFT)
        self.butao4 = Button(self.primeiro_frame,command = lambda  : self.on_button_pressed(4),width = self.w//7-1,height = self.h//16,text = '4',background = 'black',fg = 'white')
        self.butao4.pack(side = LEFT)
        self.butao5 = Button(self.primeiro_frame,command = lambda  : self.on_button_pressed(5),width = self.w//7-1,height = self.h//16,text= '5',background= 'black',fg = 'white')
        self.butao5.pack(side = LEFT)
        self.butao6 = Button(self.primeiro_frame,command = lambda  : self.on_button_pressed(6),width = self.w//7-1,height = self.h//16,text = '6',background = 'black',fg = 'white')
        self.butao6.pack(side = LEFT)
        self.butao7 = Button(self.primeiro_frame,command = lambda  : self.on_button_pressed(7),width = self.w//7-1,height = self.h//16,text = '7',background = 'black',fg = 'white')
        self.butao7.pack(side = LEFT)
        self.label_jogador = Label(self.zero_frame,text = 'È a vez do jogador :',width = self.w//2,height = self.h//16,bg = 'black',fg = 'white')
        self.label_jogador.pack(side= LEFT)
        self.canvas_jogador = Canvas(self.zero_frame,width = 49,height = 49,bg = 'black')
        self.canvas_jogador.pack(side  = LEFT) 

    def draw_current_player(self):
        if self.jogada%2:
            color = 'yellow'
        else:
            color = 'red'
        canvas = self.canvas_jogador
        r = self.w//2
        x = self.w//2
        y = self.h//2
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        canvas.create_oval(x0,y0,x1,y1,fill = color)
    def draw_circle(self,coord,color):
        canvas = self.canvas_board[coord[0]][coord[1]]
        r = self.w//2
        x = self.w//2
        y = self.h//2
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        canvas.create_oval(x0,y0,x1,y1,fill = color)
    def on_button_pressed(self,position):
        self.jogada+=1
        self.draw_current_player()
        if self.jogada%2:
            contagem = self.fall_chip(position,-1)
            if not(contagem) :
                messagebox.showinfo('Info','Jogada invalida')
                self.jogada-=1
        else:
            contagem = self.fall_chip(position,1)
            if not(contagem):
                messagebox.showinfo('Info','Jogada invalida')
                self.jogada-=1
        result = self.check_win_or_tie() 
        if result[0]:
            sim_ounao = messagebox.askquestion('Info',f'{result[1]}\n\n Quer jogar novamente ?')
            if sim_ounao=='yes':
                self.clean()
            else:
                self.master.destroy()

    
    def find_diagonais(self):
        board= np.array(self.board)
        '''
        board = self.board
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
        '''
        diags = [board[::-1,:].diagonal(i) for i in range(-board.shape[0]+1,board.shape[1])]

        diags.extend(board.diagonal(i) for i in range(board.shape[1]-1,-board.shape[0],-1))

        # Another list comp to convert back to Python lists from numpy arrays,
        # so it prints what you requested.
        return [n.tolist() for n in diags]

            
    def fall_chip(self,pos,player):
        try:
            if player == -1:
                color = 'red'
            elif player ==1 :
                color = 'yellow'
            if self.board[0][pos-1] !=0 :
                return False
            j = 0 
            while j<len(self.board)-1:
                if self.board[j+1][pos-1] == 0 :
                    self.draw_circle((j+1,pos-1),color)
                    self.master.update()
                    time.sleep(0.03)
                    self.canvas_board[j+1][pos-1].delete('all')
                    j+=1
                else:
                    break 
            self.board[j][pos-1] = player
            self.draw_circle((j,pos-1),color)
            return True
        except:
            return False
        
    def check_win_or_tie(self): 
        board = self.board   
        board = list(board)
        somas = []
        d = self.find_diagonais()
        for i in range(len(board)):
            colunas = [row[i] for row in board]
            linhas  = board[i]
            for k in range(len(linhas)-3):
                parc = colunas[k:k+4]
                parl = linhas[k:k+4]
                somas.append(sum(parc))
                somas.append(sum(parl))
                if parc.count(-1)==4 or parl.count(-1)==4:
                    return True,'Vermelho ganhou'
                elif parc.count(1)==4 or parl.count(1)==4:
                    return True,'Amarelo ganhou'
        for i in range(len(d)):
            for j in range(len(d[i])-3):
                parc1  = d[i][j:j+4]
                somas.append(sum(parc1))
                if parc1.count(-1)==4 :
                    return True,"Vermelho ganhou"
                elif parc1.count(1)==4:
                    return True,'Amarelo ganhou'
        if (np.array(board) == 0).sum() < 3 and (somas.count(3)==0 or somas.count(-3)==0):
            return True,'Empate'
        return False,'_'
    def clean(self):
        self.jogada = -1
        self.canvas_jogador.delete('all')
        for i in self.canvas_board:
            for j in i :
                j.delete('all')
                self.board = [7*[0],7*[0],7*[0],7*[0],7*[0],7*[0],7*[0]]
root = Tk()
root['background']='#856ff8'
root.geometry('400x500')
root.title('Connect Four')
App(root)
root.mainloop()