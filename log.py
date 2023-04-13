'''
Many computer programs, especially system processes, have log files to keep a record of events in the program, so that it can later be used to track potential errors, or to help understand particular output. A log file is just a text file, where lines usually have a time stamp, to kself.now when a particular event happened.

In the context of our simulation we could imagine a log file that shows the main events in the simulation, with log lines such as "Generated new map of size ... by ...", "Added ... new agents", "Ran simulation for ... steps", etc.

1.   Create a new Log class for recording main events and add it to the Simulation class.
2.   Create a log() function in the Log class, which as input has a line of text, and which saves the line, with a time stamp, to the log file.
3.   Add a get_log() function to the Simulation class, so that other parts of the code can find access to the log object. The Map class will need a reference to the simulation object passed in when the constructor is called.
4.   Add code at various points in the code (e.g. those listed above) to log main events to the file.
5.   Add code to log particular obvious errors in the simulation, such as trying to generate agents when there are no empty cells left.

Run some simulations and check whether the log file properly tracks events.


Example log file:

2021-11-18  15:02:01  Generated new map of size 10 by 10
2021-11-18  15:02:02  Added 50 new agents
2021-11-18  15:02:10  Printed map
2021-11-18  15:02:30  ERROR: Attempt to add 60 new agents, but no empty cells left!
'''

import json
import datetime

class Log:
    def __init__(self):
        pass

    def write(self, event):
        self.now = datetime.datetime.now()
        self.file = open(("{}-{}-{} {}.{}.log" .format(self.now.year, self.now.month, self.now.day, self.now.hour, self.now.minute, self.now.second)), "a") 
        entry = "{}-{}-{}  {}:{}:{}  {}\n" .format(self.now.year, self.now.month, self.now.day, self.now.hour, self.now.minute, self.now.second, event)
        self.file.write(entry)
        self.file.close()

    def read(self):
        return(file.read)



        






