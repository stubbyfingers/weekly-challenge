import tkinter as tk

window = tk.Tk()
window.title("My App")
window.geometry("500x500")

# A Frame is an empty box that holds other widgets. 
# The widgets in a frame have their own layout, so you can use grid() inside a frame, and pack() outside it
form = tk.Frame(window)
form.pack(pady=100)

label1 = tk.Label(form, text="Name:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(form)
entry1.grid(row=0, column=1)

# form = tk.Frame(window)
# form.pack(pady=10)

label2 = tk.Label(form, text="Email:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(form)
entry2.grid(row=1, column=1)

button = tk.Button(window, text="Send") #You can't use grid and pack in the same frame
button.pack()
# button = tk.Button(form, text="Send")
# button.grid(row=2)

window.mainloop()



# import tkinter as tk

# window = tk.Tk()
# window.title("My App")
# window.geometry("500x500")

# def output():
#     Name = entry1.get()
#     Email = entry2.get()
#     label3.config(text="Hello, "+ Name + ". Just to confirm, your email address is: " + Email)
#     entry1.delete(0, tk.END)
#     entry2.delete(0, tk.END)

# label1 = tk.Label(window, text="Name:", font=("Cambria, 10"))
# label1.grid(row=0, column=0)

# entry1 = tk.Entry(window)
# entry1.grid(row=0, column=1)

# label2 = tk.Label(window, text="Email:", font=("Cambria, 10"))
# label2.grid(row=1, column=0)

# entry2 = tk.Entry(window)
# entry2.grid(row=1, column=1)

# button = tk.Button(window, text="Save", font=("Cambria, 10"), command=output)
# button.grid(row=2, column=2)

# label3 =tk.Label(window)
# label3.grid(row=3, column=0)


# window.mainloop()



# import tkinter as tk

# window = tk.Tk()
# window.title("My App")
# window.geometry("300x200")

# button1 = tk.Button(window, text="One", font=("Cambria", 10))
# button1.pack(side="left")

# button2 = tk.Button(window, text="Two", font=("Cambria", 10))
# button2.pack(side="bottom")

# button3 = tk.Button(window, text="Three", font=("Cambria", 10))
# button3.pack(side="right")

# window.mainloop()




# import tkinter as tk

# window = tk.Tk()
# window.title("My App")
# window.geometry("500x500")

# def greet():
#     name = entry.get()
#     label.config(text="Hello, " + name)
#     entry.delete(0, tk.END) # delete(0, tk.END) deletes everything, from the first character (0) to the end (tk.END).

# label = tk.Label(window, text="What's your name?", font=("Cambria", 20))
# label.pack()

# entry = tk.Entry(window, font=("Cambria", 10))
# entry.pack()

# button = tk.Button(window, text="Enter", font=("Cambria", 10), command=greet)
# button.pack()

# window.mainloop()




# import tkinter as tk

# window = tk.Tk()
# window.geometry("500x500")
# window.title("My App")

# def double():
#     number = int(entry.get())
#     number = number * 2
#     label.config(text="The answer is " + str(number))

# label = tk.Label(window, text="Give me a number to double it for you", font=("Cambria", 15))
# label.pack()

# entry = tk.Entry(window, font=("Cambria", 10))
# entry.pack()

# button = tk.Button(window, text="Double", font=("Cambria", 10), command=double)
# button.pack()

# window.mainloop()




# import tkinter as tk

# window = tk.Tk()
# window.title("My App")
# window.geometry("500x500")

# def greet():
#     name = entry.get()
#     label.config(text="Hello, " + name)

# label =tk.Label(window, text="What's your name?", font=("Cambria", 20))
# label.pack()

# entry = tk.Entry(window, font=("Cambria, 15"))
# entry.pack()

# button = tk.Button(window, text="Save", font=("Cambria", 10), command=greet)
# button.pack()

# window.mainloop()




# import tkinter as tk

# window = tk.Tk()
# window.title("My App")
# window.geometry("500x500")

# def say_hello():
#     label1.config(text="Hello") #config() changes on option of a widget after it is created. Here, it changes the text of the label.

# count = 0
# def add_one():
#     global count
#     count += 1
#     label1.config(text=count)

# label1 = tk.Label(window, text="Hello!", font=("Cambria", 24), fg="white", bg="black")
# label1.pack()

# label2 = tk.Label(window, text="My name is Charity", font=("Times New Roman", 12))
# label2.pack() # pack() places the label in the window, at the top and in the middle. 
#               # Without pack(), the label is created, but you will not see it

# button = tk.Button(window,text="Click me", command=add_one)
# button.pack()

# button = tk.Button(window, text="Close", command=window.destroy)
# button.pack()


# window.mainloop()