import numpy as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder='templates', static_folder='static')

model = pickle.load(open('customer_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('after.html', data='Predicted price :{} $'.format(output))

if __name__ == '__main__':

  app.run()
  app.debug = True