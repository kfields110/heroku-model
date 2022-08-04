import flask
from flask import Flask, render_template, request
import pickle
import numpy as np
import house_price

# Running the flask app
app = Flask(__name__)

#load model using pickle
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', "POST"])
def home():
    if request.method == "POST":
        bedrooms = int(request.form['num_bedrooms'])
        bathrooms = int(request.form['num_bathrooms'])
        sqft = int(request.form['Sq_ft'])
        year = int(request.form['year_built'])
        prediction = house_price.house_prediction([[bedrooms, bathrooms, sqft, year]])
        

    return render_template('index.html', pred = prediction)

if __name__ == '__main__':
    app.run(debug=True)
