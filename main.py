import pygame
import moviepy.editor as mp
from threading import Thread
BACKGROUND = pygame.image.load('background.jpeg')
BACKGROUND = pygame.transform.scale(BACKGROUND,(1280,720))
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.Font('cambriai.ttf', 112)
text = font.render('Sprite Cranberry', True, (0, 0, 0))
text2 = font.render('Press space to start', True, (0, 0, 0))
pygame_icon = pygame.image.load('icon.ico')
running = False
score_file = open("highscore.txt", "r+")
score = 0
high_score = 0
video = mp.VideoFileClip("vid.mp4")
def play_vid():
    print("test3")
    video.preview()
    print("test4")
try:
    high_score = int(score_file.readline().strip())
except:
    print("No high score, reseting")
    score_file.truncate(0)
    score_file.seek(0)
    score_file.write(str(0))
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
while True:
    CLOCK.tick(60)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = True
    while running:
        if __name__ == "__main__":
            x = Thread(target=play_vid)
            x.start()
        if x.is_alive:
            if event.type == pygame.QUIT:
                x.raise_exception()
                running = False
                if high_score < score:
                    score_file.seek(0)
                    score_file.truncate(0)
                    score_file.write(str(high_score))
                score_file.close()
                pygame.quit()
                quit()
        else:
            score += 2
            if high_score > score:
                score_file.seek(0)
                score_file.truncate(0)
                score_file.write(str(high_score))
                    
                    
        if event.type == pygame.QUIT:
                running = False
                if high_score < score:
                        score_file.seek(0)
                        score_file.truncate(0)
                        score_file.write(str(high_score))
                score_file.close()
                pygame.quit()
                quit()



