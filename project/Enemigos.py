#Enemigos.py <- Game.py
#Contiene las clases de todos los enemigos y balas enemigas del juego 
# y sus clases generales que las heredan

import pygame
import random

#Clase general
class Enemigo(pygame.sprite.Sprite):
	def __init__(self,x,y,hp,fisDam,cost,img,parent,enems):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("gpx/"+img).convert_alpha()
		self.image.set_colorkey((0,0,0))
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.hp=hp
		self.cost=cost
		self.fisDam=fisDam
		self.parent=parent
		parent.add(self)
		enems.add(self)

	def hit(self,dam):
		self.hp-=dam
		if(self.hp<=0):
			self.delete()

	def delete(self):
		self.createCoins()
		self.kill()

	def createCoins(self):
		global coins
		e=int(self.cost*0.15)+1
		a=random.randint(self.cost-e,self.cost+e)
		while a>20:
			Coin(self.rect.x+random.randint(0,48),self.rect.y+random.randint(0,self.rect.height),"gold",self.parent,self.cs)
			a-=20
		while a>5:
			Coin(self.rect.x+random.randint(0,48),self.rect.y+random.randint(0,self.rect.height),"silver",self.parent,self.cs)
			a-=5
		while a>1:
			Coin(self.rect.x+random.randint(0,48),self.rect.y+random.randint(0,self.rect.height),"bronze",self.parent,self.cs)
			a-=1
		return

	def replace(self):
		self.rect.y=random.randint(20,300)
		self.rect.x=480+random.randint(0,600)

#Clase General
class EnemBullet(pygame.sprite.Sprite):
	def __init__(self,x,y,velx,vely,dam,img,parent,enembuls):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("gpx/"+img).convert_alpha()
		self.image.set_colorkey((0,0,0))
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.velx=velx
		self.vely=vely
		self.dam=dam
		parent.add(self)
		enembuls.add(self)

	def step(self):
		self.rect.x-=self.velx
		self.rect.y+=self.vely
		if(self.rect.x<0):
			self.delete()

	def delete(self):
		self.kill()

#Adicional Clase Coin
class Coin(pygame.sprite.Sprite):
	def __init__(self,x,y,tipo,parent,coingr):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("gpx/coin"+tipo+".png").convert_alpha()
		self.image.set_colorkey((0,0,0))
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.vely=(320-y)/45+1
		self.velx=(460-x)/45
		if tipo=="gold":
			self.value=200
		elif tipo=="silver":
			self.value=50
		else:
			self.value=10
		parent.add(self)
		coingr.add(self)

	def step(self):
		self.rect.x+=self.velx
		self.rect.y+=self.vely
		if(self.rect.y>320):
			self.ship.coins+=self.value
			self.kill()



class Meteor(Enemigo):
	def __init__(self,parent,enems):
		Enemigo.__init__(self,480+random.randint(0,600),random.randint(20,300),1,1,2,"meteor.png",parent,enems)
		self.velx=3
		self.vely=random.randint(0,4)-2

	def step(self):
		self.rect.x-=self.velx
		self.rect.y+=self.vely
		if(self.rect.x<-24):
			self.replace()
		if(self.rect.y>300 or self.rect.y<5):
			self.vely*=-1
		if(random.random()<0.01):
			self.evol()

	def evol(self):
		self.image=pygame.image.load("gpx/meteorfire.png").convert()
		self.velx=7

class MeteorM(Enemigo):
	def __init__(self,parent,enems):
		Enemigo.__init__(self,480+random.randint(0,600),random.randint(20,280),1,1,2,"meteorm.png",parent,enems)
		self.parent=parent
		self.enems=enems
		self.velx=3
		self.vely=random.randint(0,4)-2

	def step(self):
		self.rect.x-=self.velx
		self.rect.y+=self.vely
		if(self.rect.x<-24):
			self.replace()
		if(self.rect.y>300 or self.rect.y<5):
			self.vely*=-1

	def delete(self):
		Enemigo.createCoins(self)
		a=Meteor(self.parent,self.enems)
		a.rect.y=self.rect.y-4
		a.rect.x=self.rect.x+16
		a.vely=-2
		a.cs=self.cs
		b=Meteor(self.parent,self.enems)
		b.rect.y=self.rect.y+28
		b.rect.x=self.rect.x+16
		b.vely=2
		b.cs=self.cs
		self.kill()


