import cv2
import os

images = []
for filename in os.listdir('train/Images'):
    img = cv2.imread(os.path.join('train/Images',filename))
    if 'batch' not in filename:
        print(filename)
        
