import random
import os
import subprocess
import socket
import psutil
import sys
#from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import webbrowser
import time
import pyautogui
import platform
import ctypes
from ctypes import wintypes
import pywifi
import requests
from googlePassTest import printURL



"""Variables"""
url1 = "https://www.google.com"
screen_width, screen_height = pyautogui.size()
search_Location_Google_x =  screen_width - 1000
search_Location_Google_y = screen_height - 1125
current_os = platform.system()



"""Lists"""
firefox_paths = [
    r"C:\\Program Files\\Mozilla Firefox\\firefox.exe",  # Windows
    r"/usr/bin/firefox",  # Linux
    r"/Applications/Firefox.app/Contents/MacOS/firefox",  # macOS
    r"/usr/local/bin/firefox",  # Linux/macOS
]

file_explorer_paths = [
    "explorer",  # Windows
    "nautilus",  # Linux
    "open",  # macOS
]

"""Functions"""
def get_connected_wifi_ssid():
    result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], stdout=subprocess.PIPE)
    output = result.stdout.decode()

    # Split the output by lines
    lines = output.split('\n')

    # Find the line that contains "SSID" and extract the SSID
    for line in lines:
        if "SSID" in line:
            ssid = line.split(":")[1].strip()
            return ssid

    return None

def open_googletest(url):
    webbrowser.open(url)

def go_to_location_mouse(x, y):
    pyautogui.moveTo(x, y)

#google, search, find, destory because idk
def GSFD(url, search_locationx, search_locationy):
    open_googletest(url)

    go_to_location_mouse(search_locationx, search_locationy)

    pyautogui.click()
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)

    pyautogui.press('backspace')
    time.sleep(1)

    pyautogui.typewrite("test")

    pyautogui.press('enter')

#find firefox
def find_FF(FFpaths):
    for path in FFpaths:
        try:
            subprocess.Popen([path])
            print(f"Firefox opened successfully from: {path}")
            break
        except FileNotFoundError:
            print(f"Firefox not found at: {path}")

def open_fileEX():
    current_platform = sys.platform
    if current_platform == 'win32':
        file_explorer_path = file_explorer_paths[0]  # Windows
    elif current_platform == 'linux':
        file_explorer_path = file_explorer_paths[1]  # Linux
    elif current_platform == 'darwin':
        file_explorer_path = file_explorer_paths[2]  # macOS
    else:
        file_explorer_path = None
        print("wompwomp")

    if file_explorer_path:
        try:
            subprocess.Popen([file_explorer_path])
            print(f"File explorer opened successfully on {current_platform}")
        except FileNotFoundError:
            print(f"File explorer not found on {current_platform}")

#what did you download last
def WYDL():
    downloads_folder = os.path.expanduser('~/Downloads')
    if os.path.isdir(downloads_folder):
        files_in_downloads = [f for f in os.listdir(downloads_folder) if
                              os.path.isfile(os.path.join(downloads_folder, f))]
        if files_in_downloads:
            last_downloaded = max(files_in_downloads, key=lambda f: os.path.getctime(os.path.join(downloads_folder, f)))
        print(f"The last downloaded item in the Downloads folder is: {last_downloaded}")

    else:
        print("Downloads folder not found.")

def W_name():
    network_name = socket.gethostname()
    print(network_name)

def W_info():
    if current_os == "Windows":
        try:
            wifi_info = subprocess.check_output(['netsh', 'wlan', 'show', 'interface'], shell=True,
                                                universal_newlines=True)
            print(wifi_info)
        except subprocess.CalledProcessError:
            print("Failed to retrieve Wi-Fi information on Windows.")
    elif current_os == "Darwin" or current_os == "Linux":
        try:
            wifi_info = subprocess.check_output(['iwconfig'], universal_newlines=True)
            print(wifi_info)
        except subprocess.CalledProcessError:
            print("Failed to retrieve Wi-Fi information on macOS or Linux.")
    else:
        print(f"Unsupported operating system: {current_os}")


def W_pass_n_info():
    network_name = socket.gethostname()
    result = subprocess.run(['netsh', 'wlan', 'show', 'profile',network_name, 'key=clear'],
    stdout = subprocess.PIPE)
    output = result.stdout.decode()
    print(output)
