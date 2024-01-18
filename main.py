import pandas as pd
from flask import Flask,render_template,request
app=Flask(__name__)
data=pd.read_csv("Cleaned_data.csv")

@app.route('/')
def index():

    return render_template("index.html")
if__name__="__main__":
    app.run(debug=True,port=5001)
