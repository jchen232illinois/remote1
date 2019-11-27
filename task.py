import matplotlib.pyplot as plt
import numpy as np
arr = np.load("arr.npy",allow_pickle=1)
for i in range(0, 11):
	img = arr[i]
	img2 = img/32.0
	sizes = np.shape(img)
	fig = plt.figure()
	fig.set_size_inches(1. * sizes[1] / sizes[0], 1, forward = False)
	ax = plt.Axes(fig, [0., 0., 1., 1.])
	ax.set_axis_off()
	fig.add_axes(ax)
	plt.imshow(img2)
	plt.savefig("%d.png" %(i+1), dpi = sizes[0])
	plt.close()
