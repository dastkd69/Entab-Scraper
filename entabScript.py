import time
import webbrowser
import pyautogui

url = "https://www.donboscocampuscare.in" # change according to your school's URL
USERNAME = "" #Enter campusCare username
PASSWORD = "" #Enter campusCare password

webbrowser.open(url)
time.sleep(10) #wait for web browser to load the page. Increase if loading takes too much time

#Since the site automatically focuses on the text box. i have found pyautogui to be an optimal solution. 
pyautogui.write(USERNAME, interval=0.25) #prints username with quarter second keystroke delay
pyautogui.press('enter')  # press the Enter key
time.sleep(5)

pyautogui.write(PASSWORD, interval=0.25) #prints username with quarter second keystroke delay
pyautogui.press('enter')  # press the Enter key
time.sleep(5)
