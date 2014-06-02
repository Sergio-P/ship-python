#  ------   SPACE CLEAR   ------   #
# Sergio Penafiel - 2013

import pygame
import random
from Ship import Ship
from Bullets import *
from Enemigos import *
from Effects import *
from UI import *

pygame.init()
pygame.display.set_caption("Space Clear")
print "Space Clear Loading..."

screen = pygame.display.set_mode((480,320))
clock=pygame.time.Clock()

pygame.display.set_icon(pygame.image.load("gpx/ship.png").convert())

stage=pygame.sprite.Group()
stagebg=pygame.sprite.Group()
bullets=pygame.sprite.Group()
enems=pygame.sprite.Group()
enemBuls=pygame.sprite.Group()
coins=pygame.sprite.Group()
bg=MultiStar(stagebg)
nave=Ship(20,50,stage,bullets)
level=1
last=False
sld=[] #SpaceClear Levels Data
stageMenu=GameBar(screen,nave,enems,level)

pygame.mouse.set_visible(False)

def loadAllLevelsData(ruta):
	global sld
	sld=[]
	a=open(ruta)
	c=0
	for line in a:
		if line[0:-1]=="L"+str(c+1)+":":
			c+=1
		else:
			a=[]
			a.append(c)
			a.append(line[0:-1])
			sld.append(a)
	return sld

loadAllLevelsData("levels.sld")

class Controller():
	def __init__(self):
		self.i=0

	def step(self):
		global level
		if len(enems)<2:
			if sld[self.i+1][0]==level:
				self.i+=1
				self.nextWave()
			else:
				last=True
		if len(enems)==0 and last:
			print "Level UP! \nStrarting Level "+str(level+1)
			#interLevels()
			level+=1
			self.i+=1
			last=False

	def nextWave(self):
		enl=sld[self.i][1].split("-")
		for en in enl:
			if en=="MS":
				e=Meteor(stage,enems)
			elif en=="MM":
				e=MeteorM(stage,enems)
			elif en=="MG":
				e=MeteorG(stage,enems)
			elif en=="OC":
				e=OscillatorSimple(stage,enems)
			elif en=="OS":
				e=OscillatorShooter(stage,enems,enemBuls)
			elif en=="SL":
				e=LinearShooter(stage,enems,enemBuls)
			elif en=="US":
				e=UltraShooter(stage,enems,enemBuls)
			e.cs=coins

def interLevels():
	menu=True
	pygame.mouse.set_visible(True)
	while menu:
		for event in pygame.event.get():
			if(event.type==pygame.QUIT):
				menu=False
			elif(event.type==pygame.MOUSEBUTTONDOWN):
				a=pygame.mouse.get_pos()
				if a[0]>400 and a[1]>300:
					menu=False

		screen.fill((0,0,0))
		pygame.display.flip()
		clock.tick(60)

	pygame.mouse.set_visible(False)
	return


cx=Controller()
playing=True
print "Space Clear! \nStarting Level 1"
#Prueba nuevos enemigos aqui :D
#UltraShooter(stage,enems,enemBuls)

while playing and nave.alive():

	#EVENT phase
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			playing=False
		elif(event.type==pygame.MOUSEBUTTONDOWN):
			nave.fire=True
		elif(event.type==pygame.MOUSEBUTTONUP):
			nave.fire=False
		elif(event.type==pygame.KEYDOWN):
			if(event.key==pygame.K_z):
				nave.changeBul()
	

	#STEP phase
	cx.step()

	for enem in enems:
		enem.step()

	for bul in enemBuls:
		bul.step()

	for coin in coins:
		coin.step()
		coin.ship=nave

	nave.step(pygame.mouse.get_pos())
	bg.step()


	#COLLISION phase
	for bullet in bullets:
		bullet.step()
		hitEnems=pygame.sprite.spritecollide(bullet,enems,False)
		for enem in hitEnems:
			enem.hit(bullet.dam)
			bullet.kill()
			break

	hitEnems=pygame.sprite.spritecollide(nave,enems,False)
	for enem in hitEnems:
		nave.hit(enem.fisDam)
		enem.kill()
		break

	hitEnemBul=pygame.sprite.spritecollide(nave,enemBuls,False)
	for bul in hitEnemBul:
		nave.hit(bul.dam)
		bul.kill()
		break

	#DRAW phase
	screen.fill((0,0,0))
	stagebg.draw(screen)
	stage.draw(screen)
	stageMenu.draw(level)
	pygame.display.flip()

	#TIME phase
	clock.tick(60)

print "Game Over"
pygame.quit()