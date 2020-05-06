import pygame, sys
# from pygame.rect import Rect
import start, stage, sound
from start import *
from stage import *


g = start.game()

def menu(screen): 
    sound.intro_music(0.3)
    
    image = pygame.transform.scale(pygame.image.load("resources/images/screen_images/backscreen.png"), (1000, 736)).convert_alpha()
    screen.blit(image, (0, 0))
    
    start_button = pygame.transform.scale(pygame.image.load("resources/images/button_images/start_button.png"), (200, 45)).convert_alpha()
    start_rect = start_button.get_rect(x = 145, y = 580)
    help_button = pygame.transform.scale(pygame.image.load("resources/images/button_images/help_button.png"), (143, 50)).convert_alpha()
    help_rect = help_button.get_rect(x = 428, y = 577)
    close_button = pygame.transform.scale(pygame.image.load("resources/images/button_images/close_button.png"), (175, 45)).convert_alpha()
    close_rect = close_button.get_rect(x = 670, y = 582)


    screen.blit(start_button, start_rect)
    screen.blit(help_button, help_rect)
    screen.blit(close_button, close_rect)

    pygame.display.flip()


    running = True
    while running:
        for event in pygame.event.get():
            if start_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 1
            if help_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    help_screen(screen)
            if close_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    return 0

def help_screen(screen):

    image = pygame.transform.scale(pygame.image.load("resources/images/screen_images/helpscreen.png"), (1000, 736)).convert_alpha()
    
    screen.blit(image, (0, 0))
    
    goback_button =  pygame.transform.scale(pygame.image.load("resources/images/button_images/goback_button.png"), (175, 45)).convert_alpha()
    goback_rect = goback_button.get_rect(x = 100, y = 600)
    screen.blit(goback_button, goback_rect)

    pygame.display.flip()
    
    running = True
    while running:
        for event in pygame.event.get():
            if goback_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu(screen)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def complete(screen):
    sound.complete_music(0.3)

    image = pygame.transform.scale(pygame.image.load("resources/images/screen_images/complete.png"), (1000, 736)).convert_alpha() #1000,667
    screen.blit(image, (0, 0))

    continue_button = pygame.transform.scale(pygame.image.load("resources/images/button_images/continue_button.png"), (210, 48)).convert_alpha()
    continue_rect = continue_button.get_rect(x = 730, y = 50)
    
    screen.blit(continue_button, continue_rect)

    pygame.display.flip()
    
    running = True
    while running:
        for event in pygame.event.get():
            if continue_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # g.play(screen, stage.stage1())
                    return 1
                    pass
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def gameover(screen):
    sound.gameover_music(0.3)

    image = pygame.image.load("resources/images/screen_images/gameover.png")
    screen.blit(image, (0, 0))
    sound.gameover_music(0.3)
    continue_button = pygame.transform.scale(pygame.image.load("resources/images/button_images/continue_button.png"), (210, 48)).convert_alpha()
    continue_rect = continue_button.get_rect(x = 730, y = 520)

    screen.blit(continue_button, continue_rect)

    
    pygame.display.flip()
    
    running = True
    while running:
        for event in pygame.event.get():
            if continue_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # restart option
                    return 1
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
