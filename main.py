# this allows us to use code from
# the open-source pygame library
# throughout this file
#import pygame.sprite
import sys
import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import AsteroidField
from shot import Shot

def main():
    
        
        
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        
        Asteroid.containers = (asteroids,updatable,drawable)
        AsteroidField.containers = updatable
        asteroid_field = AsteroidField()  

        Shot.containers = (shots, updatable, drawable)

        Player.containers = (updatable,drawable)
        player1 = Player( SCREEN_WIDTH/2 , SCREEN_HEIGHT/2 )
        
       
        updatable.add(player1,asteroid_field)
        drawable.add(player1)
        
        
        dt = 0 


        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            updatable.update(dt)

            for asteroid in asteroids:
                if asteroid.collision_check(player1):
                    print("Game over!")
                    sys.exit()

            for asteroid in asteroids:
                 for shot in shots:
                      if asteroid.collision_check(shot):
                           asteroid.split() 
                           shot.kill()

            pygame.Surface.fill(screen,(0,0,0) )
            #screen.fill((0,0,0))

            for obj in drawable:
                
                obj.draw(screen)

            pygame.display.flip()
            #clock.tick(60)
            dt = clock.tick(60) / 1000
           
   
if __name__ == "__main__":
    main()
