trigger_key="b"



import datetime, os, time, keyboard

def glitch():
    os.system((datetime.date.today()+datetime.timedelta(days=1)).strftime('date %d-%m-%Y'))
    time.sleep(0.07)
    os.system((datetime.date.today()-datetime.timedelta(days=1)).strftime('date %d-%m-%Y'))


class Nodoubletap():
    def __init__(this, trigger):
        this.trigger = trigger
        this.wait = 1
    def periodic_call(this):
        if this.wait == 1:
            if keyboard.is_pressed(this.trigger):
                glitch()
                this.wait = 0
        else:
            if not keyboard.is_pressed(this.trigger):
                this.wait = 1

   
time.sleep(0)
controller=Nodoubletap(trigger_key)
while True:
    controller.periodic_call()
    time.sleep(0.01)
