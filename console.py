#!/bin/python3
import sys
import webbrowser
from cmd import Cmd
from os import isatty, getcwd
from os import system
from random import random
from time import sleep
import vlc
from colors import *


class FunsoleCmd(Cmd):
    player = vlc.MediaPlayer(getcwd() + '/res/SCANNER WARNING.m4a')
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

    def do_battleship(self, _):
        """spawns a drone battleship"""
        self.player.play()
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

if __name__ == '__main__':
    FunsoleCmd().cmdloop()
