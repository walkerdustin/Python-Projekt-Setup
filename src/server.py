"""
This python script represents the game logic for the simon says game.
the points, the game state and all the nessecarry functions to compute anything related to the game are here!
"""
import sys
import os

import uuid
import socket
import ipaddress
from time import sleep
from middleware import Middleware

class SimonBroadcastsGame():
    #constants/defines


    def __init__(self):
        self.UUID = uuid.uuid4()
        self.enterGame(self.UUID)
        pass

    def enterGame(self, uuid):
        
        pass


states = {}                 # python dictionary {"key": value} 
class Statemachine(object): # there should be only one Instance of this class 
    __currentState = ''

    # State Storage, Parameters and Variables 
    # these can be changed by from outside the state machine (in a separate file) (maybe even in a separate thread) 
    # by importing Statemachine (from State_Machine_example import Statemachine) and then
    # Statemachine.variable = 'something else' 
    # this variable can then be used in an if statement for transitions
    variable = 'something'
    PARAMETER = 42 
    counterN = 0 
    
    ###############################################   internal class 
    class State: # there are multiple instances of this class 
 
        def __init__(self, name:str): 
            self.name = name 
            states[name] = self          #add this state (self) to the collection (dictionary) of states with the key being its name  
 
        def run(self): 
            pass 
    ############################################## 

    @classmethod
    def switchStateTo(cls, toStateName):
        print(f'___________Switch State from {cls.__currentState} to {toStateName}')
        if "exit" in dir(states[cls.__currentState]): # check if the state has a exit() function
            states[cls.__currentState].exit() # execute the exit function
        if "entry" in dir(states[toStateName]): # check if the state has a entry() function
            states[toStateName].entry()
        cls.__currentState = toStateName
 
    def __init__(self): 
        Statemachine.__currentState = "Initializing" 
        ########################################################################### defining all states 
        ############################################## State 0 
        tempState = self.State("Initializing") 
        def run0(): 
            # State Actions 
            print("initializing....\n") 
            sleep(1) 
            print(".....") 
            sleep(1) 
            # State Transition 
            Statemachine.switchStateTo("Step 1")    # the self refers to the Statemachine (statemachine object) 
        tempState.run = run0 # overriding the run() method of state0 
        ############################################## State 1 
        tempState = self.State("Step 1") 
        def run1(): 
            # State Actions 
            print("doing step one") 
            # State Transition 
            if(True): 
                Statemachine.switchStateTo("Step 2")
        tempState.run = run1 
        ############################################## State 2 
        tempState = self.State("Step 2") 
        def run2(): 
            # State Actions 
            print("doing step two .....n = ", self.counterN) 
            self.counterN += 1 
            # State Transition 
            if(self.counterN < 10):  
                Statemachine.switchStateTo("Step 2")
            else: 
                Statemachine.switchStateTo("Finish") 
        tempState.run = run2 
        ############################################## State 3 
        tempState = self.State("Finish") 
        def run3(): 
            print("finished") 
            sleep(2) 
        tempState.run = run3 
        ############################################## 
 
    def runLoop(self): 
        states[Statemachine.__currentState].run() # run the current state 
 
if __name__ == '__main__': 
    statemachine = Statemachine() 
    while True: 
        statemachine.runLoop()
       
        sleep(1 / 1_000_000) # sleep for a microsecond to prevent unnecessary cpu utilization