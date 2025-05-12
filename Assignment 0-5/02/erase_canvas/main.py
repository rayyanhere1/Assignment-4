import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
ERASER_COLOR = (200, 200, 200)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eraser on Canvas")
clock = pygame.time.Clock()

def draw_canvas():
    for y in range(0, HEIGHT, CELL_SIZE):
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE))

def main():
    eraser_active = False
    eraser_size = 40
    eraser_rect = pygame.Rect(0, 0, eraser_size, eraser_size)
    running = True
    while running:
        screen.fill(WHITE)
        draw_canvas()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        eraser_rect.topleft = (mouse_x - eraser_size // 2, mouse_y - eraser_size // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                eraser_active = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                eraser_active = False

        if eraser_active:
            for y in range(0, HEIGHT, CELL_SIZE):
                for x in range(0, WIDTH, CELL_SIZE):
                    cell_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                    if eraser_rect.colliderect(cell_rect):
                        pygame.draw.rect(screen, WHITE, cell_rect)

        pygame.draw.rect(screen, ERASER_COLOR, eraser_rect, 2)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
