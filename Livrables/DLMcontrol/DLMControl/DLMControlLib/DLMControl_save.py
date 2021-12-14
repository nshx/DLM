import picar_4wd as fc 
import threading
import time 

"""
        172.20.10.2
"""


class DLMControlThread (threading.Thread): 

    def __init__ (self,id,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        pass

   

class DLMControl : 

    def __init__(self):
        self.speed = 0
        self.turningSpeed = 15

        self.cmd = "ST"
        self.sig_stop = False
        self.sig_start = False 
        self.sig_turn = "None"
        self.sig_type = ""
        self.sig_warning = 0 #level 0,1,2,3
        self.priority_task = 0

    

    def start(self):
        try :
            fc.start()
            print("LOG : Start of the motor")
        except : 
            print("ERROR LOG : Start failure")

    def stop(self):

        try :
            fc.stop()
            print("LOG : Stop of the motor")
        except : 
            print("ERROR LOG : Stop failure")
            
    def forwardspeed(self, speed):

 
        try :
            self.speed = speed 
            fc.forward(speed)
            print("LOG : Speed of the motor")
        except : 
            print("ERROR LOG : Go forward  failure")
    
    def turn(self, direction):
        
        if (direction == "right"):
            try : 
                fc.turn_right(self.turningSpeed)
                print("LOG : Turn right done")
            except:
                fc.forward(speed)
                print("ERROR LOG : Can't proceed turn right ")
        elif(direction == "left"):
            try : 
                fc.turn_left(self.turningSpeed)
                print("LOG : Turn left  done")
            except:
                fc.forward(speed)
                print("ERROR LOG : Can't proceed turn left")
        else:
            print("ERROR LOG : Command not understood turn('left')")

        



            
                
