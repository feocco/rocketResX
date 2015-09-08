from tkinter import *
from tkinter import ttk
from rocketResX import RocketResX

def callback():
	rocket = RocketResX()
	rocket.runtime(1)

def callback2():
	rocket = RocketResX()
	rocket.runtime(2)

root = Tk()

button1 = ttk.Button(root, text = '1 Monitor')
button1.grid(row = 1, column = 0)
button2 = ttk.Button(root, text = '2 Monitors')
button2.grid(row = 1, column = 1)

button1.config(command = callback)
button2.config(command = callback2)

label = ttk.Label(root, text = 'How many monitors would you like to play on?').grid(row = 0, column = 0)
label2 = ttk.Label(root, text = 'Will close in 10 seconds').grid(row = 2, column = 0)

root.after(10000, lambda: root.destroy())
root.mainloop()