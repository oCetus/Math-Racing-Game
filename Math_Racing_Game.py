#import pygame library
import pygame

#import random module
import random

#import operator module
import operator

from time import sleep

pygame.mixer.pre_init(44100, -16, 2, 16384)

#initiate pygame
pygame.init()

#initiate pygame mixer
pygame.mixer.init()


#Set Display to be 700 width and 700 height
Display = pygame.display.set_mode((700, 700))

#Set game name to Math Racing Game
pygame.display.set_caption('Math Racing Game')

#Set Logo to be Math Logo.jpg
Logo = pygame.image.load (r'Math Logo.png')

#Set Logo
pygame.display.set_icon(Logo)

#Clock is used for fps
Clock = pygame.time.Clock()

#Game background will equal Background which is Backgruond.png
Background = pygame.image.load (r'Background.png')

#Road Picture
Road = pygame.image.load (r'Road.png')

#Car Picture
Car = pygame.image.load (r'Car.png')

#Bot Picture
Bot = pygame.image.load (r'Bot.png')


#Set color code for black
black = (0,0,0)

#Set color code for gray
gray = (105,105,105)

#Set color code for white
white = (255,255,255)

#Set color code for red
red = (255,0,0)

#Set color code for yellow
yellow = (230,230,0)

#Set color code for green
green = (0,255,0)

#Set color code for blue
blue = (0,0,255)


Cars = pygame.mixer.Sound('cars.mp3')

Bad_Score = pygame.mixer.Sound('bad score.mp3')

Clapping = pygame.mixer.Sound('clapping.mp3')

#This is the code for the Start button on the Main Menu
def Start_Menu_Button(display, position, text):
    font = pygame.font.Font("freesansbold.ttf", 55)
    text_render = font.render(text, 1, (black))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (green))
    else:
        text_render = font.render(text, 1, (black))
        
    return display.blit(text_render, (x, y))

#This is the code for the How to Play Button on the Main Menu
def HTP_Menu_Button(display, position, text):
    font = pygame.font.Font("freesansbold.ttf", 55)
    text_render = font.render(text, 1, (black))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (255,170,200))
    else:
        text_render = font.render(text, 1, (black))
        
    return display.blit(text_render, (x, y))

#This is the code for the Quit button on the Main Menu
def Quit_Menu_Button(display, position, text):
    font = pygame.font.Font("freesansbold.ttf", 55)
    text_render = font.render(text, 1, (black))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (red))
    else:
        text_render = font.render(text, 1, (black))
        
    return display.blit(text_render, (x, y))

