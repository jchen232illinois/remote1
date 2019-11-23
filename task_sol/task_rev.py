# Reverse process
import matplotlib.pyplot as plt
import matplotlib.image as mi
import scipy.signal as ss
import numpy as np
arr = np.load("arr.npy",allow_pickle=1)
for i in range(0, 11):
	img = arr[i]
	img2 = img/32.0

	plt.figure()
	plt.imshow(img2)
	plt.savefig("%d.png" %(i+1))
