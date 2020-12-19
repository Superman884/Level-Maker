import pygame
from random import randrange
pygame.init()
win=pygame.display.set_mode((900,500))
moveleft=True
moveright=True
clock = pygame.time.Clock()
enemies_real=[]
dt=4
bouncedealy=0
j=0
lag=5
c=10
on=True
bouncy=False
friction=1.02
type1=1
delay=0
noprob=True
down=False
right_held=False
left_held=False
play_mode=False
orange=pygame.image.load("lava.png")
bg=[pygame.image.load("background- land.png"),pygame.image.load("background- space.png")]
right_img=pygame.image.load("right.png")
left_img=pygame.image.load("left.png")
slipright_img=pygame.image.load("slip right.png")
slipleft_img=pygame.image.load("slip left.png")
upright_img=pygame.image.load("jump right.png")
upleft_img=pygame.image.load("jump left.png")
right1_img=pygame.image.load("right 1.png")
right2_img=pygame.image.load("right 2.png")
right3_img=pygame.image.load("right 3.png")
left1_img=pygame.image.load("left 1.png")
left2_img=pygame.image.load("left 2.png")
left3_img=pygame.image.load("left 3.png")
right=True
left=False
bgnum=0
def reload():
	player1.momentum=0
	player1.vel=0
	for i in blocks_real:
		i.got=False
		i.hp=350
		blocks.append(i)
	player1.x=player1.startx
	player1.y=player1.starty
	player1.momentum=0
	player1.vel=0
class player:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.momentum=0.125
		self.vel=0
		self.width=20
		self.height=40
		self.startx=x
		self.starty=y
		self.ded=False
class block:
	def __init__(self,x,y,typenum):
		self.x=x
		self.y=y
		self.width=20
		self.height=20
		self.type=typenum
		self.hp=350
		self.got=False
