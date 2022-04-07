# import "packages" from flask

from flask import Flask, render_template, request
import requests

# create a Flask instance
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
# map URL route for function below

def base():
    return render_template("layouts/base.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True, port="5001")
