# font section
FONT_NAME = "font.TTF"  # this font will be used everywhere

# color section
"""
Colors in RGB
"""
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (247, 255, 0)
ORANGE = (255, 111, 0)
LIGHT_BLUE = (0, 239, 255)
PINK = (255, 0, 239)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (125, 125, 125)
PURPLE = (255, 44, 242)

# screen section
DISPLAY_WIDTH, DISPLAY_HEIGHT = 800, 600
HALF_DISP_WIDTH, HALF_DISP_HEIGHT = DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2

# main menu section
"""
Every position of text
is coordinate/coordinates
of pixel where text is located
"""
CASUAL_TEXT_SIZE = 20
CASUAL_FONT_SIZE = 32


MAIN_GREETING_X_POS, MAIN_GREETING_Y_POS = HALF_DISP_WIDTH, 100
MAIN_START_X_POS, MAIN_START_Y_POS = 305, 200
MAIN_HIGH_SCORE_X_POS, MAIN_HIGH_SCORE_Y_POS = 315, 250
MAIN_CREDITS_X_POS, MAIN_CREDITS_Y_POS = 337, 300
MAIN_EXIT_X_POS, MAIN_EXIT_Y_POS = 370, 350
MAIN_GREETING_SIZE = 30
MAIN_START_SIZE = MAIN_HIGH_SCORE_SIZE = MAIN_CREDITS_SIZE = MAIN_EXIT_SIZE = 20

# cursor section
CURSOR_OFFSET_X = -40  # offset of rectangle, where cursor image is located
CURSOR_WIDTH = 26
CURSOR_HEIGHT = 26
CURSOR_IMAGE_PATH = "cursor.png"
CURSOR_SIZE = 20
CURSOR_START_POS_X, CURSOR_START_POS_Y = MAIN_START_X_POS + CURSOR_OFFSET_X, MAIN_START_Y_POS

# credits menu section
CREDITS_TEXT1_X_POS, CREDITS_TEXT1_Y_POS = 200, 200
CREDITS_TEXT2_X_POS, CREDITS_TEXT2_Y_POS = 320, 230
CREDITS_ESCAPE_X_POS, CREDITS_ESCAPE_Y_POS = 250, 350

CREDITS_TEXT_SIZE = 20
CREDITS_ESCAPE_SIZE = 15

# high score menu section
SCORE_TITLE_X_POS, SCORE_TITLE_Y_POS = 320, 25
SCORE_ESCAPE_X_POS, SCORE_ESCAPE_Y_POS = 250, DISPLAY_HEIGHT-40
SCORE_LIST_OFFSET = 100
SCORE_ITEM_HEIGHT = 40
SCORE_FIRST_ITEM_Y_POS = 75
SCORE_TEXT_SIZE = 16

# set name menu section
SET_MENU_TITLE_X_POS, SET_MENU_TITLE_Y_POS = 250, 70
MAX_LEN_NAME = 12

# choose game section
CHOOSE_NEW_GAME_X_POS, CHOOSE_NEW_GAME_Y_POS = 280, 200
CHOOSE_LOAD_LAST_GAME_X_POS, CHOOSE_LOAD_LAST_GAME_Y_POS = 275, 250
CHOOSE_GO_BACK_X_POS, CHOOSE_GO_BACK_Y_POS = 230, DISPLAY_HEIGHT-40

# finished game menu section
FINISH_CONGRATULATIONS_POS = [100, 100]
FINISH_PLAY_AGAIN_POS = [260, 200]
FINISH_GO_MAIN_POS = [260, 300]

# game over menu section
GAME_OVER_AGAIN_POS = [260, 200]
GAME_OVER_GO_MAIN_POS = [260, 300]



#  pause menu section
PAUSE_CONTINUE_POS = [320, 200]
PAUSE_SAVE_GAME_POS = [310, 300]
PAUSE_GO_MAIN_POS = [260, 400]

# saved file is empty menu section
SAVED_NOT_FOUND_ESCAPE_Y_POS = DISPLAY_HEIGHT - 30

#  files section
SCORE_FILE_NAME = "score.csv"
NEW_MAP_FILE_NAME = "lvl1.json"
SAVED_GAME_FILE_NAME = "saved_game.json"

#  playing section
TOP_BOTTOM_PADDING, LEFT_RIGHT_PADDING = 50, 50
ROWS, COLUMNS = 25, 35
SQUARE_WIDTH, SQUARE_HEIGHT = 20, 20
MAX_FPS = 60
PLAYER_SPEED = 2
PLAYER_START_GRID_POS = [1, 6]
COUNT_PLAYER_START_LIVES = 3
CURRENT_SCORE_POS = [10, 10]
HEART_IMAGE_PATH = "heart.png"
HEART_IMAGE_WIDTH, HEART_IMAGE_HEIGHT = 30, 30

# enemy section
ENEMY_RADIUS = SQUARE_WIDTH-5
LEFT_UP_CORNER_POS = [1, 2]
LEFT_BOTTOM_CORNER_POS = [1, 23]
RIGTH_UP_CORNER_POS = [33, 2]
RIGHT_BOTTOM_CORNER_POS = [33, 23]
RANDOM_MOTION_MODE = "random"
OPTIMAL_MOTION_MODE = "optimal"