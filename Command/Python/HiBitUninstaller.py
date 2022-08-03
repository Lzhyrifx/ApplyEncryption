import operator
import os
import sys
import time

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
            os.system(r"C:\Users\Lzhyrifx\AppData\Command\Error\ModuleError.vbs")
            sys.exit()

        if operator.eq(ListOne, ListTwo):
            os.system(r"C:\Users\Lzhyrifx\AppData\Command\Error\Kill.vbs")
            os.system(r"C:\Users\Lzhyrifx\AppData\Command\Start\HiBitUninstaller.vbs")
            time.sleep(1)
            os.system(r"C:\Users\Lzhyrifx\AppData\Command\Error\Kill.vbs")
            sys.exit()

        if len(ListOne) > len(ListTwo):
            os.system(r"C:\Users\Lzhyrifx\AppData\Command\Error\ModuleError.vbs")
            sys.exit()

    except AttributeError:
        os.system(r"C:\Users\Lzhyrifx\AppData\Command\Error\ModuleError.vbs")
        sys.exit()


with keyboard.Listener(
        on_press=on_press
) as listener:
    listener.join()
