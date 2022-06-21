from Character.Character import Character
import pygame
import Physics
import Color

class Player(Character) :
    def __init__(self,x,y,keyConfig:dict,color=Color.GREEN) :
        super().__init__(x,y)
        self.surf.fill(color)
        self.keyConfig=keyConfig

    def update(self,keys,platforms) :
        keyConfig={
            "JUMP" : keys[self.keyConfig["JUMP"]],
            "LEFT" : keys[self.keyConfig["LEFT"]],
            "RIGHT" : keys[self.keyConfig["RIGHT"]]
        }
        super().update(keyConfig,platforms)