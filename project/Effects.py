#Effects.py <- Game.py
#[Opcional] Contiene efectos de background y foreground usados en la
# ejecucicion del juego pero que no afectan al funcionamiento del juego

import pygame
import random

class Star(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([2,2])
		self.image.fill(self.colorSwatch())
		self.rect=self.image.get_rect()
		self.rect.x=random.randint(0,480)
		self.rect.y=random.randint(0,480)
		self.setVel()

	def step(self):
		if self.delay==0:
			self.rect.x-=self.vel
			self.delay=self.maxdelay
		else:
			self.delay-=1
		if(self.rect.x<=0):
			self.rect.x=480
			self.rect.y=random.randint(0,480)
			self.setVel()

	def setVel(self):
		self.vel=random.random()*1.3
		if(self.vel>1):
			self.vel=2
			self.maxdelay=0
			self.delay=0
		else:
			self.vel=1
			self.maxdelay=random.randint(0,5)
			self.delay=0

	def colorSwatch(self):
		a=random.randint(1,4)
		if(a==1): return (255,255,255)
		elif(a==2): return (255,255,160)
		elif(a==3): return (255,160,255)
		elif(a==4): return (160,255,255)

class MultiStar():
	def __init__(self,parent):
		i=0
		self.sts=pygame.sprite.Group()
		while i<=50:
			i=i+1
			s=Star()
			self.sts.add(s)
			parent.add(s)
	def step(self):
		for s in self.sts:
			s.step()
