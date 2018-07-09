import time
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
    while it<tabatas:
        print("tabata number " + str(it))
        time.sleep(extime)
        print("pause")
        time.sleep(ptime)
        it+=1
    ic+=1
print("finished")
