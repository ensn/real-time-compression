import datetime, os, time

def glitch():
    os.system((datetime.date.today()+datetime.timedelta(days=1)).strftime('date %d-%m-%Y'))
    time.sleep(0.07)
    os.system((datetime.date.today()-datetime.timedelta(days=1)).strftime('date %d-%m-%Y'))

time.sleep(10)
while True:
    glitch()
    time.sleep(15)
