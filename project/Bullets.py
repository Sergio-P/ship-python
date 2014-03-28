#Bullets.py <- Game.py
#Contiene las clases de balas que la nave dispara, y su clase generica

import pygame

#Clase general
class Bullet(pygame.sprite.Sprite):
	def __init__(self,x,y,vel,dam,reld,img,parent,grupo):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("gpx/"+img).convert_alpha()
		self.image.set_colorkey((0,0,0))
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.vel=vel
		self.dam=dam
		self.reload=reld
		parent.add(self)
		grupo.add(self)
	
	def step(self):
		self.rect.x+=self.vel
		if(self.rect.x>480):
			self.kill()

class NormalBullet(Bullet):
	def __init__(self,x,y,parent,grupo):
		Bullet.__init__(self,x,y,4,1,30,"normalbul.png",parent,grupo)

class RapidBullet(Bullet):
	def __init__(self,x,y,parent,grupo):
		Bullet.__init__(self,x,y,8,0.5,12,"rapidbul.png",parent,grupo)

class FireBullet(Bullet):
	def __init__(self,x,y,parent,grupo):
		Bullet.__init__(self,x,y,6,2,18,"firebul.png",parent,grupo)

class MultiBullet(Bullet):
	def __init__(self,x,y,direction,parent,grupo):
		Bullet.__init__(self,x,y,4,0.5,24,"multibul.png",parent,grupo)
		#Bullet.__init__(self,x,y,6,2,12,"multibul.png",parent,grupo) Arma Danny <3
		self.dir=direction
	def step(self):
		Bullet.step(self)
		self.rect.y+=2*self.dir
		if(self.rect.y<0 or self.rect.y>320):
			self.kill()

