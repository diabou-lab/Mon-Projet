import pygame
from bird import Bird
from pipe import Pipe

class Game:
    def __init__(self):
        self.width = 400
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Flappy Bird")
        
        self.background = pygame.image.load("assets/background.png").convert()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        
        self.bird = Bird(self.width // 4, self.height // 2)
        self.pipes = [Pipe(self.width, self.height)]
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        
    def update(self):
        self.bird.update()
        self.manage_pipes()
        self.check_collisions()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.bird.draw(self.screen)
        for pipe in self.pipes:
            pipe.draw(self.screen)
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def manage_pipes(self):
        if self.pipes[-1].x < self.width - 200:
            self.pipes.append(Pipe(self.width, self.height))
        self.pipes = [pipe for pipe in self.pipes if pipe.x + pipe.width > 0]
        for pipe in self.pipes:
            pipe.update()
            if not pipe.passed and pipe.x + pipe.width < self.bird.x:
                pipe.passed = True
                self.score += 1

    def check_collisions(self):
        for pipe in self.pipes:
            if pipe.collides_with(self.bird):
                self.reset_game()
        if self.bird.y >= self.height or self.bird.y <= 0:
            self.reset_game()

    def reset_game(self):
        self.bird = Bird(self.width // 4, self.height // 2)
        self.pipes = [Pipe(self.width, self.height)]
        self.score = 0