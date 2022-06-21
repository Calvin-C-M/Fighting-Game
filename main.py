import pygame
import Physics
import Color
import Maps
from Platform import Platform
from Character.Player import Player

pygame.init()

WIDTH,HEIGHT=1080,640
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fighting Game")
FPS=60

def update_game_window(
    sprites: pygame.sprite.Group,
    players: list,
    platforms: pygame.sprite.Group
) :
    WIN.fill(Color.BLACK)

    keys=pygame.key.get_pressed()

    for player in players :
        player.update(keys,platforms)

    for sprite in sprites :
        WIN.blit(sprite.surf,sprite.rect)

    pygame.display.update()

def main() :
    clock=pygame.time.Clock()
    running=True

    players=[
        Player((WIDTH-Player.WIDTH)/2,(HEIGHT-Player.HEIGHT)/2,{
            "JUMP" : pygame.K_w,
            "LEFT" : pygame.K_a,
            "RIGHT" : pygame.K_d
        }, Color.BLUE),
        Player((WIDTH-Player.WIDTH)/2,(HEIGHT-Player.HEIGHT)/2,{
            "JUMP" : pygame.K_i,
            "LEFT" : pygame.K_j,
            "RIGHT" : pygame.K_l
        }, Color.RED)
    ]

    platforms=Maps.original_map(WIDTH,HEIGHT)

    all_sprites=pygame.sprite.Group()
    for player in players :
        all_sprites.add(player)
    for platform in platforms :
        all_sprites.add(platform)

    while running :
        clock.tick(FPS)
        for evt in pygame.event.get() :
            if evt.type == pygame.QUIT :
                running=False

        update_game_window(all_sprites,players,platforms)

    return 0

main()