class MeteorG(Enemigo):
	def __init__(self,parent,enems):
		Enemigo.__init__(self,480+random.randint(0,600),random.randint(20,280),1,1,4,"meteorg.png",parent,enems)
		self.parent=parent
		self.enems=enems
		self.velx=2
		self.vely=random.randint(0,2)-1

	def step(self):
		self.rect.x-=self.velx
		self.rect.y+=self.vely
		if(self.rect.x<-24):
			self.replace()
		if(self.rect.y>300 or self.rect.y<5):
			self.vely*=-1

	def delete(self):
		Enemigo.createCoins(self)
		a=MeteorM(self.parent,self.enems)
		a.rect.y=self.rect.y-4
		a.rect.x=self.rect.x+16
		a.vely=-2
		a.cs=self.cs
		b=MeteorM(self.parent,self.enems)
		b.rect.y=self.rect.y+28
		b.rect.x=self.rect.x+16
		b.vely=2
		b.cs=self.cs
		self.kill()


class LinearEnemBul(EnemBullet):
	#(self,x,y,velx,vely,img,parent,enembuls)
	def __init__(self,x,y,parent,enembuls):
		EnemBullet.__init__(self,x,y,6,0,1,"linearenembul.png",parent,enembuls)


class OscillatorSimple(Enemigo):
	def __init__(self,parent,enems):
		Enemigo.__init__(self,480+random.randint(0,600),random.randint(20,280),1,1,2,"oscillator.png",parent,enems)
		self.velx=3
		self.vely=1
		self.dir=1

	def step(self):
		self.rect.x-=self.velx
		self.rect.y+=self.vely
		if(self.rect.x<-24):
			self.replace()
		if(self.vely<-3 or self.vely>3):
			self.dir*=-1
		self.vely+=self.dir*0.25
	

class OscillatorShooter(Enemigo):
	def __init__(self,parent,enems,enembuls):
		Enemigo.__init__(self,480+random.randint(0,600),random.randint(20,280),1,1,5,"oscillatorshooter.png",parent,enems)
		self.velx=3
		self.vely=1
		self.dir=1
		self.parent=parent
		self.enembuls=enembuls

	def step(self):
		self.rect.x-=self.velx
		self.rect.y+=self.vely
		if(self.rect.x<-24):
			self.replace()
		if(self.vely<-3 or self.vely>3):
			self.dir*=-1
		self.vely+=self.dir*0.25
		if(random.random()<0.01):
			self.shoot()

	def shoot(self):
		LinearEnemBul(self.rect.x,self.rect.y+4,self.parent,self.enembuls)

class LinearShooter(Enemigo):
	def __init__(self,parent,enems,enembuls):
		Enemigo.__init__(self,480+random.randint(0,600),random.randint(20,280),1,1,5,"linearshooter.png",parent,enems)
		self.velx=3
		self.parent=parent
		self.enembuls=enembuls

	def step(self):
		self.rect.x-=self.velx
		if(self.rect.x<-24):
			self.replace()
		if(random.random()<0.015):
			self.shoot()

	def shoot(self):
		LinearEnemBul(self.rect.x,self.rect.y+4,self.parent,self.enembuls)

class UltraShooter(Enemigo):
	def __init__(self,parent,enems,enembuls):
		Enemigo.__init__(self,480+random.randint(0,600),random.randint(20,280),2,1,9,"ultrashooter.png",parent,enems)
		self.velx=4
		self.parent=parent
		self.enembuls=enembuls

	def step(self):
		self.rect.x-=self.velx
		if(self.rect.x<-24):
			self.replace()
		if(random.random()<0.025):
			self.shoot()

	def shoot(self):
		LinearEnemBul(self.rect.x,self.rect.y+4,self.parent,self.enembuls)


class EstrellaAsesina(Enemigo):
	def __init__(self,parent,enems):
		Enemigo.__init__(self,300,96,10,8,32,"estrellasesina.png",parent,enems)
		self.direction=1

	def step(self):
		self.rect.y+=self.direction
		if(self.rect.y<10):
			self.direction*=-1
		elif(self.rect.y>182):
			self.direction*=-1
		


