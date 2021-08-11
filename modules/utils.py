import win32process
import subprocess
import win32gui
import win32api
import win32con
import time


def start_hidden(executable):
    SW_MINIMIZE = 6
    info = subprocess.STARTUPINFO()
    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = SW_MINIMIZE
    return subprocess.Popen(executable, startupinfo=info)


def get_hwnds_for_pid(pid):
    def callback(hwnd, hwnds):
        _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
        if found_pid == pid:
            hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds


def send_keystroke(hwnd, key):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    time.sleep(0.05)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP,   key, 0)
    time.sleep(0.1)


def send_char(hwnd, char):
    win32api.PostMessage(hwnd, win32con.WM_CHAR, char, 0)
    time.sleep(0.1)
