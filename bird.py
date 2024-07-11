import pygame

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gravity = 0.6
        self.lift = -15
        self.velocity = 0
        
        self.image = pygame.image.load("assets/bird.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (34, 24))
        
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.velocity += self.gravity
        self.velocity *= 0.9
        self.y += self.velocity
        self.rect.centery = self.y
        if self.y > 580:
            self.y = 580
            self.velocity = 0
        if self.y < 0:
            self.y = 0
            self.velocity = 0

    def flap(self):
        self.velocity += self.lift

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)