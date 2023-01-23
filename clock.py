import tkinter as ui

import time
import math

window = ui.Tk()
window.geometry("600x600")


def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    # updating seconds hand
    seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

    # updating minutes hand
    minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    # updating hours hand
    hours_x = hours_hand_len * math.sin(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_x
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    window.after(1000, update_clock)


canvas = ui.Canvas(window, width=600, height=600, bg="white")
canvas.pack(expand=True, fill='both')

# create background
bg = ui.PhotoImage(file='akshat.png')
canvas.create_image(300, 300, image=bg)


# create clock hands
# seconds hand
center_x = 300
center_y = 300

seconds_hand_len = 195
minutes_hand_len = 165
hours_hand_len = 140

seconds_hand = canvas.create_line(300, 300, 300 + seconds_hand_len, 300 + seconds_hand_len, width=1.5, fill='red')
# minutes hand
minutes_hand = canvas.create_line(300, 300, 300 + minutes_hand_len, 300 + minutes_hand_len, width=2.5, fill='black')
# hours hand
hours_hand = canvas.create_line(300, 300, 300 + hours_hand_len, 300 + hours_hand_len, width=5, fill='black')

update_clock()

window.mainloop()