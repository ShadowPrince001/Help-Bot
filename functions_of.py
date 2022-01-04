from datetime import datetime
import pytz
import time
import random 

import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
     }

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    os.startfile(paths['notepad'])
    
def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])
    

def current_time():
    t = time.localtime()
    now_time = time.strftime("%H:%M:%S", t)
    print("Your time",current_time, "in Hour/Minute/Second format")

def timezone_time():
    tz_world= pytz.timezone(str(req_timezone))
    datetime_world = datetime.now(tz_world)
    print(tz_world "time:", datetime_world.strftime("%H:%M:%S"), "in Hour/Minute/Second format")
    


