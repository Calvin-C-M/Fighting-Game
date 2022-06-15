import pygame
import Color

class Player :
    WIDTH=50
    HEIGHT=50
    JUMP_HEIGHT=20
    VEL=5

    def __init__(self,x,y) :
        self.rect=pygame.Rect(x,y,self.WIDTH,self.WIDTH)

    def move(self,direction) :
        if direction=="RIGHT" :
            self.rect.move_ip(self.VEL,0)
        if direction=="LEFT" :
            self.rect.move_ip(-self.VEL,0)
        if direction=="JUMP" :
            self.rect.move_ip(0,-self.JUMP_HEIGHT)
        
    def update(self,win,keys,grav,ground) :
        # Key Events
        if keys[pygame.K_d] :
            self.move("RIGHT")
        if keys[pygame.K_a] :
            self.move("LEFT")

        # Gravity System
        if keys[pygame.K_w] :
            self.move("JUMP")
        else :
            # print(self.rect.collidelist(ground))
            if self.rect.collidelist(ground) < 0 :
                self.rect.move_ip(0,grav)
        
        pygame.draw.rect(win,Color.WHITE,self.rect)