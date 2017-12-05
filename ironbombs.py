from mcpi.minecraft import Minecraft
from mcpi import block    
from time import sleep
from random import randint

def init(): 
    #mc = Minecraft.create("10.183.0.11", 4711)
    mc = Minecraft.create("10.183.13.13", 4711)
    x, y, z = mc.player.getPos()  
    return mc

def makepoles(mc,x,y,z):
	for n in range(0,20):
		mc.setBlock(x, y+n,z,42,n%16)
		mc.setBlock(x-1, y+n,z,42,n%16)
		mc.setBlock(x+1, y+n,z,42,n%16)
		mc.setBlock(x, y+n,z-1,42,n%16)
		mc.setBlock(x, y+n,z+1,42,n%16)
		if n > 15:
			mc.setBlock(x-2, y+n,z,42,n%16)
			mc.setBlock(x+2, y+n,z,42,n%16)

def main():
        mc = init()
        x, y, z = mc.player.getPos()  
        count = 0
        while count < 1000:
                x1 = randint(-100,100)
                y1 = randint(0,100)
                z1 = randint(-100,100)
                h = randint(3,15)
                makepoles(mc,x1,y1,z1)
                count = count + 1

main()
