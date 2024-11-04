import pygame
screen = pygame.display.set_mode((1100, 800))
pygame.display.set_caption("Draw circle")
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            col = (85, 170, 255)
            pygame.draw.circle(
                screen, col, pos, 20, 5
            )
            pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()