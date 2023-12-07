import tkinter as tk
# from threading import Thread
import customtkinter as ctk
# from time import time, sleep
from scrubadub import clean
# import requests
from os import getenv
from openai import OpenAI

'''
TODO add openai api support
TODO scrubadub openai prompt
'''
apiKey = getenv("OPENAIKEY2")


##### links I need to remember ################
##### links I need to remember ################
'''
https://youtu.be/JDU-ycsxvqM?si=fYYgmRc_azqzHyww
https://youtu.be/1itG8q-sCGY?si=r4HOdwhsYHHWl1U3
https://github.com/TomSchimansky/CustomTkinter
https://stackoverflow.com/questions/27215326/tkinter-keypress-and-keyrelease-events
'''

def openaiGenerate(prompt):
    client = OpenAI(api_key=apiKey)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": '''You are a school teacher and shall follow the following rules:
     
     - you will be given an article that you need to re-write on a level a sixth-grader can read and understand
     - you will be given special escape sequences like {{EMAIL}} and {{PHONE_NUMBER}}, please leave these as they are.
     - 
     '''},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)



ctk.set_appearance_mode("Dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("500x500")
# app.overrideredirect(True) ## this will remove the toolbar (x button, fullscreen button, minimize button)
# app.overrideredirect(True) ## this will remove the toolbar (x button, fullscreen button, minimize button)

frame = ctk.CTkFrame(master=app)
frame.pack()
entry = ''

## tkinter keypress wrapper function
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



# tinker = tk.Tk()
# 
# tkinter window stuff
# tinker.geometry("1000x500")
# 
# text = tk.Text(tinker, height=10, width=20)
# text2 = tk.Text(tinker, height=10, width=20)
# 
# l = tk.Label(tinker, text = "input text")
# l2 = tk.Label(tinker, text = "output text")
# 
# l.config(font=("Courier", 14))

# b1 = tk.Button(tinker, text="button1", command= print("button1 pressed"))
# b2 = tk.Button(tinker, text="exit", command= tinker.destroy)
# 
# text.pack(side=tk.LEFT)
# text2.pack(side=tk.RIGHT)
# l.pack(side=tk.LEFT)
# l2.pack(side=tk.RIGHT)
# 
# b1.pack()
# b2.pack()
# 
# text.insert(tk.END, {text})
# 
# tk.mainloop()
# 