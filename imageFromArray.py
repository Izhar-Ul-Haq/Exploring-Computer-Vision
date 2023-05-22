from PIL import Image
import numpy as np
a = np.zeros((1000,1000))
im = Image.fromarray(a)
im.show()