import pygame
from Platform import Platform

def original_map(width,height) -> pygame.sprite.Group :
    platforms=[
        Platform(x=width/2,y=500,width=1000,height=20),
        # Platform(x=70,y=450,width=400,height=20)
    ]

    maps=pygame.sprite.Group()
    for platform in platforms :
        maps.add(platform)

    return maps