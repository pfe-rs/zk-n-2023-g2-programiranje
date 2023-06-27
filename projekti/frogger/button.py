import pygame 

class Button:
    def __init__(self, x, y, width, height, text, boja_text, pozadina):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.boja_text = boja_text
        self.pozadina = pozadina
    
    #crtanje dugmeta
    def draw(self, screen):
        pygame.init()
        pygame.draw.rect(screen, self.pozadina, self.rect)
        font = pygame.font.Font(None, 32)
        text_surface = font.render(self.text, True, self.boja_text)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    #provera da li je dugme kliknuto
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
