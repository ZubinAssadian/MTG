# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 14:21:33 2020

@author: Zubin
"""

import os
from shutil import copyfile
import random
import math



source = r'Z:/MTG_Samples/yolo'
ratio = .1

testDest = r'Z:/MTG_Samples/val'
trainDest = r'Z:/MTG_Samples/train'


if not os.path.exists(testDest):
    os.makedirs(testDest)
    
if not os.path.exists(trainDest):
    os.makedirs(trainDest)
    

images = [x for x in os.listdir(source) if '.png' in x]
Nimages = len(images)


Ntest = math.ceil(Nimages * ratio)
Ntrain = Nimages - Ntest



count = len(os.listdir(testDest))    

while (count < (2 * Ntest)):
    
    index = random.randint(0, Nimages - 1)
    pick = images[index]
    
    if pick in testDest:
        continue
    
    copyfile(source + '/' + pick, testDest + '/' + pick)
    copyfile(source + '/' + pick.split('.')[0] + '.txt', testDest 
             + '/' + pick.split('.')[0] + '.txt')
    count = len(os.listdir(testDest))
    
    
for file in os.listdir(source):
    
    if file in os.listdir(testDest):
        continue
    
    copyfile(source + '/' + file, trainDest + '/' + file)
    
    
print('Split Complete!')