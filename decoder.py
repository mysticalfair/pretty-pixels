import math
import numpy as np
from PIL import Image
def decoder:
    i=Image.open('file/to/path')
    array=np.array(i)
    xes=array.reshape(1, int(array.size/3), 3)
    print (xes)
    letters=[]
    for a in xes:
        for b in a:
            for c in b:
                if c !=0:
                    letters.append(chr(c))
    letters= ''.join(letters)
    print (letters)
