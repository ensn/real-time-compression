import datetime, os, time
change_time_sec=1
changes_per_minute=300


wait=60/changes_hz
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
    
