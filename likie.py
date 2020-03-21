import time as t
import keyboard

times = 0
t.sleep(10)
keyboard.press_and_release('Ctrl+shift+k')
while True:
    t.sleep(3)
    keyboard.write(
        'var x = document.querySelector(\'button[class=\"react-button__trigger artdeco-button artdeco-button--muted '
        'artdeco-button--4 artdeco-button--tertiary ember-view\"]\').click(); console.log(x)')
    keyboard.press_and_release('enter')

    times += 1
    print(times)
