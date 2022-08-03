import operator
import os
import sys

from pynput import keyboard

ListOne = []
ListTwo = ['-', '-', '+']


def on_press(key):
    try:
        if key.char == '+':
            ListOne.append('+')

        elif key.char == '-':
            ListOne.append('-')

        else:
            sys.exit()

        if operator.eq(ListOne, ListTwo):
            os.system(r"C:\Users\Lzhyrifx\AppData\Command\Error\Kill.vbs")
            sys.exit()

        if len(ListOne) > len(ListTwo):
            sys.exit()

    except AttributeError:
        sys.exit()


with keyboard.Listener(
        on_press=on_press
) as listener:
    listener.join()
