import tkinter as tk
def make_quiz():
    quiz_window = tk.Tk()
    quiz_window.title(text="Quiz")
    quiz_window.geometry("400x300")
main_window = tk.Tk()
main_window.geometry("400x300")
the_button = tk.Button(main_window,text="Quiz",command=make_quiz)
the_button.pack()
main_window.mainloop()


