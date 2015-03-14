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

