# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 12:40:23 2021

@author: Zubin
"""
import torch
import numpy as np
import pandas as pd
from PIL import Image
import math
import pytesseract 

## OCR and YOLOv5 Initialization ##

ocr = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
weights = r'Z:/MTG_Samples/YoloS.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path = weights)
pytesseract.pytesseract.tesseract_cmd = ocr



## Function for coords. to the bounding boxes corresponding to class Name ##


def GetBoxes(result):
    
    boxes = []
    
    table = result.pandas().xyxy[0]
    CardNames = table[table['class'] == 0]
    CardNames = CardNames[CardNames['confidence'] > .65]
    
    for i in range(len(CardNames)):
        
        temp = CardNames.iloc[i]
        
        xmin = math.floor(temp['xmin'])
        xmax = math.floor(temp['xmax'])
        ymin = math.floor(temp['ymin'])
        ymax = math.floor(temp['ymax'])
        
        boxes.append((ymin, ymax, xmin, xmax))
        
    return boxes



## Function to index the image according to the boxes found in previous function ##


def boxedImage(img, result):
    
    names = []
    I = Image.open(img)
    ImageArray = np.array(I)
    boxes = GetBoxes(result)
    
    for box in boxes:
        
        indexed = ImageArray[box[0] : box[1], box[2] : box[3], :] 
        name = Image.fromarray(indexed, 'RGBA')
        if (box[1] - box[0]) > (box[3] - box[2]):
            name = name.rotate(90, Image.NEAREST, expand = 1)
        names.append(name)
        
    return names




## Pass Indexed image to the OCR and print results ##


def getNameText(img):
    
    text_names = []
    result = model(img)
    names = boxedImage(img, result)
    
    for name in names:
        
        text = pytesseract.image_to_string(name, lang = 'eng')
        text = text.split('\n')[0]
        text_names.append(text)
        
    return text_names





    