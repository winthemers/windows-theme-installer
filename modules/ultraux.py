import win32con
import win32gui
import psutil

from modules import globals, utils


def run_patcher():
    print("Starting UltraUX...")
    ultraux = utils.start_hidden("resources/ultraux.exe")

    # Wait for window
    while not utils.get_hwnds_for_pid(ultraux.pid):
        pass

    # Getw HWND window id
    hwnd = utils.get_hwnds_for_pid(ultraux.pid)[0]
    hwnd = win32gui.GetWindow(hwnd, win32con.GW_CHILD)

    # Hex key codes
    KEY_ENTER = 0x0D
    KEY_TAB   = 0x09
    KEY_A     = 0x41

    # Navigate menus
    print("Navigating install procedure...")
    utils.send_keystroke(hwnd, KEY_ENTER)
    utils.send_keystroke(hwnd, KEY_TAB  )
    utils.send_char     (hwnd, KEY_A    )
    utils.send_keystroke(hwnd, KEY_TAB  )
    utils.send_keystroke(hwnd, KEY_TAB  )
    utils.send_keystroke(hwnd, KEY_ENTER)
    utils.send_keystroke(hwnd, KEY_ENTER)
    utils.send_keystroke(hwnd, KEY_ENTER)

    # Spam enter to exit after patching is done
    print("Waiting for patching to complete, system might reboot when done...")
    while psutil.pid_exists(ultraux.pid):
        try:
            utils.send_keystroke(hwnd, KEY_ENTER)
        except Exception:
            pass

    print("\n\nDONE! If needed, the system will restart shortly...")
