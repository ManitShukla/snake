import pygame   
import time  
import random    
  
 
speed_of_snake = 10  
  
SCREEN_WIDTH = 700  
SCREEN_HEIGHT = 460  

your_low_score = pygame.Color(103, 11, 161)  
battleground = pygame.Color(52, 217, 63)  
YOU_DIED = pygame.Color(220, 20, 60)  
snaki_boi = pygame.Color(104, 74, 237)  
apple = pygame.Color(242, 68, 68)  
pygame.init() 
  
display_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
  
pygame.display.set_caption('SNAKE RUN 3000')  
   
game_clock = pygame.time.Clock()  
    
position_of_snake = [100, 50]  
  
body_of_snake = [  
    [100, 50],  
    [90, 50],  
    [80, 50],  
    [70, 50]  
    ]  
    
position_of_fruit = [  
    random.randrange(1, (SCREEN_WIDTH//10)) * 10,  
    random.randrange(1, (SCREEN_HEIGHT//10)) * 10  
    ]  
spawning_of_fruit = True  
 
initial_direction = 'RIGHT'  
snake_direction = initial_direction  
  
player_score = 0  

def display_score(selection, font_color, font_style, font_size):  
 
    score_font_style = pygame.font.SysFont(font_style, font_size)  
 
    score_surface = score_font_style.render('Your Score : ' + str(player_score), True, font_color)  
  
    score_rectangle = score_surface.get_rect()  
 
    display_screen.blit(score_surface, score_rectangle)  
 
def game_over():  
   
    game_over_font_style = pygame.font.SysFont('times new roman', 50)  
   
    game_over_surface = game_over_font_style.render(  
        'Your Score is : ' + str(player_score), True, YOU_DIED  
    )  
    
    game_over_rectangle = game_over_surface.get_rect()  
    
    game_over_rectangle.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT/4)  
   
    display_screen.blit(game_over_surface, game_over_rectangle)  
   
    pygame.display.flip()  
   
    time.sleep(2)  
   
    pygame.quit()  
   
    quit()  
    
game_run = True  
  
while game_run:  

    for event in pygame.event.get():  
 
        if event.type == pygame.QUIT:  
  
            game_run = False  

        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_UP:  
                snake_direction = 'UP'  
            if event.key == pygame.K_DOWN:  
                snake_direction = 'DOWN'  
            if event.key == pygame.K_LEFT:  
                snake_direction = 'LEFT'  
            if event.key == pygame.K_RIGHT:  
                snake_direction = 'RIGHT'  

    if snake_direction == 'UP' and initial_direction != 'DOWN':  
        initial_direction = 'UP'  
    if snake_direction == 'DOWN' and initial_direction != 'UP':  
        initial_direction = 'DOWN'   
    if snake_direction == 'LEFT' and initial_direction != 'RIGHT':  
        initial_direction = 'LEFT'   
    if snake_direction == 'RIGHT' and initial_direction != 'LEFT':  
        initial_direction = 'RIGHT'  
   
    if initial_direction == 'UP':  
        position_of_snake[1] -= 10  
    if initial_direction == 'DOWN':  
        position_of_snake[1] += 10  
    if initial_direction == 'LEFT':  
        position_of_snake[0] -= 10  
    if initial_direction == 'RIGHT':  
        position_of_snake[0] += 10  
 
    body_of_snake.insert(0, list(position_of_snake))  
    if position_of_snake[0] == position_of_fruit[0] and position_of_snake[1] == position_of_fruit[1]:  
        player_score += 1  
        spawning_of_fruit = False  
    else:  
        body_of_snake.pop()  

    if not spawning_of_fruit:  
        position_of_fruit = [  
            random.randrange(1, (SCREEN_WIDTH//10)) * 10,  
            random.randrange(1, (SCREEN_HEIGHT//10)) * 10  
        ]  
    spawning_of_fruit = True  
   
    display_screen.fill(battleground)  
   
    for position in body_of_snake:  
        pygame.draw.rect(display_screen, snaki_boi, pygame.Rect(position[0], position[1], 10, 10))  
        pygame.draw.rect(display_screen, apple, pygame.Rect(position_of_fruit[0], position_of_fruit[1], 10, 10))  
   
    if position_of_snake[0] < 0 or position_of_snake[0] > SCREEN_WIDTH - 10:  
        game_over()  
    if position_of_snake[1] < 0 or position_of_snake[1] > SCREEN_HEIGHT - 10:  
        game_over()      
   
    for block in body_of_snake[1:]:  
        if position_of_snake[0] == block[0] and position_of_snake[1] == block[1]:  
            game_over  
    
    display_score(1, your_low_score, 'times new roman', 20)  
   
    pygame.display.update()  
    
    game_clock.tick(speed_of_snake)  
   
pygame.quit()  
