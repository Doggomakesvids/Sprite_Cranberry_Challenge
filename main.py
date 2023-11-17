import pygame
import moviepy.editor as mp
from threading import Thread
from cryptography import fernet
BACKGROUND = pygame.image.load('background.jpeg')
BACKGROUND = pygame.transform.scale(BACKGROUND,(1280,720))
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.Font('cambriai.ttf', 112)
text = font.render('Sprite Cranberry', True, (0, 0, 0))
text2 = font.render('Press space to start', True, (0, 0, 0))
# key = fernet.Fernet.generate_key()
#     # string the key in a file
# with open('key.txt', 'wb') as filekey:
#     filekey.write(key)


    # opening the original file to encrypt
with open('key.txt', 'rb') as file:
    key = file.read()
    key = key.decode('utf-8')
# key = key.replace("b'", "")
# key = key.replace("'", "")
# print(key)
cipher = fernet.Fernet(key)
pygame_icon = pygame.image.load('icon.ico')
running = 0
score_file = open("highscore.txt", "r+")
score = 0
high_score = 0
video = mp.VideoFileClip("vid.mp4")
# def play_vid():
#     if event.type == pygame.QUIT:
#                 if high_score < score:
#                         score_file.seek(0)
#                         score_file.truncate(0)
                        
#                 score_file.close()
#                 pygame.quit()
#                 quit()
try:
    with open('highscore.txt', 'rb') as file:
        high_score = file.read()
        high_score = high_score.decode('utf-8')

    # print(high_score)
    high_score= cipher.decrypt(high_score)
    high_score = int(high_score)
    # print(high_score)
    score = int(high_score)
except:
    print("No high score, reseting")
    score_file.truncate(0)
    score_file.seek(0)
    score_file.write('gAAAAABlTThpb5PxuJx7F2b-DbkuC2-Ox91xZ-_lB08EcFPlG7BZsALWTUCPWKsU0WEpr2d6JL-4lD77vu5Bx8Qj38Z11FClOQ==')
    with open('highscore.txt', 'rb') as file:
        high_score = file.read()
        high_score = high_score.decode('utf-8')

    # print(high_score)
    high_score= cipher.decrypt(high_score)
    high_score = int(high_score)
    # print(high_score)
    score = int(high_score)
pygame.display.set_icon(pygame_icon)

textRect = text.get_rect()
textRect.center = (1280 // 2, 720 // 2)
textRect2 = text2.get_rect()
textRect2.center = (1280 // 2, 500)
pygame.display.set_caption('Sprite Cranberry')
pygame.display.flip()
screen.blit(BACKGROUND, (0, 0))
screen.blit(text, textRect)
screen.blit(text2, textRect2)
text3 = font.render(f'Score: {score}', True, (0, 0, 0))
screen.blit(text2, (0,0))
while True:
    CLOCK.tick(60)

    pygame.display.flip()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if running == 0:
                    running = 1
        if event.type == pygame.QUIT:
            with open('highscore.txt', 'r+') as file:
                file.seek(0)
                file.truncate(0)
                score = str(score)
                score = score.encode('utf-8')
                # print(score)
                encrypted_string = cipher.encrypt(score)
                encrypted_string = encrypted_string.decode('utf-8')
                file.write(encrypted_string)
                file.flush()
                file.close()

            pygame.quit()
            quit()
    if running == 0:
        pygame.display.flip()
        screen.blit(BACKGROUND, (0, 0))
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        score = str(score)
        score = score.replace("b'", "")
        score = score.replace("'", "")
        text3 = font.render(f'Score: {score}', True, (0, 0, 0))
        score = int(score)
        screen.blit(text3, (0,0))
    if running == 1:
        running = 2
        video.preview()
        # print(score)
        score = int(score)
        score += 1

        with open('highscore.txt', 'r+') as file:
            file.seek(0)
            file.truncate(0)
            score = str(score)
            score = score.encode('utf-8')
            # print(score)
            encrypted_string = cipher.encrypt(score)
            encrypted_string = encrypted_string.decode('utf-8')
            file.write(encrypted_string)
            file.flush()
            file.close()
        running = 0

            
            

            
                
                
    # if __name__ == '__main__':
    #     if x.is_alive == False:
    #         x.start()
    #     x.join()


