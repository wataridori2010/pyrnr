# PyrNR
---

Pyramidal Noise Reduction library

## Requirements
---
- opencv-python
- numpy


Install
---
$ pip install pyrnr

Usage
---
```
from pyrnr.pyrnr import pyrnr

# load your image
img = cv2.imread("your_image")
dst = pyrnr(img)

```
