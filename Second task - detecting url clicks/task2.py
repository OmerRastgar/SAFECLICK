import win32api
import win32gui
import win32con

import time 

def get_cursor_handle():
    cursor_info = win32gui.GetCursorInfo()
    cursor_handle = cursor_info[1]
    return cursor_handle



# Monitor for cursor changes
while True:
    time.sleep(0.5)
    new_cursor_handle = get_cursor_handle()
    while (new_cursor_handle == int("7866451") or new_cursor_handle == int("65567") ):
        time.sleep(0.1)
        print(int(win32api.GetKeyState(0x01)))
        if(int(win32api.GetKeyState(0x01)) < 0):
            print("link is pressed!!!!")
