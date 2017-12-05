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
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
redwool              35,14
blackwool            35,15
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
