from scipy import ndimage
from numpy import array
from PIL import Image
from pylab import *
import wrap

im1 = array(Image.open('empire.jpg').convert('L'))
im2 = array(Image.open('AquaTermi_lowcontrast.jpg').convert('L'))
tp = array([[264,538,540,264],[40,36,605,605],[1,1,1,1]])

im3 = wrap.image_in_image(im1,im2,tp)

figure()
gray()
imshow(im3)
axis('equal')
axis('off')
show()




