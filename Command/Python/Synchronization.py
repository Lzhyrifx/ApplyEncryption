import operator
import os
import sys

from pynput import keyboard

ListOne = []
ListTwo = ['*', '*']


def on_press(key):
    try:
        if key.char == '*':
            ListOne.append('*')

        else:
            os.system(r"C:\Users\Lzhyrifx\AppData\Command\Error\SystemError.vbs")
            sys.exit()

        if operator.eq(ListOne, ListTwo):
            os.system(r"C:\Users\Lzhyrifx\AppData\Command\Error\kill.vbs")
            sys.exit()

    except AttributeError:
        os.system(r"C:\Users\Lzhyrifx\AppData\Command\Error\SystemError.vbs")
        sys.exit()


with keyboard.Listener(
        on_press=on_press
) as listener:
    listener.join()
