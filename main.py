from openai import OpenAI
from os import getenv
from scrubadub import clean
import tkinter as tk
import customtkinter as ctk
from time import time, strftime

apiKey = getenv("OPENAIKEY2")
log = open("log.txt", 'a')
grade = ''

## stolen from docs
def optionmenu_callback(choice):
    global grade
    print("dropdown clicked:", choice)
    grade = choice

def openaiGenerate(prompt, gradelevel):
    print(f"sent openai api request with grade {grade}")
    start = time()
    client = OpenAI(api_key=apiKey)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {f"role": "system", "content": '''You are a school teacher and shall follow the following rules:
     
     - you will be given an article that you need to re-write on a level someone in grade {gradelevel} would be able to read and understand
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


ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("1000x500")
app.title("ChatGPT rewriter")


## tkinter keypress wrapper function
def keypressEvent(event):
    global grade
    print("keypress event called")
    userInput = text.get("0.0", 'end')
    userInput = clean(userInput)
    
    ## send gotten text to openai
    gptRewrite = openaiGenerate(clean(text=userInput), gradelevel=grade)

    ## shove in the chatGPT rewritten stuff
    output.delete("0.0", 'end')
    output.insert("0.0", gptRewrite)

optionmenu = ctk.CTkOptionMenu(app, values=["Kindergarten", '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], anchor="w", command=optionmenu_callback)
optionmenu.set("select grade level")
optionmenu.pack(padx=10, pady=10, side="top", anchor=tk.N)

############## TEXT ENTRY ####################
text = ctk.CTkTextbox(app, width=400, height=300)

text.insert("0.0", "press enter to submit") ## insert at line 0 character 0 (column 0, row 0)
text.pack(padx=10, pady=10, side="left", anchor=tk.N)

## output label to display data gotten back from openai
output = ctk.CTkTextbox(app, width=400, height=300)

output.insert("0.0", text="output")
output.pack(padx=10, pady=10, side="right", anchor=tk.N)


text.bind('<Return>', keypressEvent)

app.mainloop()