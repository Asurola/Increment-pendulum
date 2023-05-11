import tkinter as tk

# Create a list of questions and answers
questions = [
    {"question": "Question 1: Does mass affect the period of the pendulum?", "answer": "False"},
    {"question": "Question 2: Kinetic energy increases when the object is static (not moving)", "answer": "False"},
    {"question": "Question 3: Gravitational potential energy is the highest \n in between the extreme ends of the pendulum swing", "answer": "False"},
    {"question": "Question 4: Gravitational potential energy = Total energy - Kinetic energy", "answer": "True"},
    {"question": "Question 5: If the metal bob of a simple pendulum is replaced by a \n wooden bob, the time period will change", "answer": "True"}
]

# Create variables to keep track of the current question and score
current_question = 0
score = 0

# Create a new window for the quiz
quiz_window = tk.Tk()
quiz_window.title("Quiz")
quiz_window.geometry("850x600")
quiz_window.config(bg="#f5f5f5")

question_frame = tk.Frame(quiz_window, bg="#f5f5f5")
question_frame.grid(pady=20, padx=20, column=0, row=0)

# create the question label to hold the question in a box with a border and center it in the window
question_label = tk.Label(question_frame, text=questions[current_question]["question"], font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333333", borderwidth=2, relief="solid", width=60, height=6, anchor="center")
question_label.grid(pady=20, padx=20, column=0, row=0, columnspan=2)

answer_frame = tk.Frame(quiz_window, bg="#f5f5f5")
answer_frame.grid(pady=20, padx=20, column=0, row=1)

instruction = tk.Label(answer_frame, text="Select your answer and click Next to move to the next question", font=("Arial", 16, "italic"), bg="#f5f5f5", fg="#333333")
instruction.grid(pady=10, padx=10, column=0, row=1, columnspan=2)

# Create variables to store the user's answer
answer = tk.StringVar()
answer.set(None)

# Create radio buttons for True and False
true_radio = tk.Radiobutton(answer_frame, text="True", font=("Arial", 16, "italic"), variable=answer, value="True", bg="#f5f5f5", fg="#333333")
false_radio = tk.Radiobutton(answer_frame, text="False", font=("Arial", 16, "italic"), variable=answer, value="False", bg="#f5f5f5", fg="#333333")
true_radio.grid(pady=5)
false_radio.grid(pady=5)

# Create a function to verify the user's answer and move to the next question and display the result upon pressing the Next button
def next_question():
    global current_question, score

    # Check if the user's answer is correct
    if answer.get() == questions[current_question]["answer"]:
        score += 1

    # display whether the answer is correct or wrong
    if answer.get() == questions[current_question]["answer"]:
        result_label.config(text=f"Correct!", fg="green")
    else:
        result_label.config(text=f"Wrong!", fg="red")

    # place the result label in the window under the radio buttons
    result_label.pack(side="top", pady=20, fill="x", expand=True)

    # Clear the user's answer
    answer.set(None)

    # Move to the next question
    current_question += 1
    if current_question < len(questions):
        question_label.config(text=questions[current_question]["question"])
    else:
        question_label.config(text="End of quiz!")
        next_button.pack_forget()
        submit_button.pack(side="right", padx=20, pady=20, fill="x", expand=True, anchor="e")

def back_to_menu():
    global current_question, score
    current_question = 0
    score = 0
    quiz_window.destroy()

# Create a function to display the user's score when they submit their answers
def submit_answers():
    result_label.config(text=f"Quiz complete! Your score is {score}/{len(questions)}.")

# create a frame to hold the buttons and the result label
button_frame = tk.Frame(quiz_window, bg="#f5f5f5")
button_frame.grid(pady=20, padx=20, column=0, row=2)

# Create a button to submit the answer and move to the next question
next_button = tk.Button(button_frame, text="Next", bg="#4CAF50", fg="white", font=("Arial", 12), command=next_question)
next_button.pack(side="left", padx=20, pady=20, fill="x", expand=True, anchor="w")

# Create a button to submit the answers and display the user's score
submit_button = tk.Button(button_frame, text="Submit", bg="#4CAF50", fg="white", font=("Arial", 12), command=submit_answers)
submit_button.pack(side="right", padx=20, pady=20, fill="x", expand=True, anchor="e")

# Create a label to display the result
result_label = tk.Label(button_frame, fg="white", font=("Arial", 20))
result_label.pack(side="top", pady=20, fill="x", expand=True, anchor="center")

back_button = tk.Button(button_frame, text="Back", bg="Purple", fg="white", font=("Arial", 12), command=back_to_menu)
back_button.pack(side="bottom", padx=20, pady=20, fill="x", expand=True, anchor="e")

quiz_window.resizable(False, False)
quiz_window.mainloop()