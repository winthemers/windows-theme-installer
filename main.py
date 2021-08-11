from modules import require_elevation

# Sanity check: try importing all needed packages now to avoid issues later
import os
import sys
import time
import psutil
import ctypes
import win32con
import win32api
import win32gui
import subprocess
import win32process

from modules import globals, ultraux, utils


if __name__ == '__main__':

    # Placeholder, only run ultraux for now
    ultraux.run_patcher()

    # Cool exit message
    print("Exiting in 5", end="", flush=True)
    time.sleep(0.25)
    print(".",  end="", flush=True)
    time.sleep(0.25)
    print(".",  end="", flush=True)
    time.sleep(0.25)
    print(". ", end="", flush=True)
    time.sleep(0.25)
    print("4",  end="", flush=True)
    time.sleep(0.25)
    print(".",  end="", flush=True)
    time.sleep(0.25)
    print(".",  end="", flush=True)
    time.sleep(0.25)
    print(". ", end="", flush=True)
    time.sleep(0.25)
    print("3",  end="", flush=True)
    time.sleep(0.25)
    print(".",  end="", flush=True)
    time.sleep(0.25)
    print(".",  end="", flush=True)
    time.sleep(0.25)
    print(". ", end="", flush=True)
    time.sleep(0.25)
    print("2",  end="", flush=True)
    time.sleep(0.25)
    print(".",  end="", flush=True)
    time.sleep(0.25)
    print(".",  end="", flush=True)
    time.sleep(0.25)
    print(". ", end="", flush=True)
    time.sleep(0.25)
    print("1",  end="", flush=True)
    time.sleep(0.25)
    print(".",  end="", flush=True)
    time.sleep(0.25)
    print(".",  end="", flush=True)
    time.sleep(0.25)
    print(". ", end="", flush=True)
    time.sleep(0.25)
