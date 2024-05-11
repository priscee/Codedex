import pygame
import random

#==DISPLAY SIZE==#
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

#==COLORS TO USE==#
COLOR_black = (0, 0, 0)
COLOR_white = (255, 255, 255)
COLOR_green = (57, 255, 20)

def main():

    #initialize pygame library
    pygame.init()

    #set the window screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #title for window display
    pygame.display.set_caption("Pong")

    #clock object to keep track of time
    clock = pygame.time.Clock()

    #check whether to move the ball or not, will move aft 3 secs
    started = False

    #player paddles rect(x, y, width, height)
    paddle_1_rect = pygame.Rect(30, 0, 7, 100)
    paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)

    #track how much player paddles move per frame
    paddle_1_move = 0
    paddle_2_move = 0

    # rectangle that represents the ball
    ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)

    #determine x & y speed of ball
    ball_accel_x = random.randint(2, 4) * 0.1
    ball_accel_y = random.randint(2, 4) * 0.1

    #randomize direction of ball
    if random.randint(1, 2) == 1:
        ball_accel_x *= -1
    if random.randint(1, 2) == 1:
        ball_accel_y *= -1

    while True:
        #background color
        screen.fill(COLOR_black)

        #==OPENING SCREEN==#
        #make ball move after 3 sec
        if not started:
            #load pixelify font
            font = pygame.font.Font('Font/PixelifySans.ttf', 30)

            #text in the center of the screen
            text = font.render('Press Space to Start', True, COLOR_green)
            text_rect = text. get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            screen.blit(text, text_rect)

            #update display
            pygame.display.flip()

            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        started = True
            
            continue

        #time elapse between now and last frame
        delta_time = clock.tick(60)

        for event in pygame.event.get():

            #==EXIT WINDOW==#
            if event.type == pygame.QUIT:
                return

            #==MOVING PADDLES==#
            if event.type == pygame.KEYDOWN:

                #player 1
                #P1 w = up
                if event.key == pygame.K_w:
                    paddle_1_move -= 0.6
                #P1 s = down
                if event.key == pygame.K_s:
                    paddle_1_move += 0.6
                #P1 release key, stop paddle movement

                #player 2
                #P2 ⬆ = up
                if event.key == pygame.K_UP:
                    paddle_2_move -= 0.6
                #P2 ⬇ = down
                if event.key == pygame.K_DOWN:
                    paddle_2_move += 0.6
            
            #==STOP PADDLE MOVEMENT==#
            if event.type == pygame.KEYUP:
                #P1 release key
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle_1_move == 0.0
                #P2 relese key
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle_2_move == 0.0

        #moving the paddles according to the move variables
        paddle_1_rect.top += paddle_1_move * delta_time
        paddle_2_rect.top += paddle_2_move * delta_time

        #==BOUNDARIES OF PADDLES==#
        #player 1 paddle
        if paddle_1_rect.top < 0:
            paddle_1_rect.top = 0
        if paddle_1_rect.bottom > SCREEN_HEIGHT:
            paddle_1_rect.bottom = SCREEN_HEIGHT
        
        #player 2 paddle
        if paddle_2_rect.top < 0:
            paddle_2_rect.top = 0
        if paddle_2_rect.bottom > SCREEN_HEIGHT:
            paddle_2_rect.bottom = SCREEN_HEIGHT

        #==BOUNDARIES OF BALL==#
        #if ball getting to close to the top
        if ball_rect.top < 0:
            #invent vertical velocity
            ball_accel_y *= -1
            #add a bit of y to not trigger the code again
            ball_rect.top = 0
        
        #if ball getting too close to the bottom
        if ball_rect.bottom > SCREEN_HEIGHT - ball_rect.height:
            ball_accel_y *= -1
            ball_rect.bottom = SCREEN_HEIGHT - ball_rect.height

        #ball goes out of bounds, end game
        if ball_rect.left <= 0:
            over_text = font.render('GAME OVER Player 2 Wins!', True, COLOR_green)
            over_text_rect = over_text.get_rect()
            over_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            screen.blit(over_text, over_text_rect)        
        elif ball_rect.left >= SCREEN_WIDTH:
            over_text = font.render('GAME OVER Player 1 Wins!', True, COLOR_green)
            over_text_rect = over_text.get_rect()
            over_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            screen.blit(over_text, over_text_rect)

        #==PADDLES & BALL COLLIDES==#
        #paddle 1
        if paddle_1_rect.colliderect(ball_rect) and paddle_1_rect.left < ball_rect.left:
            ball_accel_x *= -1
            ball_rect.left += 5
        #paddle 2
        if paddle_2_rect.colliderect(ball_rect) and paddle_2_rect.left > ball_rect.left:
            ball_accel_x *= -1
            ball_rect.left -= 5

        #==GAME STARTED AFTER 3 SECS==#
        if started:
            #move ball
            ball_rect.left += ball_accel_x * delta_time
            ball_rect.top += ball_accel_y * delta_time

        #==DRAWING THE GAME==#
        #draw player paddles with white
        pygame.draw.rect(screen, COLOR_white, paddle_1_rect)
        pygame.draw.rect(screen, COLOR_white, paddle_2_rect)
    
        #draw ball with white
        pygame.draw.rect(screen, COLOR_white, ball_rect)

        #update display
        pygame.display.update()

#Run the game
if __name__ == '__main__':
  main()