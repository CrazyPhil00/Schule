"""

Eigene Aufgabe

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

import os
import time
import webbrowser
import keyboard
import threading

sleep_time = 0.1  # Too glitchy? increase this int (!reduces/increases input time! - !makes game faster/slower!)

debug = False  # shows additional debug information


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


# Entity class
class Entity:
    def __init__(self, x, y, facing, is_jumping, is_sneaking, is_visible):
        self.x = x
        self.y = y
        self.facing = facing
        self.is_jumping = is_jumping
        self.is_sneaking = is_sneaking
        self.is_visible = is_visible


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


# Initialize Player and Entity

player = Entity(10, 8, "S", False, False, True)

entity = Entity(5, 8, "S", False, False, False)

# Game Windows
info = \
    """
====================================================================================================
||                                                                                                ||
||          ONLY RUN THIS GAME IN CMD/TERMINAL, NOT DIRECTLY FROM PYCHARM OR GOOGLE COLAB!        ||
||                                                                                                ||
||                                      (only play in fullscreen!)                                ||
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
fun = \
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
    # splitting the menu into an array
    menu_array = menu.split("?")
    new_menu = ""

    for y in range(0, len(menu_array)):
        for x in range(0, len(menu_array[y])):
            if menu_array[y][x] == str(selected_menu):
                # showing wich menuitem is selected
                new_menu += "\033[1m-\033[0m"
            else:
                new_menu += menu_array[y][x]

    return str(new_menu).replace("1", " ").replace("2", " ").replace("3", " ")


frame_count = 0

text_x, text_y = 0, 0
text_msg = ""
entity_text = ""


def edit_world():
    global frame_count
    # splitting the World into an array
    world_array = world.split("?")
    string_index = 0
    entity_string_index = 0
    new_world = ""
    frame_count += 1
    for y in range(0, len(world_array)):
        for x in range(0, len(world_array[y])):

            # adding the player to the World
            if x == player.x and y == player.y - 2:
                if player.is_sneaking:
                    new_world += "o"
                else:
                    new_world += "O"

            elif x == player.x and y == player.y:
                if player.is_sneaking:
                    new_world += "|"
                else:
                    new_world += world_array[y][x]

            elif x == player.x - 1 and y == player.y:
                if not player.is_sneaking or player.facing == "O":
                    new_world += "/"
                else:
                    new_world += world_array[y][x]

            elif x == player.x + 1 and y == player.y:
                if not player.is_sneaking or player.facing == "W":
                    new_world += "\\"
                else:
                    new_world += world_array[y][x]

            elif x == player.x - 1 and y == player.y - 1:
                new_world += "/"

            elif x == player.x and y == player.y - 1:
                new_world += "|"

            elif x == player.x + 1 and y == player.y - 1:
                new_world += "\\"

            # adding the Entity to the World
            elif entity.is_visible and x == entity.x - 1 and y == entity.y - 2:
                new_world += "\\"

            elif entity.is_visible and x == entity.x + 1 and y == entity.y - 2:
                new_world += "/"

            elif entity.is_visible and x == entity.x - 1 and y == entity.y - 1:
                new_world += "\\"

            elif entity.is_visible and x == entity.x + 1 and y == entity.y - 1:
                new_world += "/"

            elif entity.is_visible and x == entity.x and y == entity.y - 1:
                new_world += "|"
            elif entity.is_visible and x == entity.x and y == entity.y:
                new_world += "o"

            # adding label for the Player
            elif not text_msg == "" and y == text_y and text_x <= x <= text_x + len(text_msg) - 1:
                new_world += text_msg[string_index]
                string_index += 1

            # adding label for the Entity
            elif not entity_text == "" and y == entity.y - 2 and entity.x <= x <= entity.x + len(entity_text) - 1:
                new_world += entity_text[entity_string_index]
                entity_string_index += 1

            # adding the background
            else:
                new_world += world_array[y][x]

    if debug:
        return new_world.replace("%FRAMES%", str(frame_count))
    else:
        return new_world.replace("Printed Frames: %FRAMES%", "")


def player_jump():
    global player
    player.is_jumping = True

    player.y -= 1
    time.sleep(0.4)
    player.y += 1

    player.is_jumping = False


