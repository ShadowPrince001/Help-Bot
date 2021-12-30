from datetime import datetime
import random 

import os
import subprocess as sp

def open_camera():
    sp.run('start microsoft.windows.camera:', hell=True)

def open_notepad():
    os.startfile(paths['notepad'])
    
def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])


