import os
import time
import webbrowser
# from ctypes import windll
# from ctypes import c_int
# from ctypes import c_uint
# from ctypes import c_ulong
# from ctypes import POINTER
# from ctypes import byref
import random

import keyboard
import threading
from subprocess import call

"""
# ------------------------------------------------------------------------------------- #
#         __          __  _____    _____   _    _   _______   _____    _____   _        #
#         \ \        / / |_   _|  / ____| | |  | | |__   __| |_   _|  / ____| | |       #
#          \ \  /\  / /    | |   | |      | |__| |    | |      | |   | |  __  | |       #
#           \ \/  \/ /     | |   | |      |  __  |    | |      | |   | | |_ | | |       #
#            \  /\  /     _| |_  | |____  | |  | |    | |     _| |_  | |__| | |_|       #
#             \/  \/     |_____|  \_____| |_|  |_|    |_|    |_____|  \_____| (_)       #
#                                                                                       #
#             Nur in cmd/terminal ausführen, nicht in pycharm oder Google Colab!        #                                                
# ------------------------------------------------------------------------------------- #                                                                                                                                                              
"""

# fun_mode = False  # Do you want to have fun? (AT OWN RISK, only for windows :( ) (!REMOVED!)

sleep_time = 0.1  # Too glitchy? increase this int (!reduces/increases input time! - !makes game faster/slower!)

debug = True  # shows additional debug information


def printf(s):
    # so it doesn't add a new line
    print(s, end='')


# Clearing the cmd
def clear():
    # windows
    if os.name == 'nt':
        _ = os.system('cls')

    # mac / linux
    else:
        _ = os.system('clear')


""" REMOVED
def trigger_fun():
    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19),
        c_uint(1),
        c_uint(0),
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B),
        c_ulong(0),
        nullptr,
        nullptr,
        c_uint(6),
        byref(c_uint())
    )
"""


# threading doesn't allow multiple threads running at the same time so...
class MTThread(threading.Thread):
    def __init__(self, name="", target=None):
        self.mt_name = name
        self.mt_target = target
        threading.Thread.__init__(self, name=name, target=target)

    def start(self):
        super().start()
        threading.Thread.__init__(self, name=self.mt_name, target=self.mt_target)

    def run(self):
        super().run()
        threading.Thread.__init__(self, name=self.mt_name, target=self.mt_target)


start_time = time.time()
frame_count = 0
fps = 0

player_is_jumping = False
player_is_sneaking = False
player_facing = "S"

show_dialog = True

info = \
    """
====================================================================================================
||                                                                                                ||
||          ONLY RUN THIS GAME IN CMD/TERMINAL, NOT DIRECTLY FROM PYCHARM OR GOOGLE COLAB!        ||
||                                                                                                ||
||                                                                                                ||
||                 This game doesn't really have a story (didn't have enough time)                ||
||                                                                                                ||
||                                        Have fun with... idk                                    ||
||                                                                                                ||
||                                      press [\033[1mENTER\033[0m] to continue                                 ||
||                                                                                                ||
====================================================================================================
"""

story = \
    """
====================================================================================================
||                                                                                                ||
||                                                                                                ||
||                                    Just one advise                                             ||
||                                                                                                ||
||                                                                                                ||
||                                                                                                ||
||                                  \033[1m DONT COME NEAR IT      \033[0m                                      ||
||                                                                                                ||
||                                                                                                ||
||                                                                                                ||
====================================================================================================


"""

menu = \
    """
==================================================================================================== ?
||                                                                                                || ?
||                                             GAME MENU                                          || ?
||                                                                                                || ?
||                                                                                                || ?
||          [W ^]                            1 Start Game                                         || ?
||          [S v]                                                                                 || ?
||          [ENTER]                          2 Options                                            || ?
||                                                                                                || ?
||                                           3 Quit                                               || ?
||  by CrazyPhil                                                                                  || ?
==================================================================================================== ?
    
"""

good_bye = \
    """
====================================================================================================
||                                                                                                ||
||                                                                                                ||
||                                                                                                ||
||                                                                                                ||
||                                         Goodbye!                                               ||
||                                                                                                ||
||                                                                                                ||
||                                                                                                ||
||                                                                                                ||
||                                                                                                ||
====================================================================================================

"""

