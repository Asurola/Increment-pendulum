import math
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib import animation
import sys
import os


length=100
mass=10
angle=0
w=0
g=9.81
import subprocess
status="down"#down or up
switch=True

mainwindow=tk.Tk()
mainwindow.title("Pendulum Simulation")
mainwindow.geometry("900x1300+900+10")
# make the window fullscreen by default
mainwindow.config(bg="#f5f5f5")


c_h=1000
c_w=1000
DIAMETER=50
pivotx,pivoty=c_w/2,100
centralx,centraly=pivotx,pivoty+length
length=100
canvas=tk.Canvas(mainwindow,height=c_h,width=c_w)
canvas.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH, anchor=tk.NW)

canvas.create_oval(centralx-DIAMETER/2,centraly-DIAMETER/2,centralx+DIAMETER/2,centraly+DIAMETER/2,fill='red',width=2)
canvas.create_line(c_w/2,10,centralx,centraly,fill='dodger blue',width=6)
    
def calculate_energy(length,mass,angle,angularvelocity,g=9.81):
    global a_scale
    height=length-length*math.cos(DtoR(angle))
    velocity=length*angularvelocity
    potential_energy=mass*g*height
    total_energy=mass*g*(length-length*math.cos(DtoR(a_scale.get())))
    kinetic_energy=total_energy-potential_energy
    return kinetic_energy,potential_energy,total_energy


def Slide(move):
    global length, w, angle,mass,m_scale,l_scale,g,canvas,centralx,centraly,pivotx,pivoty,g_scale,DIAMETER
    mass=m_scale.get()
    length=l_scale.get()
    angle=a_scale.get()
    g=g_scale.get()
    DIAMETER=mass*5
    centralx=pivotx+length*math.sin(DtoR(angle))
    centraly=pivoty+length*math.cos(DtoR(angle))
    canvas.delete(tk.ALL)
    canvas.create_oval(centralx-DIAMETER/2, centraly-DIAMETER/2, centralx+DIAMETER/2, centraly+DIAMETER/2, fill='red', width=2)
    canvas.create_line(c_w/2, 10, centralx, centraly, fill='dodger blue', width=6)
    

def animate_pendulum():
    global angle,mass,g,centralx,centraly,w,canvas,length,submit_button,switch
    w=w+g/length*math.sin(DtoR(angle))
    angle=angle-w
    centralx=pivotx+length*math.sin(DtoR(angle))
    centraly=pivoty+length*math.cos(DtoR(angle))

    canvas.delete(tk.ALL)  # Clear the canvas
    canvas.create_oval(centralx-DIAMETER/2, centraly-DIAMETER/2, centralx+DIAMETER/2, centraly+DIAMETER/2, fill='red', width=2)
    canvas.create_line(c_w/2, 10, centralx, centraly, fill='dodger blue', width=6)
    if switch:
        canvas.after(10, animate_pendulum)

def start():
    global angle,mass,g,centralx,centraly,w,canvas,length,submit_button,switch
    m_scale["state"] = tk.DISABLED
    l_scale["state"] = tk.DISABLED
    a_scale["state"] = tk.DISABLED
    g_scale["state"] = tk.DISABLED
    submit_button["state"] = tk.DISABLED
    switch = True
    animate_pendulum()
    # Call animation function with interval
    ani = animation.FuncAnimation(fig, animate, interval=10)

    # Show plot
    plt.show()

def DtoR(degree):
    return math.pi/180*degree

# Reset the pendulum and the parameters
def reset():
    plt.close()
    subprocess.Popen([sys.executable] + sys.argv)
    sys.exit()

#frame for buttons and sliders and labels to be placed to the right of the canvas
frame=tk.Frame(mainwindow)
frame.place(relx=0.8,rely=0.1,relwidth=0.2,relheight=0.8,anchor='n')

m_label=tk.Label(frame,text="Mass(kg)",font=("Arial",15))
m_label.pack(side=tk.TOP,anchor='w',padx=10,fill=tk.X,expand=True)
m_scale=tk.Scale(frame,from_=10,to=100,resolution=0.1,orient=tk.HORIZONTAL, command = Slide ,length=300,width=30,font=("Arial",15))
m_scale.pack()

l_label=tk.Label(frame,text="Length(m)",font=("Arial",15))
l_label.pack(side=tk.TOP,pady=10,anchor='w',padx=10,fill=tk.X,expand=True)
l_scale=tk.Scale(frame,from_=100,to=300,resolution=0.1,orient=tk.HORIZONTAL, command = Slide, length=300,width=30,font=("Arial",15))
l_scale.pack()

a_label=tk.Label(frame,text="Initial Angle (degrees)",font=("Arial",15))
a_label.pack(side=tk.TOP,pady=10,anchor='w',padx=10,fill=tk.X,expand=True)
a_scale=tk.Scale(frame,from_=-90,to=90,orient=tk.HORIZONTAL,command=Slide,state="normal",length=300,width=30,font=("Arial",15))
a_scale.pack()

g_label=tk.Label(frame,text="Gravitational acceleration (m/s^2)",font=("Arial",15))
g_label.pack(side=tk.TOP,pady=10,anchor='w',padx=10,fill=tk.X,expand=True)
g_scale=tk.Scale(frame,from_=1,to=100,resolution=0.01,orient=tk.HORIZONTAL,command=Slide,state="normal",length=300,width=30,font=("Arial",15))
g_scale.pack()
g_scale.set(9.81)

submit_button=tk.Button(frame,text="Start",command=start,width=25,height=2,font=("Arial",15))
reset_button=tk.Button(frame,text="Reset",command=reset,width=25,height=2,font=("Arial",15))
reset_button.pack(pady=10)
submit_button.pack(pady=10)

# Create lists to store energy values
kinetic_energy_list=[]
potential_energy_list=[]
total_energy_list=[]

# Set up figure and axis
fig,ax=plt.subplots()

# Define animation function
def animate(i):
    global w,angle
    # Calculate energies
    kinetic_energy,potential_energy,total_energy=calculate_energy(length, mass, angle, w, g)
    kinetic_energy_list.append(kinetic_energy)
    potential_energy_list.append(potential_energy)
    total_energy_list.append(total_energy)
    
    # Clear previous plot
    ax.clear()
    
    # Plot energy values
    ax.plot(kinetic_energy_list, label='Kinetic Energy')
    ax.plot(potential_energy_list, label='Potential Energy')
    ax.plot(total_energy_list, label='Total Energy')
    
    # Add legend and axis labels
    ax.legend()
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Energy (J)')
    ax.set_title('Energy of Pendulum')
    
    # Update angle and angular velocity
    w+=g/length*math.sin(DtoR(angle))
    angle-=w


# define back function to destroy the current windows and return to main menu
def back():
    mainwindow.destroy()  
    plt.close()

# making a second pendulum
c_h=2000
c_w=2000
DIAMETER=50
pivotx,pivoty=c_w/4,200
centralx,centraly=pivotx,pivoty+length
length=100
canvas=tk.Canvas(mainwindow,height=c_h,width=c_w)
canvas.pack(side=tk.LEFT, padx=20, pady=20, expand=True, fill=tk.BOTH, anchor=tk.NW)

canvas.create_oval(centralx-DIAMETER/2,centraly-DIAMETER/2,centralx+DIAMETER/2,centraly+DIAMETER/2,fill='red',width=2)
canvas.create_line(c_w/4,20,centralx,centraly,fill='dodger blue',width=6)


# Back button to return to main menu
back_button = tk.Button(frame, text="Back", command=back, width=25,height=2,font=("Arial",15))
back_button.pack(pady=10)

mainwindow.mainloop()