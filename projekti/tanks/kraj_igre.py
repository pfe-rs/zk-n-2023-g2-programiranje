import pygame
import sys
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_HEIGHT=720
SCREEN_WIDTH=1280
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def game_over():
    font = pygame.font.Font(None, 64)


    game_over_text = font.render("Game Over", True, WHITE)
    restart_text = font.render("Press R to restart", True, WHITE)


    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50))
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))

    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_over = False


        screen.fill(BLACK)


        screen.blit(game_over_text, game_over_rect)
        screen.blit(restart_text, restart_rect)

        pygame.display.flip()