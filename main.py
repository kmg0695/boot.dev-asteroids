import pygame

import asteroidfield
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        for player in updatable:
            player.update(dt)
            asteroidfield.update(dt)
        for player in drawable:
            player.draw(screen)
        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta / 1000


if __name__ == "__main__":
    main()
