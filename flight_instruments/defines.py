#----------------------------------------------------------------------------------------------------------
# You only nedd to change these parameters
#----------------------------------------------------------------------------------------------------------
X_SPACE_BETWEEN_ALL_INSTRUMENTS = 40
SIZE_OF_INSTRUMENT_1            = (400, 400)
SIZE_OF_INSTRUMENT_2            = (300, 300)
Y_POS_FOR_ALL_INSTRUMENTS       = 20
SPEED_OF_NEEDLE                 = 1.0


#----------------------------------------------------------------------------------------------------------
# screen size and screen origo
#----------------------------------------------------------------------------------------------------------
WIDTH        = 1400
HEIGHT       = 600
SCREEN_ORIGO = (0,0)
WINDOW_POS   = 10,30    # position of window,upper left corner
WINDOW_STYLE = 0        # no flag is set
COLOR_DEPTH  = 32


#----------------------------------------------------------------------------------------------------------
# define colors
#----------------------------------------------------------------------------------------------------------
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
# Frames per second
#----------------------------------------------------------------------------------------------------------
FPS = 60


#----------------------------------------------------------------------------------------------------------
# misc defines for flight instruments
#----------------------------------------------------------------------------------------------------------
NEEDLE_OFFSET_X = 60
NEEDLE_OFFSET_Y = 60

X_SPEED_DIAL_COORD = X_SPACE_BETWEEN_ALL_INSTRUMENTS 
Y_SPEED_DIAL_COORD = Y_POS_FOR_ALL_INSTRUMENTS 
X_SPEED_NEEDLE_COORD_INSTR1 = X_SPEED_DIAL_COORD+SIZE_OF_INSTRUMENT_1[0]/2 
Y_SPEED_NEEDLE_COORD_INSTR1 = Y_SPEED_DIAL_COORD+SIZE_OF_INSTRUMENT_1[1]/2

X_SPEED_DIAL_COORD_INSTR2   = X_SPACE_BETWEEN_ALL_INSTRUMENTS*10
Y_SPEED_DIAL_COORD_INSTR2   = Y_POS_FOR_ALL_INSTRUMENTS 
X_SPEED_NEEDLE_COORD_INSTR2 = X_SPEED_DIAL_COORD_INSTR2+SIZE_OF_INSTRUMENT_2[0]/2 
Y_SPEED_NEEDLE_COORD_INSTR2 = Y_SPEED_DIAL_COORD_INSTR2+SIZE_OF_INSTRUMENT_2[0]/2

#X_SPEEDO_DIAL_COORD_INSTR3   = X_SPACE_BETWEEN_ALL_INSTRUMENTS*19 
#Y_SPEEDO_DIAL_COORD_INSTR3   = Y_POS_FOR_ALL_INSTRUMENTS 
#X_SPEEDO_NEEDLE_COORD_INSTR3 = X_SPEEDO_DIAL_COORD_INSTR3+200 
#Y_SPEEDO_NEEDLE_COORD_INSTR3 = Y_SPEEDO_DIAL_COORD_INSTR3+200

# composite pos
SPEEDO_DIAL_POS_INSTR1   = (X_SPEED_DIAL_COORD, Y_SPEED_DIAL_COORD)
SPEEDO_NEEDLE_POS_INSTR1 = (X_SPEED_NEEDLE_COORD_INSTR1, Y_SPEED_NEEDLE_COORD_INSTR1)
SPEEDO_DIAL_POS_INSTR2   = (X_SPEED_DIAL_COORD_INSTR2,   Y_SPEED_DIAL_COORD_INSTR2)
SPEEDO_NEEDLE_POS_INSTR2 = (X_SPEED_NEEDLE_COORD_INSTR2, Y_SPEED_NEEDLE_COORD_INSTR2)
#SPEEDO_DIAL_POS_INSTR3   = (X_SPEEDO_DIAL_COORD_INSTR3,   Y_SPEEDO_DIAL_COORD_INSTR3)
#SPEEDO_NEEDLE_POS_INSTR3 = (X_SPEEDO_NEEDLE_COORD_INSTR3, Y_SPEEDO_NEEDLE_COORD_INSTR3)

