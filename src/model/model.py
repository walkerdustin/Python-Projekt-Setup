"""
This python script represents the game logic for the simon says game.
the points, the game state and all the nessecarry functions to compute anything related to the game are here!
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))    # this adds the src folder to the path # now you can import stuff
# add to path # get parent directory        #get absolut path of # this python file

# the path looks like this now: python looks here vor .py files
# for p in sys.path:
#     print(p)
# c:\Git_Repos\distributed-systems-game\src\model
# C:\Users\du-wa\AppData\Local\Programs\Python\Python39\python39.zip
# C:\Users\du-wa\AppData\Local\Programs\Python\Python39\DLLs
# C:\Users\du-wa\AppData\Local\Programs\Python\Python39\lib
# C:\Users\du-wa\AppData\Local\Programs\Python\Python39
# c:\Git_Repos\distributed-systems-game\venv
# c:\Git_Repos\distributed-systems-game\venv\lib\site-packages
# c:\Git_Repos\distributed-systems-game\venv\lib\site-packages\win32
# c:\Git_Repos\distributed-systems-game\venv\lib\site-packages\win32\lib
# c:\Git_Repos\distributed-systems-game\venv\lib\site-packages\Pythonwin
# c:\Git_Repos\distributed-systems-game\src                                         <----------

import uuid
import socket
import ipaddress
from broadcastSender import broadcast
from time import sleep
from controller.middleware import Middleware

class SimonBroadcastsGame():
    #constants/defines


    def __init__(self):
        self.UUID = uuid.uuid4()
        self.enterGame(self.UUID)
        pass

    def enterGame(self, uuid):
        
        pass


states = {}                 # python dictionary {"key": value} 
class Statemashine(object): # there should be only one Instance of this class 
    # states = {}                 # this is a class variable, it is consistent in every Instance (Object olf the same class) 
                                # python dictionary {"key": value} 
    # State Storage, Parameters and Variables 
    PARAMETER = 42 
    counterN = 0 
    ###############################################   internal class 
    class State: # there are multiple instances of this class 
        total_Number_of_states = 0  # this is a class variable, it is consistent in every Instance (Object olf the same class) 
 
        def __init__(self, name): 
            self.name = name 
            self.ID = self.total_Number_of_states 
            self.total_Number_of_states += 1 
            states[name] = self          #add this state (self) to the collection (dictionary) of states with the key being name  
 
        def run(self): 
            pass 
    ############################################## 
 
    def __init__(self): 
        self.currentState = "Initializing" 
        ########################################################################### defining all states 
        ############################################## State 0 
        tempState = self.State("Initializing") 
        def run0(): 
            # State Actions 
            print("initializing....\n") 
            sleep(1) 
            print(".....") 
            sleep(1) 
            print(".....") 
            # State Transition 
            self.currentState = "Step 1"    # the self refers to the Statemashine (SM objekt) 
        tempState.run = run0 # overriding the run() method of state0 
        ############################################## State 1 
        tempState = self.State("Step 1") 
        def run1(): 
            # State Actions 
            print("doing step one") 
            # State Transition 
            if(True): 
                self.currentState = "Step 2" 
        tempState.run = run1 
        ############################################## State 2 
        tempState = self.State("Step 2") 
        def run2(): 
            print("doing step two .....n = ", self.counterN) 
            self.counterN += 1 
            if(self.counterN < 10):  
                self.currentState = "Step 1" 
            else: 
                self.currentState = "Finish" 
        tempState.run = run2 
        ############################################## State 3 
        tempState = self.State("Finish") 
        def run3(): 
            print("finished") 
            sleep(2) 
        tempState.run = run3 
        ############################################## 
 
    def runLoop(self): 
        states[self.currentState].run() # run the current state 
 
if __name__ == '__main__': 
    SM = Statemashine() 
    while True: 
        SM.runLoop()