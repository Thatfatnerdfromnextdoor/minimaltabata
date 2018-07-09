import time
import os
print("amount of cycles:")
cycles=int(input())
print("amount of exercises:")
tabatas=int(input())
print("exercise time:")
extime=int(input())
print("pause time:")
ptime=int(input())
ic=0
print("starting tabata session with a duration of " + str(cycles * tabatas * (extime + ptime) / 60) + " minutes")
while ic<cycles:
    print("cycle number " + str(ic))
    it=0
    os.system("nohup play resources/startbeep.wav</dev/null &>/dev/null")
    time.sleep(3.5)
    while it<tabatas:
        print("tabata number " + str(it))
        time.sleep(extime)
        os.system("nohup play resources/pausebeep.wav</dev/null &>/dev/null")
        print("pause")
        it+=1 #tabata increment
        time.sleep(ptime -3.5)
        if it != tabatas:    #check if it is necessary to start sound(only false for last tabata of the current cycle)
            os.system("nohup play resources/startbeep.wav</dev/null &>/dev/null")
        time.sleep(3.5)
    ic+=1
print("finished")