world = \
    """
...................................................................................................................................................... ?
|                                                                                ^                                                                   | ?
|                                       _                                       / \                                                                  | ?
|                                     /   \                                    /   \    /\                                                           | ?
|                                    /     \                                  /     \  /  \                                                          | ?
|                                   /_______\     ^                   ^      /       \/    \                                                         | ?
|                                   | __  __|    / \                 / \    /         \     \                                                        | ?
|                                   ||__||  |   /___\               /___\  /           \     \                                                       | ?
|___________________________________|____|__|_____|___________________|___/_____________\_____\______________________________________________________| ?
|         CONTROLS        |           DEBUG          |                                               | ?
|     W                   | Printed Frames: %FRAMES% |                                               | ?
|   A S D    SPACE    C   |                          |                                               | ?
------------------------------------------------------------------------------------------------------ ?
"""
# nothing to see here.
jumpscare = \
    """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣠⠤⠶⠶⠤⠴⢤⠶⠤⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡞⠉⠁⣴⡆⣸⣿⣿⣿⣿⠛⣷⣌⡻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠘⠿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣮⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣯⣀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⢈⣽⣿⣿⠟⠛⠛⠉⠛⠉⠁⠀⠀⠀⠘⢻⣿⣧⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢥⣼⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⢘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⣀⣀⣀⣠⣄⠀⠀⢠⣤⣄⣀⠀⣿⡿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢿⢿⣿⡇⠀⠻⣿⣭⣽⢹⣇⠀⠘⣿⣶⣮⠟⢹⣇⢛⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣘⣿⡇⠀⠚⠉⠀⠂⠈⣙⠀⠀⠈⠀⠀⠀⣘⣻⠿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡺⣧⠈⢷⡄⠀⠀⠀⠀⢠⣶⣤⠀⢠⡄⢀⡄⢸⣿⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣽⣶⣾⣄⡀⠀⠀⠀⢘⣇⣉⣀⡀⠃⠘⣶⢫⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠈⣿⣇⠀⠀⠀⢿⡿⡶⢿⣟⣠⣤⣏⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⢹⡽⠆⠀⠀⢀⡽⠷⢶⣶⠶⣯⣯⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⢸⣷⠀⠀⠀⠀⢀⣠⢿⣿⡀⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣾⣿⣿⢸⣿⠀⠀⠀⠀⠈⠁⣸⡏⡷⣏⢻⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣿⣿⣿⣿⣿⣿⡆⠻⣆⢠⠂⣠⣀⣰⣟⣻⣯⣸⠈⣿⣿⣿⣿⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠙⢧⡀⠀⠀⠸⣯⣿⣿⣽⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀
⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣄⠈⢻⣄⠀⠀⢩⣟⡈⠁⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀
⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⠀⠀⠈⠓⠶⠿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣦⡔⠶⠶⢦⣤⣤⠀⠀⣤⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⢰⣼⠿⠿⣿⣿⣿⣿⠛⠛⠒⠶⠶⠶⢤⣠⣬⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⡞⣿⠉⠈⠀⠛⠻⢿⣿⣟⠛⠓⠒⠶⠶⢾⣧⣶⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢹⣇⢻⣿⣿⣿⣿⣿⣿⣿⣿⠇⢾⠃⠙⠓⠒⠰⣴⣶⣾⣿⣿⠛⠛⠛⠒⠒⢻⠠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣸⠀⠀⠀⣤⠀⠈⢻⣿⣿⣿⡛⠛⠛⠛⠒⠚⠶⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠁⠀⠈⠀⢬⣤⣶⣿⣿⣿⣿⣟⠉⠛⠛⠛⣿⡾⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

GAME_STATE = "INFO"
EASTER_EGG_STATE = ""
selected_menu = 1


def add_menu():
    menu_array = menu.split("?")
    new_menu = ""

    for y in range(0, len(menu_array)):
        for x in range(0, len(menu_array[y])):
            if menu_array[y][x] == "1" or menu_array[y][x] == "2" or menu_array[y][x] == "3" or menu_array[y][x] == "4":
                pass
            if menu_array[y][x] == str(selected_menu):
                new_menu += "\033[1m-\033[0m"
            else:
                new_menu += menu_array[y][x]

    return str(new_menu).replace("1", " ").replace("2", " ").replace("3", " ")


frame_ = 0

text_x, text_y = 0, 0
text_msg = ""

entity_text = ""

entity_x, entity_y = 5, 8
entity_shown = False


def edit_world():
    global world, player_x, player_y, frame_
    world_array = world.split("?")
    string_index = 0
    entity_string_index = 0
    new_world = ""
    frame_ += 1
    for y in range(0, len(world_array)):
        for x in range(0, len(world_array[y])):

            # adding player

            if x == player_x and y == player_y - 2:
                if player_is_sneaking:
                    new_world += "o"
                else:
                    new_world += "O"

            elif x == player_x and y == player_y:
                if player_is_sneaking:
                    new_world += "|"
                else:
                    new_world += world_array[y][x]

            elif x == player_x - 1 and y == player_y:
                if not player_is_sneaking or player_facing == "O":
                    new_world += "/"
                else:
                    new_world += world_array[y][x]

            elif x == player_x + 1 and y == player_y:
                if not player_is_sneaking or player_facing == "W":
                    new_world += "\\"
                else:
                    new_world += world_array[y][x]

            elif x == player_x - 1 and y == player_y - 1:
                new_world += "/"

            elif x == player_x and y == player_y - 1:
                new_world += "|"

            elif x == player_x + 1 and y == player_y - 1:
                new_world += "\\"



            # adding e#ti$Ä
            elif entity_shown and x == entity_x - 1 and y == entity_y - 2:
                new_world += "\\"

            elif entity_shown and x == entity_x + 1 and y == entity_y - 2:
                new_world += "/"

            elif entity_shown and x == entity_x - 1 and y == entity_y - 1:
                new_world += "\\"

            elif entity_shown and x == entity_x + 1 and y == entity_y - 1:
                new_world += "/"

            elif entity_shown and x == entity_x and y == entity_y - 1:
                new_world += "|"
            elif entity_shown and x == entity_x and y == entity_y:
                new_world += "o"

            # adding text
            elif not text_msg is "" and y == text_y and text_x <= x <= text_x + len(text_msg) - 1:
                new_world += text_msg[string_index]
                string_index += 1
            # adding text
            elif not entity_text is "" and y == entity_y - 2 and entity_x <= x <= entity_x + len(entity_text) - 1:
                new_world += entity_text[entity_string_index]
                entity_string_index += 1
            else:
                new_world += world_array[y][x]

    if debug:
        return new_world.replace("%FRAMES%", str(frame_))
    else:
        return new_world.replace("Printed Frames: %FRAMES%", "")


def player_jump():
    global player_is_jumping, player_y
    player_is_jumping = True

    player_y -= 1
    time.sleep(0.4)
    player_y += 1

    player_is_jumping = False


player_jump_thread = MTThread(target=player_jump)

frame_then = 0


def entity_run():
    global entity_x
    for i in range(0, 200):
        entity_x += 1
        time.sleep(0.03)


def summon_entity():
    global entity_y, entity_shown, entity_text
    entity_shown = True
    entity_y = 0
    time.sleep(0.3)
    entity_y = 1
    time.sleep(0.3)
    entity_y = 2
    time.sleep(0.3)
    entity_y = 3
    time.sleep(0.3)
    entity_y = 4
    time.sleep(0.3)
    entity_y = 5
    time.sleep(0.3)
    entity_y = 6
    time.sleep(0.3)
    entity_y = 7
    time.sleep(0.3)
    entity_y = 8


def run_dialog():
    global text_msg, text_x, text_y, entity_shown, entity_text
    text_msg = "What am I supposed to do?"
    time.sleep(4)
    text_msg = "And what did they mean by 'it'?"
    time.sleep(6)
    text_msg = "?!"
    summon_entity()
    time.sleep(2)
    text_msg = "That's what they meant."
    time.sleep(3)
    text_msg = "AHHHHH"
    entity_run()


dialog_thread = MTThread(target=run_dialog)


def process_player_input():
    global player_x, player_y, selected_menu, GAME_STATE, player_is_sneaking, EASTER_EGG_STATE, text_msg, frame_then, player_facing
    world_width = len(world.split("?")[0])

    if frame_then + 50 == frame_:
        text_msg = ""

        EASTER_EGG_STATE = ""

    if EASTER_EGG_STATE == "WALK":
        if keyboard.is_pressed("d") or keyboard.is_pressed("a") or keyboard.is_pressed("c") or keyboard.is_pressed(
                "space"):
            text_msg = "Oh you are here"
            frame_then = frame_

    if GAME_STATE == "INFO":
        if keyboard.is_pressed("enter"):
            GAME_STATE = "MAIN_MENU"
            time.sleep(0.2)

    elif GAME_STATE == "WORLD":
        if keyboard.is_pressed("W"):
            player_facing = "N"

        if keyboard.is_pressed("S"):
            player_facing = "S"

        if keyboard.is_pressed("d"):
            if player_x >= world_width:
                player_x = world_width - 1
            else:
                player_x += 1
            player_facing = "O"

        if keyboard.is_pressed("a"):
            if player_x <= 2:
                player_x = 2
            else:
                player_x -= 1

            player_facing = "W"

        if keyboard.is_pressed("space"):
            # jump
            if not player_is_jumping:
                # thread because sleep would pause the game
                player_jump_thread.start()

        if keyboard.is_pressed("c"):
            # sneak
            player_is_sneaking = True

        if not keyboard.is_pressed("c"):
            # sneak
            player_is_sneaking = False

        if keyboard.is_pressed("escape"):
            GAME_STATE = "MAIN_MENU"

    if GAME_STATE == "MAIN_MENU":
        if keyboard.is_pressed("w"):
            if not selected_menu <= 1:
                selected_menu -= 1
        if keyboard.is_pressed("s"):
            if not selected_menu >= 4:
                selected_menu += 1

        if keyboard.is_pressed("enter"):
            if selected_menu == 1:
                GAME_STATE = "ADVISE"

            elif selected_menu == 2:
                GAME_STATE = "OPTIONS"

            elif selected_menu == 3:
                clear()
                print(good_bye)
                time.sleep(1.5)
                clear()
                exit(0)
    if GAME_STATE == "OPTIONS":
        # ...
        if keyboard.is_pressed("escape"):
            # if fun_mode:
            #   trigger_fun()
            GAME_STATE = "MAIN_MENU"


player_x, player_y = 10, 8

clear()
print(info)

while True:
    # printing the world

    if GAME_STATE == "WORLD":
        text_x = player_x + 2
        text_y = player_y - 3
        if entity_x >= player_x and entity_shown:
            print(jumpscare)
            time.sleep(0.5)
            url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            webbrowser.open(url)
            exit("gub")
        else:
            print(edit_world())

        if frame_ == 100 and player_x == 10 and player_y == 8:
            EASTER_EGG_STATE = "WALK"
            text_msg = "Hello is someone there?"
            text_x = player_x + 2
            text_y = player_y - 3

        if EASTER_EGG_STATE == "WALK" and frame_ == 140 and player_x == 10 and player_y == 8:
            text_msg = "Do you know how to walk?"

        if EASTER_EGG_STATE == "WALK" and frame_ == 180 and player_x == 10 and player_y == 8:
            text_msg = "or is the game bugging?"

        if EASTER_EGG_STATE == "WALK" and frame_ == 280 and player_x == 10 and player_y == 8:
            text_msg = "Your gonna make me angry"

        if EASTER_EGG_STATE == "WALK" and frame_ >= 400 and player_x <= 10 and player_y == 8:
            text_msg = "No im not doing this anymore."
            player_x -= 1

        if EASTER_EGG_STATE != "WALK" and not EASTER_EGG_STATE == "ENTITY" and not player_x == 10 and frame_ >= 80:
            EASTER_EGG_STATE = "ENTITY"
            dialog_thread.start()

        print("\n")
    elif GAME_STATE == "ADVISE":
        print(story)
        time.sleep(4)
        GAME_STATE = "WORLD"

    elif GAME_STATE == "MAIN_MENU":
        print(add_menu())
        print("\n")

    elif GAME_STATE == "OPTIONS":
        # TODO OPTIONS
        print(
            "UNDER CONSTRUCTION!\n\n\n\n\n\n\n                                                                                                    but do you want some fun?")
        pass

    process_player_input()

    time.sleep(sleep_time)
    if GAME_STATE != "INFO":
        clear()
