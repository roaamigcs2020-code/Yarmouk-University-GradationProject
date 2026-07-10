'''
we need to call Eel module to connect backend and frontend
this will allow us to call python functions from JS and vice versa
'''

import os
import eel
from engine.features import *
from engine.command import *


def main():
    eel.init('www')

    # Play assistant sound once on startup
    #playAssistantSound()

    # Start Eel and open a single Chrome window
    eel.start('index.html', mode='chrome', host='localhost', port=8000, block=True)
    # to tell eel which file is frontend


if __name__ == '__main__':
    main()



