import sys
import pygame
import pygame.image
from asteroidfield import *
from asteroid import *
from constants import *
from player import *
from shots import Shot


def set_background_opacity(screen, background_image, opacity):
    screen.fill("black")
    background_image.set_alpha(opacity * 255)
    screen.blit(background_image, (0, 0))


def main():
    print("Starting asteroids!")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load(
        'assets/background.png').convert_alpha()

    opacity = 0.5

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    opacity = min(1.0, opacity + 0.1)
                elif event.key == pygame.K_DOWN:
                    opacity = max(0.0, opacity - 0.1)

        for obj in updatable:
            obj.update(dt)

        set_background_opacity(screen, background_image, opacity)

        for asteroid in asteroids:
            if asteroid.collision(player) is True:
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collision(shot) is True:
                    shot.kill()
                    asteroid.split()

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
