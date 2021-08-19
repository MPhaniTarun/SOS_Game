def playGame():
    #================================Game Grid=================================== 
    def Grid():
        n=int(input("Choose your preferred NxN Grid size (>=3): "))
        grid=[]
        if n>=3:
            l1=["+"]
            k=1
            for i in range(0,n+2):
                l1.append('-')
            l1.append("+")
            grid.append(l1)
            l1=["|"]
            for i in range(0,n+2):
                l1.append(i+1)
            l1.append("|")
            grid.append(l1)
            for i in range(0,n):
                k+=1
                l1=["|",k]
                for i in range(0,n):
                    l1.append(".")
                l1.append(k)
                l1.append("|")
                grid.append(l1)
            k+=1
            l1=["|"]
            for i in range(0,n+2):
                l1.append(i+1)
            l1.append("|")
            grid.append(l1)
            k1=1
            l1=["+"]
            for i in range(0,n+2):
                l1.append('-')
            l1.append("+")
            grid.append(l1)
            # =====================Printing the NxN Grid===================
            for i in range(0,len(grid)):
                for j in range(0,len(grid[i])):
                    print(grid[i][j],end=" ")
                print()
            return grid
        else:
            print("Invalid Grid Size. Select an appropriate Size")
            Grid()
    grid=Grid()
    #==============================HOW TO PLAY THE GAME====================

    print("\n\n\t\t\t\t HOW TO PLAY :-\n")
    print("1. Player can choose a dot using co-ordinates available on the game grid.")
    print("2. Player who found a pattern 'SOS' in horizontal, vertical or  diagonally scores a point.")
    print("3. Player who scores a point gets an extra chance.")
    print("4. Player with maximum points wins the game.")
    print("\n\n")


    #===========================Ending the Game===============================

    l1=[]
    l2=[]
    def end_game(grid):
        dots=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j]=='.':
                    dots+=1
        if dots==0:
            print("\n\n-x-x-x-x-x-x-x------Game Over------x-x-x-x-x-x-x-")
            print("Results :")
            print(p1,"Scores:",sum(l1))
            print(p2,"Scores:",sum(l2))
            if sum(l1)>sum(l2):
                print(p1,"Wons the Game !!!")
            elif sum(l2)>sum(l1):
                print(p2,"Wons the Game !!!")
            else:
                print("Draw Match. Well Played !!!")
            def askend():
                a=input("Play Again [y or n]:")
                if a.lower()=='y':
                    playGame()
                elif a.lower()=='n':
                    print("\n\n-x-x-x-x-x-x-x------Game Over------x-x-x-x-x-x-x-\n")
                    exit()
                else:
                    print("Invalid input. Please enter a valid Input!!!")
                    askend()
            askend()

    #================================Evaluating the Player Move=============================
                
    def sos(grid,p,a,b):
        l=0
        if grid[a][b]=='s':        
            if grid[a-1][b]=='o' or grid[a-1][b]=='O':       # Above
                if grid[a-2][b]=='s' or grid[a-2][b]=='S':
                    grid[a-2][b]='S'
                    grid[a-1][b]='O'
                    grid[a][b]='S'
                    l+=1
            if grid[a+1][b]=='o' or grid[a+1][b]=='O':      # below
                if grid[a+2][b]=='s' or grid[a+2][b]=='S':
                    grid[a+2][b]='S'
                    grid[a+1][b]='O'
                    grid[a][b]='S'
                    l+=1
            if grid[a][b-1]=='o' or grid[a][b-1]=='O':     #left
                if grid[a][b-2]=='s' or grid[a][b-2]=='S':
                    grid[a][b-2]='S'
                    grid[a][b-1]='O'
                    grid[a][b]='S'
                    l+=1
            if grid[a][b+1]=='o' or grid[a][b+1]=='O':       #right
                if grid[a][b+2]=='s' or grid[a][b+2]=='S':
                    grid[a][b+2]='S'
                    grid[a][b+1]='O'
                    grid[a][b]='S'
                    l+=1
            if grid[a-1][b-1]=='o' or grid[a-1][b-1]=='O':    # upleft
                if grid[a-2][b-2]=='s' or grid[a-2][b-2]=='S':
                    grid[a-2][b-2]='S'
                    grid[a-1][b-1]='O'
                    grid[a][b]='S'
                    l+=1
            if grid[a-1][b+1]=='o' or grid[a-1][b+1]=='O':    # upright
                if grid[a-2][b+2]=='s' or grid[a-2][b+2]=='S':
                    grid[a-2][b+2]='S'
                    grid[a-1][b+1]='O'
                    grid[a][b]='S'
                    l+=1
            if grid[a+1][b-1]=='o' or grid[a+1][b-1]=='O':    # downleft
                if grid[a+2][b-2]=='s' or grid[a+2][b-2]=='S':
                    grid[a+2][b-2]='S'
                    grid[a+1][b-1]='O'
                    grid[a][b]='S'
                    l+=1
            if grid[a+1][b+1]=='o' or grid[a+1][b+1]=='O':    # downright
                if grid[a+2][b+2]=='s' or grid[a+2][b+2]=='S':
                    grid[a+2][b+2]='S'
                    grid[a+1][b+1]='O'
                    grid[a][b]='S'
                    l+=1
        if grid[a][b]=='o':
            if grid[a-1][b]=='s' or grid[a-1][b]=='S':
                if grid[a+1][b]=='s' or grid[a+1][b]=='S':   # up down Line
                    grid[a+1][b]='S'
                    grid[a-1][b]='S'
                    grid[a][b]='O'
                    l+=1
            if grid[a][b-1]=='s' or grid[a][b-1]=='S':       # left right
                if grid[a][b+1]=='s' or grid[a][b+1]=='S':
                    grid[a][b+1]='S'
                    grid[a][b-1]='S'
                    grid[a][b]='O'
                    l+=1
            if grid[a-1][b-1]=='s' or grid[a-1][b-1]=='S':     #  left right down
                if grid[a+1][b+1]=='s' or grid[a+1][b+1]=='S':
                    grid[a+1][b+1]='S'
                    grid[a-1][b-1]='S'
                    grid[a][b]='O'
                    l+=1
            if grid[a+1][b-1]=='s' or grid[a+1][b-1]=='S':     #  right left down
                if grid[a-1][b+1]=='s' or grid[a-1][b+1]=='S':
                    grid[a-1][b+1]='S'
                    grid[a+1][b-1]='S'
                    grid[a][b]='O'
                    l+=1
        if l>0 and p==1:
            l1.append(l)
            print(p1,"Score:",sum(l1))
            print(p2,"Score:",sum(l2))
        if l>0 and p==2:
            l2.append(l)
            print(p1,"Score:",sum(l1))
            print(p2,"Score:",sum(l2))
        if l>0:
            if p==1:
                print(p1,"gets extra chance")
                for i in range(0,len(grid)):
                    for j in range(0,len(grid[i])):
                        print(grid[i][j],end=" ")
                    print()
                end_game(grid)
                user1(grid,p1,p2)
            elif p==2:
                print(p2,"gets extra chance")
                for i in range(0,len(grid)):
                    for j in range(0,len(grid[i])):
                        print(grid[i][j],end=" ")
                    print()
                end_game(grid)
                user2(grid,p1,p2)
    #============================PLAYERS==================================
                
    def user2(grid,p1,p2):
        print(p2,end=" ")
        a=int(input("choose your row number:"))
        print(p2,end=" ")
        b=int(input("choose your column number:"))
        if grid[a][b]==".":
            print(p2,end=" ")
            c=input("choose s or o:")
            if ((a>=2 and a<=8) or (b>=2 and b<=8)):
                grid[a][b]=c
            else:
                print("Invalid Index!!! Please give valid index")
                user2(grid,p1,p2)
            grid[a][b]=c
            for i in range(0,len(grid)):
                for j in range(0,len(grid[i])):
                    if grid[i][j]=='s' or grid[i][j]=='o':
                        print(grid[i][j],end=" ")
                    else:
                        print(grid[i][j],end=" ")
                print()
            sos(grid,2,a,b)
            end_game(grid)
            user1(grid,p1,p2)
        else:
            print("Invalid Move. Not an empty space. Please enter a valid move.\n")
            user2(grid,p1,p2)
    def user1(grid,p1,p2):
        print(p1,end=" ")
        a=int(input("choose your row number:"))
        print(p1,end=" ")
        b=int(input("choose your column number:"))
        if grid[a][b]==".":
            print(p1,end=" ")
            c=input("choose s or o:")
            if ((a>=2 and a<=8) or (b>=2 and b<=8)):
                grid[a][b]=c
            else:
                print("Invalid Index!!! Please give valid index")
                user1(grid,p1,p2)
            grid[a][b]=c
            for i in range(0,len(grid)):
                for j in range(0,len(grid[i])):
                    print(grid[i][j],end=" ")
                print()
            sos(grid,1,a,b)
            end_game(grid)
            user2(grid,p1,p2)
        else:
            print("Invalid Move. Not an empty space. Please enter a valid move.\n")
            user1(grid,p1,p2)
    p1=input("Enter Player 1 Name :")
    p2=input("Enter Player 2 Name :")
    user1(grid,p1,p2)
playGame()

'''


FUNCTION                      DESCRIPTION
--------------------------------------------------------------------------------------------------------------------------------------------------------
playGame()  --->   Main Function where the entire code is present.
Grid()      --->   Function takes input from players and create a NxN Adjustable Game Grid.
user1()     --->   Function for Player 1, which takes input for the Player's move.
user2()     --->   Function for Player 2, which takes input for the Player's move.
sos()       --->   Function which evalutes both the player moves, checks whether the particular player won a point by that move and also update scores.
endgame()   --->   Function checks whether all the dots in the grid are filled and print Game results.
askend()    --->   Function takes input if the players wont to play again after the game end. 


'''
