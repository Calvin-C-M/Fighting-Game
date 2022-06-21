import pygame
import Color
import Physics

class Character(pygame.sprite.Sprite) :
    WIDTH=50
    HEIGHT=50
    JUMP_HEIGHT=10

    def __init__(self,x,y) :
        super().__init__()
        self.surf=pygame.Surface((self.WIDTH,self.HEIGHT))
        self.rect=self.surf.get_rect()

        self.pos=pygame.math.Vector2((x,y))
        self.acc=pygame.math.Vector2((0,0))
        self.vel=pygame.math.Vector2((0,0))

        self.health=100

    def jump(self,hits) :
        if hits :
            self.vel.y = -self.JUMP_HEIGHT

    def update(self,keyCom,platforms) :
        self.acc=pygame.math.Vector2((0,0.5))
        hits=pygame.sprite.spritecollide(self,platforms,False)

        # Key Movements
        if keyCom["LEFT"] :
            self.acc.x = -Physics.ACC
        if keyCom["RIGHT"] :
            self.acc.x = Physics.ACC
        if keyCom["JUMP"] :
            self.jump(hits)

        # Update player's physics
        self.acc.x += self.vel.x * Physics.FRIC
        self.vel += self.acc
        self.pos += self.vel+Physics.ACC*self.acc

        if self.vel.y > 0 :
            if hits :
                self.pos.y=hits[0].rect.top+1
                self.vel.y=0

        self.rect.midbottom=self.pos # Update player position