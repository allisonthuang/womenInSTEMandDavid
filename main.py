# import "packages" from flask

from flask import Flask, render_template, request
import requests

# create a Flask instance
app = Flask(__name__)


#from gigiChat import app_gigiChat
#app.register_blueprint(app_gigiChat)

# create a Flask instance
# connects default URL to render index.html

@app.route('/base/')
def base():
    return render_template("layouts/base.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True, port="5001")
