from Augment import Pipeline
import matplotlib.pyplot as plt
from skimage import io
import time
import numpy as np
p = Pipeline()

p.rotate(0.5, 25, 25)
p.rotate90(probability=0.5)
p.rotate270(probability=0.5)
p.flip_left_right(probability=0.5)
p.flip_top_bottom(probability=0.5)
p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
p.random_distortion(probability=0.5, grid_width=4, grid_height=4, magnitude=8)
##p.crop_random(probability=0.5, percentage_area=0.9)


img = io.imread('test_img.jpg')
##print time.ctime()
print img.shape
res,g = p.sample_with_array(img,img)
res1,g1 = p.sample_with_array(img,img)
res2,g2 = p.sample_with_array(img,img)
print time.ctime()

plt.subplot(231)
plt.imshow(res)
plt.subplot(232)
plt.imshow(res1)
plt.subplot(233)
plt.imshow(res2)
plt.subplot(234)
plt.imshow(g)
plt.subplot(235)
plt.imshow(g1)
plt.subplot(236)
plt.imshow(g2)
plt.show()
