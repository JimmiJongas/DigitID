import NeuralNetwork


print "Trying to make a neural network..."
nn = NeuralNetwork.NeuralNetwork([10, 10, 10])
print "Seems to have worked.\n"


print "Trying to make an invalid neural network..."
try:
  nn = NeuralNetwork.NeuralNetwork([10])
except NeuralNetwork.ArchitectureException as e:
  print "Good job, we don't allow NNs with one layer, caught exception:\n", e

