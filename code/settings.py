# screen settings
WIDTH = 1000
HEIGTH = 1000
FPS = 200

# canvas settings
CVS_WIDTH = 1000
CVS_HEIGTH = 1000
CVS_OFFSET_X = 0
CVS_OFFSET_Y = 0
PIXEL_SIZE = 3

# drawer settings
MAX_VECTORS = 0 # 0 means infinite
DEFAULT_SIMULATION_SPEED = 0.05 # seconds per second
POINT_RADIUS = 1
POINT_COLOR = (0,255,255) # pygame compatible colors (rgb: tuple, hex: str ("#FFFFFF"), some base colors like 'red', 'green', 'white', ...)
DRAW_CENTER = False
DRAW_NUMBER_LINE = True
CENTER_COLOR = 'red'
SCALER = 1 # choose to scale every Arrow
BACKGROUND_COLOR = 'black'
DRAW_ARROWS = True
ARROW_WIDTH = 2
AUTO_COLORS = True # will cycle through COLORS for every Arrow(vector) added in the drawer - VERY RECCOMENDED
COLORS = [(255,0,0,10), (0,255,0,10), (0,0,255,10), (255, 255, 0, 10), (0,255,255,10), (255,255,255,0)]

i = complex(0, 1)
