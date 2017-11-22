from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init(): 
    mc = Minecraft.create("10.183.13.13", 4711)
    x, y, z = mc.player.getPos()  
    return mc

def clear_with_air(mc, x, y, z):
	air = 0
	mc.setBlocks(x-50, y-10, z, x+60, y+50, z+50, 0)

def room(mc,x,y,z):
	redwool = 35,14
	air = 0
	glass = 102
	mc.setBlocks(x-2, y-1, z+22, x+2, y-4, z+26, redwool)
	mc.setBlocks(x-2, y-2, z+22, x+2, y-3, z+26, glass)
	#mc.setBlock(x, y-2, z+20, x, y-7, z+28, redwool)
	#mc.setBlocks(x-1, y-2, z+21, x+1, y-2, z+21, redwool)
	#mc.setBlocks(x-1, y-2, z+22, x+1, y-2, z+22, redwool)
	#mc.setBlocks(x-1, y-3, z+21, x+1, y-3, z+21, redwool)
	#mc.setBlocks(x-1, y-3, z+22, x+1, y-3, z+22, redwool)
	#empty room
	mc.setBlocks(x-1, y-2, z+2, x+1, y-3, z+25, air)
	

#main  
  
mc = init()
mc.player.setPos(0, 30, 0)
x, y, z = mc.player.getPos()  
#mc.player.setPos(x-30, y, z+30)
#clear_with_air(mc, x,y,z)
#boat(mc, x,y,z)
room(mc,x,y,z)
#fin_b(mc,x,y+2,z+50)
#fin_c(mc,x,y+5,z+50)
#bridge(mc,x,y+5,z+20)
#mc.player.setPos(-17,30, 20)
#sleep(2)
#mc.player.setPos(-5,21, -3)
#sleep(2)
#mc.player.setPos(-17,35,23)
#sleep(2)
#mc.player.setPos(0,35,23)
# multiple line comment
