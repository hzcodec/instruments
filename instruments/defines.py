# ---------------------------------------------------------------------------------
# You only nedd to change these two parameters in order set the position
# of the instruments on the screen.
# ---------------------------------------------------------------------------------
X_SPACE_BETWEEN_ALL_INSTRUMENTS = 50
Y_POS_FOR_ALL_INSTRUMENTS       = 50
# ---------------------------------------------------------------------------------

# screen size
WIDTH          = 1400
HEIGHT         = 600

# define colors
RED         = (255, 0, 0)
GREEN       = (0, 255, 0)
BLUE        = (0, 0, 255)
LIGHT_BLUE  = (0, 255, 255)
BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
STEEL       = (0, 100, 100)
GREY        = (85,85,85)


# define position of dials and needles
X_DIAL_COORD_INSTR1   = X_SPACE_BETWEEN_ALL_INSTRUMENTS 
Y_DIAL_COORD_INSTR1   = Y_POS_FOR_ALL_INSTRUMENTS 
X_NEEDLE_COORD_INSTR1 = X_DIAL_COORD_INSTR1+200 
Y_NEEDLE_COORD_INSTR1 = Y_DIAL_COORD_INSTR1+200 

X_DIAL_COORD_INSTR2   = X_SPACE_BETWEEN_ALL_INSTRUMENTS*10
Y_DIAL_COORD_INSTR2   = Y_POS_FOR_ALL_INSTRUMENTS 
X_NEEDLE_COORD_INSTR2 = X_DIAL_COORD_INSTR2+200 
Y_NEEDLE_COORD_INSTR2 = Y_DIAL_COORD_INSTR2+200 

X_DIAL_COORD_INSTR3   = X_SPACE_BETWEEN_ALL_INSTRUMENTS*19 
Y_DIAL_COORD_INSTR3   = Y_POS_FOR_ALL_INSTRUMENTS 
X_NEEDLE_COORD_INSTR3 = X_DIAL_COORD_INSTR3+200 
Y_NEEDLE_COORD_INSTR3 = Y_DIAL_COORD_INSTR3+200 

# rotation offset for needle
OFFSET_X = 55
OFFSET_Y = 55

# composite postion of dials and needles
DIAL_POS_INSTR1   = (X_DIAL_COORD_INSTR1, Y_DIAL_COORD_INSTR1)
NEEDLE_POS_INSTR1 = (X_NEEDLE_COORD_INSTR1, Y_NEEDLE_COORD_INSTR1)
DIAL_POS_INSTR2   = (X_DIAL_COORD_INSTR2, Y_DIAL_COORD_INSTR2)
NEEDLE_POS_INSTR2 = (X_NEEDLE_COORD_INSTR2, Y_NEEDLE_COORD_INSTR2)
DIAL_POS_INSTR3   = (X_DIAL_COORD_INSTR3, Y_DIAL_COORD_INSTR3)
NEEDLE_POS_INSTR3 = (X_NEEDLE_COORD_INSTR3, Y_NEEDLE_COORD_INSTR3)

# instrument number
INSTRUMENT1 = 1
INSTRUMENT2 = 2
INSTRUMENT3 = 3
