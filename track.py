import numpy as np
import cv2
import matplotlib.pyplot as plt

# TODO: rename to python convention

class parameters:
    intensityFilter = None
    diffThreshold = None

params = parameters()

params.intensityFilter = 75
params.diffThreshold = 100

# We're using only the green channel at first

past = cv2.imread('img_145.jpg')
present = cv2.imread('img_146.jpg')

assert(past.shape == present.shape)

# save image for Past duplication

past_org = np.zeros((past.shape[0], past.shape[1]))

# Filter pixels with less than intensityFilter intensity

for x in range(past.shape[0]):
    for y in range(past.shape[1]):

        # save pixels in original image, for view
        past_org[x][y] = past[x][y][1]

        if past[x][y][1] < 75:
            past[x][y][1] = 0

for x in range(present.shape[0]):
    for y in range(present.shape[1]):
        if present[x][y][1] < 75:
            present[x][y][1] = 0


hotspots = []

# Subtract Present from Past

for x in range(past.shape[0]):
    for y in range(past.shape[1]):
        val = 0 if past[x][y][1] >= present[x][y][1] else present[x][y][1] - past[x][y][1]
        val = 0 if val < params.diffThreshold else val

        if val > 0:
            hotspots.append((x,y))

if 1 == 1:
    plt.figure()
    plt.style.use('grayscale')

    # Mark hotspots
    for x in hotspots:
        plt.scatter(x[1], x[0], s=5, c='red', marker='o')

    plt.imshow(past_org)
    plt.show()