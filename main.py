import datetime
import pyglet
from time import sleep

music = pyglet.resource.media('birds.mp3')
time_now = datetime.datetime.now()
print(time_now)

print('День')
day = input()
print('Час')
hour = input()
print('Минуты')
minutes = input()

if len(day == 1):
    day = '0' + day
if len(hour == 1):
    hour = '0' + hour
if len(minutes == 1):
    minutes = '0' + minutes

while True:
    time_now = datetime.datetime.now()
    if str(time_now.hour) == hour and str(time_now.minute) == minutes and str(time_now.day) == day:
        music.play()
        break
    sleep(1)
pyglet.app.run()