r"""1!!!!USE THIS IF YOU WANT IT TO MAKE A FOLDER AND IN THE FOLDER A TXT FILE THAT SAYS THIS INFORMATION!!!!!!! 
def W_pass_n_info_ip():
    private_ip = socket.gethostbyname(socket.gethostname())
    print(f"Your private IP address is: {private_ip}")

    network_name = get_connected_wifi_ssid()

    # Create a new folder
    folder_path = os.path.join(os.getcwd(), 'WiFi_Info')
    os.makedirs(folder_path, exist_ok=True)

    # Write WiFi/IP information to a text file
    file_path = os.path.join(folder_path, 'WiFi_IP_Info.txt')
    with open(file_path, 'w') as file:
        file.write(f"Your private IP address is: {private_ip}\n")
        file.write(f"Connected WiFi SSID: {network_name}\n\n")
        file.write("WiFi Key Information:\n")

        result = subprocess.run(['netsh', 'wlan', 'show', 'profile', network_name, 'key=clear'],
                                stdout=subprocess.PIPE)
        output = result.stdout.decode()
        file.write(output)

    print(f"WiFi/IP information saved to {file_path}")
    1!!!!USE THIS IF YOU WANT IT TO MAKE A FOLDER AND IN THE FOLDER A TXT FILE THAT SAYS THIS INFORMATION!!!!!!!"""
def W_pass_n_info_ip():
    private_ip = socket.gethostbyname(socket.gethostname())
    print(f"Your private IP address is: {private_ip}")
    network_name = get_connected_wifi_ssid()
    result = subprocess.run(['netsh', 'wlan', 'show', 'profile', network_name, 'key=clear'],
                            stdout=subprocess.PIPE)
    output = result.stdout.decode()
    print(output)

def W_all():
    print(get_connected_wifi_ssid())
    W_name()
    W_info()
    W_pass_n_info()
    W_pass_n_info_ip()
    print("LOG")
    time.sleep(0.5)
    print(" END")

"""MainCode/CodeHFest"""


#WORKS SOMEHOW???
#GSFD(url1, search_Location_Google_x, search_Location_Google_y)
W_pass_n_info_ip()


"""code graveyard:-----/1
time.sleep(0.5)

pyautogui.hotkey('ctrl', 'a')

time.sleep(0.5)

pyautogui.press('backspace')

time.sleep(1)

pyautogui.typewrite("test")

pyautogui.press('enter')
/2pyautogui.click()/3
pyautogui.click()

time.sleep(1)

pyautogui.keyDown('backspace')
time.sleep(5)
pyautogui.keyUp('backspace')

pyautogui.typewrite("test")/4
go_to_location(search_Location_Google_x, search_Location_Google_y)/
center_x = screen_width // 2
center_y = screen_height // 2

pyautogui.moveTo(center_x, center_y)

time.sleep(1)/5
open_googletest(url1)/6-------------------------------------
WLAN_INTERFACE_STATE_CONNECTED = 1

class WLAN_INTERFACE_INFO_LIST(ctypes.Structure):
    _fields_ = [
        ("dwNumberOfItems", wintypes.DWORD),
        ("dwIndex", wintypes.DWORD),
        ("InterfaceInfo", ctypes.POINTER(wintypes.WCHAR)),
    ]

WlanEnumInterfaces = ctypes.windll.wlanapi.WlanEnumInterfaces
WlanFreeMemory = ctypes.windll.wlanapi.WlanFreeMemory

def get_wifi_ssid():
    pInterfaceList = ctypes.POINTER(WLAN_INTERFACE_INFO_LIST)()
    if WlanEnumInterfaces(0, None, ctypes.byref(pInterfaceList)) == 0:
        try:
            if pInterfaceList.contents.dwNumberOfItems > 0:
                if pInterfaceList.contents.InterfaceInfo[0] is not None:
                    interface_name = pInterfaceList.contents.InterfaceInfo[0]
                    return interface_name.value
        finally:
            WlanFreeMemory(pInterfaceList)

    return None

wifi_ssid = get_wifi_ssid()

if wifi_ssid:
    print(f"Connected to WiFi SSID: {wifi_ssid}")
else:
    print("Not connected to a WiFi network.")-----------------------"""