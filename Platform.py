import pygame
import Color

class Platform(pygame.sprite.Sprite) :
    def __init__(self,x,y,width,height) :
        super().__init__()
        self.surf=pygame.Surface((width,height))
        self.surf.fill(Color.WHITE)
        self.rect=self.surf.get_rect()

        # self.pos=pygame.math.Vector2((x,y))
        self.rect.midbottom=(x,y)