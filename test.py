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
print time.ctime()
print img.shape
res = p.sample_with_array(img)
res1 = p.sample_with_array(img)
res2 = p.sample_with_array(img)
res3 = p.sample_with_array(img)
res4 = p.sample_with_array(img)
res5 = p.sample_with_array(img)
res6 = p.sample_with_array(img)
res7 = p.sample_with_array(img)
res8 = p.sample_with_array(img)
res9 = p.sample_with_array(img)
print time.ctime()

plt.subplot(331)
plt.imshow(res1)
plt.subplot(332)
plt.imshow(res2)
plt.subplot(333)
plt.imshow(res3)
plt.subplot(334)
plt.imshow(res4)
plt.subplot(335)
plt.imshow(res5)
plt.subplot(336)
plt.imshow(res6)
plt.subplot(337)
plt.imshow(res7)
plt.subplot(338)
plt.imshow(res8)
plt.subplot(339)
plt.imshow(res9)
plt.show()
