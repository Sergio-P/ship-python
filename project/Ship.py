#Ship.py <- Game.py
#La clase de la nave, objeto manejado por usuario

import pygame
from Bullets import *

class Ship(pygame.sprite.Sprite):
	
	def __init__(self,x,y,parent,bullets):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("gpx/ship.png").convert_alpha()
		self.image.set_colorkey((0,0,0))
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.reload=0
		self.fire=False
		self.hp=5
		self.coins=0
		self.currentBul=0
		self.bulcost=["inf",100,4000,50]
		self.parent=parent
		self.bullets=bullets
		parent.add(self)

	def step(self,pos):
		self.rect.x=pos[0]/3
		self.rect.y=pos[1]-16
		
		if(self.reload>0):
			self.reload-=1

		if(self.fire and self.reload==0):
			self.attack(self.currentBul)
		
	def changeBul(self):
		self.currentBul+=1
		if(self.currentBul>3):
			self.currentBul=0

	def attack(self,cb):
		if(cb==0):
			b=NormalBullet(self.rect.x+32,self.rect.y+16,self.parent,self.bullets)
		elif(cb==1):
			b=RapidBullet(self.rect.x+32,self.rect.y+16,self.parent,self.bullets)
		elif(cb==2):
			b=MultiBullet(self.rect.x+32,self.rect.y+16,-1,self.parent,self.bullets)
			c=MultiBullet(self.rect.x+32,self.rect.y+16,0,self.parent,self.bullets)
			d=MultiBullet(self.rect.x+32,self.rect.y+16,1,self.parent,self.bullets)
		elif(cb==3):
			b=FireBullet(self.rect.x+32,self.rect.y+16,self.parent,self.bullets)
		self.reload=b.reload

	def hit(self,dam):
		self.hp-=dam
		if(self.hp<=0):
			self.delete()

	def delete(self):
		self.kill()


