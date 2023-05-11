import tkinter as tk

def explanation_window():
    explanation_window = tk.Tk()
    explanation_window.title("Read Me")
    explanation_window.geometry("1920x1080")
    explanation_frame=tk.Frame(explanation_window)
    explanation_frame.pack(anchor="center")

    # Create a label to display the overview
    explanation_label = tk.Label(explanation_frame, text="How do Pendulums Work", font=("Arial", 24, "bold"), pady=5)
    explanation_label.grid(row=0, column=0, columnspan=4)

    # Create a frame to hold the explanation and terms labels
    label_frame = tk.Frame(explanation_frame, width=600, height=400)
    label_frame.grid(row=1, column=0, columnspan=4)

    # Create the explanation label and pack it to the left of the frame
    explanation_label = tk.Label(label_frame, text="A basic pendulum is a machine in which the point mass is hung from a fixed support by a light, inextensible string. The mean position of a simple pendulum is shown by a vertical line moving through a fixed support. The length of the simple pendulum, abbreviated as L, is the vertical distance from the point of suspension to the centre of mass of the suspended body while it is in the mean position. The resonant mechanism supporting this type of pendulum has a single resonant frequency.", font=("Arial", 12), wraplength=550, justify="center")
    explanation_label.grid(row=0, column=0, padx=10, pady=10)

    # Create the terms label and pack it below the explanation label
    terms_label = tk.Label(label_frame, text="Essential terms \nA simple pendulum's oscillating motion: The pendulum's periodic back and forth motion is referred to as oscillatory motion, and the equilibrium position is the oscillation's centre. \nThe time period of a basic pendulum is: It is symbolised by the letter 'T' and is defined as the amount of time needed for the pendulum to complete one full oscillation. \nThe amplitude of a basic pendulum: The distance the pendulum travels from its equilibrium point to one side is how it is defined. \nThe length of a basic pendulum is represented by the letter 'L' and is defined as the distance from the point of suspension to the centre of the bob.", font=("Arial", 12), wraplength=550, justify="center")
    terms_label.grid(row=1, column=0, padx=10, pady=10)

    # Add the terms, period, ke, and pe labels to the window in a grid
    terms_period_frame = tk.Frame(explanation_frame, width=600, height=400)
    terms_period_frame.grid(row=2, column=0, columnspan=4)

    period_label = tk.Label(terms_period_frame, text="Period", font=("Arial", 16, "bold"), wraplength=550, justify="center")
    period_label.grid(row=0, column=1, padx=10, pady=10)

    pe_label = tk.Label(terms_period_frame, text="Potential Energy", font=("Arial", 16, "bold"), wraplength=550, justify="center")
    pe_label.grid(row=0, column=2, padx=10, pady=10)

    # Add the explanations of period, ke, and pe to the grid
    period_explanation_label = tk.Label(terms_period_frame, text="Simple Pendulum Derivation Time Period. \nThe formula for the equation of motion is T - mg cos = mv2L. \nThe mass tends to be brought to its equilibrium position by the torque, \nτ = mgL × sinθ = mgsinθ × L = I × α \nIn small angles of oscillation, sin θ is near equal to θ, and can be abbreviated as so, \nTherefore, Iα = -mgLθ\nα = -(mgLθ)/I\n– ω02 θ = -(mgLθ)/I\nω02 = (mgL)/I\nω0 = √(mgL/I)\nUse I = ML2, where I represents the bob's moment of inertia\n0 = (g/L) is obtained.\nThus, the basic pendulum's time period can be calculated using the formula\nT = 2π/ω0 = 2π × √(L/g)", font=("Arial", 12), wraplength=550, justify="center")
    period_explanation_label.grid(row=1, column=1, padx=10, pady=10)

    ke_explanation_label = tk.Label(terms_period_frame, text="K.E = (1/2) mv^2 is the formula for the pendulum's kinetic energy.\nm is the pendulum's mass.\nv denotes the pendulum's speed.\nThe kinetic energy is zero at the highest position and is at its maximum at the lowest point. The overall energy, however, is stable over time.", font=("Arial", 12), wraplength=550, justify="center")
    ke_explanation_label.grid(row=2, column=1, padx=10, pady=10)

    pe_explanation_label = tk.Label(terms_period_frame, text="Potential energy\nThe fundamental equation for potential energy is:\nmgh = potential energy, where m is the object's mass, where g is gravitational acceleration, and h is the height of the object\nHowever, the rod or string acts as a restraint, preventing the pendulum's movement from being in free fall. The length L and angle θ are used to express the height. As a result, h = L(1 - cos )\nThe pendulum is at its highest position when θ = 900. When cos 900 equals 0, h equals L.\nTherefore, Potential Energy = mgL\nThe pendulum is at its lowest position when θ = 0. So, cos 0 = 1. As a result, h = L (1-1) = 0.\nPotential energy is equal to mgL (1-1)=0.\nAt all the points in between the potential energy is given as mgL (1 – cos θ).", font=("Arial", 12), wraplength=550, justify="center")
    pe_explanation_label.grid(row=1, column=2, padx=10, pady=10)

    back_button = tk.Button(explanation_frame, text="Back to Main Menu", font=("Arial", 14, "bold"), padx=20, pady=10, bg="#4CAF50", fg="white", relief="groove", command=explanation_window.destroy)
    back_button.grid(row=3, column=1, columnspan=2 , padx=10, pady=10)

def information_frame():
    overview_window = tk.Tk()
    overview_window.title("Read Me")
    overview_window.geometry("700x500")

    # Create a label to display the overview
    overview_label = tk.Label(overview_window, text="Welcome to the Pendulum program", font=("Arial", 20, "bold"), pady = 5)
    overview_label.pack()
    info_frame = tk.Frame(overview_window, width=600, height=400)
    info_frame.pack(pady=20)
    description_label = tk.Label(info_frame, text="This program simulates the motion of a simple pendulum. The user can change the length, mass, initial angle and graviational accelerationof the pendulum. The user can also start a quiz to test their knowledge of the simple pendulum.", font=("Arial", 12), wraplength=550, justify="center")
    description_label.pack(pady=10)
    Instructions_label = tk.Label(info_frame, text="Instructions: \n1. Use the sliders to change the length, mass, initial angle and gravitational acceleration of the pendulum. \n2. Click the 'Reset' button to reset the pendulum. \n3. Click the 'Start Quiz' button to start the quiz. \n4. 'Back' buttons are present along the program windows for ease of navigation", font=("Arial", 12), wraplength=550, justify="center")
    Instructions_label.pack(pady=10)
    back_button = tk.Button(overview_window, text="Back to Main Menu", font=("Arial", 14, "bold"), padx=20, pady=10, bg="#4CAF50", fg="white", relief="groove", command=overview_window.destroy)
    back_button.pack(pady=10)
    explanation_button = tk.Button(overview_window, text="Full Explanation to Pendulums", font=("Arial", 14, "bold"), padx=20, pady=10, bg="#4CAF50", fg="white", relief="groove", command=explanation_window)
    explanation_button.pack(pady=10)

    overview_window.mainloop()

information_frame()