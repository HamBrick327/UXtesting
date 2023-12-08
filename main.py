from openai import OpenAI
from os import getenv
from scrubadub import clean
import tkinter as tk
import customtkinter as ctk
from time import time, strftime

apiKey = getenv("OPENAIKEY2")
log = open("log.txt", 'a')


def openaiGenerate(prompt):
    print("sent openai api request")
    start = time()
    client = OpenAI(api_key=apiKey)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": '''You are a school teacher and shall follow the following rules:
     
     - you will be given an article that you need to re-write on a level a sixth-grader can read and understand
     - you will be given special escape sequences like {{EMAIL}} and {{PHONE}}, please leave these as they are.
     - please ensure to keep the same message and information as the article, but rewritten to be understood by a sixth-grader
     '''},
    {"role": "user", "content": str(prompt)}
    ]
    )
    print(f"openai responded in {time() - start} seconds")
    log.write("\n\n")
    log.write(strftime("%H:%M %m-%e"))
    log.write(completion.choices[0].message.content)
    return completion.choices[0].message.content


ctk.set_appearance_mode("Dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("1000x500")
app.title("ChatGPT article rewriter")
# app.overrideredirect(True) ## this will remove the toolbar (x button, fullscreen button, minimize button)

# frame = ctk.CTkFrame(master=app)
# frame.pack()
# entry = ''

## tkinter keypress wrapper function
def keypressEvent(event):
    print("keypress event called")
    userInput = text.get("0.0", 'end')
    userInput = clean(userInput)
    ## send gotten text to openai
    gptRewrite = openaiGenerate(clean(text=userInput))
    output.insert("0.0", gptRewrite)


############## TEXT ENTRY ####################
# entry = ctk.CTkEntry(master=frame, placeholder_text="press enter to enter")
# entry.pack(pady=10, padx=10)

text = ctk.CTkTextbox(app, width=400, height=300)

text.insert("0.0", "input") ## insert at line 0 character 0 (column 0, row 0)
text.pack(padx=10, pady=10, side="left", anchor=tk.N)

# Create a label to display the result
output = ctk.CTkTextbox(app, width=400, height=300)

output.insert("0.0", text="output")
output.pack(padx=10, pady=10, side="right", anchor=tk.N)


text.bind('<Return>', keypressEvent)

app.mainloop()