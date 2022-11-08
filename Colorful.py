from PIL import Image
import numpy as np

a = np.array(Image.open('test.jpg'))
b = [255,255,255]-a
im = Image.fromarray(b.astype('uint8'))
im.save('new.jpg')
