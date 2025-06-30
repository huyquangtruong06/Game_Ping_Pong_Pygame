import pygame
from define import *
from player import Player
from ball import Ball 

pygame.init()

pygame.display.set_caption("Rush Hour")
WINDOW_GAME = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
programIcon = pygame.image.load("RUSHHOUR.png")
pygame.display.set_icon(programIcon)

def key_events() : 
    global run, window_color
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False 
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                window_color = YELLOW

            if event.key == pygame.K_UP :
                PlayerRight.move_up()
            if event.key == pygame.K_DOWN :
                PlayerRight.move_down()
            
            if event.key == pygame.K_w :
                PlayerLeft.move_up()
            if event.key == pygame.K_s :
                PlayerLeft.move_down()
        

# Initalize player :
PlayerLeft = Player(RED, PLAYER_WIDTH, (WINDOW_HEIGHT - PLAYER_HEIGHT) / 2)
PlayerRight = Player(GREEN, WINDOW_WIDTH - 2 * PLAYER_WIDTH, (WINDOW_HEIGHT - PLAYER_HEIGHT) / 2)
ball = Ball(BLACK, 100, 100, BALL_SIZE)

window_color = GRAY
run = True 
score_left = 0
score_right = 0
font = pygame.font.SysFont(None, 48)  # font mặc định, kích thước 48

while run : 
    pygame.time.delay(100)
    WINDOW_GAME.fill(window_color)

    # Draw line
    pygame.draw.line(WINDOW_GAME, YELLOW, ((WINDOW_WIDTH) / 2, 0), ( (WINDOW_WIDTH) / 2, WINDOW_HEIGHT), LINE_WIDTH)
    
    score_text = font.render(f"{score_left}     {score_right}", True, BLACK)
    WINDOW_GAME.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, 20))

    #Play 1
    PlayerLeft.show(WINDOW_GAME)
    #Play 2
    PlayerRight.show(WINDOW_GAME)

    
    scorer = ball.move_ball(PlayerLeft, PlayerRight)
    if scorer == "left":
        score_left += 1
        ball.x = WINDOW_WIDTH // 2
        ball.y = WINDOW_HEIGHT // 2
        ball.speed_x = -abs(ball.speed_x)  # right
    elif scorer == "right":
        score_right += 1
        ball.x = WINDOW_WIDTH // 2
        ball.y = WINDOW_HEIGHT // 2
        ball.speed_x = abs(ball.speed_x)  # left

    ball.show_ball(WINDOW_GAME)
    key_events()


    pygame.display.update()

pygame.quit()

