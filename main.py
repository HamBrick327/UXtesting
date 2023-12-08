from openai import OpenAI
from os import getenv
from scrubadub import clean
import tkinter as tk
import customtkinter as ctk
from time import time

apiKey = getenv("OPENAIKEY2")

def openaiGenerate(prompt):
    print(time() + ": sent openai api request")
    start = time()
    client = OpenAI(api_key=apiKey)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": '''You are a school teacher and shall follow the following rules:
     
     - you will be given an article that you need to re-write on a level a sixth-grader can read and understand
     - you will be given special escape sequences like {{EMAIL}} and {{PHONE_NUMBER}}, please leave these as they are.
     - 
     '''},
    {"role": "user", "content": str(prompt)}
    ]
    )
    print(f"openai returned call in {time() - start} seconds")
    return completion.choices[0].message.content


ctk.set_appearance_mode("Dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("500x500")
# app.overrideredirect(True) ## this will remove the toolbar (x button, fullscreen button, minimize button)

frame = ctk.CTkFrame(master=app)
frame.pack()
entry = ''

## tkinter keypress wrapper function
def keypressEvent(event):
    userInput = text.get()
    ## send gotten text to openai
    openaiGenerate(clean(text=userInput))
    resultLabel.insert("0.0", "")
    print("keypress event called")


############## TEXT ENTRY ####################
entry = ctk.CTkEntry(master=frame, placeholder_text="press enter to enter")
entry.pack(pady=10, padx=10)

text = ctk.CTkTextbox(app)

text.insert("0.0", "press enter to enter") ## insert at line 0 character 0 (column 0, row 0)
text.pack(padx=10, pady=10, anchor=ctk.W)

# Create a label to display the result
resultLabel = ctk.CTkLabel(master=frame, text="")
resultLabel.pack(pady=10)

output = ctk.CTkTextbox(app, state="disabled")

entry.bind('<Return>', keypressEvent)

app.mainloop()