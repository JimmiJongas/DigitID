import time 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy import io 


def getPixelMap(example):
  return np.reshape(example, (20, 20)).T



mat = io.loadmat('ex4data1.mat')


X = mat['X']




#f = plt.figure("mything")




nGrid = 10
mGrid = 10


samples = np.random.choice(np.size(X,0), nGrid * mGrid, replace=False)

(f, subplots) = plt.subplots(nGrid, mGrid)


n = 1 
for i in range(nGrid):
  for j in range(mGrid):
    
    p = subplots[i][j]
    p.axes.get_xaxis().set_visible(False)
    p.axes.get_yaxis().set_visible(False)
    
    pixMap = getPixelMap(X[samples[n-1]])  
    p.imshow(pixMap)

    n += 1
    
  

  