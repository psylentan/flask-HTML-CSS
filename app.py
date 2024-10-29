# This is basic
#! This is important
#? This is a question
#TODO

from flask import Flask, render_template
from config import secret
from tryme import image_url

#Creating a flask App
app = Flask(__name__)

#Routing
@app.route('/')
#Function
# def hello_world():
# return f'''<img src="{image_url}"> this is our dall-e image</p>'''

def index():
    return render_template('index.html', image_url=image_url)


#Running Condition
if __name__ == "__main__":
    #App.run --> run the application
    #Debug=TRUE --> Show all the errors in the terminal
    app.run(debug=True)