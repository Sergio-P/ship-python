#UI.py <- Game.py
#Contiene los elementos de interfaz de usuario, los menus, y las barras que
# muestran la informacion

import pygame

class Simple(pygame.sprite.Sprite):
	def __init__(self,x,y,img,parent):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("gpx/"+img).convert()
		self.image.set_colorkey((0,0,0))
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		parent.add(self)

class GameBar:
	def __init__(self,screen,ship,enems,lv):
		self.screen=screen
		self.ship=ship
		self.enems=enems
		self.lv=lv
		#Creacion de elementos visuales
		self.drawable=pygame.sprite.Group()
		self.hpbar=[]
		i=0
		while i<=8:
			b=Simple(100+36*i,308,"hpbit.png",self.drawable)
			self.hpbar.append(b)
			i=i+1
		Simple(416,2,"enemsic.png",self.drawable)
		Simple(388,296,"coingoldhd.png",self.drawable)
		self.bulimg=Simple(12,308,"normalbul.png",self.drawable)
		self.fnt=pygame.font.SysFont("Berlin Sans FB",18)
		self.fntm=pygame.font.SysFont("Berlin Sans FB",16)

	def barUpdate(self):
		i=0
		while i<len(self.hpbar):
			self.hpbar[i].image.set_alpha(0)
			i=i+1
		i=1
		while i<=self.ship.hp:
			self.hpbar[i-1].image.set_alpha(255)
			i=i+1

	def draw(self,lvl):
		self.bulimg.image=pygame.image.load("gpx/"+self.buld(self.ship.currentBul,3)).convert()
		self.drawable.draw(self.screen)
		self.barUpdate()
		self.lvtxt=self.fnt.render("LEVEL "+str(lvl),1,(255,255,255))
		self.screen.blit(self.lvtxt,(4,2))
		self.enemtxt=self.enemtxt=self.fnt.render("x"+str(len(self.enems)),1,(255,255,255))
		self.screen.blit(self.enemtxt,(444,2))
		self.bultype=self.fntm.render(self.buld(self.ship.currentBul,1),1,self.buld(self.ship.currentBul,2))
		self.screen.blit(self.bultype,(8,288))
		self.bulcost=self.fnt.render("x "+str(self.ship.bulcost[self.ship.currentBul]),1,self.buld(self.ship.currentBul,2))
		self.screen.blit(self.bulcost,(32,300))
		self.hptxt=self.fntm.render("HP:",1,(13,198,32))
		self.screen.blit(self.hptxt,(104,288))
		self.cointxt=self.fnt.render(str(self.ship.coins),1,(255,204,0))
		self.screen.blit(self.cointxt,(416,298))
	
	def buld(self,cb,dat):
		if(cb==0):
			if dat==1: return "Basic"
			elif dat==2: return (13,198,32)
			elif dat==3: return "normalbul.png"
		elif(cb==1):
			if dat==1: return "Rapid"
			elif dat==2: return (180,12,234)
			elif dat==3: return "rapidbul.png"
		elif(cb==2):
			if dat==1: return "Multi"
			elif dat==2: return (32,78,214)
			elif dat==3: return "multibul.png"
		elif(cb==3):
			if dat==1: return "Fire"
			elif dat==2: return (235,65,14)
			elif dat==3: return "firebul.png"