import datetime, os, time, keyboard
change_time_sec=1
changes_per_minute=150


wait=60/changes_per_minute
last_call=0
state=0


while True:
    if state==0:
        if time.perf_counter()>last_call+wait:
            last_call=time.perf_counter()
            os.system((datetime.datetime.today()+datetime.timedelta(seconds=change_time_sec)).strftime('time %H:%M:%S'))
            state=1
    else:
        if time.perf_counter()>last_call+wait:
            last_call=time.perf_counter()
            os.system((datetime.datetime.today()-datetime.timedelta(seconds=change_time_sec)).strftime('time %H:%M:%S'))
            state=0
    if keyboard.is_pressed("r"):
        os.system((datetime.date.today()+datetime.timedelta(days=1)).strftime('date %d-%m-%Y'))
        time.sleep(0.07)
        os.system((datetime.date.today()-datetime.timedelta(days=1)).strftime('date %d-%m-%Y'))
        time.sleep(5)
