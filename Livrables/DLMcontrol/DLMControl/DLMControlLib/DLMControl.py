import picar_4wd as fc 
import threading 
#import thread
import time 

"""
        172.20.10.2
"""

"""
class DLMControlThread (threading.Thread): 
    
    def __init__ (self,id,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    
    def run(self):
        pass
"""

class DLMControl : 

    def __init__(self):
        self.speed = 0
        self.turningSpeed = 15

        #self.cmd
        self.ThsigListen = threading.Thread.__init__(self)
        self.sig_stop = False
        self.sig_start = False 
        self.sig_turn = "None"
        self.sig_type = ""
        self.sig_warning = 0 #level 0,1,2,3
        self.priority_task = 0

    
    def threadStart(self):

        try: 
            self.ThsigListen = threading.Thread(target=self.sigListen)
            self.ThsigListen.start()
            self.start()
            self.forwardspeed(5)
            print("LOG DEBUG: Thread sigListen is running ")
        except : 
            print("LOG ERROR: Failure to start sigListen ")

        #thread.start_new_thread()
    
    def threadStop(self):
        pass


    
    def DLMControl(self):

        pass
            

    def sigSend(self, sig_warning):
            self.sig_warning = sig_warning 
            print("LOG : Signal sent level",sig_warning)
    
    
    def sig_TLdetected(self,TLcolor):
        
        if (TLcolor == "red"):
            self.sigSend(3)
            print("LOG: Red light detected")
        elif (TLcolor == "green"):
            self.sigSend(0)
            self.speed=15
            self.forwardspeed(15)
            print("LOG: Green Light restart")
        else:
            print("ERROR LOG: Error light color")
            
            
        
        
        

    def sigListen(self):

        
        while True : 
            warning = self.sig_warning
            if (warning == 0) : 
                self.speed = 15
                #self.stop()
                print("LOG : current speed")
            elif (warning == 1):
                #self.forwardspeed(5)
                self.speed = 10
                print("LOG : Speed reduce speed", self.speed)
            elif (warning == 2):
                self.speed = 5
                #self.forwardspeed(5)
                print("LOG : Speed reduce", self.speed)
            elif (warning == 3):
                self.speed = 0
                self.stop()
                print("LOG : DANGER STOP ", self.speed)
            else:
                print("ERROR LOG : DANGER STOP ", self.speed)
                
            time.sleep(2)
        




    def ecoMode(self):
        self.forwardspeed(5)
        print("LOG : Engine passed in Ecomode")
        


    #Basic control function 
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
            print("LOG : Spped of the motor")
        except : 
            print("ERROR LOG : Stop failure")
    
    def turn(self, direction):
        
        if (direction == "right"):
            try : 
                fc.turn_right(self.turningSpeed)
                print("LOG : Turn right done")
            except:
                fc.forward(speed)
                print("ERROR LOG : Can't proceed turn right ")
        elif (direction == "left"):
            try : 
                fc.turn_right(self.turningSpeed)
                print("LOG : Turn left done")
            except:
                fc.forward(speed)
                print("ERROR LOG : Can't proceed turn left")
        else:
            print("ERROR LOG : Command not understood turn('left')")

        

    

            
                
