# It is usedto create game and multimedia application for pyton
import pygame
import sys

#initialized the font module of Pygame, use text rendering and used for
#setup , font creation , text rendering, game loop, update disply
pygame.init()
pygame.font.init()


screen = pygame.display.set_mode((500, 600))

pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACK ALGO")
img = pygame.image.load("image.jpg")#load the imge
pygame.display.set_icon(img)#set the image in window

x = 0 # coordinate of current select X cell
y = 0 # Y coordinate of screen

# represent the width and height of each cell
#how?
#we need a sqare box and 9 boxes in each row and column . Teh width of window
# is 500px . so we divide the 500 px in 9 equal parts
diff = 500 / 9

# the val object store that value that we want to place in empty cell/box
# to completing the sukodu
val = 0

# Deafult Sukodu board (problem)that we are going to solve in this game
# 0 represent empty cell/box, and others no are present by default

grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]

]

#font with two different font size
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)

# when user click on the particular cell/box , its x and y coordinate store in pos tuple . Each coordinate
# divided (// which give abs value) by diff(size of each cell(height and width))
# and give address of each cell in form of row and column(x,y= 0,1 either 3,4)
def get_cell(pos):
    global x #we declare x gobal so , we can modiy it  from outside the function
    x = pos[0] // diff
    global y # global so that we can modify it from outside the function
    y = pos[0] // diff

#draw_box highlight each cell with red color, [range(2) means it run two time for [0,1] top ,botto , left and right
# Here x is the cell grom get_cell
# and diff is the width of cell -3 and +3 is for better visibility and 7 is for thickness
#get_cell convert coordinate to cell adress(in form of list) and x * diff convert back to coordinates
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * diff - 3, (y + i) * diff), (x * diff + diff + 3, (y + i) * diff), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * diff, y * diff), ((x + i) * diff, y * diff + diff), 7)

def draw():

# color the sudoku grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                #fill blue color in already numbers unsolved_sudoku
                # rect is for rectangle
                pygame.draw.rect(screen,(0, 153, 153), (i * diff, j * diff, diff + 1, diff + 1))

                # Fill unsolved_sukodu(grid) with default numbers specified
                #str convert integers into string
                text1 = font1.render(str[grid[i][j], True, (0, 0, 0)])
                # size and postion of numbers
                screen.blit(text1, (i * diff + 15, j * diff + 1))
        #now rantangle is formed , number is placed,  coloring is done ,
        # now it`s time for line formation
        for i in range(10):
            if i % 3 == 0 :
                thick = 7
            else:
                thick = 1
            pygame.draw.line(screen, (0, 0, 0), (0, i * diff),(500, i * diff), thick)
            pygame.draw.line(screen, (0, 0, 0), (i * diff, 0), (i * diff, 500), thick)

        #now the question arises -- why we color first and then makes a grid line ,
        # It is due to if we draw line first then there will be color overlap ,
        # to avoid overlap we build lines later

# draw_val is used to placing the value on to the screen
# screen.blit(): draw one surface (in this case, text1) onto another surface
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * diff + 15 , y * diff + 1))

def raise_error1():
    text1 = font1.render("WRONG !@!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))

def raise_error2():
    text1 = font1.render("Wrong !!! Not a valid key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))

#check if enter value is  valid or not
def valid(m , i  , j , val):
    for value in range(9):
        if m[i][value] == val:
            return False
        if m[value][j] == val:
            return False

        value_i = i // 3
        value_j = j // 3
        for i in range(value_i * 3, value_i * 3 + 3):
            for j in range(value_j * 3, value_j * 3 + 3):
                if m[i][j] == val:
                    return False
        return True

# Solve the sudoku board with BACKTRACK ALGORITHM
def solve(grid, i, j):
    while grid[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for value in range(1, 10):
        if valid(grid, i, j, value) == True:
            grid[i][j] = value
            global x, y
            x = i
            y = j
            # while color background
            screen.fill((255, 255, 255))
            draw()  #color sukodu grid and built lines
            draw_box() #red heighligh around cell
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j) == 1: #recursive call
                return True
            else:
                grid[i][j] = 0  #backtrack
                screen.fill((255, 255, 255))

                draw()  # color sukodu grid and built lines
                draw_box()  # red highlight around cell
                pygame.display.update()
                pygame.time.delay(50)
            return False

# Display instruction for the game
def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
    text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 540))

# Display options when solved
def result():
    text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))

run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
# The loop thats keep the window running
while run:

    # White color background
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False
        # Get the mouse position to insert number
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cell(pos)
        # Get the number to be inserted if key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9

            if event.key == pygame.K_RETURN:
                flag2 = 1

            # R press its going to clear the window or sukodu board
            if event.key == pygame.K_r:

                rs = 0
                error = 0
                flag2 = 0
                grid = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
                # If D is pressed reset the board to default
                if event.key == pygame.K_d:
                    rs = 0
                    error = 0
                    flag2 = 0
                    grid = [
                        [7, 8, 0, 4, 0, 0, 1, 2, 0],
                        [6, 0, 0, 0, 7, 5, 0, 0, 9],
                        [0, 0, 0, 6, 0, 1, 0, 7, 8],
                        [0, 0, 7, 0, 4, 0, 2, 6, 0],
                        [0, 0, 1, 0, 5, 0, 9, 3, 0],
                        [9, 0, 4, 0, 6, 0, 0, 0, 5],
                        [0, 7, 0, 3, 0, 0, 0, 1, 2],
                        [1, 2, 0, 0, 0, 7, 4, 0, 0],
                        [0, 4, 9, 2, 0, 6, 0, 0, 7]
                    ]

            if flag2 == 1:
                if solve(grid, 0, 0) == False:
                    error = 1
                else:
                    rs = 1
                    flag2 = 0

            if val !=0:
                draw_val(val)
                if valid(grid, int(x), int(y), val) == True:
                    grid[int(x)][int(y)] = val
                    flag1 = 0
                else:
                    grid[int(x)][int(y)] = 0
                    raise_error2()
                val = 0

            if error == 1:
                raise_error1()
            if rs == 1:
                result()
            draw()
            if flag1 == 1:
                draw_box()
            instruction()
            pygame.display.update()



pygame.quit()