# thread for jumping
player_jump_thread = MTThread(target=player_jump)

frame_count_then = 0


def entity_run():
    global entity
    for i in range(0, 200):
        entity.x += 1
        time.sleep(0.03)


def summon_entity():
    entity.is_visible = True
    entity.y = 0
    time.sleep(0.3)
    entity.y = 1
    time.sleep(0.3)
    entity.y = 2
    time.sleep(0.3)
    entity.y = 3
    time.sleep(0.3)
    entity.y = 4
    time.sleep(0.3)
    entity.y = 5
    time.sleep(0.3)
    entity.y = 6
    time.sleep(0.3)
    entity.y = 7
    time.sleep(0.3)
    entity.y = 8


def run_dialog():
    global text_msg, text_x, text_y
    text_msg = "What am I supposed to do?"
    time.sleep(6)
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


# processing the player input
def process_player_input():
    global selected_menu, GAME_STATE, EASTER_EGG_STATE, text_msg, frame_count_then
    world_width = len(world.split("?")[0])

    if frame_count_then + 50 == frame_count:
        text_msg = ""
        EASTER_EGG_STATE = ""

    if EASTER_EGG_STATE == "WALK":
        if keyboard.is_pressed("d") or keyboard.is_pressed("a") or keyboard.is_pressed("c") or keyboard.is_pressed(
                "space"):
            text_msg = "Oh you are here"
            frame_count_then = frame_count

    if GAME_STATE == "INFO":
        if keyboard.is_pressed("enter"):
            GAME_STATE = "MAIN_MENU"
            time.sleep(0.2)

    elif GAME_STATE == "WORLD":
        if keyboard.is_pressed("W") or keyboard.is_pressed("up"):
            player.facing = "N"

        if keyboard.is_pressed("S") or keyboard.is_pressed("down"):
            player.facing = "S"

        if keyboard.is_pressed("d") or keyboard.is_pressed("right"):
            if player.x >= world_width:
                player.x = world_width - 1
            else:
                player.x += 1
            player.facing = "O"

        if keyboard.is_pressed("a") or keyboard.is_pressed("left"):
            if player.x <= 2:
                player.x = 2
            else:
                player.x -= 1

            player.facing = "W"

        if keyboard.is_pressed("space"):
            # jump
            if not player.is_jumping:
                # thread because sleep would pause the game
                player_jump_thread.start()

        if keyboard.is_pressed("c"):
            # sneak
            player.is_sneaking = True

        if not keyboard.is_pressed("c"):
            # sneak
            player.is_sneaking = False

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


clear()
print(info)

while True:
    # printing the world

    if GAME_STATE == "WORLD":
        text_x = player.x + 2
        text_y = player.y - 3
        if entity.x >= player.x and entity.is_visible:
            url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            webbrowser.open(url)
            time.sleep(0.5)
            print(fun)
            exit(0)
        else:
            print(edit_world())
        # trigger event when the framecount reached 100 frames
        if frame_count == 100 and player.x == 10 and player.y == 8:
            EASTER_EGG_STATE = "WALK"
            text_msg = "Hello is someone there?"
            text_x = player.x + 2
            text_y = player.y - 3

        if EASTER_EGG_STATE == "WALK" and frame_count == 140 and player.x == 10 and player.y == 8:
            text_msg = "Do you know how to walk?"

        if EASTER_EGG_STATE == "WALK" and frame_count == 180 and player.x == 10 and player.y == 8:
            text_msg = "or is the game bugging?"

        if EASTER_EGG_STATE == "WALK" and frame_count == 280 and player.x == 10 and player.y == 8:
            text_msg = "You're gonna make me angry"

        if EASTER_EGG_STATE == "WALK" and frame_count >= 400 and player.x <= 10 and player.y == 8:
            text_msg = "No im not doing this anymore."
            player.x -= 1

        if EASTER_EGG_STATE != "WALK" and not EASTER_EGG_STATE == "ENTITY" and not player.x == 10 and frame_count >= 140:
            # trigger the dialog when 140 frames passed
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
        print("UNDER CONSTRUCTION!")
        pass

    process_player_input()

    time.sleep(sleep_time)
    if GAME_STATE != "INFO":
        clear()
