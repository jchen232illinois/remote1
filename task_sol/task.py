import matplotlib.pyplot as plt
import matplotlib.image as mi
import scipy.signal as ss
import numpy as np

arr = []
for i in range(1, 12):
	fil = "%d.PNG" %i
	img = mi.imread(fil)
	img2 = img*32.0
	img3 = img2/32.0
	arr.append(img2)
	plt.imshow(img)
	plt.show()
	plt.imshow(img2)
	plt.show()
	plt.imshow(img3)
	plt.show()

np.save("arr",arr)


