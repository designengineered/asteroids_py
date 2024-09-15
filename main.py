import sys
import pygame
from asteroidfield import *
from asteroid import *
from constants import *
from player import *
from shots import Shot


def main():
    print("Starting asteroids!")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # FPS Assignment
    clock = pygame.time.Clock()

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH)/2, (SCREEN_HEIGHT)/2)

    Shot.containers = (shots, updatable, drawable)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        screen.fill("black")
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collision(shot) == True:
                    shot.kill()
                    asteroid.kill()

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
