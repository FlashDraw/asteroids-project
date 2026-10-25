import sys
import pygame
from asteroidfield import AsteroidField
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    clock = pygame.time.Clock()
    run = True
    dt = 0.0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, drawable, updatable)

    meteor = AsteroidField()
    ship = Player(x,y)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt=clock.tick(FPS)/1000
        updatable.update(dt)
        screen.fill("black")

        for asteroid in asteroids:
            if asteroid.collides_with(ship):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for pellet in shots:
                if asteroid.collides_with(pellet):
                    log_event("asteroid_shot")
                    asteroid.split()
                    pellet.kill()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()




if __name__ == "__main__":
    main()
