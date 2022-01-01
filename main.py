import utils
from datetime import datetime
from utils import open_calculator, open_camera, open_cmd, open_notepad
from info import opening_text, paths
import random 

import os
import subprocess as sp


def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 0) and (hour < 12):
        print("Good Morning Mr.",(username),".")
    elif (hour >= 12) and (hour < 16):
        print("Good Afternoon Mr.",(username),".")
    elif (hour >= 16) and (hour <24 ):
        print("Good Evening Mr.",(username),".")

def take_user_input():
    query = input("I am AVA. How may I assist you? \n")
    if "exit" in query or "stop" in query:
        hour = datetime.now().hour
        if hour >= 21 and hour < 6:
            print("Good night sir, take care!")
        else:
            print('Have a good day sir!')
    elif "Start" in query:
        open_task = input("The options are camera,calculator, command prompt or notepad\n")
        if "exit" in query or "stop" in query:
            take_user_input()
        elif "camera" in open_task:
            open_camera()
        elif "calculator" in open_task:
            open_calculator()
        elif "command prompt" or "cmd"in open_task:
            open_cmd()
        elif "notepad" in open_task:
            open_notepad()
    else:
        print(random.choice(opening_text))  
    return query

username=input("May I have your name please? \n")
greet_user()
take_user_input()

