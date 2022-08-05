import datetime, os, time, keyboard

#p toggels partial (1s; 150 t/min)
#o toggles full auto (1day; 15 sec/t)
#r extra boost (5 sec/use)

def glitch(sec):
    os.system((datetime.datetime.today()+datetime.timedelta(seconds=sec)).strftime('time %H:%M:%S'))
    time.sleep(0.07)
    os.system((datetime.datetime.today()-datetime.timedelta(seconds=sec)).strftime('time %H:%M:%S'))

def glitchday():
    os.system((datetime.date.today()+datetime.timedelta(days=1)).strftime('date %d-%m-%Y'))
    time.sleep(0.07)
    os.system((datetime.date.today()-datetime.timedelta(days=1)).strftime('date %d-%m-%Y'))
    

class Controller():
    def __init__(this):
        this.running = 0
        this.start_time=0
        this.wait_for_manual = 1
    def periodic_call(this):
        if this.running == 0:
            if keyboard.is_pressed("o"):
                glitchday()
                time.sleep(0.5)
                this.start_time=time.perf_counter()-0.5
                this.running = 1
            if keyboard.is_pressed("p"):
                glitch(1)
                time.sleep(0.5)
                this.start_time=time.perf_counter()-0.5
                this.running=2
                
        elif this.running == 1:
            if keyboard.is_pressed("o"):
                time.sleep(0.5)
                this.running=0
            elif time.perf_counter()>this.start_time+15:
                glitchday()
                this.start_time=time.perf_counter()
        
        else:
            if keyboard.is_pressed("p"):
                time.sleep(0.5)
                this.running=0
            elif time.perf_counter()>this.start_time+(60/150):
                glitch(1)
                this.start_time=time.perf_counter()

        
        if this.wait_for_manual ==1:
            if keyboard.is_pressed("r"):
                glitch(5)
                this.wait_for_manual = 0
        else:
            if not keyboard.is_pressed("r"):
                this.wait_for_manual = 1
            

   
time.sleep(0)
c=Controller()
while True:
    c.periodic_call()
    time.sleep(0.01)
