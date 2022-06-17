from re import L
import pygame
import Color
import Physics

class Player(pygame.sprite.Sprite) :
    WIDTH=50
    HEIGHT=50

    def __init__(self,x,y) :
        super().__init__()
        self.surf=pygame.Surface((self.WIDTH,self.HEIGHT))
        self.surf.fill(Color.GREEN)
        self.rect=self.surf.get_rect()

        self.pos=pygame.math.Vector2((x,y))
        self.acc=pygame.math.Vector2((0,0))
        self.vel=pygame.math.Vector2((0,0))

    def move(self,direction) :
        if direction=="LEFT" :
            self.acc.x = -Physics.ACC
        if direction=="RIGHT" :
            self.acc.x = Physics.ACC

    def update(self,keys) :
        self.acc=pygame.math.Vector2((0,0))

        # Key Movements
        if keys[pygame.K_a] :
            self.move("LEFT")
        if keys[pygame.K_d] :
            self.move("RIGHT")

        # Update player's physics
        self.acc.x += self.vel.x * Physics.FRIC
        self.vel += self.acc
        self.pos += self.vel+Physics.ACC*self.acc

        self.rect.midbottom=self.pos # Update player position