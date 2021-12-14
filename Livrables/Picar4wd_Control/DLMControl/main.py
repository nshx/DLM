from DLMControlLib import DLMControl as DLMC
import time

DLMcontrol = DLMC.DLMControl()

#DLMcontrol.start()
#DLMcontrol.turn("right")
#DLMcontrol.turn("left")

DLMcontrol.threadStart()

time.sleep(5)

DLMcontrol.sigSend(3)
