import tkinter as tk
from threading import Thread
import customtkinter as ctk
from time import time, sleep

##### references ################
'''
https://youtu.be/JDU-ycsxvqM?si=fYYgmRc_azqzHyww
https://youtu.be/1itG8q-sCGY?si=r4HOdwhsYHHWl1U3
https://github.com/TomSchimansky/CustomTkinter
https://stackoverflow.com/questions/27215326/tkinter-keypress-and-keyrelease-events
'''

ctk.set_appearance_mode("Dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("500x500")
# app.overrideredirect(True) ## this will remove the toolbar (x button, fullscreen button, minimize button)

frame = ctk.CTkFrame(master=app)
frame.pack()
entry = ''

def keypressEvent(event):
    userInput = entry.get()
    resultLabel.configure(text='You entered: ' + userInput)
    print("keypress event called")

############### STOLEN BUTTON CODE ####################################

# def button_function():
#     print("button pressed")

# Use CTkButton instead of tkinter Button
# button = ctk.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.0, rely=0.5, anchor=ctk.CENTER) ## relx means relative x, same for y. the value is the percentage across the window the widget goes

################# STOLEN TEXTBOX CODE ################################

# text = ctk.CTkTextbox(app)

# text.insert("0.0", "new text to insert") ## insert at line 0 character 0 (column 0, row 0)
# text.place(relx=0.1, rely=0.1, anchor=ctk.CENTER)

# sleep(5)
# string = text.get("0.0", "end") ## get all the text from 0, 0 to the end of the box
# print("\n\n TEXT INPUTTED BY USER: ", string)
# # text.delete("0.0", "end") ## delete all the text in the textbox
# # text.configure(state='disabled') ## make the textbox unwritable; read-only
BEGIN = time()

############## ALT TEXTBOX CODE ####################
entry = ctk.CTkEntry(master=frame, placeholder_text="press enter to enter")
entry.pack(pady=10, padx=10)

text = ctk.CTkTextbox(app)

text.insert("0.0", "new text to insert") ## insert at line 0 character 0 (column 0, row 0)
text.pack(padx=10, pady=10, anchor=ctk.W)

# Create a label to display the result
resultLabel = ctk.CTkLabel(master=frame, text="")
resultLabel.pack(pady=10)

entry.bind('<Return>', keypressEvent)

app.mainloop()



'''
tinker = tk.Tk()

## tkinter window stuff
tinker.geometry("1000x500")

text = tk.Text(tinker, height=10, width=20)
text2 = tk.Text(tinker, height=10, width=20)

l = tk.Label(tinker, text = "input text")
l2 = tk.Label(tinker, text = "output text")

#l.config(font=("Courier", 14))

# b1 = tk.Button(tinker, text="button1", command= print("button1 pressed"))
b2 = tk.Button(tinker, text="exit", command= tinker.destroy)

text.pack(side=tk.LEFT)
text2.pack(side=tk.RIGHT)
l.pack(side=tk.LEFT)
l2.pack(side=tk.RIGHT)

# b1.pack()
b2.pack()

# text.insert(tk.END, {text})

tk.mainloop()
'''