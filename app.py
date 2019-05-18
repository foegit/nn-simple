import os
from flask import Flask, flash, redirect, render_template, request, url_for, jsonify
from m_network import NeuralNetwork
import numpy as np
from io import StringIO

net = NeuralNetwork()
app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
  try:
    content = request.get_json()
    if len(content['data']) == 0:
      return jsonify(error='Empty data'), 500
    data = np.genfromtxt(StringIO(content['data']), delimiter=',')
    net.set_data(data)
    net.train()
    predict_val = net.predict(float(content['predict']))
    return jsonify(val = round(predict_val, 2))
  except IndexError:
    return jsonify(error='Wrong data format'), 500
  except ValueError:
    return jsonify(error='Wrong data format'), 500

app.secret_key = 'fpaiajfbasshougiubfajs'
if __name__ == "__main__":
  app.run()