onground=True
run=True
gravity=0.001
player1=player(50,250)
player1.momentum=0
enemies=[]
blocks=[]
blocks_real=[]
block_img1=pygame.image.load("block1.png")
block_img2=pygame.image.load("spike.png")
block_img3=pygame.image.load("ice.png")
block_img4=pygame.image.load("spring.png")
block_img5=pygame.image.load("grab.png")
block_img6=pygame.image.load("cloud.png")
while run:
	keys=pygame.key.get_pressed()
	if keys[pygame.K_RIGHT] and moveright and play_mode:
		right_held=True
		if onground:
			right=True
			left=False
		player1.momentum+=0.003
		player1.x+=0.00005
	if keys[pygame.K_LEFT] and moveleft and play_mode:
		left_held=True
		if onground:
			right=False
			left=True
		player1.momentum-=0.003
		player1.x-=0.00005
	if c%10==0:
		if onground:
			if right_held and player1.momentum<0:
				player_img=slipleft_img
			elif left_held and player1.momentum>0:
				player_img=slipright_img
			elif right_held and player1.momentum!=0:
				x=randrange(9)
				if x==0 or x==3 or x==6:
					player_img=right1_img
				if x==1 or x==4 or x==7:
					player_img=right2_img
				if x==2 or x==5 or x==8:
					player_img=right3_img
			elif left_held and player1.momentum!=0:
				x=randrange(9)
				if x==0 or x==3 or x==6:
					player_img=left1_img
				if x==1 or x==4 or x==7:
					player_img=left2_img
				if x==2 or x==5 or x==8:
					player_img=left3_img			
			elif right:
				player_img=right_img
			elif left:
				player_img=left_img

	mousex=pygame.mouse.get_pos()[0]-(pygame.mouse.get_pos()[0]%20)
	mousey=pygame.mouse.get_pos()[1]-(pygame.mouse.get_pos()[1]%20)
	if not play_mode:
		if type1==1:
				win.blit(block_img1,(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
		elif type1==2:
				win.blit(block_img2,(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
		elif type1==3:
				win.blit(block_img3,(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
		elif type1==4:
				win.blit(block_img4,(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
		elif type1==5:
				win.blit(block_img5,(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
		elif type1==6:
				win.blit(block_img6,(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
		elif type1==7:
				win.blit(pygame.image.load("man.png"),(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
		else:
			win.blit(player_img,(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
	if c%5:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False
			if event.type == pygame.MOUSEBUTTONDOWN and not play_mode:
				down=True
			elif event.type==pygame.MOUSEBUTTONUP:
				down=False
	if down:
		for i in blocks:
			if i.x//1==mousex//1 and i.y//1==mousey//1:
				noprob=False
		if noprob:
			if type1!=0 and type1!=7:
				blocks.append(block(mousex,mousey,type1))
				blocks_real.append(block(mousex,mousey,type1))
			elif type1==0:
				player1=player(mousex,mousey)
			else:
				if len(enemies_real)<=5:
					for u in enemies:
						if u.x//1==mousex//1 and u.y//1==mousey//1:
							noprob=False
					if noprob:
						enemies.append(player(mousex,mousey))
						enemies_real.append(player(mousex,mousey))

		noprob=True
	if play_mode:
		if keys[pygame.K_UP] and onground:
			player1.vel=-0.5
			player1.y-=1
			onground=False
			if right:
				player_img=upright_img
			elif left:
				player_img=upleft_img
	if keys[pygame.K_0]:
		type1=0
	if keys[pygame.K_1]:
		type1=1
	if keys[pygame.K_2]:
		type1=2
	if keys[pygame.K_3]:
		type1=3
	if keys[pygame.K_4]:
		type1=4
	if keys[pygame.K_5]:
		type1=5	
	if keys[pygame.K_6]:
		type1=6
	if keys[pygame.K_7] and len(enemies_real)!=5:
		type1=7
	if keys[pygame.K_n]:
		blocks=[]
		reload()
		play_mode=not play_mode
		enemies=[]
		for player2 in enemies_real:
			player2.x=player2.startx
			player2.y=player2.starty
			player2.ded=False
			enemies.append(player2)
	if keys[pygame.K_r] and delay==0 and not play_mode:
		bgnum+=1
		bgnum%=2
		delay=100
	for i in blocks:
		if i.got:
			i.hp-=1
		if i.hp==0:
			blocks.pop(blocks.index(i))
		i.y=i.y-(i.y%20)
		i.x=i.x-(i.x%20)
		if i.type==1:
			win.blit(block_img1,(i.x,i.y))
		elif i.type==2:
			win.blit(block_img2,(i.x,i.y))
		elif i.type==3:
			win.blit(block_img3,(i.x,i.y))
		elif i.type==4:
			win.blit(block_img4,(i.x,i.y))
		elif i.type==5:
			win.blit(block_img5,(i.x,i.y))
		elif i.type==6:
			win.blit(block_img6,(i.x,i.y))
		if play_mode:
			if i.type!=2 and i.type!=6:
				if player1.x-5<i.x and player1.x+25>i.x:
					if (player1.y+2<i.y and player1.y+38>i.y+20) or (player1.y-2<i.y and player1.y+38>i.y) or (player1.y-2>i.y and player1.y<i.y+18):
						moveright=False
						player1.momentum=0
						player1.x-=2
					else:
						moveright=True
				
				else:
					moveright=True
				for player2 in enemies:
					print(player2.vel)
					if (player2.x//1==i.x//1+20 or player2.x//1+20==i.x//1):
						if (player2.y<i.y+20 and player2.y+20>i.y+20) or (player2.y>i.y and player2.y<i.y+20) or (player2.y>i.y+7 and player2.y+7<i.y):
							player2.momentum*=-1
							player2.x+=player2.momentum*10
							player2.y-=1
					if (player2.x+3<=i.x and player2.x+17>=i.x) or (player2.x-3>=i.x and player2.x<i.x+17) or (player2.x-4<=i.x and player2.x+24>i.x+20):
						if player2.y<=i.y and player2.y+20>=i.y:
							player2.vel=0
				if (player1.x<=i.x and player1.x+20>=i.x) or (player1.x>=i.x and player1.x<i.x+20) or (player1.x-2<=i.x and player1.x+27>i.x+20):
					if (player1.y+2<i.y and player1.y+38>i.y+20) or (player1.y-2<i.y and player1.y+38>i.y) or (player1.y-2>i.y and player1.y<i.y+18):
						player1.momentum=0
						moveleft=False
						player1.x+=2
					else:
						moveleft=True
				else:
					moveleft=True
	
				if (player1.x+3<i.x and player1.x+17>i.x) or (player1.x-3>i.x and player1.x<i.x+17) or (player1.x-4<i.x and player1.x+24>i.x+20):
					if player1.y<i.y and player1.y+40>i.y:
						if i.type!=4:
							player1.vel=0
							player1.y=i.y-40
							on=True
							if i.type==3:
								friction=1.0004
							if i.type==5:
								i.got=True
						else:
							player1.vel=(player1.vel+0.05)*-0.88
					elif player1.y<=i.y+i.height and player1.y+40>i.y+i.height:
						player1.vel=0
						player1.y+=1
			if i.type==2:
				if (player1.x>=i.x and player1.x<=i.x+20) or (player1.x<=i.x and player1.x+20>=i.x):
					if (player1.y+40>=i.y and player1.y<=i.y):
						blocks=[]
						reload()
						for player2 in enemies:
							player2.x=player2.startx
							player2.y=player2.starty
			if i.type==6 and player1.vel>=0:
				if (player1.x+3<=i.x and player1.x+17>=i.x) or (player1.x-3>=i.x and player1.x<i.x+17) or (player1.x-4<=i.x and player1.x+24>i.x+20):
					if player1.y<=i.y and player1.y+40>=i.y:
						player1.vel=0
						on=True
	if on:
		onground=True
	else:
		onground=False
	on=False
	win.blit(player_img,(player1.x,player1.y))
	pygame.display.update()
	if player1.y<=420 and not onground and play_mode:
		player1.y+=player1.vel*dt
		player1.vel+=gravity*dt
	else:
		onground=True
	if player1.y>424:
		player1.y=424
	if play_mode:
		player1.x+=player1.momentum*dt
	if player1.momentum>=0.25:
		player1.momentum=0.25
	if player1.momentum<=-0.25:
		player1.momentum=-0.25
	player1.momentum/=friction
	friction=1.004
	if bouncy:
		if bouncedealy!=0:
			bouncedealy-=1
		else:
			player1.vel=-0.2
			player1.y-=10
			bouncy=False
	if c%3==0:
		win.blit(bg[bgnum],(0,0))
	c+=1
	right_held=False
	left_held=False
	if delay!=0:
		delay-=1
	hit=[]
	for player2 in enemies:
		if j<=240*dt:
			win.blit(pygame.image.load("man.png"),(player2.x,player2.y))
		else:
			win.blit(pygame.image.load("man 2.png"),(player2.x,player2.y))
		if play_mode:
			player2.x+=player2.momentum*dt
			player2.y+=player2.vel
			if player2.y<=440:
				player2.vel=1
			else:
				player2.vel=0
		j%=480*dt
		if play_mode:
			j+=1
			if (player1.x<=player2.x and player1.x+20>=player2.x) or (player1.x+20>=player2.x and player1.x+20<player2.x+20):
				if (player1.y<=player2.y and player1.y+40>=player2.y) or (player1.y+40>=player2.y and player1.y+40<=player2.y+20):
					if player1.vel>0 and not onground:
						hit.append(player2)
						break
					else:
						blocks=[]
						reload()
						enemies=[]
						for player2 in enemies_real:
							player2.x=player2.startx
							player2.y=player2.starty
							enemies.append(player2)
							player2.ded=False
				
	for o in hit:
		o.ded=True
		bouncedealy=9
		bouncy=True
		enemies.pop(enemies.index(o))
