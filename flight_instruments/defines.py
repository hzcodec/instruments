# ---------------------------------------------------------------------------------
# You only nedd to change these two parameters in order set the position
# of the instruments on the screen.
# ---------------------------------------------------------------------------------
X_SPEEDO_SPACE_BETWEEN_ALL_INSTRUMENTS = 50
Y_POS_FOR_ALL_INSTRUMENTS = 50
# ---------------------------------------------------------------------------------

# screen size
WIDTH  = 1400
HEIGHT = 600

# define colors
RED         = (255, 0, 0)
GREEN       = (0, 255, 0)
BLUE        = (0, 0, 255)
LIGHT_BLUE  = (0, 255, 255)
BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
STEEL       = (0, 100, 100)
GREY        = (85,85,85)
LIGHT_GREY  = (150,150,150)
BACKGR_GREY = (80,80,80)


#----------------------------------------------------------------------------------------------------------
# defines for speedo
#----------------------------------------------------------------------------------------------------------

NEEDLE_OFFSET_X = 40
NEEDLE_OFFSET_Y = 40

X_SPEED_DIAL_COORD   = X_SPEEDO_SPACE_BETWEEN_ALL_INSTRUMENTS 
Y_SPEED_DIAL_COORD   = Y_POS_FOR_ALL_INSTRUMENTS 
X_SPEED_NEEDLE_COORD_INSTR1 = X_SPEED_DIAL_COORD+180 
Y_SPEED_NEEDLE_COORD_INSTR1 = Y_SPEED_DIAL_COORD+180

#X_SPEEDO_DIAL_COORD_INSTR2   = X_SPEEDO_SPACE_BETWEEN_ALL_INSTRUMENTS*10
#Y_SPEEDO_DIAL_COORD_INSTR2   = Y_POS_FOR_ALL_INSTRUMENTS 
#X_SPEEDO_NEEDLE_COORD_INSTR2 = X_SPEEDO_DIAL_COORD_INSTR2+200 
#Y_SPEEDO_NEEDLE_COORD_INSTR2 = Y_SPEEDO_DIAL_COORD_INSTR2+200
#
#X_SPEEDO_DIAL_COORD_INSTR3   = X_SPEEDO_SPACE_BETWEEN_ALL_INSTRUMENTS*19 
#Y_SPEEDO_DIAL_COORD_INSTR3   = Y_POS_FOR_ALL_INSTRUMENTS 
#X_SPEEDO_NEEDLE_COORD_INSTR3 = X_SPEEDO_DIAL_COORD_INSTR3+200 
#Y_SPEEDO_NEEDLE_COORD_INSTR3 = Y_SPEEDO_DIAL_COORD_INSTR3+200

# composite pos
SPEEDO_DIAL_POS_INSTR1   = (X_SPEED_DIAL_COORD, Y_SPEED_DIAL_COORD)
SPEEDO_NEEDLE_POS_INSTR1 = (X_SPEED_NEEDLE_COORD_INSTR1, Y_SPEED_NEEDLE_COORD_INSTR1)
#SPEEDO_DIAL_POS_INSTR2   = (X_SPEEDO_DIAL_COORD_INSTR2,   Y_SPEEDO_DIAL_COORD_INSTR2)
#SPEEDO_NEEDLE_POS_INSTR2 = (X_SPEEDO_NEEDLE_COORD_INSTR2, Y_SPEEDO_NEEDLE_COORD_INSTR2)
#SPEEDO_DIAL_POS_INSTR3   = (X_SPEEDO_DIAL_COORD_INSTR3,   Y_SPEEDO_DIAL_COORD_INSTR3)
#SPEEDO_NEEDLE_POS_INSTR3 = (X_SPEEDO_NEEDLE_COORD_INSTR3, Y_SPEEDO_NEEDLE_COORD_INSTR3)

# instrument number
INSTRUMENT1 = 1
INSTRUMENT2 = 2
INSTRUMENT3 = 3
