from microbit import *
count = temperature()
while True:
    if button_a.was_pressed():
        display.scroll(count)    
        display.scroll('Nathan')
    