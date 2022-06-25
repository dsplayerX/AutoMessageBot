import pyautogui as pg
import time

print('Starting!')
time.sleep(1)
print('You have 10 seconds to place the cursor in a text field or abort')
time.sleep(1)

countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

text_file = open('animals.txt', 'r')

String = 'You are a'

for word in text_file:
    pg.write(String + ' ' + word)
    pg.press('Enter')

print('Completed!')
