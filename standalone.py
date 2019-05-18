from m_network import NeuralNetwork

net = NeuralNetwork()
net.read_txt('test1.txt')
net.train()
print('k =', round(net.W, 2))
print(round(net.predict(33), 2))
