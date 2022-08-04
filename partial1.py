import datetime, os, time
change_time_sec=1
changes_per_minute=150


def glitch():
    os.system((datetime.datetime.today()+datetime.timedelta(seconds=change_time_sec)).strftime('time %H:%M:%S'))
    time.sleep(0.07)
    os.system((datetime.datetime.today()-datetime.timedelta(seconds=change_time_sec)).strftime('time %H:%M:%S'))

time.sleep(10)
while True:
    glitch()
    time.sleep(60/changes_per_minute-0.1)
