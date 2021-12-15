import matplotlib.pyplot as plt 
import numpy as np
import pickle
from numpy import exp
import os

lr = np.load("TrainData/multi-lr.npy")
dft = np.load("TrainData/multi-lr-dft.npy")

plt.plot(lr[0])
plt.show()

plt.plot(dft[0])
plt.show()

lr_data = np.asarray(lr)
np.savetxt("TrainData/multi-lr.csv", lr_data, delimiter = ",")

dft_data = np.asarray(dft)
np.savetxt("TrainData/multi-lr-dft.csv", dft_data, delimiter = ",")

with open('TrainData/multi-lr.npy', 'rb') as f:
    W = np.load(f) #weight vector
    b = np.load(f) #bias
    lr_loss = np.load(f)
    lr_acc = np.load(f)

lr_data_acc = np.asarray(lr_acc)
np.savetxt("TrainData/multi-lr_acc.csv", lr_data_acc, delimiter = ",")
    
lr_data_loss = np.asarray(lr_loss)
np.savetxt("TrainData/multi-lr_loss.csv", lr_data_loss, delimiter = ",")

with open('TrainData/multi-lr-dft.npy', 'rb') as f:
    W = np.load(f) #weight vector
    b = np.load(f) #bias
    dft_loss = np.load(f)
    dft_acc = np.load(f)

dft_data_acc = np.asarray(dft_acc)
np.savetxt("TrainData/multi-lr-dft_acc.csv", dft_data_acc, delimiter = ",")
    
dft_data_loss = np.asarray(dft_loss)
np.savetxt("TrainData/multi-lr-dft_loss.csv", dft_data_loss, delimiter = ",")









