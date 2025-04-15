import pygame
import random
import math
import time
from pygame import mixer

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders - Extended")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('background.png')
mixer.music.load('background.wav')
mixer.music.play(-1)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
player_lives = 3

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = 'ready'

# Score and font
score_value = 0
high_score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over font
over_font = pygame.font.Font('freesansbold.ttf', 64)
restart_font = pygame.font.Font('freesansbold.ttf', 32)

# Timer
start_time = time.time()

# Enemy setup
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
enemy_speed = 4
MAX_ENEMIES = 20

def spawn_enemies(num):
    for _ in range(num):
        enemyImg.append(pygame.image.load('enemy.png'))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(enemy_speed)
        enemyY_change.append(40)

spawn_enemies(num_of_enemies)

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    return distance < 27

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_high_score():
    high = font.render("High Score : " + str(high_score), True, (255, 215, 0))
    screen.blit(high, (10, 50))

def show_lives():
    lives = font.render("Lives : " + str(player_lives), True, (255, 0, 0))
    screen.blit(lives, (650, 10))

def show_timer():
    elapsed = int(time.time() - start_time)
    timer = font.render(f"Time : {elapsed}s", True, (255, 255, 255))
    screen.blit(timer, (350, 10))

def game_over_text():
    over = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over, (200, 250))
    restart = restart_font.render("Press R to Restart", True, (255, 255, 255))
    screen.blit(restart, (250, 320))

# Game loop
running = True
game_over = False
last_spawn_time = time.time()

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == 'ready':
                bullet_sound = mixer.Sound('laser.wav')
                bullet_sound.play()
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
            if event.key == pygame.K_r and game_over:
                # Restart logic
                player_lives = 3
                score_value = 0
                start_time = time.time()
                last_spawn_time = time.time()
                enemyImg.clear()
                enemyX.clear()
                enemyY.clear()
                enemyX_change.clear()
                enemyY_change.clear()
                spawn_enemies(num_of_enemies)
                bulletY = 480
                bullet_state = 'ready'
                game_over = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    if not game_over:
        playerX += playerX_change
        playerX = max(0, min(playerX, 736))

        if bulletY <= 0:
            bulletY = 480
            bullet_state = 'ready'

        if bullet_state == 'fire':
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        for i in range(len(enemyX)):
            if enemyY[i] > 440:
                player_lives -= 1
                enemyY[i] = random.randint(50, 150)
                if player_lives <= 0:
                    for j in range(len(enemyY)):
                        enemyY[j] = 2000
                    game_over = True
                    break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = abs(enemy_speed)
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -abs(enemy_speed)
                enemyY[i] += enemyY_change[i]

            if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
                explosion_sound = mixer.Sound('explosion.wav')
                explosion_sound.play()
                bulletY = 480
                bullet_state = 'ready'
                score_value += 1
                if score_value > high_score:
                    high_score = score_value
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        # Limit enemy spawning
        if time.time() - last_spawn_time > 30 and len(enemyX) < MAX_ENEMIES:
            spawn_enemies(1)
            last_spawn_time = time.time()

        player(playerX, playerY)
        show_score(textX, textY)
        show_high_score()
        show_lives()
        show_timer()

    else:
        game_over_text()

    pygame.display.update()
