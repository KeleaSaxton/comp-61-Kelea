import pygame
import random
import time
from pygame import mixer

# Initialize Pygame
pygame.init()
mixer.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_img = pygame.image.load('background.jpg')
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

pygame.display.set_caption("Color Catcher")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 64)

def show_title_screen():
    screen.fill(BLACK)
    title_font = pygame.font.Font(None, 72)
    subtitle_font = pygame.font.Font(None, 36)

    title_text = title_font.render("COLOR CATCHER", True, WHITE)
    subtitle_text = subtitle_font.render("Press any key to start", True, (200, 200, 200))
    subtitle_text2 = subtitle_font.render("Catch red balls and move from blue balls", True, (200, 200, 200))
    

    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 200))
    screen.blit(subtitle_text, (WIDTH // 2 - subtitle_text.get_width() // 2, 300))
    screen.blit(subtitle_text2, (WIDTH // 2 - subtitle_text.get_width() // 1, 350))
    pygame.display.update()

    # Wait for keypress
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Sounds
catch_sound = mixer.Sound('catch.wav')
miss_sound = mixer.Sound('miss.wav')

# Background music
mixer.music.load('background.mp3')
mixer.music.set_volume(0.4)
mixer.music.play(-1)

# Game settings
player_width, player_height = 100, 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 40
player_speed = 7

score = 0
lives = 3
start_time = time.time()
game_duration = 5 * 60  # 5 minutes

# Falling shape settings
shapes = []
shape_speed = 4
shape_interval = 1500  # milliseconds
last_shape_time = pygame.time.get_ticks()

# Clock
clock = pygame.time.Clock()

# Function to create a new shape
def create_shape():
    shape = {
        'x': random.randint(20, WIDTH - 20),
        'y': -20,
        'color': random.choice([RED, BLUE]),  # RED = good, BLUE = bad
        'radius': 20
    }
    shapes.append(shape)

# Function to draw everything on screen
def draw_screen():
    # screen.fill(WHITE)
    screen.blit(background_img, (0, 0))

    
    # Draw player
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))

    # Draw shapes
    for shape in shapes:
        pygame.draw.circle(screen, shape['color'], (shape['x'], shape['y']), shape['radius'])

    # Draw score and timer
    elapsed = int(time.time() - start_time)
    time_left = max(0, game_duration - elapsed)
    timer_text = font.render(f"Time: {time_left}s", True, BLACK)
    score_text = font.render(f"Score: {score}", True, BLACK)
    lives_text = font.render(f"Lives: {lives}", True, BLACK)
    screen.blit(timer_text, (10, 10))
    screen.blit(score_text, (10, 40))
    screen.blit(lives_text, (10, 70))
    
    pygame.display.flip()

def show_game_over_screen(score):
    screen.fill(WHITE)
    game_over_text = large_font.render("Game Over", True, BLACK)
    score_text = font.render(f"Final Score: {score}", True, BLACK)
    restart_text = font.render("Click to Restart", True, (0, 100, 255))

    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 100))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 40))

    # Restart button
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 30, 200, 50)
    pygame.draw.rect(screen, (0, 100, 255), button_rect)
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 40))

    pygame.display.update()
    return button_rect

# Show the title screen before starting the game
show_title_screen()

# Game loop
running = True
while running:
    clock.tick(60)
    current_time = pygame.time.get_ticks()

    # Check for game end
    if time.time() - start_time >= game_duration or lives <= 0:
        screen.fill(WHITE)
        end_text = large_font.render("Game Over", True, BLACK)
        final_score = font.render(f"Final Score: {score}", True, BLACK)
        screen.blit(end_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        screen.blit(final_score, (WIDTH // 2 - 100, HEIGHT // 2 + 10))
        pygame.display.flip()
        pygame.time.wait(4000)
        break

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Create new shapes at interval
    if current_time - last_shape_time > shape_interval:
        create_shape()
        last_shape_time = current_time

    # Move and check collisions
    for shape in shapes[:]:
        shape['y'] += shape_speed
        if shape['y'] >= player_y:
            if player_x < shape['x'] < player_x + player_width:
                if shape['color'] == RED:
                    score += 1
                    catch_sound.play()
                else:
                    lives -= 1
                    miss_sound.play()
            shapes.remove(shape)
        elif shape['y'] > HEIGHT:
            shapes.remove(shape)
        elapsed = int(time.time() - start_time)

        # Gradually increase falling speed (caps at 12)
        if elapsed % 10 == 0 and shape_speed < 12:
            shape_speed = 4 + elapsed // 10

        # Gradually increase spawn rate (caps at 400ms)
        shape_interval = max(400, 1500 - (elapsed * 10))
        
        # Check for game end
        if time.time() - start_time >= game_duration or lives <= 0:
            restart_button = show_game_over_screen(score)
            waiting_for_restart = True

            while waiting_for_restart:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        waiting_for_restart = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            # Reset all variables
                            score = 0
                            lives = 3
                            start_time = time.time()
                            shapes.clear()
                            shape_speed = 4
                            shape_interval = 1500
                            last_shape_time = pygame.time.get_ticks()
                            player_x = WIDTH // 2 - player_width // 2
                            waiting_for_restart = False



    draw_screen()

pygame.quit()