import arcade
import random
import os


snail1 = arcade.load_texture("Snail3.png")
snail2 = arcade.load_texture("Snail2.png")
back = arcade.load_texture("3.png")
sp1 = arcade.load_texture("splash1.png")
sp2 = arcade.load_texture("splash2.png")
vs = arcade.load_texture("vs.png")
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
MARGIN = 5
boxSize = SCREEN_HEIGHT // 10 

class Game(arcade.View):
    def __init__(self):
        super().__init__()
        self.board = []
        self.human1 = 1
        self.BOT = 2
        self.turn = "human1"
        self.win = "0"
        self.state = "GameMenu"
        self.BOTScore = 0
        self.human1Score = 0
        self.initilizeBoard(10, 10)
        self.Score_Checker = 0
        self.Human_Sore_Record = 0
        self.Bot_Score_Record = 0


    def initilizeBoard(self, rows, cols):
        for i in range(cols):
            tempBoard = []
            for i in range(0, rows):
                tempBoard.append(0)
            self.board.append(tempBoard)
        self.board[0][9] = 2
        self.board[9][0] = 1


    def on_key_press(self, key, modifiers):
        if self.state == "GameMenu":
            if key:
                self.human1 = 1
                self.BOT = 2
                self.state = "GameOn"

    def on_show(self):
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
        

    def draw_horizental(self, grid_size, box_size, pixel):
        temp = box_size
        for i in range(1, grid_size):
            arcade.draw_line(0, box_size, (box_size*grid_size), box_size,  arcade.color.BLACK, pixel)
            box_size = box_size + temp 


    def draw_vertical(self, grid_size, box_size, pixel):
        temp = box_size
        for i in range(1, grid_size):
            arcade.draw_line(box_size, 0, box_size, (box_size*grid_size),  arcade.color.BLACK, pixel)
            box_size = box_size + temp 
 
    def reset(self):
            self.board = []
            self.human1 = 1
            self.BOT = 2
            self.turn = "human1"
            self.win = "0"
            self.state = "GameMenu"
            self.BOTScore = 0
            self.human1Score = 0
            self.initilizeBoard(10, 10) 

    def on_draw(self):
        arcade.start_render()
        if self.state == "GameMenu":
            arcade.draw_text("Welcome to Mess wala Chacha(Snail) game", 100, 300, arcade.color.WHITE, font_size=28)
            arcade.draw_text("Press any key to continue", 480, 250, arcade.color.WHITE, font_size=30, anchor_x="center")
            self.__init__()

        elif self.state == "GameOn":
            arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,back)
            
            
            self.draw_horizental(10, boxSize, 4)
            self.draw_vertical(10, boxSize, 4)
            arcade.draw_lrwh_rectangle_textured(600, 0,1000, SCREEN_HEIGHT,back)
            arcade.draw_text("Mess wala Chacha(Snail) Game", 630, 515, arcade.color.WHITE, font_size=18)
            arcade.draw_text(" Human1 Score = " + str(self.human1Score), 690, 450,font_size=18)
            arcade.draw_text(" Human2 Score = " + str(self.BOTScore), 690, 400, font_size=18)
            arcade.draw_lrwh_rectangle_textured(600,70, 400, 300, vs)
            Y = boxSize
            temp = 0
            #print(self.board)
            for row in range (0, len(self.board)):
                X = 0
                for col in range (0, len(self.board)):
                    if self.board[row][col] == 1 : 
                        arcade.draw_lrwh_rectangle_textured( X+MARGIN, SCREEN_HEIGHT-Y, boxSize-MARGIN, boxSize-MARGIN, snail1)
                    
                    elif self.board[row][col] == 2 : 
                        arcade.draw_lrwh_rectangle_textured( X+MARGIN, SCREEN_HEIGHT-Y, boxSize-MARGIN, boxSize-MARGIN, snail2)
                    
                    elif self.board[row][col] == 11 : 
                        arcade.draw_lrwh_rectangle_textured( X+MARGIN, SCREEN_HEIGHT-Y, boxSize-MARGIN, boxSize-MARGIN, sp1)
                    
                    elif self.board[row][col] == 22 : 
                        arcade.draw_lrwh_rectangle_textured( X+MARGIN, SCREEN_HEIGHT-Y, boxSize-MARGIN, boxSize-MARGIN, sp2)
                    
                    X += boxSize
                temp += 1
                Y += boxSize
                

        elif self.state == "GameOver":
            if self.human1Score > self.BOTScore:
                self.win = "human1"
            elif self.human1Score < self.BOTScore:
                self.win = "BOT"
            elif self.human1Score == self.BOTScore:
                self.win = "draw"

            if self.win == "human1":
                arcade.draw_text("Congratulations, Bot has Won !", 100, 300, arcade.color.WHITE, font_size=35)
                arcade.draw_text("Click to continue", 480, 250, arcade.color.WHITE, font_size=30, anchor_x="center")
              

            elif self.win == "BOT":
                arcade.draw_text("Congratulation Human has Won :)", 100, 300, arcade.color.WHITE, font_size=35)
                arcade.draw_text("Click to continue", 480, 250, arcade.color.WHITE, font_size=20, anchor_x="center")
            

            elif self.win == "draw":
                arcade.draw_text("It's a draw..", 350, 300, arcade.color.WHITE, font_size=35)
                arcade.draw_text("Click to continue", 480, 250, arcade.color.WHITE, font_size=30, anchor_x="center")
            

    def LSlip(self, Player):
        if Player == 2:
            x, y = self.getBOTPosition()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 22 or self.board[x][y] == 2:
                    self.board[x1][y1] = 11
                    self.board[x][y+1] = 1
                  #  self.turn = "human1"
                    break
                elif y == 0:
                    self.board[x1][y1] = 11
                    self.board[x][y] = 1
                 #   self.turn = "human1"
                    break
                else:
                    y = y-1
        elif Player == 1:
            x, y = self.gethuman1Position()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 11 or self.board[x][y] == 1:
                    self.board[x1][y1] = 22
                    self.board[x][y+1] = 2
                 #   self.turn = "BOT"
                    break
                elif y == 0:
                    self.board[x1][y1] = 22
                    self.board[x][y] = 2
                 #   self.turn = "BOT"
                    break
                else:
                    y = y-1


    def RSlip(self, Player):
        if Player == 2:
            x, y = self.getBOTPosition()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 22 or self.board[x][y] == 2:
                    self.board[x1][y1] = 11
                    self.board[x][y-1] = 1
                 #   self.turn = "human1"
                    break
                elif y == 9:
                    self.board[x1][y1] = 11
                    self.board[x][y] = 1
                 #   self.turn = "human1"
                    break
                else:
                    y = y+1
        elif Player == 1:
            x, y = self.gethuman1Position()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 11 or self.board[x][y] == 1:
                    self.board[x1][y1] = 22
                    self.board[x][y-1] = 2
                 #   self.turn = "BOT"
                    break
                elif y == 9:
                    self.board[x1][y1] = 22
                    self.board[x][y] = 2
                  #  self.turn = "BOT"
                    break
                else:
                    y = y+1

    def DownSlip(self, Player):
        if Player == 2:
            x, y = self.getBOTPosition()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 22 or self.board[x][y] == 2:
                    self.board[x1][y1] = 11
                    self.board[x-1][y] = 1
                 #   self.turn = "human1"
                    break
                elif x == 9:
                    self.board[x1][y1] = 11
                    self.board[x][y] = 1
                 #   self.turn = "human1"
                    break
                else:
                    x = x+1
        elif Player == 1:
            x, y = self.gethuman1Position()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 11 or self.board[x][y] == 1:
                    self.board[x1][y1] = 22
                    self.board[x-1][y] = 2
                 #   self.turn = "BOT"
                    break
                elif x == 9:
                    self.board[x1][y1] = 22
                    self.board[x][y] = 2
                   # self.turn = "BOT"
                    break
                else:
                    x = x+1
    def UPSlip(self, Player):
        if Player == 2:
            x, y = self.getBOTPosition()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 22 or self.board[x][y] == 2:
                    self.board[x1][y1] = 11
                    self.board[x+1][y] = 1
                   # self.turn = "human1"
                    break
                elif x == 0:
                    self.board[x1][y1] = 11
                    self.board[x][y] = 1
                   # self.turn = "human1"
                    break
                else:
                    x = x-1
        elif Player == 1:
            x, y = self.gethuman1Position()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 11 or self.board[x][y] == 1:
                    self.board[x1][y1] = 22
                    self.board[x+1][y] = 2
                   # self.turn = "BOT"
                    break
                elif x == 0:
                    self.board[x1][y1] = 22
                    self.board[x][y] = 2
                    #self.turn = "BOT"
                    break
                else:
                    x = x-1
        

    #Function to check if we are stuck
    def StuckCondition(self):
        if self.Human_Sore_Record == self.human1Score or self.Bot_Score_Record == self.BOTScore:
            self.Score_Checker += 1
        else:
            self.Human_Sore_Record , self.Bot_Score_Record, self.Score_Checker = self.human1Score , self.BOTScore , 0
        if self.Score_Checker == 5:
            self.state = "GameOver"

    def calcRowCol(self, x, y):
        x1 = y // boxSize
        y1 = x // boxSize
        return 9-x1, y1

    #To check the validity of the click
    def checkValidClick(self, x, y):
        if 0 <= x <= SCREEN_WIDTH and 0 <= y <= SCREEN_HEIGHT:
            return True
        elif 0 > x > SCREEN_WIDTH and 0 > y > SCREEN_HEIGHT:
            return False
    #To find the points where we are currently standing
    def gethuman1Position(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if self.board[i][j] == 2:
                    return i,j


    def getBOTPosition(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if self.board[i][j] == 1:
                    return i,j

    #Heurestic Funtion which causes the ai agent to move intelligently
    def BOTTurn(self):
        self.MoveRightChance = 0
        self.MoveLeftChance = 0
        self.MoveDownChance = 0
        self.MoveUpChance = 0
        self.NoOfOnes = []
        x, y = self.getBOTPosition()
        for a in range(0,10):
            if y+a <= 9:
                if self.board[x][y+a] == 22:
                    break
                if self.board[x][y+a] == 0:
                    self.MoveRightChance += 1 
            else:
                break
        self.NoOfOnes.append(self.MoveRightChance)
        for b in range(0,10): 
            if y-b>=0:
                if self.board[x][y-b] == 22:
                    break
                if self.board[x][y-b] == 0:
                    self.MoveLeftChance += 1
            else:
                break
        self.NoOfOnes.append(self.MoveLeftChance)
        for c in range(0,10):
            if x+c<=9:
                if self.board[x+c][y] == 22:
                    break
                if self.board[x+c][y] == 0:
                    self.MoveDownChance += 1
            else:
                break
        self.NoOfOnes.append(self.MoveDownChance)
        for d in range(0,10):   
            if x-d>=0:
                if self.board[x-d][y] == 22:
                    break
                if self.board[x-d][y] == 0:
                    self.MoveUpChance += 1
            else:
                break
        self.NoOfOnes.append(self.MoveUpChance)

        self.NoOfOnes.sort()

        self.maxVal = self.NoOfOnes[3]  

        if x != 9 and y != 9:
            if self.board[x][y+1] != 11 and self.board[x][y-1] != 11 and self.board[x+1][y] != 11 and self.board[x-1][y] != 11:
                if self.maxVal == self.MoveRightChance and y != 9 and self.board[x][y+1] == 11:
                    self.maxVal = self.NoOfOnes[2]
                elif self.maxVal == self.MoveLeftChance and y != 0 and self.board[x][y-1] == 11:
                    self.maxVal = self.NoOfOnes[2]
                elif self.maxVal == self.MoveDownChance and x != 9 and self.board[x+1][y] == 11:
                    self.maxVal = self.NoOfOnes[2]
                elif self.maxVal == self.MoveUpChance and x != 0 and self.board[x-1][y] == 11:
                    self.maxVal = self.NoOfOnes[2]

        if self.maxVal == self.MoveRightChance and y != 9:
            print("self.MoveRightChance")
            if  self.board[x][y+1] == 11:
                self.RSlip(2)
            else:
                if  self.board[x][y+1] == 22 or self.board[x][y+1] == 2:
                    return
                else:
                    self.board[x][y+1], self.board[x][y] = 1, 11
                    self.BOTScore += 1

        elif self.maxVal == self.MoveLeftChance and y != 0:
            print("self.MoveLeftChance")
            if  self.board[x][y-1] == 11:
                self.LSlip(2)
            else:
                if self.board[x][y-1] == 22 or self.board[x][y-1] == 2:
                    return
                else:
                    self.board[x][y-1], self.board[x][y] = 1, 11
                    self.BOTScore += 1

        elif self.maxVal == self.MoveDownChance and x != 9:
            print("MoveDownChance")
            if  self.board[x+1][y] == 11:
                self.DownSlip(2)
            else:
                if self.board[x+1][y] == 22 or self.board[x+1][y] == 2:
                    return
                else:
                    self.board[x+1][y], self.board[x][y] = 1, 11
                    self.BOTScore += 1

        elif self.maxVal == self.MoveUpChance and x != 0:
            print("self.MoveUpChance")
            if  self.board[x-1][y] == 11:
                self.UPSlip(2)
            else:
                if self.board[x-1][y] == 22 or self.board[x-1][y] == 2:
                    return
                else:
                    self.board[x-1][y], self.board[x][y] = 1, 11
                    self.BOTScore += 1
        self.turn = "human1"

    def on_mouse_press(self, x, y, _button, _modifiers):
        if self.state == "GameOn":
            row, col = self.calcRowCol(x,y)
            print(row , col)
            if self.checkValidClick(x, y):
                # Now check weather the clicked space is next to the Position of player
                if self.turn == "human1":
                    x,y = self.gethuman1Position()
                    if   row==x and y+1==col and self.board[row][col]==0 or self.board[row][col] == 22 and row==x and y+1==col: #Right Move
                        if self.board[row][col] == 22:
                            self.RSlip(1)
                        else:
                            self.board[row][col], self.board[x][y] = 2, 22
                          #  self.turn = "BOT"
                            self.human1Score += 1
                        
                    elif row==x and y-1==col and self.board[row][col]==0 or self.board[row][col] == 22 and row==x and y-1==col: #Left Move
                        if self.board[row][col] == 22:
                            self.LSlip(1)
                        else:
                            self.board[row][col], self.board[x][y] = 2, 22
                          #  self.turn = "BOT"
                            self.human1Score += 1
                    elif x+1==row and y==col and self.board[row][col]==0 or self.board[row][col] == 22 and x+1==row and y==col: #down Move
                        if self.board[row][col]==22:
                            self.DownSlip(1)
                        else:
                            self.board[row][col], self.board[x][y] = 2, 22
                        #    self.turn = "BOT"
                            self.human1Score += 1
                    elif x-1==row and y==col and self.board[row][col]==0 or self.board[row][col]==22 and x-1==row and y==col: #Up Move
                        if self.board[row][col]==22:
                            self.UPSlip(1)
                        else:
                            self.board[row][col], self.board[x][y] = 2, 22
                         #   self.turn = "BOT"
                            self.human1Score += 1
                    else:
                     #   self.turn = "BOT"
                        print("INVALID CLICK, human1 TURN LOST !!!!")
                self.BOTTurn()
                self.StuckCondition()
                self.score()
            

        elif self.state == "GameOver":
            self.board = []
            self.human1 = 1
            self.BOT = 2
            self.turn = "human1"
            self.win = "0"
            self.state = "GameMenu"

    def score(self):
        print(self.human1Score)
        print(self.BOTScore)

        if self.human1Score > 49 or self.BOTScore > 49:
            self.state = "GameOver"
            if self.human1Score > self.BOTScore:
                self.win = "human1"
            elif self.human1Score < self.BOTScore:
                self.win = "BOT"
        elif  self.human1Score == 49 and self.BOTScore == 49:
            self.state = "GameOver"
            self.win = "draw"

         
        

if __name__ == "__main__":
    window = arcade.Window(SCREEN_HEIGHT+400, SCREEN_WIDTH, "SNAILS GAME")
    game_view = Game()
    window.center_window()
    window.show_view(game_view)
    arcade.run()