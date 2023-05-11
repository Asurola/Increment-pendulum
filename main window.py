import tkinter as tk
import os
import subprocess
import sys
from PIL import ImageTk, Image, ImageSequence

root = tk.Tk()
root.title("Simple pendulum animation")

# set window size and position
root.geometry("1300x500+200+200")
screen_width = 600
screen_height = 500

# create animation frame
animation_frame=tk.Frame(root)
animation_frame.grid(row=0,column=0,pady=10,padx=10)

# import GIF
GIF = Image.open(os.path.realpath(os.path.dirname(__file__))+'\\Oscillating_pendulum.GIF')
GIF_frames = []
for frame in ImageSequence.Iterator(GIF):
    frame = frame.resize((screen_width, screen_height), Image.ANTIALIAS)
    GIF_frames.append(ImageTk.PhotoImage(frame))
GIF_label = tk.Label(animation_frame, image=GIF_frames[0])
GIF_label.pack(expand=True,fill='both')
def animate_GIF(frame_num):
    GIF_label.configure(image=GIF_frames[frame_num])
    root.after(100, animate_GIF, (frame_num + 1) % len(GIF_frames))   
root.after(0, animate_GIF, 1)

# create widgets frame
widgets_frame=tk.Frame(root)
widgets_frame.grid(row=0,column=1,padx=10,pady=10)

# create a canvas widget
canvas = tk.Canvas(widgets_frame, width=600, height=500)
canvas.create_text(300, 100, text="Simple Pendulum", font=("Helvetica", 30))

def run_pendulum_simulation():
    name=os.path.basename(__file__)
    path=sys.argv[0].replace(name,"Pendulum Simulation.py")
    subprocess.Popen([sys.executable] + [path])
    
def overview():
    name=os.path.basename(__file__)
    path=sys.argv[0].replace(name,"Overview.py")
    subprocess.Popen([sys.executable] + [path])

def start_quiz():
    name=os.path.basename(__file__)
    path=sys.argv[0].replace(name,"Start quiz.py")
    subprocess.Popen([sys.executable] + [path])

# add menu items
menu_items = ["Pendulum Simulator", "Read Me", "Quiz Mode"]
for i in range(len(menu_items)):
    item = tk.Button(canvas, text=menu_items[i], font=("Arial", 20), fg="white", bg="#4CAF50", cursor="hand2", width=18)
    item_window = canvas.create_window(300, 200 + (i*75), anchor="center", window=item)
    
    # bind menu items to open new windows
    if i == 0:
        item.bind("<Button-1>", lambda e: run_pendulum_simulation())
    elif i == 1:
        item.bind("<Button-1>", lambda e: overview())
    elif i == 2:
        item.bind("<Button-1>", lambda e: start_quiz())

# add exit button
button = tk.Button(widgets_frame, text="Exit", command=root.quit, bg="#FF0000", font=("Arial", 16), fg="white", borderwidth=0, width=4)
button.pack(pady=400)
button_window = canvas.create_window(300, 400, window=button)

# display the canvas
canvas.pack()

# start the main event loop
root.mainloop()