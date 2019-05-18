import numpy as np

class NeuralNetwork:
  def __init__(self, e = 0.00001):
    self.X = []
    self.Y = []
    self.e = e
    self.W = 1


  def read_txt(self, filename):
    try:
      from_file = np.genfromtxt(filename, delimiter=',')
      self.set_data(from_file)
      return True
    except IOError:
      raise IOError


  # add plain data set contains 2 col (X, Y)
  # data represents as NumPy array
  def set_data(self, data):
    min_val = np.min(data)
    max_val = np.max(data)

    x = np.array(data[:, 0])
    y = np.array(data[:, 1])

    x = self.normalize_data(x, min_val, max_val)
    y = self.normalize_data(y, min_val, max_val)

    self.X = x
    self.Y = y

  def normalize_data(self, data, min_val=None, max_val=None):
    if min_val == None:
      min_val = np.min(data)
    if max_val == None:
      max_val = np.max(data)
    return [self.normalize(i, min_val, max_val) for i in data]

  def normalize(self, val, min_val, max_val):
    return round((val)/(max_val - min_val), 5)

  def train(self):
    perfect = False
    counter = 0
    while not perfect and counter < 1000:
        counter += 1
        for i in range(len(self.X)):
          perfect = True
          predict_val = self.predict(self.X[i])
          if self.Y[i] > predict_val + self.e or self.Y[i] < predict_val - self.e:
            perfect = False
            self.W += self.Y[i] - predict_val

  def predict(self, value):
    return value * self.W
