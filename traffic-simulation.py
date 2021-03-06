import Tkinter as tk
import threading
import time
from threading import Thread
from Tkinter import *

# horizontal road
light = True

def changeLights():
    global light
    light = not light

root = tk.Tk()
root.title("Traffic Simulation")
button = tk.Button(root, text = 'Change Lights', width = 25, command = changeLights)
button.pack()

# window size
# lane_width(px) = WIDTH
WIDTH = 60
SIZE = 10 * WIDTH

canvas = tk.Canvas(root, width = SIZE, height = SIZE, bg = "#FFE19C")
canvas.pack()

# draw the intersection on the screen
# canvas.create_line(x0, y0, x1, y1, ..., xn, yn, option, ...)

intersection_colors = [
    (0, 6 * WIDTH, SIZE, WIDTH * 4),
    (6 * WIDTH, 0, WIDTH * 4, SIZE)
]

for t in intersection_colors:
    canvas.create_rectangle(t, fill = "#999999", outline = '#999999')

intersection_data = [
    (0, 4 * WIDTH, SIZE, 4 * WIDTH),
    (0, 6 * WIDTH, SIZE, 6 * WIDTH),
    (4 * WIDTH, 0, 4 * WIDTH, SIZE),
    (6 * WIDTH, 0, 6 * WIDTH, SIZE)
]

for t in intersection_data:
    canvas.create_line(t, width = 5)

intersection_lines = [
    (0, 5 * WIDTH, SIZE, 5 * WIDTH),
    (5 * WIDTH, 0, 5 * WIDTH, SIZE)
]

for t in intersection_lines:
    canvas.create_line(t, width = 5, fill = "White")

padding = 10
class Car(Thread, object):
    def __init__(self, spawn, outline = 'blue', fill = 'blue'):
        self.spawn = spawn
        Thread.__init__(self)
        self.pos = self.getPos(spawn)
        self._x = 0
        self._y = 0
        self.rect = canvas.create_rectangle(self.pos, outline = outline, fill = fill)
        self.speed = (0, 0)
    def move(self):
        # print self._x
        if (self.spawn == 1):
            if(light):
                canvas.move(self.rect, self.speed[0], self.speed[1])
                self._x += self.speed[0]
                self._y += self.speed[1]
            else:
                if (abs(self._x) < 180):
                    canvas.move(self.rect, self.speed[0], self.speed[1])
                    self._x += self.speed[0]
                    self._y += self.speed[1]
                if (abs(self._x) > 190):
                    canvas.move(self.rect, self.speed[0], self.speed[1])
                    self._x += self.speed[0]
                    self._y += self.speed[1]

        if (self.spawn == 2):
            if(light):
                canvas.move(self.rect, self.speed[0], self.speed[1])
                self._x += self.speed[0]
                self._y += self.speed[1]
            else:
                if (abs(self._x) < 180):
                    canvas.move(self.rect, self.speed[0], self.speed[1])
                    self._x += self.speed[0]
                    self._y += self.speed[1]
                if (abs(self._x) > 190):
                    canvas.move(self.rect, self.speed[0], self.speed[1])
                    self._x += self.speed[0]
                    self._y += self.speed[1]


        if (self.spawn == 3):
            if(not light):
                canvas.move(self.rect, self.speed[0], self.speed[1])
                self._x += self.speed[0]
                self._y += self.speed[1]
            else:
                if (abs(self._y) < 180):
                    canvas.move(self.rect, self.speed[0], self.speed[1])
                    self._x += self.speed[0]
                    self._y += self.speed[1]
                if (abs(self._y) > 190):
                    canvas.move(self.rect, self.speed[0], self.speed[1])
                    self._x += self.speed[0]
                    self._y += self.speed[1]

        if (self.spawn == 4):
            if(not light):
                canvas.move(self.rect, self.speed[0], self.speed[1])
                self._x += self.speed[0]
                self._y += self.speed[1]
            else:
                if (abs(self._y) < 180):
                    canvas.move(self.rect, self.speed[0], self.speed[1])
                    self._x += self.speed[0]
                    self._y += self.speed[1]
                if (abs(self._y) > 190):
                    canvas.move(self.rect, self.speed[0], self.speed[1])
                    self._x += self.speed[0]
                    self._y += self.speed[1]

    def set_speed(self, x, y):
        self.speed = x, y
    def getPos(self, spawn):
        if (spawn == 1):
            a = 0
            b = 5 * WIDTH + padding
            c = WIDTH
            d = 6 * WIDTH - padding
            self._x = a
            self._y = b
            return (a, b, c, d)
        if (spawn == 2):
            a = SIZE
            b = 4 * WIDTH + padding
            c = 9 * WIDTH
            d = 5 * WIDTH - padding
            self._x = a
            self._y = b
            return (a, b, c, d)
        if (spawn == 3):
            c = 5 * WIDTH - padding + 20
            b = SIZE
            a = 4 * WIDTH + padding + 100
            d = 1 * WIDTH + 485
            self._x = a
            self._y = b
            return (a, b, c, d)
        if (spawn == 4):
            a = 5 * WIDTH - padding
            b = 0
            c = 4 * WIDTH + padding
            d = 1 * WIDTH
            self._x = a
            self._y = b
            return (a, b, c, d)

car1 = Car(1, outline = 'blue', fill = 'blue')
car1.set_speed(2, 0)
car2 = Car(2, outline = 'red', fill = 'red')
car2.set_speed(-2, 0)
car3 = Car(3, outline = 'red', fill = 'red')
car3.set_speed(0, -2)
car4 = Car(4, outline = 'green', fill = 'green')
car4.set_speed(0, 2)

# move cars
for x in range(10000):
    time.sleep(0.025)
    car1.move()
    car2.move()
    car3.move()
    car4.move()
    canvas.update()

# start the Simulation
root.mainloop()
