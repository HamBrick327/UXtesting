import tkinter as tk

tinker = tk.Tk()

## tkinter window stuff
tinker.geometry("1000x500")

text = tk.Text(tinker, height=10, width=20)

l = tk.Label(tinker, text = "input text")
#l.config(font=("Courier", 14))

b1 = tk.Button(tinker, text="button1", command= print("button1 pressed"))
b2 = tk.Button(tinker, text="exit", command= tinker.destroy)

l.pack()
text.pack()
b1.pack()
b2.pack()

# text.insert(tk.END, {text})

tk.mainloop()