#!/bin/python3
import sys
from os import isatty
from sys import argv

from models import setting_storage

try:
    import vlc
    sound = True
except ImportError:
    argc = len(argv)
    if (not (argc > 1 and (argv[1] == '-i' or argv[1] == '--ignore-warnings'))
        and isatty(sys.stdin.isatty()) and setting_storage.all()['show_warnings']):
        print("Could not import vlc. Please install package 'vlc' "
              "to hear audio. 1 command uses sound.")
        print("One possible command to install vlc would be this command:")
        print("pip install vlc")
        print("or, if that doesn't work, try:")
        print("pip install python-vlc")
        print("The console will continue without sound. To run without this "
              "message, do './console.py -i' or './console.py --ignore-warnings'"
              " or, in this console, do 'settings show_warnings false' to "
              "never show this message again.\n")
    sound = False
import os
import webbrowser
from cmd import Cmd
from random import random
from time import sleep
from colors import *


class FunsoleCmd(Cmd):
    def __init__(self):
        super().__init__()
        if isatty(sys.stdin.isatty()):  # only sets intro in interactive
            self.intro = ('Welcome to the Funsole console! Type '
                          '"help" or "?" for a list of commands. Type '
                          '"exit" or "quit" to exit.')
        self.prompt = '\033[1;34m\033[5m>_\033[0m \033[7m'  # reverses background & foreground

    def precmd(self, line):
        """
        overrides the default method the runs between when the input is parsed
        and when the command is run. This override resets the text color to
        undo the effect from adding \033[7m to the prompt, which reverses the
        background and foreground colors for the user input. This makes sure
        that the output doesn't retain this effect.
        :param line: user input
        :return: the same thing the original command returns, which is line,
        according to the source code for cmd.py.
        """
        reset_color()
        return super().precmd(line)

    def default(self, line):
        match line:
            case "EOF":
                return True
            case "easter egg":
                print("You found the easter egg!")
            case "line21", "line 21":
                print("You've just ran line 21 of this program's script!")
            case _:
                super().default(line)

    def emptyline(self):
        pass

    @staticmethod
    def do_exit(self):
        """Exits the console"""
        return True

    @staticmethod
    def do_quit(self):
        """Exits the console"""
        return True

    @staticmethod
    def do_rickroll(self):
        """Rickrolls you"""
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    @staticmethod
    def do_selfdestruct(timer: str):
        """
Activates self-destruct mode, which starts a countdown from the specified
number, or 5 if not given. Exits the command line interpreter when
the countdown reaches 0.
Arguments: number (optional) - amount of seconds to count down from
Usage: selfdestruct <number>
        """
        t = 5
        if timer.isnumeric():
            t = int(timer)
        elif timer != '':
            print("Please specify a valid number, or leave blank.")
            return

        FunsoleCmd.play_sound('alarm', True )

        set_color('red')
        set_color('bold')
        set_color('reverse')
        set_color('blinking')
        print("SELF DESTRUCT MODE INITIATED.\n")
        reset_color()
        while t > 0:
            if t <= 3:
                set_color('light red')
            else:
                reset_color()
            sleep(1)
            print(t)
            t -= 1
        sleep(1)
        reset_color()
        set_color('yellow')
        print("The console has been obliterated. Goodbye.")
        reset_color()
        # system("systemctl reboot")
        return True

    @staticmethod
    def do_battleship(_):
        """spawns a drone battleship"""
        FunsoleCmd.play_sound('scanner warning')
        sleep(6.75)
        set_color('blinking')
        set_color('red')
        set_color('bold')
        set_color('reverse')
        print("SCANNER WARNING")
        reset_color()
        print('A high-energy signature is closing on your position.')
        sleep(11.9)

    @staticmethod
    def do_rainbow(self):
        """prints a rainbow"""
        if random() < 0.5:
            set_color('reverse')
        set_color('bold')
        set_color('red')
        print("r",end='')
        set_color('brown')
        print("a",end='')
        set_color('yellow')
        print("i",end='')
        set_color('green')
        print("n",end='')
        set_color('cyan')
        print("b",end='')
        set_color('blue')
        print("o",end='')
        set_color('purple')
        print("w",end='')
        set_color('light red')
        print("!")
        reset_color()

    @staticmethod
    def do_password(self):
        """Enter a password and be judged strictly."""
        print("Please enter your password.")
        set_color('concealed')
        user_input = input()
        reset_color()
        set_color('bold')
        set_color('red')
        set_color('reverse')
        set_color('blink')
        print("WEAK PASSWORD ALERT!!")
        reset_color()
        pw_with_quotes = f"'{user_input}'"
        if user_input == '':
            pw_with_quotes = "No password? Just enter"
        print(f"Really? {pw_with_quotes}? That's a terrible password.")
        if (user_input in ("password", "password123", "123456", "12345",
            "1234", "123", "")):
            print("Such a bad password that you're being kicked out. Bye!")
            return True

    # ====================== console settings ======================

    @staticmethod
    def do_settings(argstr):
        """
Change console settings.
Usages:
settings <setting> <value> | change a setting's value
settings <setting> | see a setting's current value
settings | list all settings and their current values
        """
        setting_storage.reload()
        args = FunsoleCmd.parse_args(argstr, 2)

        # for usage: 'settings': display all settings
        if args[0] == '':
            for key, value in setting_storage.all().items():
                print(f"{key}: {value}")
        # for usage: 'settings <setting>': display <setting>'s value
        elif args[1] == '':
            setting = args[0]
            if setting in setting_storage.all():
                print(f"{setting}: {setting_storage.all()[setting]}")
            else:
                print(f"** setting '{setting}' does not exist **")
        # for usage: 'settings <setting> <value>': update given settings value
        elif args[1] != '':
            setting = args[0]
            value = args[1]

            # convert value to boolean
            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
            elif value != '':
                print("** please enter true or false **")
                return

            setting_storage.new(setting, value)
            setting_storage.save()
            print(f"Setting '{setting}' updated to {value}.")

    @staticmethod
    def play_sound(sound: str, repeat: bool = False):
        """
        plays an audio file.
        :param sound: must be one of 4 specific non-case-sensitive strings
        to indicate which of the 2 sounds to play
        :param repeat: boolean to indicate if the sound should loop infinitely.
        default value is false if not given.
        """
        if not sound or  not setting_storage.all()['sound']:
            return
        sep = os.sep
        player = vlc.Instance()
        media_list = player.media_list_new()
        media_player = player.media_list_player_new()
        match sound.lower():
            case "battleship" | "scanner warning":
                alarm = player.media_new(
                    os.getcwd() + f'{sep}assets{sep}SCANNER WARNING.m4a')
            case "alarm" | "self destruct":
                alarm = player.media_new(
                    os.getcwd() + f'{sep}assets{sep}alarm.mp3')
            case _:
                raise ValueError(
                    "valid values for the `sound` param for play_sound() "
                    "are: 'battleship' or 'scanner warning' for "
                    "SCANNER WARNING.m4a; or 'alarm' or 'self destruct' "
                    "for alarm.mp3")

        media_list.add_media(alarm)
        media_player.set_media_list(media_list)

        if repeat:
            media_player.get_media_player().event_manager().event_attach(
                vlc.EventType.MediaPlayerEndReached,
                lambda event: FunsoleCmd.play_sound(sound, repeat)
            )
        media_player.play()

    @staticmethod
    def parse_args(argstr, num_args=3):
        """
        parse args by converting a string of args (argstr) into individual args
        :param argstr: string of arguments, separated by spaces.
        :param num_args: number of args to parse. 3 by default if left empty
        :return: a list of args
        """
        args = argstr.split(' ')
        if len(args) < num_args:
            add_args = num_args - len(args)
            for i in range(add_args):
                args.append('')
        return args


if __name__ == '__main__':
    FunsoleCmd().cmdloop()
