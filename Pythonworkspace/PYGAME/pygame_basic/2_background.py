from turtle import back
import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width,screen_height)) # 튜플 형식 

# 화면 타이틀 설정
pygame.display.set_caption("Rrrre Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\이승미\\OneDrive\\바탕 화면\\Pythonworkspace\\pygame_basic\\background.png") # \\ = /

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
            
    # screen.fill((0,0,255)) # RGB 값으로 배경 그리기
    screen.blit(background, (0,0)) # 배경 그리기
    
    pygame.display.update() # 게임화면 다시 그리기 ! (반드시 해야함)

# pygame 종료
pygame.quit()