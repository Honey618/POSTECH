# import the necessary packages
from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
import numpy as np
import argparse
import glob
import cv2
 
# construct the argument parser and parse the arguments

 
# initialize the index dictionary to store the image name
# and corresponding histograms and the images dictionary
# to store the images themselves
index = {}
images = {}


# loop over the image paths

image1 = cv2.imread('test2.jpeg')
images["test2"] = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
image2 = cv2.imread('test1.jpeg')
images["test1"] = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
image3 = cv2.imread('test2.jpg')
images["test2jpg"] = cv2.cvtColor(image3, cv2.COLOR_BGR2RGB)
image4 = cv2.imread('test4.png')
images["test4"] = cv2.cvtColor(image4, cv2.COLOR_BGR2RGB)
	# extract a 3D RGB color histogram from the image,
	# using 8 bins per channel, normalize, and update
	# the index
hist = cv2.calcHist([image1], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
hist = cv2.normalize(hist, hist).flatten()
index["test2"] = hist
hist = cv2.calcHist([image2], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
hist = cv2.normalize(hist, hist).flatten()
index["test1"] = hist
hist = cv2.calcHist([image3], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
hist = cv2.normalize(hist, hist).flatten()
index["test2jpg"] = hist
hist = cv2.calcHist([image4], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
hist = cv2.normalize(hist, hist).flatten()
index["test4"] = hist
# METHOD #1: UTILIZING OPENCV
# initialize OpenCV methods for histogram comparison
OPENCV_METHODS = (
	("Correlation", cv2.HISTCMP_CORREL),
	("Chi-Squared", cv2.HISTCMP_CHISQR),
	("Intersection", cv2.HISTCMP_INTERSECT), 
	("Hellinger", cv2.HISTCMP_BHATTACHARYYA))
 
# loop over the comparison methods
for (methodName, method) in OPENCV_METHODS:
	# initialize the results dictionary and the sort
	# direction
	results = {}
	reverse = False
 
	# if we are using the correlation or intersection
	# method, then sort the results in reverse order
	if methodName in ("Correlation", "Intersection"):
		reverse = True
	for (k, hist) in index.items():
		# compute the distance between the two histograms
		# using the method and update the results dictionary
		d = cv2.compareHist(index["test2jpg"], hist, method)
		results[k] = d
 
	# sort the results
	results = sorted([(v, k) for (k, v) in results.items()], reverse = reverse)
	fig = plt.figure("Query")
	ax = fig.add_subplot(1, 1, 1)
	ax.imshow(images["test2jpg"])
	plt.axis("off")
 
	# initialize the results figure
	fig = plt.figure("Results: %s" % (methodName))
	fig.suptitle(methodName, fontsize = 20)
 
	# loop over the results
	for (i, (v, k)) in enumerate(results):
		# show the result
		ax = fig.add_subplot(1, len(images), i + 1)
		ax.set_title("%s: %.2f" % (k, v))
		plt.imshow(images[k])
		plt.axis("off")
 
# show the OpenCV methods
plt.show()