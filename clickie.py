import time as t
from datetime import date
import keyboard
import random


def keyboard_input(input_in):
    keyboard.write('var x = document.querySelector(\'button[data-control-name="{}"]\').click();'.format(input_in))
    keyboard.press_and_release('enter')


inputs = ['companies_follow', 'group_join', 'people_connect', 'series_subscribe']
times = 0
reload_times = 100
first_time = True

companies_follow = 0
group_join = 0
people_connect = 0

keyboard.press_and_release('Ctrl+shift+k')
while True:
    if first_time:
        t.sleep(3)
        keyboard.press_and_release('Ctrl+shift+k')
        first_time = False

    r_input = random.randrange(0, len(inputs))
    if r_input == 0:
        companies_follow += 1
        t.sleep(random.randrange(1, 5))
        keyboard_input(inputs[r_input])
    if r_input == 1:
        group_join += 1
        t.sleep(random.randrange(2, 7))
        keyboard_input(inputs[r_input])

    if r_input == 2:
        people_connect += 1
        t.sleep(random.randrange(13, 20))
        keyboard_input(inputs[r_input])
    
    if r_input == 3:
        group_join += 1
        t.sleep(random.randrange(2, 7))
        keyboard_input(inputs[r_input])

    print(r_input)

    times += 1

    if times >= reload_times:
        keyboard.press_and_release('Ctrl+r')
        ra_time = random.randrange(6, 12)
        print("restarting in {}".format(ra_time))
        print("{},{},{};".format(companies_follow, group_join, people_connect))
        t.sleep(ra_time)
        times = 0

    key = keyboard.is_pressed('esc')
    if key:
        with open("{}".format(date.today()), "w+") as file:
            file.write("{},{},{};".format(companies_follow, group_join, people_connect))
        file.close()
        break

with open("{}".format(date.today()), "w+") as file:
    file.write("{},{},{};".format(companies_follow, group_join, people_connect))

file.close()
exit(0)
