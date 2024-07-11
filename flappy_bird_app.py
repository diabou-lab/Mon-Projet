import pygame
from application import Application
from game import Game

class FlappyBirdApp(Application):
    def __init__(self):
        pygame.init()
        self.game = Game()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.game.update()
            self.game.draw()
            pygame.display.flip()
            pygame.time.Clock().tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.bird.flap()

    def stop(self):
        self.running = False
        pygame.quit()