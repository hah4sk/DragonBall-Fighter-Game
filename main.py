import pygame
import time
from sprite import *
from player import *

pygame.init()
clock = pygame.time.Clock()
FPS = 30


# **COLORS ** #
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# ** LENGTHS ** #
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 800
delta_size = 10
punch_length_right = 5
punch_length_left = 65
kick_length_right = 5
kick_length_left = 65

# ** BACKGROUND IMAGE ** #
background = pygame.image.load("Backgrounds\Battleground.jpg")
background = pygame.transform.scale(background, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

# ** FONTS ** #
font = pygame.font.SysFont(None, 25)
myfont = pygame.font.SysFont(None, 35)

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption("Battle")


def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [DISPLAY_WIDTH/2-300, DISPLAY_HEIGHT/2])


def draw_background_and_players(player1, player2):
    global background
    if player1.getDamaged(): player1.setFlicker(player1.getFlicker()+1)
    if player2.getDamaged(): player2.setFlicker(player2.getFlicker()+1)

    gameDisplay.blit(background, (0, 0))
    # check if flickering,if so, draw based on flicker rate
    if player1.getDamaged():
        if player1.getFlicker() % 6 != 0:
            gameDisplay.blit(player1.getSprite().getImage(), (player1.getSprite().getX(), player1.getSprite().getY()))
    else:
        
        gameDisplay.blit(player1.getSprite().getImage(), (player1.getSprite().getX(), player1.getSprite().getY()))
    if player2.getDamaged():
        if player2.getFlicker() % 6 != 0:
            gameDisplay.blit(player2.getSprite().getImage(), (player2.getSprite().getX(), player2.getSprite().getY()))
    else:
        gameDisplay.blit(player2.getSprite().getImage(), (player2.getSprite().getX(), player2.getSprite().getY()))
    healthdisplay1 = myfont.render('PLAYER 1 HEALTH: ' + str(player1.getHealth()), 1, green)
    healthdisplay2 = myfont.render('PLAYER 2 HEALTH: ' + str(player2.getHealth()), 1, red)
    gameDisplay.blit(healthdisplay1, (100, 0))
    gameDisplay.blit(healthdisplay2, (DISPLAY_WIDTH / 2 + 100, 0))

    # done flickering, no longer damaged
    if player1.getFlicker() == 60:
        player1.setDamaged(False)
        player1.setFlicker(0)
    if player2.getFlicker() == 60:
        player2.setDamaged(False)
        player2.setFlicker(0)


