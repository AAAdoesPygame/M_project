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
import requests

url1 = "https://www.google.com"
screen_width, screen_height = pyautogui.size()
search_Location_Google_x =  screen_width - 1000
search_Location_Google_y = screen_height - 1092.5
google_pass_open1x = screen_width - 45
google_pass_open1y = screen_height - 1088
google_pass_open2x = screen_width - 200
google_pass_open2y = screen_height - 830
google_pass_open3x = screen_width - 45
google_pass_open3y = screen_height - 1088
google_pass_open4x = screen_width - 45
google_pass_open4y = screen_height - 1088
"""delete this if you want TO HAVE A BRAIN ANJURIZMemailG = input()
passG = input()

payload1G = {emailG, passG}"""

"""payload = {
'Email': 'accountemail@gmail.com',
'Passwd': 'accountemailpassword'
}"""

def printURL():
    print("zrl")


def open_googletest(url):
    webbrowser.open(url)
    print("S")

def go_to_location_mouse(x, y):
    pyautogui.moveTo(x, y)
    print("S")

def GSFD(url, search_locationx, search_locationy):
    global url1, search_Location_Google_y, search_Location_Google_x
    open_googletest(url)

    go_to_location_mouse(search_locationx, search_locationy)
    print("S")

#GSFD(url1, search_Location_Google_x, search_Location_Google_y)

def GSFD2(loc1, loc2):
    global google_pass_open1y, google_pass_open1x
    go_to_location_mouse(loc1, loc2)
    time.sleep(0.4)
    pyautogui.click()
    print("S")


#GSFD2(google_pass_open1x, google_pass_open1y)

def GSFD3(loc1, loc2):
    global google_pass_open2y, google_pass_open2x
    go_to_location_mouse(loc1, loc2)
    time.sleep(0.3)
    pyautogui.click()
    print("S")

#GSFD3(google_pass_open2x, google_pass_open2y)

def GSFDmain():
    global emailG, passG, payload1G
    emailG = input("enter EmailG:")
    passG = input("enter PassG:")

    payload1G = {'Email': emailG, 'Passwd': passG}
    print("YOU HAVE TO IMPORT GSFD, GSFD2 and GSFD3 TO MAKE THIS WORK")
    GSFD(url1, search_Location_Google_x, search_Location_Google_y)
    GSFD2(google_pass_open1x, google_pass_open1y)
    GSFD3(google_pass_open2x, google_pass_open2y)
    print("Success")

"""with requests.Session() as s:
    p = s.post('https://accounts.google.com/signin/challenge/sl/password', data=payload1G)
    # print the html returned or something more intelligent to see if it's a successful login page.
    print(p.text)"""