#--main.py--
import pygame
from settings import *
from support import *
from timer import Timer
from enemy import Player, Enemy

class Game:
    def __init__(self):
        #setup
        pygame.init()
        self.screen = pygame.display.set_mode((window_width,window_height))
        pygame.display.set_caption('Tester Battle')
        self.clock = pygame.time.Clock()
        self.running = True
        self.import_assets()
        #groups
        self.all_sprites = pygame.sprite.Group()

        #data
        player_list=['shaili', 'anqi', 'saee', 'twinkles', 'kami', 'charlie']
        self.player=[Player(name, self.back_surfs[name]) for name in player_list]
        self.player=self.player[0]
        self.all_sprites.add(self.player)
        enemy_name=choice(list(enemy_data.keys()))
        self.enemy=Enemy(enemy_name, self.front_surfs[enemy_name], self.all_sprites)

    def import_assets(self):
        self.back_surfs=folder_importer('..', 'images', 'back')
        self.front_surfs=folder_importer('..', 'images', 'front')
        self.bg_surfs=folder_importer('..', 'images', 'other')

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000 #60 fps cap
            #event loop 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #update
            self.all_sprites.update(dt)

            #draw
            self.screen.blit(self.bg_surfs['bg'], (0,0))
            self.all_sprites.draw(self.screen)
            pygame.display.update()

        pygame.quit()

        
if __name__ == '__main__':
    game = Game()
    game.run()


