import pygame
import Color
from Player import Player
from Platform import Platform

pygame.init()

WIDTH,HEIGHT=1080,640
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fight Game")

GRAV=9

def update_game_window(
    keys,
    player: Player,
    platforms: list()
) :
    WIN.fill(Color.BLACK)

    player.update(WIN,keys,GRAV,platforms)
    for platform in platforms :
        platform.update(WIN)

    pygame.display.flip()
    pygame.display.update()

def main() :
    clock=pygame.time.Clock()
    gameRunning=True

    player1SpawnPoint=((WIDTH-Player.WIDTH)/2,(HEIGHT-Player.HEIGHT)/2)

    player=Player(player1SpawnPoint[0],player1SpawnPoint[1])

    platforms=[
        Platform(50,500,1000,20),
        Platform(50,450,400,20),
    ]

    while(gameRunning) :
        clock.tick(60)
        for evt in pygame.event.get() :
            if evt.type == pygame.QUIT :
                gameRunning=False

        keys=pygame.key.get_pressed()
        
        update_game_window(keys,player,platforms)

main()