# Importing necessary Python Library :
import pygame, sys, time, random, os

pygame.init()
pygame.mixer.init()

# Creating Window
screen_width = 800
screen_height = 580
gameWindow = pygame.display.set_mode((screen_width, screen_height))
icon = pygame.image.load('Artwork/icon.png')
pygame.display.set_icon(icon)
# Background Image adding
startbg = pygame.image.load("Artwork/intro.jpg")
startbg = pygame.transform.scale(startbg, (screen_width, screen_height)).convert_alpha()
logoimg = pygame.image.load('Artwork/intro.png')
logoimg = pygame.transform.scale(logoimg, (100, 40))
clicksound = pygame.mixer.music.load('Audio/click.wav')

# Colours ( on RGB colours)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
gray = (128, 128, 128)
darkgray = (50, 50, 50)
blue = (0, 0, 255)
darkgreen = (60, 130, 50)
green = (0, 255, 0)
greenyellow = (173, 255, 47)
yellow = (255, 255, 0)
darkyellow = (255, 150, 0)
orange = (255, 145, 0)

flag = 0

# Game Title
pygame.display.set_caption("Classic Snake Game")
pygame.display.update()

clock = pygame.time.Clock()

def startgame():                                                                                                          # Defining "startgame" as a Function for startgame screen
    exit_game = False
    while not exit_game:
        gameWindow.blit(startbg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    quitgame()
        button('START', ((screen_width // 2) - 50), (screen_height // 2) + 30, 100, 50, black, darkyellow, difficulty)
        button('QUIT', ((screen_width // 2) - 50), (screen_height // 2) + 100, 100, 50, black, red, quitgame)

        button('START', ((screen_width // 2) - 48), (screen_height // 2) + 32, 96, 46, white, yellow, difficulty)
        button('QUIT', ((screen_width // 2) - 48), (screen_height // 2) + 102, 96, 46, white, orange, quitgame)

        pygame.display.update()
        clock.tick(30)

def button(text, x, y, w, h, inactive_color, active_color, command=None):
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > pos[0] > x and y + h > pos[1] > y:
        pygame.draw.rect(gameWindow, active_color, (x, y, w, h))
        if click[0] == 1 and command != None:
            pygame.mixer.music.load('Audio/click.wav')
            pygame.mixer.music.play()
            command()
    else:
        pygame.draw.rect(gameWindow, inactive_color, (x, y, w, h))

    button_text = pygame.font.SysFont('Adobe Gothic Std B', 27, bold=0)
    button_win = button_text.render(text, True, black)
    button_rect = button_win.get_rect()
    button_rect.center = ((x + (w // 2)), (y + (h // 2)))
    gameWindow.blit(button_win, button_rect)

def quitgame():
    pygame.quit()

def difficulty():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        difficulty_font = pygame.font.SysFont('BahnSchrift', 35)
        difficulty_win = difficulty_font.render('CHOOSE DIFFICULTY LEVEL', True, black)
        difficulty_rect = difficulty_win.get_rect()
        difficulty_rect.center = (screen_width // 2, screen_height // 4)
        gameWindow.fill(white)
        gameWindow.blit(difficulty_win, difficulty_rect)

        difficulty_button('Beginner', (screen_width // 15), (screen_height // 2) - 50, 100, 50, black, black, 10, 1)
        difficulty_button('Intermediate', ((screen_width // 2) - 50), (screen_height // 2) - 50, 100, 50, black,
                          black, 25, 3)
        difficulty_button('Professional', (screen_width - (screen_width // 15) - 100), (screen_height // 2) - 50, 100,
                          50, black, black, 60, gameloop)

        difficulty_button('Beginner', (screen_width // 15) + 2, (screen_height // 2) - 48, 96, 46, (255, 255, 100),
                          yellow, 10, 1)
        difficulty_button('Intermediate', ((screen_width // 2) - 48), (screen_height // 2) - 48, 96, 46,
                          (255, 200, 0), yellow, 25, 3)
        difficulty_button('Professional', (screen_width - (screen_width // 15) - 98), (screen_height // 2) - 48, 96,
                          46, (255, 0, 0), yellow, 60, gameloop)

        pygame.display.update()

def difficulty_button(text, x, y, w, h, inactive_color, active_color, fps, command=None):
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(gameWindow, inactive_color, (x, y, w, h))
    if x + w > pos[0] > x and y + h > pos[1] > y:
        pygame.draw.rect(gameWindow, active_color, (x, y, w, h))
        if click[0] == 1 and command != None:
            clicksound = pygame.mixer.music.play()
            gameloop(fps)
    else:
        pygame.draw.rect(gameWindow, inactive_color, (x, y, w, h))

    difficultybutton_text = pygame.font.SysFont('Adobe Gothic STD B', 23)
    difficultybutton_win = difficultybutton_text.render(text, True, black)
    difficultybutton_rect = difficultybutton_win.get_rect()
    difficultybutton_rect.center = ((x + (w // 2)), (y + (h // 2)))
    gameWindow.blit(difficultybutton_win, difficultybutton_rect)

def gameloop(fps):                                                                                                      # Defining "gameloop(fps)" as a Function for main game screen

    # Game sepcific variables
    exit_game = False
    snake_x = 300
    snake_y = 200
    food_x = random.randrange( 4, (screen_width -4 )// 10) * 10
    food_y = random.randrange( 6, (screen_height -4) //10) * 10
    score = 0
    direction = 'R'
    change_to = direction
    velocity = 10
    snake_pos = [snake_x, snake_y]
    snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]
    food_pos = [food_x, food_y]
    food_spawn = True

    # Checking & Linking or Making "Highscore.txt" file :
    if (not os.path.exists("Highscore.txt")):                                                                           # Checking "Highscore.txt" exist or not
        with open("Highscore.txt", "w") as f:                                                                           # If not found , it will makea new file
            f.write("0")
    with open("Highscore.txt", 'r') as f:                                                                               # If found , it will read the file
        highscore = f.read()

    def GameOver():
        # gameoversound = pygame.mixer.music.load('Audio/gameover.mp3')
        GameOver_font = pygame.font.SysFont('Verdana', 90, bold=0)
        GameOver_win = GameOver_font.render('YOU DIED', True, red)
        GameOver_rect = GameOver_win.get_rect()
        GameOver_rect.midtop = (screen_width/2, screen_height/10)
        gameWindow.fill(black)
        pygame.draw.rect(gameWindow, white, (10, 40, 780, 530))
        gameWindow.blit(GameOver_win, GameOver_rect)
        show_score(0, darkgreen, 'BahnSchrift', 30)
        show_highscore(0, darkgray, 'BahnSchrift', 30)
        difficulty_button('Play Again', screen_width/2 - 75, screen_height/2 + 50, 150, 50, black, darkyellow, difficulty)
        button('QUIT', screen_width/2 - 75, screen_height/2 + 125, 150, 50, black, red, quitgame)

        button('Play Again', screen_width/2 - 73, screen_height/2 + 52, 146, 46, white, yellow, difficulty)
        button('QUIT', screen_width/2 - 73, screen_height/2 + 127, 146, 46, white, orange, quitgame)
        # gameoversound = pygame.mixer.music.load('Audio/gameover.mp3')
        # pygame.mixer.music.play()
        pygame.display.flip()

        with open("Highscore.txt", "w") as f:                                                                           # When game over , highscore will update in "Highscore.txt" file
            f.write(str(highscore))
        pygame.display.flip()

    def show_score(choice, color, font, size):                                                                          # Defining "show_score" as a Functionfor showing score
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (screen_width/ 8, 6)
        else:
            score_rect.midtop = (screen_width // 2,  screen_height/3)
        gameWindow.blit(score_surface, score_rect)

    def show_highscore(choice, color, font, size):                                                                      # Defining "show_highscore" as a Functionfor showing high-score
        highscore_font = pygame.font.SysFont(font, size)
        highscore_surface = highscore_font.render('HighScore : ' + str(highscore), True, color)
        highscore_rect = highscore_surface.get_rect()
        if choice == 1:
            highscore_rect.midtop = (screen_width - screen_width/5.5, 6)
        else:
            highscore_rect.midtop = (screen_width // 2, screen_height / 2.25)
        gameWindow.blit(highscore_surface, highscore_rect)


    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    change_to = 'U'
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    change_to = 'D'
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    change_to = 'L'
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    change_to = 'R'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        if change_to == 'U' and direction != 'D':
            direction = 'U'
        if change_to == 'D' and direction != 'U':
            direction = 'D'
        if change_to == 'L' and direction != 'R':
            direction = 'L'
        if change_to == 'R' and direction != 'L':
            direction = 'R'

        if direction == 'U':
            snake_pos[1] -= velocity
        if direction == 'D':
            snake_pos[1] += velocity
        if direction == 'L':
            snake_pos[0] -= velocity
        if direction == 'R':
            snake_pos[0] += velocity

        snake_body.insert(0, list(snake_pos))
        if abs(snake_pos[0] - food_pos[0]) < 5 and abs(snake_pos[1] - food_pos[1]) < 5 :
            score = score + 10
            food_spawn = False
#            pygame.mixer.music.load("Audio/beep.mp3")                                          #Showing Error !
#            pygame.mixer.music.play()
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange( 4, (screen_width -4 )// 10) * 10, random.randrange( 6, (screen_height -4) //10) * 10]
        food_spawn = True

        gameWindow.fill(black)
        gameWindow.blit(logoimg, (350, 1))

        pygame.draw.rect(gameWindow, white, (10, 40, 780, 530))
        
        for pos in snake_body:
            pygame.draw.rect(gameWindow, darkgreen, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(gameWindow, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        if score > int(highscore):
            highscore = score
        show_score(1, white, 'Constantia', 30)
        show_highscore(1, white, 'Constantia', 30)

        if snake_pos[0] < 10 or snake_pos[0] > screen_width - 20:
            flag = 1
            GameOver()
        if snake_pos[1] < 40 or snake_pos[1] > screen_height - 20:
            flag = 1
            GameOver()
        for head in snake_body[1:]:
            if snake_pos[0] == head[0] and snake_pos[1] == head[1]:
                flag = 1
                GameOver()

        pygame.display.update()
        clock.tick(fps)
    if flag != 0:
        pygame.mixer.music.load('Audio/gameover.mp3')
        pygame.mixer.music.play()
    pygame.quit()
startgame()                                                                                                               # Calling "start" function