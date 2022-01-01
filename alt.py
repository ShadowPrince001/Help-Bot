import utils
from datetime import datetime
from utils import open_calculator, open_camera, open_cmd, open_notepad
from info import opening_text, paths
import random

import os
import subprocess as sp


def greet_user():
    """Greets the user according to the time"""
    username = input("May I have your name please? \n")
    hour = datetime.now().hour
    if (hour >= 0) and (hour < 12):
        print("Good Morning Mr.", (username), ".I am AVA. ")
    elif (hour >= 12) and (hour < 16):
        print("Good Afternoon Mr.", (username), ".I am AVA. ")
    elif (hour >= 16) and (hour < 24):
        print("Good Evening Mr.", (username), ".I am AVA. ")


def take_user_input():
    query = input("How may I assist you? \n")
    if not "exit" in query or "stop" in query:
        print(random.choice(opening_text))
    else:
        hour = datetime.now().hour
        if hour >= 21 and hour < 6:
            print("Good night sir, take care!")
        else:
            print("Have a good day sir!")
        exit()
    return query


if __name__ == "__main__":
    greet_user()
    while True:
        query = take_user_input()
        if "open camera" in query:
            open_camera()
        elif "open calculator" in query:
            open_calculator()
        elif "open command prompt" in query:
            open_cmd()
        elif "open notepad" in query:
            open_notepad()
        else:
            print("Sorry, I could not understand you Sir.")
            query = "None"

