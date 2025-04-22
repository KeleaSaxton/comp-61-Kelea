import pygame
import random
import time
from pygame import mixer

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Catchers")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.SysFont('Arial', 32)
large_font = pygame.font.SysFont('Arial', 64)

# Load assets
background_img = pygame.image.load('ExtraCredit2.0/background.jpg')
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Sounds
mixer.music.load('ExtraCredit2.0/background.mp3')
catch_sound = mixer.Sound('ExtraCredit2.0/catch.wav')
miss_sound = mixer.Sound('ExtraCredit2.0/miss.wav')

# Game Variables
player_width, player_height = 100, 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 8

shapes = []
shape_speed = 4
shape_interval = 1500  # milliseconds
last_shape_time = pygame.time.get_ticks()

score = 0
lives = 3
start_time = 0
game_duration = 300  # seconds

# Game States
MENU = "menu"
INSTRUCTIONS = "instructions"
SPLASH = "splash"
GAME = "game"
GAME_OVER = "game_over"
current_state = SPLASH

# Splash screen timer
splash_start_time = time.time()
ball_x = WIDTH // 2
ball_y = 0
ball_radius = 20
ball_speed = 4


def draw_text(text, size, x, y, color=BLACK):
    f = pygame.font.SysFont('Arial', size)
    render = f.render(text, True, color)
    screen.blit(render, (x - render.get_width() // 2, y))


def draw_button(text, x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, (0, 100, 255), rect)
    draw_text(text, 30, x + w // 2, y + 10, WHITE)
    if rect.collidepoint(mouse) and click[0] == 1:
        time.sleep(0.2)
        if action:
            action()


def start_game():
    global current_state, start_time, score, lives, shapes, last_shape_time, shape_speed
    current_state = GAME
    start_time = time.time()
    score = 0
    lives = 3
    shapes.clear()
    last_shape_time = pygame.time.get_ticks()
    shape_speed = 4
    mixer.music.play(-1)


def quit_game():
    pygame.quit()
    quit()


def show_instructions():
    global current_state
    current_state = INSTRUCTIONS


def show_menu():
    global current_state
    current_state = MENU


def spawn_shape():
    color = RED if random.random() > 0.3 else BLUE
    shapes.append({
        'x': random.randint(20, WIDTH - 20),
        'y': 0,
        'radius': 20,
        'color': color
    })


def draw_game():
    global player_x, shape_speed, last_shape_time
    screen.blit(background_img, (0, 0))

    # Handle shapes
    current_time = pygame.time.get_ticks()
    if current_time - last_shape_time > shape_interval:
        spawn_shape()
        last_shape_time = current_time

    for shape in shapes[:]:
        shape['y'] += shape_speed
        pygame.draw.circle(screen, shape['color'], (shape['x'], shape['y']), shape['radius'])
        if player_y < shape['y'] + shape['radius'] < player_y + player_height and player_x < shape['x'] < player_x + player_width:
            if shape['color'] == RED:
                global score
                score += 1
                catch_sound.play()
            else:
                global lives
                lives -= 1
                miss_sound.play()
            shapes.remove(shape)
        elif shape['y'] > HEIGHT:
            shapes.remove(shape)

    # Draw player
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))

    # HUD
    draw_text(f"Score: {score}", 24, 70, 10)
    draw_text(f"Lives: {lives}", 24, WIDTH - 70, 10)
    time_left = max(0, game_duration - int(time.time() - start_time))
    draw_text(f"Time: {time_left}", 24, WIDTH // 2, 10)


def draw_game_over():
    screen.fill(WHITE)
    draw_text("Game Over", 60, WIDTH // 2, 150)
    draw_text(f"Score: {score}", 40, WIDTH // 2, 230)
    draw_button("Retry", WIDTH // 2 - 100, 300, 200, 50, start_game)
    draw_button("Main Menu", WIDTH // 2 - 100, 370, 200, 50, show_menu)


def draw_splash():
    global ball_y
    screen.fill(WHITE)
    draw_text("Color Catchers", 60, WIDTH // 2, HEIGHT // 2 - 100)
    draw_text("By Kelea", 30, WIDTH // 2, HEIGHT // 2 - 30)
    draw_text("Loading...", 20, WIDTH // 2, HEIGHT // 2 + 40)

    pygame.draw.circle(screen, RED, (ball_x, int(ball_y)), ball_radius)
    ball_y += ball_speed
    if ball_y > HEIGHT:
        ball_y = -20


def draw_menu():
    screen.fill(WHITE)
    draw_text("Color Catchers", 60, WIDTH // 2, 100)
    draw_button("Start Game", WIDTH // 2 - 100, 220, 200, 50, start_game)
    draw_button("Instructions", WIDTH // 2 - 100, 290, 200, 50, show_instructions)
    draw_button("Quit", WIDTH // 2 - 100, 360, 200, 50, quit_game)


def draw_instructions():
    screen.fill(WHITE)
    draw_text("Instructions", 48, WIDTH // 2, 50)
    draw_text("Move with LEFT and RIGHT arrows", 28, WIDTH // 2, 130)
    draw_text("Catch RED circles to score", 28, WIDTH // 2, 180)
    draw_text("Avoid BLUE circles or lose lives", 28, WIDTH // 2, 230)
    draw_text("Survive for 5 minutes!", 28, WIDTH // 2, 280)
    draw_button("Back", WIDTH // 2 - 100, 400, 200, 50, show_menu)


# Main Loop
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if current_state == GAME:
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        player_x = max(0, min(WIDTH - player_width, player_x))

    if current_state == SPLASH:
        draw_splash()
        if time.time() - splash_start_time > 3:
            current_state = MENU

    elif current_state == MENU:
        draw_menu()

    elif current_state == INSTRUCTIONS:
        draw_instructions()

    elif current_state == GAME:
        draw_game()
        if lives <= 0 or time.time() - start_time >= game_duration:
            current_state = GAME_OVER
            mixer.music.stop()

    elif current_state == GAME_OVER:
        draw_game_over()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
