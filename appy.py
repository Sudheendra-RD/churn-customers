import flask
from flask import Flask, request, jsonify, render_template
import jinja2
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('churn.pkl', 'rb'))

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/", methods=["POST", "GET"])
def preprocess():                                           
    if request.method == 'POST':
        a = request.form['age']
        b = request.form['CUS']
        c = request.form['gender']
        d = request.form['year']
        e = request.form['TDA']
        f = request.form['TDT']
        g = request.form['TCA']
        h = request.form['TCT']

        s_list = [a,b,c,d,e,f,g,h]
        new_list = [int(i) for i in s_list]
        df=np.array(new_list)
        data = df.reshape(1,-1)

        pre = model.predict(data)

        # if pre == 1:
        #     print('NO CHURN')
        # else:
        #     print('CHURN')

    return render_template("index.html", line_1= pre)


# class DataForm(Form):

if __name__ == "__main__":
    app.run(debug=True)



