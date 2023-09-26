# from https://github.com/PBahner/Serial-Monitor/

import os
import serial
import threading
import time


class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    # from: https://code.activestate.com/recipes/134892-getch-like-unbuffered-character-reading-from-stdin/

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch().decode()


class ListenOnSerialPort(threading.Thread):
    def __init__(self, keyboard_thread, ser=None, getch=None):
        threading.Thread.__init__(self)
        self.getch = getch  # save `getch` as instance variable
        self.ser = ser  # save `ser` as instance variable
        self.keyboard_thread = keyboard_thread

    def run(self):
        while True:
            if not self.keyboard_thread.input_active:
                try:
                    ser_in = self.ser.readline().decode('utf-8').strip('\n')
                    print(ser_in)
                except UnicodeDecodeError:
                    print("Serial Error")


class ListenOnKeyboard(threading.Thread):
    def __init__(self, ser=None, getch=None):
        threading.Thread.__init__(self)
        self.getch = getch  # save `getch` as instance variable
        self.ser = ser  # save `ser` as instance variable
        self.input_active = False

    def run(self):
        while True:
            cmd_in = self.getch()
            print(cmd_in)
            if cmd_in == "i":  # if key 'i' is pressed
                self.input_active = True
                time.sleep(0.1)
                string = input(">> ")
                self.ser.write(string.encode())
                self.input_active = False
            elif cmd_in == "q":
                os._exit(1)


def monitor(port):

    print("Press 'i' for sending data")
    print("Press 'q' to quit")
    port = port
    baud = 9600

    getch = _Getch()
    ser = serial.Serial(port, baud)

    kb_listen = ListenOnKeyboard(ser=ser, getch=getch)
    sp_listen = ListenOnSerialPort(kb_listen, ser=ser)
    kb_listen.start()
    sp_listen.start()