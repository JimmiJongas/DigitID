
from numpy import matrix


class Layer:
  def __init__(self,numNodes,numInputs,eps,theta=None):
    # numNodes both numInputs both includes bias node
    self.nNodes = numNodes
    self.nInputs = numInputs
    if type(theta) == type(matrix(1)):
      # Check that passed theta is the correct size for the layer.
      # Number of rows in theta should be equal it number of nodes in layer.
      # Number of columns should be equal to the number of inputs from the 
      # previous layer (including the bias term).
      thetaSize = theta.shape
      #print thetaSize
      if(thetaSize[0] == numNodes and thetaSize[1] == numInputs):
        self.theta = theta
      else:
        print "Hey fucker you gave me a matrix of the wrong size"
        #randomInitialize(numNodes,numInputs,eps)
    else:
      print "Random initialize"
      #randomInitialize(eps)


### Custom exception class for handling problems with architecture 
class ArchitectureException(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)


class NeuralNetwork:
  ### Constructor which takes architecture for neural network.  Architecture 
  ### is specified as a list of integers
  def __init__(self, arch):
    self.arch = arch
    self.layers = []
    if len(self.arch) < 2:
      raise ArchitectureException("Must have at least two layers to be a " + 
                                  "neural network, invalid arcitecture " + 
                                  "specified: " + str(self.arch))
                      
    # Input to second layer will be number of inputs 
    inputCount = arch[0]
    for nodeCount in arch[1:]:
      if not type(nodeCount) == type(3):
        raise ArchitectureException("Invalid node count:" + str(nodeCount))

      self.layers.append((inputCount, nodeCount))
      # Input to next layer will be number of nodes in this layer
      inputCount = nodeCount



