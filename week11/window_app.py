import tkinter as tk

window = tk.Tk()
window.title("My App")
window.geometry("500x500")

label = tk.Label(window, text="Hello!", font=("Cambria", 24), fg="white", bg="black", )
label.pack()
label = tk.Label(window, text="My name is Charity", font=("Times New Roman", 12))
label.pack() #pack() places the label in the window, at the top and in the middle. 
             #Without pack(), the label is created, but you will not see it

window.mainloop()