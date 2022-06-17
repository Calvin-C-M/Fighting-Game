import pygame
import Physics
import Color
from Platform import Platform
from Player import Player

pygame.init()

WIDTH,HEIGHT=1080,640
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fighting Game")
FPS=60

def update_game_window(
    sprites: pygame.sprite.Group,
    player: Player
) :
    WIN.fill(Color.BLACK)

    keys=pygame.key.get_pressed()

    player.update(keys)

    for sprite in sprites :
        WIN.blit(sprite.surf,sprite.rect)

    pygame.display.update()

def main() :
    clock=pygame.time.Clock()
    running=True

    player=Player((WIDTH-Player.WIDTH)/2,(HEIGHT-Player.HEIGHT)/2)
    platform=Platform(x=50,y=500,width=1000,height=20)

    all_sprites=pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(platform)

    while running :
        clock.tick(FPS)
        for evt in pygame.event.get() :
            if evt.type == pygame.QUIT :
                running=False

        update_game_window(all_sprites,player)

    return 0

main()