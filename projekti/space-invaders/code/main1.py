import pygame, sys
from player import Player ##badaboi
import obstacle
from alien import Alien, Extra
from random import choice, randint ### Sto ovo... bira vanzemaljca
from laser import Laser



class Game:
    def __init__(self):
        ## BBBB BOI, PLEJER 
        player_sprite= Player((screen_width/2, 540), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        ##zivoti i skor bababoija
        self.lives = 3
        self.lives_surf = pygame.image.load('ssets/heart4.jpg').convert_alpha()
        self.live_x_start_pos = screen_width - (self.lives_surf.get_size()[0] * 2 + 20)
        self.score = 0
        self.font = pygame.font.Font('ssets/Pixeled.ttf',20)


        ##preprekeeeee ali ne iymedju nas, mryim eng tastaturu
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num*(screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(*self.obstacle_x_positions, x_start=40, y_start=380)

        #Vanyemuljci
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows = 4, cols = 6)
        self.alien_direction = 1 ##baj baj baterflaj odose desno,popravi kas
        self.alien_lasers = pygame.sprite.Group() ##specijalizovani vanzemuljski laseri
       
       
        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(400,800)

        #muzika za djuskanje
        music = pygame.mixer.Sound('ssets/mjuza.wav')
        music.set_volume(0.4)
        music.play(loops =- 1)
        self.laser_sound = pygame.mixer.Sound('ssets/laser.wav')
        self.laser_sound.set_volume(0.5)
        self.explotion_sound = pygame.mixer.Sound('ssets/kaboom.wav')
        self.explotion_sound.set_volume(0.3)
        


    def create_obstacle(self,x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
                for col_index, col in enumerate(row):
                    if col== 'X':
                        x = x_start + col_index * self.block_size + offset_x
                        y = y_start + row_index * self.block_size
                        block = obstacle.Block(self.block_size,(150, 225, 0),x,y)
                        self.blocks.add(block)
    
    def create_multiple_obstacles(self, *offset,x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def alien_setup(self, rows, cols, x_distance = 70 , y_distance = 48, x_offset = 100, y_offset = 50):
         for row_index, row in enumerate(range (rows)):
                for col_index, col in enumerate(range (cols)):
                        x = col_index * x_distance + x_offset
                        y  = row_index * y_distance + y_offset

                        if row_index == 0 : alien_sprite = Alien('yellow',x,y)
                        elif 1<= row_index <= 2: alien_sprite = Alien('red',x,y)
                        else: alien_sprite = Alien('green',x,y)
                        self.aliens.add(alien_sprite)  

    def alien_position_checker(self): ##da ne izlaze napolje
         all_aliens = self.aliens.sprites()
         for alien in all_aliens:
              if alien.rect.right >= screen_width:
                   self.alien_direction = -1
                   self.alien_move_down(2)
              elif alien.rect.left <= 0:
                   self.alien_direction = 1
                   self.alien_move_down(2)
         
    def alien_move_down(self, distance): ##silaze dole
         if self.aliens:
              for alien in self.aliens.sprites():
                   alien.rect.y += distance
  
    def alien_shoot(self):  ##ashooot
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center,6, screen_height)
            self.alien_lasers.add(laser_sprite)
            self.laser_sound.play()
    def extra_alien_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <=0:
            self.extra.add(Extra(choice(['right','left']),screen_width))
            self.extra_spawn_time = randint(400,800)
         
    def collision_checks(self):
        ##bababoi laser
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
              ###obstacle collisions
              if pygame.sprite.spritecollide(laser, self.blocks, True):  
                   laser.kill()
              
              ####vanzemuljac rip
              aliens_hit = pygame.sprite.spritecollide(laser, self.aliens, True)
              if aliens_hit:
                  for alien in aliens_hit:
                    self.score += alien.value
                    laser.kill()
                    self.explotion_sound.play()

              
                  
            
              ###extra bye bye
              if pygame.sprite.spritecollide(laser, self.extra, True):  
                   self.score += 500
                   laser.kill()   

        ### vanyemuljski laseri
        if self.alien_lasers:
            for laser in self.alien_lasers:

                if pygame.sprite.spritecollide(laser, self.blocks, True):  
                   laser.kill()
                if pygame.sprite.spritecollide(laser, self.player, False):  
                   laser.kill()
                   self.lives -= 1
                   if self.lives <= 0:
                       pygame.quit()
                       sys.exit()
        #### oooo i'm an aien, im a legal alien, i am an englishman in NYoooOOooork
        if self.aliens:
             for alien in self.aliens:
                  pygame.sprite.spritecollide(alien, self.blocks, True)
                 
                  if pygame.sprite.spritecollide(alien, self.player, False):  
                   pygame.quit()
                   sys.exit()

    def display_lives(self):

        for live in range(self.lives - 1):
            x = self.live_x_start_pos + (live* (self.lives_surf.get_size()[0] + 10))
            screen.blit(self.lives_surf,(x,550))              
 
    def display_score(self):
        score_surf = self.font.render(f'score: {self.score}', False, 'white')
        score_rect = score_surf.get_rect(topleft = (0,550))
        screen.blit(score_surf,score_rect)

    def victory_message(self):
        if not self.aliens.sprites():
            victory_surf = self.font.render('You won!', False, 'white')
            victory_rect = victory_surf.get_rect(center=(300, 310))
            screen.blit(victory_surf,victory_rect)


    def run(self):
        #rrradim na sebi, updajtovi
        self.player.update()
        self.extra.update()
        self.aliens.update(self.alien_direction)
        self.alien_position_checker()

        self.extra_alien_timer()
        self.alien_lasers.update()
        self.collision_checks()
        self.player.sprite.lasers.draw(screen) ##bababoi laseri

        self.display_lives()

        self.player.draw(screen)
        self.blocks.draw(screen) ##rasiri ves
        self.aliens.draw(screen)
        self.extra.draw(screen)
        self.alien_lasers.draw(screen)
        self.display_score()
        self.victory_message()




if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 620

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER,800)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == ALIENLASER:
                 game.alien_shoot()

        screen.fill((0,0,0))
        game.run()

        pygame.display.flip()
        clock.tick(60)
