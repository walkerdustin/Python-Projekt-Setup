"""
This is just a terminal application that
(for now)
"""

from os import getpid
from time import sleep

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))    # this adds the src folder to the path # now you can import stuff

if __name__ == '__main__':
    """this is the terminal application that
    output is displayed here;
    user input here is forwarded to the controller
    """
    print("HELLO, this is Simon multicasts\n\n")

    print("this is my process id: ", getpid())

    print("sleeping for 3 second\n\n")
    sleep(3)



