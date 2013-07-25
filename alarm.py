import time

sethour = input("hour = ")
setminute = input("minute = ")

status = 1

while(status):
    now = list(time.localtime())
    hour = now[3]
    minute = now[4]
    if hour == sethour and minute == setminute:
        print "Alarm On"
        status = 0