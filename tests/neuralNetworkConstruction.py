import NeuralNetwork


print "Trying to make a neural network..."
nn = NeuralNetwork.NeuralNetwork([10, 10, 10])
print "Seems to have worked.\n"


print "Trying to make a nonsensical neural network with one layer..."
try:
  nn = NeuralNetwork.NeuralNetwork([10])
except NeuralNetwork.ArchitectureException as e:
  print "Good job, we don't allow NNs with one layer, caught exception:\n", e


print "Trying to make a decimal neural network..."
try:
  nn = NeuralNetwork.NeuralNetwork([10, 3.14])
except NeuralNetwork.ArchitectureException as e:
  print "Good job, we don't allow NNs decimal node counts:\n", e