def gameLoop():
    gameExit = False
    gameOver = False

    goku = Sprite("Goku\gokuIdleRight.png", 0, 0)
    vegeta = Sprite("Vegeta\VegetaIdleLeft.png", DISPLAY_WIDTH-200, DISPLAY_HEIGHT-200)
    player1 = Player(goku, Orientation.RIGHT)
    player2 = Player(vegeta, Orientation.LEFT)

    delta_x1 = 0
    delta_y1 = 0
    delta_x2 = 0
    delta_y2 = 0

    while not gameExit:

        while gameOver:
            gameDisplay.fill(black)

            losingPlayer = ""
            if (player1.getHealth() == 0):
                losingPlayer = "Goku"
            else:
                losingPlayer = "Vegeta"

            message_to_screen(losingPlayer + " Lost Cuz He Sucks. Press C To Play Again Or Q To Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                # PLAYER1 MOVEMENT
                if event.key == pygame.K_a:
                    delta_x1 = -delta_size
                    player1.setOrientation(Orientation.LEFT)
                elif event.key == pygame.K_d:
                    delta_x1 = delta_size
                    player1.setOrientation(Orientation.RIGHT)
                elif event.key == pygame.K_w:
                    delta_y1 = -delta_size
                elif event.key == pygame.K_s:
                    delta_y1 = delta_size
                # PLAYER2 MOVEMENT
                if event.key == pygame.K_LEFT:
                    delta_x2 = -delta_size
                    player2.setOrientation(Orientation.LEFT)
                elif event.key == pygame.K_RIGHT:
                    delta_x2 = delta_size
                    player2.setOrientation(Orientation.RIGHT)
                elif event.key == pygame.K_UP:
                    delta_y2 = -delta_size
                elif event.key == pygame.K_DOWN:
                    delta_y2 = delta_size
                # PLAYER1 ATK
                if event.key == pygame.K_z:
                    if player1.getOrientation() == Orientation.RIGHT:
                        player1.getSprite().moveHorizontally(punch_length_right)
                    elif player1.getOrientation() == Orientation.LEFT:
                        player1.getSprite().moveHorizontally(-punch_length_left)
                    player1.setAtking(True)
                # PLAYER2 ATK
                if event.key == pygame.K_COMMA:
                    if player2.getOrientation() == Orientation.RIGHT: player2.getSprite().moveHorizontally(punch_length_right)
                    elif player2.getOrientation() == Orientation.LEFT: player2.getSprite().moveHorizontally(-punch_length_left)
                    player2.setAtking(True)
                # PLAYER1 GUARD
                if event.key == pygame.K_x:
                    player1.setGuarding(True)
                # PLAYER2 GUARD
                if event.key == pygame.K_PERIOD:
                    player2.setGuarding(True)
            if event.type == pygame.KEYUP:
                # PLAYER1 MOVEMENT
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    delta_x1 = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    delta_y1 = 0
                # PLAYER2 MOVEMENT
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    delta_x2 = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    delta_y2 = 0
                # PLAYER1 RELEASE ATK
                if event.key == pygame.K_z:
                    if player1.getOrientation() == Orientation.RIGHT:
                        player1.getSprite().moveHorizontally(-punch_length_right)
                    elif player1.getOrientation() == Orientation.LEFT:
                        player1.getSprite().moveHorizontally(punch_length_left)
                    player1.setAtking(False)
                # PLAYER2 RELEASE ATK
                if event.key == pygame.K_COMMA:
                    if player2.getOrientation() == Orientation.RIGHT:
                        player2.getSprite().moveHorizontally(-punch_length_right)
                    elif player2.getOrientation() == Orientation.LEFT:
                        player2.getSprite().moveHorizontally(punch_length_left)
                    player2.setAtking(False)
                # PLAYER1 RELEASE GUARD
                if event.key == pygame.K_x:
                    player1.setGuarding(False)
                # PLAYER2 RELEASE GUARD
                if event.key == pygame.K_PERIOD:
                    player2.setGuarding(False)

        # determine which image to use, based on previous orientation/activity inputs
        # player1
        if player1.isFacingLeft():
            if player1.getAtking():
                player1.getSprite().setImage("Goku\gokuPunchLeft.png")
            elif player1.getGuarding():
                player1.getSprite().setImage("Goku\gokuGuardingLeft.png")
            else:
                player1.getSprite().setImage("Goku\gokuIdleLeft.png")
        elif player1.isFacingRight():
            if player1.getAtking():
                player1.getSprite().setImage("Goku\gokuPunchRight.png")
            elif player1.getGuarding():
                player1.getSprite().setImage("Goku\gokuGuardingRight.png")
            else:
                player1.getSprite().setImage("Goku\gokuIdleRight.png")
        # player2
        if player2.isFacingLeft():
            if player2.getAtking():
                player2.getSprite().setImage("Vegeta\VegetaKickLeft.png")
            elif player2.getGuarding():
                player2.getSprite().setImage("Vegeta\VegetaGuardingLeft.png")
            else:
                player2.getSprite().setImage("Vegeta\VegetaIdleLeft.png")
        elif player2.isFacingRight():
            if player2.getAtking():
                player2.getSprite().setImage("Vegeta\VegetaKickRight.png")
            elif player2.getGuarding():
                player2.getSprite().setImage("Vegeta\VegetaGuardingRight.png")
            else:
                player2.getSprite().setImage("Vegeta\VegetaIdleRight.png")

        # ******** MAKING SURE SPRITES DON'T OCCUPY SAME AREA ******** #
        if not (player1.getAtking() or player1.getGuarding()):   # can't move if guarding or attacking
            player1.getSprite().moveHorizontally(delta_x1)
            if collision(player1.getSprite(),player2.getSprite()) and not (player1.getAtking() or player2.getAtking()):
                player1.getSprite().moveHorizontally(-delta_x1)

            player1.getSprite().moveVertically(delta_y1)
            if collision(player1.getSprite(), player2.getSprite()) and not (player1.getAtking() or player2.getAtking()):
                player1.getSprite().moveVertically(-delta_y1)

        if not (player2.getAtking() or player2.getGuarding()):
            player2.getSprite().moveHorizontally(delta_x2)
            if collision(player1.getSprite(), player2.getSprite()) and not (player1.getAtking() or player2.getAtking()):
                player2.getSprite().moveHorizontally(-delta_x2)

            player2.getSprite().moveVertically(delta_y2)
            if collision(player1.getSprite(), player2.getSprite()) and not (player1.getAtking() or player2.getAtking()):
                player2.getSprite().moveVertically(-delta_y2)

        # **********WHEN SOMEONE ATTACKS OR GUARDS********** #
        if collision(player1.getSprite(), player2.getSprite()):
            #if player1.getAtking() and not player2.getDamaged():
            if player1.getAtking():
                # player2 recoils
                if player1.getSprite().getX() < player2.getSprite().getX():
                    player2.getSprite().moveHorizontally(player1.getSprite().getX()+player1.getSprite().getWidth()-player2.getSprite().getX()+10)
                else:
                    player2.getSprite().moveHorizontally(-(player2.getSprite().getX()+player2.getSprite().getWidth()-player1.getSprite().getX())-10)
                if not player2.getGuarding() and not player2.getDamaged():
                    player2.setHealth(player2.getHealth()-1)  # player2 loses HP
                    player2.setDamaged(True)
            #if player2.getAtking() and not player1.getDamaged():
            if player2.getAtking():
                # player1 recoils
                if player1.getSprite().getX() < player2.getSprite().getX():
                    player1.getSprite().moveHorizontally( -(player1.getSprite().getX()+player1.getSprite().getWidth()-player2.getSprite().getX())-10 )
                else:
                    player1.getSprite().moveHorizontally(player2.getSprite().getX()+player2.getSprite().getWidth()-player1.getSprite().getX()+10)
                if not player1.getGuarding() and not player1.getDamaged():
                    player1.setHealth(player1.getHealth()-1)  # player1 loses HP
                    player1.setDamaged(True)

        draw_background_and_players(player1, player2)

        # Update And Tick The Clock
        pygame.display.update()
        clock.tick(FPS)

        if player2.getHealth() == 0 or player1.getHealth() == 0:
            gameOver = True

    # when gameExit
    pygame.quit()
    quit()


gameLoop()

################ P1: GOKU  P2: VEGETA ################