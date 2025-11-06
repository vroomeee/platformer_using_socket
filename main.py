import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Boilerplate")

clock = pygame.time.Clock()
FPS = 60

player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos[1] -= player_speed
    # if keys[pygame.K_s]:
    #     player_pos[1] += player_speed
    # if keys[pygame.K_a]:
    #     player_pos[0] -= player_speed
    # if keys[pygame.K_d]:
    #     player_pos[0] += player_speed

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (200, 50, 50), (*player_pos, 40, 40))

    pygame.display.flip()
    clock.tick(FPS)
