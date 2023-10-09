from flask import Flask, render_template, jsonify
from time import sleep
from random import randint
import requests
import json
import os

print(os.getcwd())

app = Flask(__name__)
variable_to_display = 0

def variable():
    # return randint(1, 1000)
    try:
        response = requests.get(f"https://api.api-ninjas.com/v1/jokes?limit={1}", headers={'X-Api-Key' : "FWIYfCodkizNPtWSfjMNYw==BpZw8KgtJ4foUCyJ"})
        if response.status_code == requests.codes.ok:
            response = json.loads(response.text)[0]['joke']
            return response
    except:
        print("thing broke lmao")


# Define a route for the home page
@app.route('/')
def index():
    # Pass the variable to the HTML template
    return render_template('index.html', variable=variable())

@app.route('/get_variable')
def get_variable():
    # print(jsonify(variable=variable()))
    return jsonify(variable=variable())




if __name__ == '__main__':
    app.run(port=8080)



'''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Flask Variable Example</title>
</head>
<body>
    <h1>Variable Value: <span id="variable"></span></h1>

    <script>
        // update the variable in real time
        function updateVar() {
            fetch('/get_variable')
                .then(response => response.json())
                .then(data => {
                    //update variable on the webpage
                    document.getElementById('variable').innerText = data.variable;
                })
                .catch(error => console.error("Error:", error));
        }

        setInterval(updateVar, 100);
    </script>
</body>
</html>
'''