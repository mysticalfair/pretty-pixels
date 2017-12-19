import math
import numpy as np
from PIL import Image
def convert(s):
    s=bytes(s, 'utf8')
    sqq=len(s)**.5;
    sqq=int(math.ceil(sqq))
    thesquare=sqq*sqq*3;
    s= list(s)+ [0]*(thesquare-len(s));

    ar=[];
    for i in range(0, len(s), 3):
        subar=[s[i], s[i+1], s[i+2]];
        ar.append(subar);

    arr=np.array(ar)
    arra=[arr];
    arra=np.array(arra).astype('uint8');
    arra=arra.reshape(sqq, sqq, 3)
    i=Image.fromarray(arra)
    i.show()