#This is the code for the About button on the Main Menu
def About_Menu_Button(display, position, text):
    font = pygame.font.Font("freesansbold.ttf", 35)
    text_render = font.render(text, 1, (0,0,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (blue))
    else:
        text_render = font.render(text, 1, (black))
    return display.blit(text_render, (x, y))

#This is the code for the Contact button on the Main Menu
def Contact_Menu_Button(display, position, text):
    font = pygame.font.Font("freesansbold.ttf", 20)
    text_render = font.render(text, 1, (0,0,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (yellow))
    else:
        text_render = font.render(text, 1, (black))
    return display.blit(text_render, (x, y))

#This is the code for the Back button on every menu
def Back_Menu_Button(display, position, text):
    font = pygame.font.Font("freesansbold.ttf", 35)
    text_render = font.render(text, 1, (0,0,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (red))
    else:
        text_render = font.render(text, 1, (black))
    return display.blit(text_render, (x, y))


#This is the code for the Difficulty Menu button
def Easy_Difficulty_Menu_Botton(display, position, text):
    font = pygame.font.Font("freesansbold.ttf", 55)
    text_render = font.render(text, 1, (0,0,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (green))
    else:
        text_render = font.render(text, 1, (black))
    return display.blit(text_render, (x, y))

#This is the code for the Difficulty Menu button
def Medium_Difficulty_Menu_Botton(display, position, text):
    font = pygame.font.Font("freesansbold.ttf", 55)
    text_render = font.render(text, 1, (0,0,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (yellow))
    else:
        text_render = font.render(text, 1, (black))
    return display.blit(text_render, (x, y))

#This is the code for the Difficulty Menu button
def Hard_Difficulty_Menu_Botton(display, position, text):
    font = pygame.font.Font("freesansbold.ttf", 55)
    text_render = font.render(text, 1, (0,0,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (red))
    else:
        text_render = font.render(text, 1, (black))
    return display.blit(text_render, (x, y))


#This is the code for the Chose Menu button on the End Menu
def Chose_Menu_Botton(display, position, text):
    font = pygame.font.Font("freesansbold.ttf", 35)
    text_render = font.render(text, 1, (0,0,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (red))
    else:
        text_render = font.render(text, 1, (black))
    return display.blit(text_render, (x, y))


#This is the code for the Multiplication Menu button 
def Multiplication_Menu_Button(display, position, text):
    font = pygame.font.Font("freesansbold.ttf", 50)
    text_render = font.render(text, 1, (0,0,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (blue))
    else:
        text_render = font.render(text, 1, (black))
    return display.blit(text_render, (x, y))

#This is the code for the Multiplication Table button
def Multiplication_Table_Button(display, position, text):
    font = pygame.font.Font('freesansbold.ttf', 50)
    text_render = font.render(text, 1, (0,0,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (blue))
    else:
        text_render = font.render(text, 1, (black))
    return display.blit(text_render, (x, y))

#This is the code for the Multiplication Table Mixed button
def Multiplication_Table_Mixed_Button(display, position, text):
    font = pygame.font.Font('freesansbold.ttf', 55)
    text_render = font.render(text, 1, (0,0,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (blue))
    else:
        text_render = font.render(text, 1, (black))
    return display.blit(text_render, (x, y))


#This is the code for the Addition Menu button
def Addition_Menu_Button(display, position, text):
    font = pygame.font.Font('freesansbold.ttf', 50)
    text_render = font.render(text, 1, (0,0,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (green))
    else:
        text_render = font.render(text, 1, (black))
    return display.blit(text_render, (x, y))

#This is the code for the Addition Table button
def Addition_Table_Button(display, position, text):
    font = pygame.font.Font('freesansbold.ttf', 50)
    text_render = font.render(text, 1, (0,0,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (green))
    else:
        text_render = font.render(text, 1, (black))
    return display.blit(text_render, (x, y))

#This is the code for the Addition Table Mixed button
def Addition_Table_Mixed_Button(display, position, text):
    font = pygame.font.Font('freesansbold.ttf', 55)
    text_render = font.render(text, 1, (0,0,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (green))
    else:
        text_render = font.render(text, 1, (black))
    return display.blit(text_render, (x, y))


#This is the code for the Subtraction Menu button
def Subtraction_Menu_Button(display, position, text):
    font = pygame.font.Font('freesansbold.ttf', 50)
    text_render = font.render(text, 1, (0,0,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (red))
    else:
        text_render = font.render(text, 1, (black))
    return display.blit(text_render, (x, y))

#This is the code for the Subtraciton Table button
def Subtraction_Table_Button(display, position, text):
    font = pygame.font.Font('freesansbold.ttf', 70)
    text_render = font.render(text, 1, (0,0,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        text_render = font.render(text, 1, (red))
    else:
        text_render = font.render(text, 1, (black))
    return display.blit(text_render, (x, y))


#This is the code for the Easy Difficulty Answer Box
def Easy_Answer_Box():
     
    Display.blit(Road, (0, 0))   

    maincar = pygame.image.load('Car.png')
    maincarX = 215
    maincarY = 330
    Display.blit(maincar,(maincarX,maincarY))

    botcar = pygame.image.load('Bot.png')
    botcarX = 340
    botcarY = 330
    Display.blit(botcar,(botcarX,botcarY))

    Number = Easy_Multiplication_Menu.num_1 or Easy_Addition_Menu.num_1 or Easy_Subtraction_Menu.num_1

    font = pygame.font.Font('freesansbold.ttf', 47)
    counter = 30
    text = font.render(str(f'Time = {counter}'), True, (black))
    timer_event = pygame.USEREVENT+1
    pygame.time.set_timer(timer_event, 1000)

    Back_Button = Back_Menu_Button(Display,(5,665),'Back')
    
    Answer_font = pygame.font.Font('freesansbold.ttf', 80)
    input_rect = pygame.Rect(35, 410, 150, 90)
    Player_text = ''
    
    pygame.draw.rect(Display, (150,150,150), input_rect)
    text_surface = Answer_font.render(Player_text, True, (black))
    Display.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(100, text_surface.get_width()+10)

    Easy_Answer_Box.score = 0
    k = 0

    operators = (Easy_Chose_Menu.operators)
    if Easy_Multiplication_Menu.q == 0 and Easy_Addition_Menu.q == 0:
        
        if Number == Easy_Multiplication_Menu.num_1 or Easy_Addition_Menu.num_1:
            num_1 = (Number)
            num_2 = random.randint(0, 10)
        else:
            num_1 = random.randint(Number, 10)
            num_2 = (Number)
    else:
        num_1 = random.randint(0, 10)
        num_2 = random.randint(0, 10)
        
    operation = random.choice(list(operators.keys()))
    solution = operators.get(operation)(num_1, num_2)
    Answer_Box_font = pygame.font.Font('freesansbold.ttf', 60)
    Answer_Box_surf = Answer_Box_font.render(str(f'{num_1} {operation} {num_2} ='), 1, (black))
    Answer_Box_pos = [0, 240]
    Display.blit(Answer_Box_surf, Answer_Box_pos)
    Display.fill(pygame.Color(44,210,0), (0, 240, 225, 100))
    Display.blit(Answer_Box_surf, Answer_Box_pos)
    
    while True:

        if k <= 4:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Back_Button.collidepoint(event.pos):
                        pygame.mixer.music.load('click.wav')
                        pygame.mixer.music.play()
                        Easy_Chose_Menu()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        Easy_Chose_Menu()
            
                    if event.key == pygame.K_RETURN:

                        operators = (Easy_Chose_Menu.operators)
                        if Easy_Multiplication_Menu.q == 0 and Easy_Addition_Menu.q == 0:
        
                            if Number == Easy_Multiplication_Menu.num_1 or Easy_Addition_Menu.num_1:
                                num_1 = (Number)
                                num_2 = random.randint(0, 10)
                            else:
                                num_1 = random.randint(Number, 10)
                                num_2 = (Number)
                        else:
                            num_1 = random.randint(0, 10)
                            num_2 = random.randint(0, 10)
                        
                        operation = random.choice(list(operators.keys()))
                        solution = operators.get(operation)(num_1, num_2)
                        Answer_Box_font = pygame.font.Font('freesansbold.ttf', 60)
                        Answer_Box_surf = Answer_Box_font.render(str(f'{num_1} {operation} {num_2} ='), 1, (black))
                        Answer_Box_pos = [0, 240]
                        Display.blit(Answer_Box_surf, Answer_Box_pos)
                        Display.fill(pygame.Color(44,210,0), (0, 240, 225, 100))
                        Display.blit(Answer_Box_surf, Answer_Box_pos)
                        
                if event.type == pygame.KEYDOWN:  

                    if event.key == pygame.K_BACKSPACE:
                        Player_text = Player_text[:-1]
                    elif event.key == pygame.K_RETURN:
            
                        Player_text = Player_text[:-10]

                        if Player_text == str(solution):
                            
                            k += 1
                        else:
                            k += 1

                    else:

                        Player_text += event.unicode

                        if Player_text == str(solution):                         
                            Easy_Answer_Box.score += 1
                            Cars.play()
                            maincarY -= 80
                            botcarY -= 30
                            Display.fill(0)
                            Display.blit(Road, (0,0))
                            Display.fill(pygame.Color(44,210,0), (0, 240, 225, 100))
                            Display.blit(Answer_Box_surf, Answer_Box_pos)
                            Display.fill(pygame.Color(44,210,0), (500, 330, 200, 45))
                            Display.blit(text, text_rect)
                            Display.blit(maincar,(maincarX,maincarY))
                            Display.blit(botcar,(botcarX,botcarY))
                            Back_Button = Back_Menu_Button(Display,(5,665),'Back')                       
                        else: 
                            Easy_Answer_Box.score += 0
                            botcarY -= 40
                            Display.fill(0)
                            Display.blit(Road, (0,0))
                            Display.fill(pygame.Color(44,210,0), (0, 240, 225, 100))
                            Display.blit(Answer_Box_surf, Answer_Box_pos)
                            Display.fill(pygame.Color(44,210,0), (500, 330, 200, 45))
                            Display.blit(text, text_rect)
                            Display.blit(maincar,(maincarX,maincarY))
                            Display.blit(botcar,(botcarX,botcarY))
                            Back_Button = Back_Menu_Button(Display,(5,665),'Back')  
                            
                            
                    pygame.draw.rect(Display, (150,150,150), input_rect)
                    text_surface = Answer_font.render(Player_text, True, (black))
                    Display.blit(text_surface, (input_rect.x+5, input_rect.y+5))
                    input_rect.w = max(100, text_surface.get_width()+10)
                    pygame.display.update()

                if event.type == timer_event:
                    counter -= 1
                    text = font.render(str (f'Time = {counter}'), True, (black))
                    if counter == 0:
                        pygame.time.set_timer(timer_event, 0)
                        Easy_End_Menu()
            
            Display.fill(pygame.Color(44,210,0), (500, 330, 200, 45))
            text_rect = [480, 330]
            Display.blit(text, text_rect)
            pygame.display.update()
            
        else:
            Easy_End_Menu()

#This is the code for the Medium Difficulty Answer Box
def Medium_Answer_Box():

    Display.blit(Road, (0, 0))

    maincar = pygame.image.load('Car.png')
    maincarX = 215
    maincarY = 330
    Display.blit(maincar,(maincarX,maincarY))

    botcar = pygame.image.load('Bot.png')
    botcarX = 340
    botcarY = 330
    Display.blit(botcar,(botcarX,botcarY))

    Number = Medium_Multiplication_Menu.num_1 or Medium_Addition_Menu.num_1 or Medium_Subtraction_Menu.num_1

    font = pygame.font.Font('freesansbold.ttf', 47)
    counter = 30
    text = font.render(str(f'Time = {counter}'), True, (black))
    timer_event = pygame.USEREVENT+1
    pygame.time.set_timer(timer_event, 1000)

    Back_Button = Back_Menu_Button(Display,(5,665),'Back')
    Answer_font = pygame.font.Font('freesansbold.ttf', 80)
    input_rect = pygame.Rect(35, 410, 150, 90)
    Player_text = ''
    
    pygame.draw.rect(Display, (150,150,150), input_rect)
    text_surface = Answer_font.render(Player_text, True, (black))
    Display.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(100, text_surface.get_width()+10)

    Medium_Answer_Box.score = 0
    k = 0

    operators = (Medium_Chose_Menu.operators)
    if Medium_Multiplication_Menu.q == 0 and Medium_Addition_Menu.q == 0:
        
        if Number == Medium_Multiplication_Menu.num_1 or Medium_Addition_Menu.num_1:
            num_1 = (Number)
            num_2 = random.randint(0, 10)
        else:
            num_1 = random.randint(Number, 10)
            num_2 = (Number)
    else:
        num_1 = random.randint(0, 10)
        num_2 = random.randint(0, 10)
        
    operation = random.choice(list(operators.keys()))
    solution = operators.get(operation)(num_1, num_2)
    Answer_Box_font = pygame.font.Font('freesansbold.ttf', 60)
    Answer_Box_surf = Answer_Box_font.render(str(f'{num_1} {operation} {num_2} ='), 1, (black))
    Answer_Box_pos = [0, 240]
    Display.blit(Answer_Box_surf, Answer_Box_pos)
    Display.fill(pygame.Color(44,210,0), (0, 240, 225, 100))
    Display.blit(Answer_Box_surf, Answer_Box_pos)

    while True:

        if k <= 9:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Back_Button.collidepoint(event.pos):
                        pygame.mixer.music.load('click.wav')
                        pygame.mixer.music.play()
                        Medium_Chose_Menu()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        Medium_Chose_Menu()
            
                    if event.key == pygame.K_RETURN:

                        operators = (Medium_Chose_Menu.operators)
                        if Medium_Multiplication_Menu.q == 0 and Medium_Addition_Menu.q == 0:
        
                            if Number == Medium_Multiplication_Menu.num_1 or Medium_Addition_Menu.num_1:
                                num_1 = (Number)
                                num_2 = random.randint(0, 10)
                            else:
                                num_1 = random.randint(Number, 10)
                                num_2 = (Number)
                        else:
                            num_1 = random.randint(0, 10)
                            num_2 = random.randint(0, 10)
                        
                        operation = random.choice(list(operators.keys()))
                        solution = operators.get(operation)(num_1, num_2)
                        Answer_Box_font = pygame.font.Font('freesansbold.ttf', 60)
                        Answer_Box_surf = Answer_Box_font.render(str(f'{num_1} {operation} {num_2} ='), 1, (black))
                        Answer_Box_pos = [0, 240]
                        Display.blit(Answer_Box_surf, Answer_Box_pos)
                        Display.fill(pygame.Color(44,210,0), (0, 240, 225, 100))
                        Display.blit(Answer_Box_surf, Answer_Box_pos)
                        

                if event.type == pygame.KEYDOWN:  

                    if event.key == pygame.K_BACKSPACE:
                        Player_text = Player_text[:-1]
                    elif event.key == pygame.K_RETURN:
            
                        Player_text = Player_text[:-10]

                        if Player_text == str(solution):

                            k += 1
                        else:
                            k += 1

                    else:

                        Player_text += event.unicode

                        if Player_text == str(solution):
                            Medium_Answer_Box.score += 1
                            Cars.play()
                            maincarY -= 40
                            botcarY -= 20
                            Display.fill(0)
                            Display.blit(Road, (0,0))
                            Display.fill(pygame.Color(44,210,0), (0, 240, 225, 100))
                            Display.blit(Answer_Box_surf, Answer_Box_pos)
                            Display.fill(pygame.Color(44,210,0), (500, 330, 200, 45))
                            Display.blit(text, text_rect)
                            Display.blit(maincar,(maincarX,maincarY))
                            Display.blit(botcar,(botcarX,botcarY))
                            Back_Button = Back_Menu_Button(Display,(5,665),'Back')                       
                        else: 
                            Medium_Answer_Box.score += 0
                            botcarY -= 20
                            Display.fill(0)
                            Display.blit(Road, (0,0))
                            Display.fill(pygame.Color(44,210,0), (0, 240, 225, 100))
                            Display.blit(Answer_Box_surf, Answer_Box_pos)
                            Display.fill(pygame.Color(44,210,0), (500, 330, 200, 45))
                            Display.blit(text, text_rect)
                            Display.blit(maincar,(maincarX,maincarY))
                            Display.blit(botcar,(botcarX,botcarY))
                            Back_Button = Back_Menu_Button(Display,(5,665),'Back')
                            
                    pygame.draw.rect(Display, (150,150,150), input_rect)
                    text_surface = Answer_font.render(Player_text, True, (black))
                    Display.blit(text_surface, (input_rect.x+5, input_rect.y+5))
                    input_rect.w = max(100, text_surface.get_width()+10)
                    pygame.display.update()
                    
                if event.type == timer_event:
                    counter -= 1
                    text = font.render(str (f'Time = {counter}'), True, (black))
                    if counter == 0:
                        pygame.time.set_timer(timer_event, 0)
                        Medium_End_Menu()
            
            Display.fill(pygame.Color(44,210,0), (500, 330, 200, 45))
            text_rect = timer_pos = [480, 330]
            Display.blit(text, text_rect)
            pygame.display.update()
            
        else:
            Medium_End_Menu()

#This is the code for the Hard Difficulty Answer Box
def Hard_Answer_Box():

    Display.blit(Road, (0, 0))

    maincar = pygame.image.load('Car.png')
    maincarX = 215
    maincarY = 330
    Display.blit(maincar,(maincarX,maincarY))

    botcar = pygame.image.load('Bot.png')
    botcarX = 340
    botcarY = 330
    Display.blit(botcar,(botcarX,botcarY))

    Number = Hard_Multiplication_Menu.num_1 or Hard_Addition_Menu.num_1 or Hard_Subtraction_Menu.num_1

    font = pygame.font.Font('freesansbold.ttf', 47)
    counter = 30
    text = font.render(str(f'Time = {counter}'), True, (black))
    timer_event = pygame.USEREVENT+1
    pygame.time.set_timer(timer_event, 1000)

    Back_Button = Back_Menu_Button(Display,(5,665),'Back')
    Answer_font = pygame.font.Font('freesansbold.ttf', 80)
    input_rect = pygame.Rect(35, 410, 150, 90)
    Player_text = ''
    
    pygame.draw.rect(Display, (150,150,150), input_rect)
    text_surface = Answer_font.render(Player_text, True, (black))
    Display.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(100, text_surface.get_width()+10)

    Hard_Answer_Box.score = 0
    k = 0

    operators = (Hard_Chose_Menu.operators)
    if Hard_Multiplication_Menu.q == 0 and Hard_Addition_Menu.q == 0:
        
        if Number == Hard_Multiplication_Menu.num_1 or Hard_Addition_Menu.num_1:
            num_1 = (Number)
            num_2 = random.randint(0, 10)
        else:
            num_1 = random.randint(Number, 10)
            num_2 = (Number)
    else:
        num_1 = random.randint(0, 10)
        num_2 = random.randint(0, 10)
        
    operation = random.choice(list(operators.keys()))
    solution = operators.get(operation)(num_1, num_2)
    Answer_Box_font = pygame.font.Font('freesansbold.ttf', 60)
    Answer_Box_surf = Answer_Box_font.render(str(f'{num_1} {operation} {num_2} ='), 1, (black))
    Answer_Box_pos = [0, 240]
    Display.blit(Answer_Box_surf, Answer_Box_pos)
    Display.fill(pygame.Color(44,210,0), (0, 240, 225, 100))
    Display.blit(Answer_Box_surf, Answer_Box_pos)

    while True:

        if k <= 14:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Back_Button.collidepoint(event.pos):
                        pygame.mixer.music.load('click.wav')
                        pygame.mixer.music.play()
                        Hard_Chose_Menu()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        Hard_Chose_Menu()
            
                    if event.key == pygame.K_RETURN:

                        operators = (Hard_Chose_Menu.operators)
                        if Hard_Multiplication_Menu.q == 0 and Hard_Addition_Menu.q == 0:
        
                            if Number == Hard_Multiplication_Menu.num_1 or Hard_Addition_Menu.num_1:
                                num_1 = (Number)
                                num_2 = random.randint(0, 10)
                            else:
                                num_1 = random.randint(Number, 10)
                                num_2 = (Number)
                        else:
                            num_1 = random.randint(0, 10)
                            num_2 = random.randint(0, 10)
                        
                        operation = random.choice(list(operators.keys()))
                        solution = operators.get(operation)(num_1, num_2)
                        Answer_Box_font = pygame.font.Font('freesansbold.ttf', 60)
                        Answer_Box_surf = Answer_Box_font.render(str(f'{num_1} {operation} {num_2} ='), 1, (black))
                        Answer_Box_pos = [0, 240]
                        Display.blit(Answer_Box_surf, Answer_Box_pos)
                        Display.fill(pygame.Color(44,210,0), (0, 240, 225, 100))
                        Display.blit(Answer_Box_surf, Answer_Box_pos)
                        

                if event.type == pygame.KEYDOWN:  

                    if event.key == pygame.K_BACKSPACE:
                        Player_text = Player_text[:-1]
                    elif event.key == pygame.K_RETURN:
            
                        Player_text = Player_text[:-10]

                        if Player_text == str(solution):

                            k += 1
                        else:
                            k += 1

                    else:

                        Player_text += event.unicode

                        if Player_text == str(solution):
                            Hard_Answer_Box.score += 1
                            Cars.play()
                            maincarY -= 25
                            botcarY -= 5
                            Display.fill(0)
                            Display.blit(Road, (0,0))
                            Display.fill(pygame.Color(44,210,0), (0, 240, 225, 100))
                            Display.blit(Answer_Box_surf, Answer_Box_pos)
                            Display.fill(pygame.Color(44,210,0), (500, 330, 200, 45))
                            Display.blit(text, text_rect)
                            Display.blit(maincar,(maincarX,maincarY))
                            Display.blit(botcar,(botcarX,botcarY))
                            Back_Button = Back_Menu_Button(Display,(5,665),'Back')                       
                        else: 
                            Hard_Answer_Box.score += 0
                            botcarY -= 15
                            Display.fill(0)
                            Display.blit(Road, (0,0))
                            Display.fill(pygame.Color(44,210,0), (0, 240, 225, 100))
                            Display.blit(Answer_Box_surf, Answer_Box_pos)
                            Display.fill(pygame.Color(44,210,0), (500, 330, 200, 45))
                            Display.blit(text, text_rect)
                            Display.blit(maincar,(maincarX,maincarY))
                            Display.blit(botcar,(botcarX,botcarY))
                            Back_Button = Back_Menu_Button(Display,(5,665),'Back')
                            
                    pygame.draw.rect(Display, (150,150,150), input_rect)
                    text_surface = Answer_font.render(Player_text, True, (black))
                    Display.blit(text_surface, (input_rect.x+5, input_rect.y+5))
                    input_rect.w = max(100, text_surface.get_width()+10)
                    pygame.display.update()
                    
                if event.type == timer_event:
                    counter -= 1
                    text = font.render(str (f'Time = {counter}'), True, (black))
                    if counter == 0:
                        pygame.time.set_timer(timer_event, 0)
                        Hard_End_Menu()
            
            Display.fill(pygame.Color(44,210,0), (500, 330, 200, 45))
            text_rect = timer_pos = [480, 330]
            Display.blit(text, text_rect)
            pygame.display.update()
            
        else:
            Hard_End_Menu()


#This is the code for the "Math Game!" text in the Main Menu
def Title_objects(text, font):
    textSurface = font.render(text, True, (255,100,100))
    return textSurface, textSurface.get_rect()

#This is the code for the "Math Game!" text in the Main Menu
def Title_display(text):

    TitleText = pygame.font.Font('freesansbold.ttf',70)
    TextSurf, TextRect = Title_objects(text, TitleText)
    TextRect.center = ((700/2),(135))
    Display.blit(TextSurf, TextRect)

    Clock.tick(60)

#This is the code for the "Math Game!" text in the Main Menu
def Title():

    Title_display('Math')


#This is the code for the "Math Game!" text in the Main Menu
def Title_objects2(text, font):
    textSurface = font.render(text, True, (255,100,100))
    return textSurface, textSurface.get_rect()

#This is the code for the "Math Game!" text in the Main Menu
def Title_display2(text):

    TitleText = pygame.font.Font('freesansbold.ttf',70)
    TextSurf, TextRect = Title_objects2(text, TitleText)
    TextRect.center = ((700/2),(220))
    Display.blit(TextSurf, TextRect)

    Clock.tick(60)

#This is the code for the "Math Game!" text in the Main Menu
def Title2():

    Title_display2('Racing Game')


#This is the code for the Main Menu
def Main_Menu():

    while True:

        Display.blit(Background,(0,0))

        Start_Button = Start_Menu_Button(Display,(280,320),'Start')
        Quit_Button = Quit_Menu_Button(Display,(285,390),'Quit')
        HTP_Button = HTP_Menu_Button(Display,(200,460), 'How to Play')
        About_Button = About_Menu_Button(Display,(92,575),'About')
        Contact_Button = Contact_Menu_Button(Display,(450, 570),'Contact Us')

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Quit_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()

                if Start_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Difficulty_Menu()

                if HTP_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    HTP_Menu()

                if About_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    About_Menu()

                if Contact_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Contact_Menu()
        
        Title()
        Title2()
        pygame.display.update()
        Clock.tick(60)

#This is the code for the HTP Menu
def HTP_Menu():

    while True:

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Main_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Main_Menu()

        HTP_font = pygame.font.Font('freesansbold.ttf', 55)
        HTP_surf = HTP_font.render(str(f'How to Play'), 1, (255,170,200))
        HTP_pos = [185,120]
        Display.blit(HTP_surf, HTP_pos)

        HTP1_font = pygame.font.Font('freesansbold.ttf', 28)
        HTP1_surf = HTP1_font.render(str(f'Easy: 5 questions in 30 seconds'), 1, (green))
        HTP1_pos = [125,250]
        Display.blit(HTP1_surf, HTP1_pos)

        HTP2_font = pygame.font.Font('freesansbold.ttf', 28)
        HTP2_surf = HTP2_font.render(str(f'Medium: 10 questions in 30 seconds'), 1, (yellow))
        HTP2_pos = [95,370]
        Display.blit(HTP2_surf, HTP2_pos)

        HTP3_font = pygame.font.Font('freesansbold.ttf', 28)
        HTP3_surf = HTP3_font.render(str(f'Hard: 15 questions in 30 seconds'), 1, (red))
        HTP3_pos = [110,485]
        Display.blit(HTP3_surf, HTP3_pos)
        
        pygame.display.update()
        Clock.tick(60)

#This is the code for the About Menu
def About_Menu():

    while True:

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Main_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Main_Menu()

        About_font = pygame.font.Font('freesansbold.ttf', 70)
        About_surf = About_font.render(str(f'About'), 1, (100,100,255))
        About_pos = [245,120]
        Display.blit(About_surf, About_pos)

        About_font = pygame.font.Font('freesansbold.ttf', 32)
        About_surf = About_font.render(str(f'This game was programmed'), 1, (black))
        About_pos = [125,210]
        Display.blit(About_surf, About_pos)

        About_font = pygame.font.Font('freesansbold.ttf', 31)
        About_surf = About_font.render(str(f'by Hussein Nabeel Ibrahim,'), 1, (black))
        About_pos = [135,260]
        Display.blit(About_surf, About_pos)

        About_font = pygame.font.Font('freesansbold.ttf', 32)
        About_surf = About_font.render(str(f'15 years old in the 10th grade at'), 1, (black))
        About_pos = [95,310]
        Display.blit(About_surf, About_pos)

        About_font = pygame.font.Font('freesansbold.ttf', 23)
        About_surf = About_font.render(str(f'Al-Harthiya Distinguished Secondary School.'), 1, (black))
        About_pos = [95,360]
        Display.blit(About_surf, About_pos)

        About_font = pygame.font.Font('freesansbold.ttf', 23)
        About_surf = About_font.render(str(f'This is the updated version of Math Game'), 1, (black))
        About_pos = [95,400]
        Display.blit(About_surf, About_pos)

        About_font = pygame.font.Font('freesansbold.ttf', 25)
        About_surf = About_font.render(str(f'The aim of this game is to encourage'), 1, (black))
        About_pos = [95,440]
        Display.blit(About_surf, About_pos)

        About_font = pygame.font.Font('freesansbold.ttf', 30)
        About_surf = About_font.render(str(f'children to learn the principles of'), 1, (black))
        About_pos = [100,480]
        Display.blit(About_surf, About_pos)

        About_font = pygame.font.Font('freesansbold.ttf', 30)
        About_surf = About_font.render(str(f'math in a competitive way.'), 1, (black))
        About_pos = [150,520]
        Display.blit(About_surf, About_pos)
        
        pygame.display.update()
        Clock.tick(60)

#This is the code for the Contact Menu
def Contact_Menu():
    
    while True:

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Main_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Main_Menu()

        Contact_font = pygame.font.Font('freesansbold.ttf', 60)
        Contact_surf = Contact_font.render(str(f'Contact Us'), 1, (yellow))
        Contact_pos = [180,150]
        Display.blit(Contact_surf, Contact_pos)

        Contact1_font = pygame.font.Font('freesansbold.ttf', 30)
        Contact1_surf = Contact1_font.render(str(f'If you need any help'), 1, (black))
        Contact1_pos = [200,250]
        Display.blit(Contact1_surf, Contact1_pos)
        
        Contact2_font = pygame.font.Font('freesansbold.ttf', 30)
        Contact2_surf = Contact2_font.render(str(f'or find any bugs'), 1, (black))
        Contact2_pos = [225,290]
        Display.blit(Contact2_surf, Contact2_pos)

        Contact3_font = pygame.font.Font('freesansbold.ttf', 30)
        Contact3_surf = Contact3_font.render(str(f'please contact us at'), 1, (black))
        Contact3_pos = [197,330]
        Display.blit(Contact3_surf, Contact3_pos)

        Contact4_font = pygame.font.Font('freesansbold.ttf', 25)
        Contact4_surf = Contact4_font.render(str(f'Email: hussein270607@gmail.com'), 1, (red))
        Contact4_pos = [150,410]
        Display.blit(Contact4_surf, Contact4_pos)

        Contact5_font = pygame.font.Font('freesansbold.ttf', 25)
        Contact5_surf = Contact5_font.render(str(f'Telegram Username: oCetus'), 1, (50,50,255))
        Contact5_pos = [150,450]
        Display.blit(Contact5_surf, Contact5_pos)

        Contact6_font = pygame.font.Font('freesansbold.ttf', 25)
        Contact6_surf = Contact6_font.render(str(f'Discord: Cetus#0021'), 1, (blue))
        Contact6_pos = [150,490]
        Display.blit(Contact6_surf, Contact6_pos)

        pygame.display.update()
        Clock.tick(60)

#This is the code for the Difficulty Menu where you chose from Easy, Medium, and Hard
def Difficulty_Menu():

    while True:

        Bad_Score.stop()
        Clapping.stop()
        Cars.stop()

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')
        Easy_Difficulty_Botton = Easy_Difficulty_Menu_Botton(Display,(285,250),'Easy')
        Medium_Difficulty_Botton = Medium_Difficulty_Menu_Botton(Display,(250,350),'Medium')
        Hard_Difficulty_Botton = Hard_Difficulty_Menu_Botton(Display,(285,450),'Hard')

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Main_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Main_Menu()

                if Easy_Difficulty_Botton.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Chose_Menu()

                if Medium_Difficulty_Botton.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Chose_Menu()

                if Hard_Difficulty_Botton.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Chose_Menu()

        pygame.display.update()
        Clock.tick(60)


#This is the code for the Chose Menu where you chose from Multiplication Menu, Addition Menu, and Subtraciton Menu
def Easy_Chose_Menu():

    while True:
        
        Cars.stop()

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')
        Multiplication_Button = Multiplication_Menu_Button(Display,(200,250),'Multiplication')
        Addition_Button = Addition_Menu_Button(Display,(250,350),'Addition')
        Subtraction_Button = Subtraction_Menu_Button(Display,(215,450),'Subtraction')

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Difficulty_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Difficulty_Menu()

                if Multiplication_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Chose_Menu.operators = {'x' : operator.mul}
                    Easy_Multiplication_Menu()

                if Addition_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Chose_Menu.operators = {'+' : operator.add}
                    Easy_Addition_Menu()

                if Subtraction_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Chose_Menu.operators = {'-' : operator.sub}
                    Easy_Subtraction_Menu()

        pygame.display.update()
        Clock.tick(60)

#This is the code for the Chose Menu where you chose from Multiplication Menu, Addition Menu, and Subtraciton Menu
def Medium_Chose_Menu():

    while True:

        Cars.stop()

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')
        Multiplication_Button = Multiplication_Menu_Button(Display,(200,250),'Multiplication')
        Addition_Button = Addition_Menu_Button(Display,(250,350),'Addition')
        Subtraction_Button = Subtraction_Menu_Button(Display,(215,450),'Subtraction')

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Difficulty_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    Difficulty_Menu()

                if Multiplication_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Chose_Menu.operators = {'x' : operator.mul}
                    Medium_Multiplication_Menu()

                if Addition_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Chose_Menu.operators = {'+' : operator.add}
                    Medium_Addition_Menu()

                if Subtraction_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Chose_Menu.operators = {'-' : operator.sub}
                    Medium_Subtraction_Menu()

        pygame.display.update()
        Clock.tick(60)

#This is the code for the Chose Menu where you chose from Multiplication Menu, Addition Menu, and Subtraciton Menu
def Hard_Chose_Menu():

    while True:

        Cars.stop()

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')
        Multiplication_Button = Multiplication_Menu_Button(Display,(200,250),'Multiplication')
        Addition_Button = Addition_Menu_Button(Display,(250,350),'Addition')
        Subtraction_Button = Subtraction_Menu_Button(Display,(215,450),'Subtraction')

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Difficulty_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Difficulty_Menu()

                if Multiplication_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Chose_Menu.operators = {'x' : operator.mul}
                    Hard_Multiplication_Menu()

                if Addition_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Chose_Menu.operators = {'+' : operator.add}
                    Hard_Addition_Menu()

                if Subtraction_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Chose_Menu.operators = {'-' : operator.sub}
                    Hard_Subtraction_Menu()

        pygame.display.update()
        Clock.tick(60)


#This is the code for the Multiplcation Menu which contains x1 through x10 and mixed
def Easy_Multiplication_Menu():

    while True:

        Easy_Multiplication_Menu.q = 0
        Easy_Addition_Menu.q = 0

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')
        Multiplication_1 = Multiplication_Table_Button(Display,(210,110),'x1')
        Multiplication_2 = Multiplication_Table_Button(Display,(210,170),'x2')
        Multiplication_3 = Multiplication_Table_Button(Display,(210,230),'x3')
        Multiplication_4 = Multiplication_Table_Button(Display,(210,290),'x4')
        Multiplication_5 = Multiplication_Table_Button(Display,(210,350),'x5')
        Multiplication_6 = Multiplication_Table_Button(Display,(410,110),'x6')
        Multiplication_7 = Multiplication_Table_Button(Display,(410,170),'x7')
        Multiplication_8 = Multiplication_Table_Button(Display,(410,230),'x8')
        Multiplication_9 = Multiplication_Table_Button(Display,(410,290),'x9')
        Multiplication_10 = Multiplication_Table_Button(Display,(400,350),'x10')
        Multiplication_Mixed = Multiplication_Table_Mixed_Button(Display,(260,450),'Mixed')

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Difficulty_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Difficulty_Menu()

                if Multiplication_1.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Multiplication_Menu.num_1 = 1
                    Easy_Answer_Box()

                if Multiplication_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Multiplication_Menu.num_1 = 2
                    Easy_Answer_Box()

                if Multiplication_3.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Multiplication_Menu.num_1 = 3
                    Easy_Answer_Box()
                    
                if Multiplication_4.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Multiplication_Menu.num_1 = 4
                    Easy_Answer_Box()

                if Multiplication_5.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Multiplication_Menu.num_1 = 5
                    Easy_Answer_Box()

                if Multiplication_6.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Multiplication_Menu.num_1 = 6
                    Easy_Answer_Box()

                if Multiplication_7.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Multiplication_Menu.num_1 = 7
                    Easy_Answer_Box()

                if Multiplication_8.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Multiplication_Menu.num_1 = 8
                    Easy_Answer_Box()

                if Multiplication_9.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Multiplication_Menu.num_1 = 9
                    Easy_Answer_Box()

                if Multiplication_10.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Multiplication_Menu.num_1 = 10
                    Easy_Answer_Box()
                
                if Multiplication_Mixed.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Multiplication_Menu.num_1 = random.randint(0, 10)
                    Easy_Multiplication_Menu.q = 1
                    Easy_Answer_Box()

        pygame.display.update()
        Clock.tick(60)

#This is the code for the Addition Menu which contains +1 through +10 and mixed
def Easy_Addition_Menu():

    Easy_Addition_Menu.q = 0
    Easy_Multiplication_Menu.q = 0
    Easy_Multiplication_Menu.num_1 = 0

    while True:

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')
        Addition_1 = Addition_Table_Button(Display,(210,110),'+1')
        Addition_2 = Addition_Table_Button(Display,(210,170),'+2')
        Addition_3 = Addition_Table_Button(Display,(210,230),'+3')
        Addition_4 = Addition_Table_Button(Display,(210,290),'+4')
        Addition_5 = Addition_Table_Button(Display,(210,350),'+5')
        Addition_6 = Addition_Table_Button(Display,(410,110),'+6')
        Addition_7 = Addition_Table_Button(Display,(410,170),'+7')
        Addition_8 = Addition_Table_Button(Display,(410,230),'+8')
        Addition_9 = Addition_Table_Button(Display,(410,290),'+9')
        Addition_10 = Addition_Table_Button(Display,(400,350),'+10')
        Addition_Mixed = Addition_Table_Mixed_Button(Display,(260,450),'Mixed')

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Difficulty_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Difficulty_Menu()

                if Addition_1.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Addition_Menu.num_1 = 1
                    Easy_Answer_Box()

                if Addition_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Addition_Menu.num_1 = 2
                    Easy_Answer_Box()

                if Addition_3.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Addition_Menu.num_1 = 3
                    Easy_Answer_Box()
                    
                if Addition_4.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Addition_Menu.num_1 = 4
                    Easy_Answer_Box()

                if Addition_5.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Addition_Menu.num_1 = 5
                    Easy_Answer_Box()

                if Addition_6.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Addition_Menu.num_1 = 6
                    Easy_Answer_Box()

                if Addition_7.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Addition_Menu.num_1 = 7
                    Easy_Answer_Box()

                if Addition_8.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Addition_Menu.num_1 = 8
                    Easy_Answer_Box()

                if Addition_9.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Addition_Menu.num_1 = 9
                    Easy_Answer_Box()

                if Addition_10.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Addition_Menu.num_1 = 10
                    Easy_Answer_Box()
                
                if Addition_Mixed.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Addition_Menu.num_1 = random.randint(0, 10)
                    Easy_Addition_Menu.q = 1
                    Easy_Answer_Box()

        pygame.display.update()
        Clock.tick(60)

#This is the code for the Subtraction Menu which contains -1 through -5
def Easy_Subtraction_Menu():

    Easy_Multiplication_Menu.q = 0
    Easy_Addition_Menu.q = 0
    Easy_Multiplication_Menu.num_1 = 0
    Easy_Addition_Menu.num_1 = 0

    while True:

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')
        Subtraction_1 = Subtraction_Table_Button(Display,(210,110),'-1')
        Subtraction_2 = Subtraction_Table_Button(Display,(210,300),'-2')
        Subtraction_3 = Subtraction_Table_Button(Display,(410,110),'-3')
        Subtraction_4 = Subtraction_Table_Button(Display,(410,300),'-4')
        Subtraction_5 = Subtraction_Table_Button(Display,(310,450),'-5')

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Difficulty_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Difficulty_Menu()

                if Subtraction_1.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Subtraction_Menu.num_1 = 1
                    Easy_Answer_Box()

                if Subtraction_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Subtraction_Menu.num_1 = 2
                    Easy_Answer_Box()

                if Subtraction_3.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Subtraction_Menu.num_1 = 3
                    Easy_Answer_Box()
                    
                if Subtraction_4.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Subtraction_Menu.num_1 = 4
                    Easy_Answer_Box()

                if Subtraction_5.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Easy_Subtraction_Menu.num_1 = 5
                    Easy_Answer_Box()

        pygame.display.update()
        Clock.tick(60)

#This is the code for the End Menu of the questions
def Easy_End_Menu():

    while True:

        Display.blit(Background,(0,0))

        Menu_Button = Chose_Menu_Botton(Display,(92,575),'Menu')

        Score_font = pygame.font.Font('freesansbold.ttf', 50)
        Score_surf = Score_font.render(str(f'Your score is {Easy_Answer_Box.score}!'), 1, (blue))
        Score_pos = [160,350]
        Display.blit(Score_surf, Score_pos)

        for event in pygame.event.get():
            
                if (event.type == pygame.QUIT):
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Difficulty_Menu()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Menu_Button.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.music.load('click.wav')
                        pygame.mixer.music.play()
                        Difficulty_Menu()

        if Easy_Answer_Box.score >= 4:
            Congratulations_font = pygame.font.Font('freesansbold.ttf', 50)
            Congratulations_surf = Congratulations_font.render(str(f'Congratulations'), 1, (green))
            Congratulations_pos = [150,210]
            Display.blit(Congratulations_surf, Congratulations_pos)
            Cars.stop()
            Clapping.play(-10)

        if Easy_Answer_Box.score == 3 or Easy_Answer_Box.score == 2:
            Keep_Trying_font = pygame.font.Font('freesansbold.ttf', 50)
            Keep_Trying_surf = Keep_Trying_font.render(str(f'Keep Trying'), 1, (yellow))
            Keep_Trying_pos = [200,210]
            Display.blit(Keep_Trying_surf, Keep_Trying_pos)
            Cars.stop()
        
        if Easy_Answer_Box.score <= 1:
            Good_Luck_Next_Time_font = pygame.font.Font('freesansbold.ttf', 45)
            Good_Luck_Next_Time_surf = Good_Luck_Next_Time_font.render(str(f'Good luck next time'), 1, (red))
            Good_Luck_Next_Time_pos = [130,210]
            Display.blit(Good_Luck_Next_Time_surf, Good_Luck_Next_Time_pos)
            Cars.stop()
            Bad_Score.play()

        pygame.display.update()
        Clock.tick(60)


#This is the code for the Multiplcation Menu which contains x1 through x10 and mixed
def Medium_Multiplication_Menu():

    while True:

        Medium_Multiplication_Menu.q = 0
        Medium_Addition_Menu.q = 0

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')
        Multiplication_1 = Multiplication_Table_Button(Display,(210,110),'x1')
        Multiplication_2 = Multiplication_Table_Button(Display,(210,170),'x2')
        Multiplication_3 = Multiplication_Table_Button(Display,(210,230),'x3')
        Multiplication_4 = Multiplication_Table_Button(Display,(210,290),'x4')
        Multiplication_5 = Multiplication_Table_Button(Display,(210,350),'x5')
        Multiplication_6 = Multiplication_Table_Button(Display,(410,110),'x6')
        Multiplication_7 = Multiplication_Table_Button(Display,(410,170),'x7')
        Multiplication_8 = Multiplication_Table_Button(Display,(410,230),'x8')
        Multiplication_9 = Multiplication_Table_Button(Display,(410,290),'x9')
        Multiplication_10 = Multiplication_Table_Button(Display,(400,350),'x10')
        Multiplication_Mixed = Multiplication_Table_Mixed_Button(Display,(260,450),'Mixed')

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Difficulty_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Difficulty_Menu()

                if Multiplication_1.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Multiplication_Menu.num_1 = 1
                    Medium_Answer_Box()

                if Multiplication_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Multiplication_Menu.num_1 = 2
                    Medium_Answer_Box()

                if Multiplication_3.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Multiplication_Menu.num_1 = 3
                    Medium_Answer_Box()
                    
                if Multiplication_4.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Multiplication_Menu.num_1 = 4
                    Medium_Answer_Box()

                if Multiplication_5.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Multiplication_Menu.num_1 = 5
                    Medium_Answer_Box()

                if Multiplication_6.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Multiplication_Menu.num_1 = 6
                    Medium_Answer_Box()

                if Multiplication_7.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Multiplication_Menu.num_1 = 7
                    Medium_Answer_Box()

                if Multiplication_8.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Multiplication_Menu.num_1 = 8
                    Easy_Answer_Box()

                if Multiplication_9.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Multiplication_Menu.num_1 = 9
                    Medium_Answer_Box()

                if Multiplication_10.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Multiplication_Menu.num_1 = 10
                    Medium_Answer_Box()
                
                if Multiplication_Mixed.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Multiplication_Menu.num_1 = random.randint(0, 10)
                    Medium_Multiplication_Menu.q = 1
                    Medium_Answer_Box()

        pygame.display.update()
        Clock.tick(60)

#This is the code for the Addition Menu which contains +1 through +10 and mixed
def Medium_Addition_Menu():

    Medium_Addition_Menu.q = 0
    Medium_Multiplication_Menu.q = 0
    Medium_Multiplication_Menu.num_1 = 0

    while True:

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')
        Addition_1 = Addition_Table_Button(Display,(210,110),'+1')
        Addition_2 = Addition_Table_Button(Display,(210,170),'+2')
        Addition_3 = Addition_Table_Button(Display,(210,230),'+3')
        Addition_4 = Addition_Table_Button(Display,(210,290),'+4')
        Addition_5 = Addition_Table_Button(Display,(210,350),'+5')
        Addition_6 = Addition_Table_Button(Display,(410,110),'+6')
        Addition_7 = Addition_Table_Button(Display,(410,170),'+7')
        Addition_8 = Addition_Table_Button(Display,(410,230),'+8')
        Addition_9 = Addition_Table_Button(Display,(410,290),'+9')
        Addition_10 = Addition_Table_Button(Display,(400,350),'+10')
        Addition_Mixed = Addition_Table_Mixed_Button(Display,(260,450),'Mixed')

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Difficulty_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Difficulty_Menu()

                if Addition_1.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Addition_Menu.num_1 = 1
                    Medium_Answer_Box()

                if Addition_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Addition_Menu.num_1 = 2
                    Medium_Answer_Box()

                if Addition_3.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Addition_Menu.num_1 = 3
                    Medium_Answer_Box()
                    
                if Addition_4.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Addition_Menu.num_1 = 4
                    Medium_Answer_Box()

                if Addition_5.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Addition_Menu.num_1 = 5
                    Medium_Answer_Box()

                if Addition_6.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Addition_Menu.num_1 = 6
                    Medium_Answer_Box()

                if Addition_7.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Addition_Menu.num_1 = 7
                    Medium_Answer_Box()

                if Addition_8.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Addition_Menu.num_1 = 8
                    Medium_Answer_Box()

                if Addition_9.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Addition_Menu.num_1 = 9
                    Medium_Answer_Box()

                if Addition_10.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Addition_Menu.num_1 = 10
                    Medium_Answer_Box()
                
                if Addition_Mixed.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Addition_Menu.num_1 = random.randint(0, 10)
                    Medium_Addition_Menu.q = 1
                    Medium_Answer_Box()

        pygame.display.update()
        Clock.tick(60)

#This is the code for the Subtraction Menu which contains -1 through -5
def Medium_Subtraction_Menu():

    Medium_Multiplication_Menu.q = 0
    Medium_Addition_Menu.q = 0
    Medium_Multiplication_Menu.num_1 = 0
    Medium_Addition_Menu.num_1 = 0

    while True:

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')
        Subtraction_1 = Subtraction_Table_Button(Display,(210,110),'-1')
        Subtraction_2 = Subtraction_Table_Button(Display,(210,300),'-2')
        Subtraction_3 = Subtraction_Table_Button(Display,(410,110),'-3')
        Subtraction_4 = Subtraction_Table_Button(Display,(410,300),'-4')
        Subtraction_5 = Subtraction_Table_Button(Display,(310,450),'-5')

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Difficulty_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Difficulty_Menu()

                if Subtraction_1.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Subtraction_Menu.num_1 = 1
                    Medium_Answer_Box()

                if Subtraction_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Subtraction_Menu.num_1 = 2
                    Medium_Answer_Box()

                if Subtraction_3.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Subtraction_Menu.num_1 = 3
                    Medium_Answer_Box()
                    
                if Subtraction_4.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Subtraction_Menu.num_1 = 4
                    Medium_Answer_Box()

                if Subtraction_5.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Medium_Subtraction_Menu.num_1 = 5
                    Medium_Answer_Box()

        pygame.display.update()
        Clock.tick(60)

#This is the code for the End Menu of the questions
def Medium_End_Menu():

    while True:

        Display.blit(Background,(0,0))

        Menu_Button = Chose_Menu_Botton(Display,(92,575),'Menu')

        Score_font = pygame.font.Font('freesansbold.ttf', 50)
        Score_surf = Score_font.render(str(f'Your score is {Medium_Answer_Box.score}!'), 1, (blue))
        Score_pos = [160,350]
        Display.blit(Score_surf, Score_pos)

        for event in pygame.event.get():
            
                if (event.type == pygame.QUIT):
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Difficulty_Menu()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Menu_Button.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.music.load('click.wav')
                        pygame.mixer.music.play()
                        Difficulty_Menu()

        if Medium_Answer_Box.score >= 7:
            Congratulations_font = pygame.font.Font('freesansbold.ttf', 50)
            Congratulations_surf = Congratulations_font.render(str(f'Congratulations'), 1, (0,255,0))
            Congratulations_pos = [150,210]
            Display.blit(Congratulations_surf, Congratulations_pos)
            Cars.stop()
            Clapping.play()

        if Medium_Answer_Box.score <= 6 and Medium_Answer_Box.score > 3:
            Keep_Trying_font = pygame.font.Font('freesansbold.ttf', 50)
            Keep_Trying_surf = Keep_Trying_font.render(str(f'Keep Trying'), 1, (yellow))
            Keep_Trying_pos = [200,210]
            Display.blit(Keep_Trying_surf, Keep_Trying_pos)
            Cars.stop()
        
        if Medium_Answer_Box.score <= 3:
            Good_Luck_Next_Time_font = pygame.font.Font('freesansbold.ttf', 45)
            Good_Luck_Next_Time_surf = Good_Luck_Next_Time_font.render(str(f'Good luck next time'), 1, (red))
            Good_Luck_Next_Time_pos = [130,210]
            Display.blit(Good_Luck_Next_Time_surf, Good_Luck_Next_Time_pos)
            Cars.stop()
            Bad_Score.play()

        pygame.display.update()
        Clock.tick(60)


#This is the code for the Multiplcation Menu which contains x1 through x10 and mixed
def Hard_Multiplication_Menu():

    while True:

        Hard_Multiplication_Menu.q = 0
        Hard_Addition_Menu.q = 0

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')
        Multiplication_1 = Multiplication_Table_Button(Display,(210,110),'x1')
        Multiplication_2 = Multiplication_Table_Button(Display,(210,170),'x2')
        Multiplication_3 = Multiplication_Table_Button(Display,(210,230),'x3')
        Multiplication_4 = Multiplication_Table_Button(Display,(210,290),'x4')
        Multiplication_5 = Multiplication_Table_Button(Display,(210,350),'x5')
        Multiplication_6 = Multiplication_Table_Button(Display,(410,110),'x6')
        Multiplication_7 = Multiplication_Table_Button(Display,(410,170),'x7')
        Multiplication_8 = Multiplication_Table_Button(Display,(410,230),'x8')
        Multiplication_9 = Multiplication_Table_Button(Display,(410,290),'x9')
        Multiplication_10 = Multiplication_Table_Button(Display,(400,350),'x10')
        Multiplication_Mixed = Multiplication_Table_Mixed_Button(Display,(260,450),'Mixed')

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Difficulty_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Difficulty_Menu()

                if Multiplication_1.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Multiplication_Menu.num_1 = 1
                    Hard_Answer_Box()

                if Multiplication_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Multiplication_Menu.num_1 = 2
                    Hard_Answer_Box()

                if Multiplication_3.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Multiplication_Menu.num_1 = 3
                    Hard_Answer_Box()
                    
                if Multiplication_4.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Multiplication_Menu.num_1 = 4
                    Hard_Answer_Box()

                if Multiplication_5.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Multiplication_Menu.num_1 = 5
                    Hard_Answer_Box()

                if Multiplication_6.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Multiplication_Menu.num_1 = 6
                    Hard_Answer_Box()

                if Multiplication_7.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Multiplication_Menu.num_1 = 7
                    Hard_Answer_Box()

                if Multiplication_8.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Multiplication_Menu.num_1 = 8
                    Hard_Answer_Box()

                if Multiplication_9.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Multiplication_Menu.num_1 = 9
                    Hard_Answer_Box()

                if Multiplication_10.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Multiplication_Menu.num_1 = 10
                    Hard_Answer_Box()
                
                if Multiplication_Mixed.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Multiplication_Menu.num_1 = random.randint(0, 10)
                    Hard_Multiplication_Menu.q = 1
                    Hard_Answer_Box()

        pygame.display.update()
        Clock.tick(60)

#This is the code for the Addition Menu which contains +1 through +10 and mixed
def Hard_Addition_Menu():

    Hard_Addition_Menu.q = 0
    Hard_Multiplication_Menu.q = 0
    Hard_Multiplication_Menu.num_1 = 0

    while True:

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')
        Addition_1 = Addition_Table_Button(Display,(210,110),'+1')
        Addition_2 = Addition_Table_Button(Display,(210,170),'+2')
        Addition_3 = Addition_Table_Button(Display,(210,230),'+3')
        Addition_4 = Addition_Table_Button(Display,(210,290),'+4')
        Addition_5 = Addition_Table_Button(Display,(210,350),'+5')
        Addition_6 = Addition_Table_Button(Display,(410,110),'+6')
        Addition_7 = Addition_Table_Button(Display,(410,170),'+7')
        Addition_8 = Addition_Table_Button(Display,(410,230),'+8')
        Addition_9 = Addition_Table_Button(Display,(410,290),'+9')
        Addition_10 = Addition_Table_Button(Display,(400,350),'+10')
        Addition_Mixed = Addition_Table_Mixed_Button(Display,(260,450),'Mixed')

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Difficulty_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Difficulty_Menu()

                if Addition_1.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Addition_Menu.num_1 = 1
                    Hard_Answer_Box()

                if Addition_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Addition_Menu.num_1 = 2
                    Hard_Answer_Box()

                if Addition_3.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Addition_Menu.num_1 = 3
                    Hard_Answer_Box()
                    
                if Addition_4.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Addition_Menu.num_1 = 4
                    Hard_Answer_Box()

                if Addition_5.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Addition_Menu.num_1 = 5
                    Hard_Answer_Box()

                if Addition_6.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Addition_Menu.num_1 = 6
                    Hard_Answer_Box()

                if Addition_7.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Addition_Menu.num_1 = 7
                    Hard_Answer_Box()

                if Addition_8.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Addition_Menu.num_1 = 8
                    Hard_Answer_Box()

                if Addition_9.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Addition_Menu.num_1 = 9
                    Hard_Answer_Box()

                if Addition_10.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Addition_Menu.num_1 = 10
                    Hard_Answer_Box()
                
                if Addition_Mixed.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Addition_Menu.num_1 = random.randint(0, 10)
                    Hard_Addition_Menu.q = 1
                    Hard_Answer_Box()

        pygame.display.update()
        Clock.tick(60)

#This is the code for the Subtraction Menu which contains -1 through -5
def Hard_Subtraction_Menu():

    Hard_Multiplication_Menu.q = 0
    Hard_Addition_Menu.q = 0
    Hard_Multiplication_Menu.num_1 = 0
    Hard_Addition_Menu.num_1 = 0

    while True:

        Display.blit(Background,(0,0))

        Back_Button = Back_Menu_Button(Display,(92,575),'Back')
        Subtraction_1 = Subtraction_Table_Button(Display,(210,110),'-1')
        Subtraction_2 = Subtraction_Table_Button(Display,(210,300),'-2')
        Subtraction_3 = Subtraction_Table_Button(Display,(410,110),'-3')
        Subtraction_4 = Subtraction_Table_Button(Display,(410,300),'-4')
        Subtraction_5 = Subtraction_Table_Button(Display,(310,450),'-5')

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Difficulty_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Difficulty_Menu()

                if Subtraction_1.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Subtraction_Menu.num_1 = 1
                    Hard_Answer_Box()

                if Subtraction_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Subtraction_Menu.num_1 = 2
                    Hard_Answer_Box()

                if Subtraction_3.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Subtraction_Menu.num_1 = 3
                    Hard_Answer_Box()
                    
                if Subtraction_4.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Subtraction_Menu.num_1 = 4
                    Hard_Answer_Box()

                if Subtraction_5.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    Hard_Subtraction_Menu.num_1 = 5
                    Hard_Answer_Box()

        pygame.display.update()
        Clock.tick(60)

#This is the code for the End Menu of the questions
def Hard_End_Menu():

    while True:

        Display.blit(Background,(0,0))

        Menu_Button = Chose_Menu_Botton(Display,(92,575),'Menu')

        Score_font = pygame.font.Font('freesansbold.ttf', 50)
        Score_surf = Score_font.render(str(f'Your score is {Hard_Answer_Box.score}!'), 1, (blue))
        Score_pos = [160,350]
        Display.blit(Score_surf, Score_pos)

        for event in pygame.event.get():
            
                if (event.type == pygame.QUIT):
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Difficulty_Menu()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Menu_Button.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.music.load('click.wav')
                        pygame.mixer.music.play()
                        Difficulty_Menu()

        if Hard_Answer_Box.score >= 13:
            Congratulations_font = pygame.font.Font('freesansbold.ttf', 50)
            Congratulations_surf = Congratulations_font.render(str(f'Congratulations'), 1, (0,255,0))
            Congratulations_pos = [150,210]
            Display.blit(Congratulations_surf, Congratulations_pos)
            Cars.stop()
            Clapping.play()

        if Hard_Answer_Box.score <= 12 and Hard_Answer_Box.score > 8:
            Keep_Trying_font = pygame.font.Font('freesansbold.ttf', 50)
            Keep_Trying_surf = Keep_Trying_font.render(str(f'Keep Trying'), 1, (yellow))
            Keep_Trying_pos = [200,210]
            Display.blit(Keep_Trying_surf, Keep_Trying_pos)
            Cars.stop()
        
        if Hard_Answer_Box.score <= 7:
            Good_Luck_Next_Time_font = pygame.font.Font('freesansbold.ttf', 45)
            Good_Luck_Next_Time_surf = Good_Luck_Next_Time_font.render(str(f'Good luck next time'), 1, (red))
            Good_Luck_Next_Time_pos = [130,210]
            Display.blit(Good_Luck_Next_Time_surf, Good_Luck_Next_Time_pos)
            Cars.stop()
            Bad_Score.play()

        pygame.display.update()
        Clock.tick(60)

Main_Menu()