#1. change the speed (slower)* trial and error
#2. change the score color is. *trial and error
#3. different wordings in menu *friends suggestion
#4. different font size *my decision
#5. change menu picture into pink *another documentation
#6 changw the apple to a heart

import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0, 155, 0)
pink = (255, 153, 255)
purple = (255, 51, 255)
lpink= (255, 204, 255)
pp=(51, 51, 204)
blue =(0, 0, 153)
sky=(66, 244, 235)


display_width = 800
display_height = 600


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake')

icon = pygame.image.load('C:/Users/Family/Desktop/snake/heart2.png')
pygame.display.set_icon(icon)

img = pygame.image.load('C:/Users/Family/Desktop/snake/snakeHead.png')
appleimg = pygame.image.load ('C:/Users/Family/Desktop/snake/heart2.png')
background_image = pygame.image.load("pinksnow.jpg").convert()
background_image2 = pygame.image.load("blue.jpg").convert()




gameExit = False

lead_x = display_width/2
lead_y = display_height/2

lead_x_change = 0
lead_y_change = 0

#fps
clock = pygame.time.Clock()

block_size = 30
FPS = 10

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 15)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 70)

#do a def displa then create a boundr
##def randAppleGen():
##    randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
##    randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0


##randAppleX,randAppleY = randAppleGen()

def score (score):
    text = medfont.render("score: "+ str(score), True, pink)
    gameDisplay.blit(text, [550,20])
      

def game_intro():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                  
        gameDisplay.blit(background_image, [0,0])
        message_to_screen("Welcome to Slithers***",
            sky,
            -100,
            size ="large")
        message_to_screen("In order to survive in this world, you need to eat the red fruit that contains HP. ",
            black,
            30)
    
        message_to_screen("When you consume the fruit, you will grow longer and live longer.",
            black,
            60)
            
        message_to_screen("Warning!!! Do not go outside the windows and do not eat ourself. If you do, you will die.",
            white,
            100)
        message_to_screen("Press c to play or q to quit.",
            green,
            150,
            size= "medium")
            
        pygame.display.update()
        clock.tick(15)

def snake(block_size, snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img,270)
    if direction == "left":
        head = pygame.transform.rotate(img,90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img,180)
        
    gameDisplay.blit(head, (snakelist[-1][0], snakelist [-1][1]))
    for XnY in snakelist[:-1]:
      pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])
      
def text_objects(text,color, size):
    if size =="small":
        textSurface = smallfont.render(text, True, color)
    elif size =="medium":
        textSurface = medfont.render(text, True, color)
    elif size =="large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)
    
def gameLoop():
  global direction
 
  direction = 'right'
  gameExit = False
  gameOver = False

  lead_x = display_width/2
  lead_y = display_height/2
 
  lead_x_change = 10
  lead_y_change = 0
 
  snakeList = []
  snakeLength = 1 #snake starts at 1 block
 
  randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
  randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0


 
  while not gameExit:
      while gameOver == True:
          message_to_screen("Game over!!!",
                      red,
                      y_displace=-50,
                      size = "large")
          message_to_screen("Press c to play again or q to quit",
                      purple,
                      y_displace= 75,
                      size = "medium")
          pygame.display.update()
          
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  gameExit = True
                  gameOver = False
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_q:
                      gameOver = False
                      gameExit = True
                      
                  if event.key == pygame.K_c:
                      gameLoop()
                      
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              gameExit = True
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                  direction = "left"
                  lead_x_change = -block_size
                  lead_y_change = 0
              elif event.key == pygame.K_RIGHT:
                  direction = "right"
                  lead_x_change = block_size
                  lead_y_change = 0
              elif event.key == pygame.K_UP:
                  direction = "up"
                  lead_y_change = -block_size
                  lead_x_change = 0
              elif event.key == pygame.K_DOWN:
                  direction = "down"
                  lead_y_change = block_size
                  lead_x_change = 0
    #boundaries     
      if lead_x > display_width or lead_x < 0 or lead_y > display_height or lead_y < 0:
          gameOver = True
          
    
      lead_x += lead_x_change
      lead_y += lead_y_change
      
      AppleThickness = 30
      gameDisplay.blit(background_image2, [0,0])
      #pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY, AppleThickness, AppleThickness])
      
      gameDisplay.blit(appleimg, (randAppleX, randAppleY))
     
      snakeHead = []
      snakeHead.append(lead_x)
      snakeHead.append(lead_y)
      snakeList.append(snakeHead)
      
      if len(snakeList) > snakeLength:
          del snakeList[0]
          
      for eachSegment in snakeList[:-1]:
          if eachSegment == snakeHead:
              gameOver = True
      
      snake(block_size, snakeList)
      
      score(snakeLength-1)
      
      pygame.display.update()
              
      if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
          
          if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
             randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
             randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0


             snakeLength += 1
          
          elif lead_y + block_size > randAppleY and lead_y + block_size< randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0


                snakeLength += 1
          
    #frames per second(made snake slower)
      clock.tick(FPS)
    
  pygame.quit()
  quit()

game_intro()
gameLoop()

