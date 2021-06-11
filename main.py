import pygame

pygame.init()
# definiowanie okna gry
win = pygame.display.set_mode((500, 500))
# wyświetlenie okna gry
pygame.display.set_caption("Moja Gra")

run = True

while run:
    # obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    # warunki do zmiany pozycji obiektu
    if keys[pygame.K_ESCAPE]:
        run = False

    pygame.time.delay(50)
