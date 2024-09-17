import sys
import pygame
import pygame.image
from asteroidfield import *
from asteroid import *
from constants import *
from game_state import GameState
import game_state
from player import *
from shots import Shot


def set_background_opacity(screen, background_image, opacity):
    # Scale the background image to fill the screen
    scaled_background = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    temp_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    temp_surface.fill((255, 255, 255, int(opacity * 255)))
    scaled_background.blit(temp_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    screen.blit(scaled_background, (0, 0))


def main():
    print("Starting asteroids!")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load(
        'assets/background.png').convert_alpha()

    opacity = 0.35  # Set initial opacity to 65%

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
    game_state = GameState.MENU
    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 96)
    blink_time = 0
    show_text = True

    def reset_game():
        player.reset(screen.get_width()/2, screen.get_height()/2)
        for asteroid in asteroids:
            asteroid.kill()
        asteroids.empty()
        for shot in shots:
            shot.kill()
        shots.empty()
        asteroid_field.reset()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    opacity = min(1.0, opacity + 0.1)
                elif event.key == pygame.K_DOWN:
                    opacity = max(0.0, opacity - 0.1)
                elif event.key == pygame.K_ESCAPE:
                    if game_state == GameState.PLAYING:
                        game_state = GameState.MENU
                    else:
                        sys.exit()
                elif event.key == pygame.K_RETURN:
                    if game_state == GameState.MENU:
                        reset_game()
                        game_state = GameState.PLAYING
                    elif game_state == GameState.GAME_OVER:
                        game_state = GameState.MENU

        screen.fill((0, 0, 0))  # Clear the screen before drawing the background
        set_background_opacity(screen, background_image, opacity)

        if game_state == GameState.PLAYING:
            for obj in updatable:
                obj.update(dt)

            for asteroid in asteroids:
                if asteroid.collision(player) is True:
                    game_state = GameState.GAME_OVER
                    break

                for shot in shots:
                    if asteroid.collision(shot) is True:
                        shot.kill()
                        asteroid.split()

            for obj in drawable:
                obj.draw(screen)

        elif game_state == GameState.MENU:
            title_text = title_font.render("ASTEROIDS", True, (255, 215, 0))
            screen.blit(title_text, (screen.get_width()/2 -
                        title_text.get_width()/2, screen.get_height()/2 - 100))

            blink_time += dt
            if blink_time >= 0.5:
                show_text = not show_text
                blink_time = 0

            if show_text:
                start_text = font.render(
                    "Press ENTER to start", True, (255, 255, 255))
                screen.blit(start_text, (screen.get_width()/2 -
                            start_text.get_width()/2, screen.get_height()/2 + 50))

        elif game_state == GameState.GAME_OVER:
            game_over_text = title_font.render(
                "GAME OVER", True, (255, 255, 255))
            screen.blit(game_over_text, (screen.get_width()/2 -
                        game_over_text.get_width()/2, screen.get_height()/2 - 50))

            blink_time += dt
            if blink_time >= 0.5:
                show_text = not show_text
                blink_time = 0

            if show_text:
                restart_text = font.render(
                    "Press ENTER to return to menu", True, (255, 255, 255))
                screen.blit(restart_text, (screen.get_width()/2 -
                                           restart_text.get_width()/2, screen.get_height()/2 + 50))

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
