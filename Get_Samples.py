# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:19:52 2020

@author: Zubin
"""
import os
from shutil import copyfile
import random


source = r'Z:/MTG'                  # source path of cards
destination = r'Z:/MTG_Samples2'     # destination path for cards to train on
Folders = os.listdir(source)        # returns list containing names of subdir. ( Card Editions)
nFolders = len(Folders)             # number of Card Editions

n = 1000                            # number of images to select at random to train

checkDest = r'Z:/MTG_Samples/pascal voc'

while(len(os.listdir(destination)) < n):        # terminates when destination folder contains n images
    
    r1 = random.randrange(0, nFolders)          # select random card edition 
    Edition = Folders[r1]                       # returns string that is the name of selected edition
    
    if os.path.isfile(Edition) or 'pycache' in Edition:     # folder contains subdir. we don't care about
        continue
    
    CardFolder = source + '/' + Edition                     # path to card edition folder
    
    Cards = os.listdir(CardFolder)                      # returns list containing strings that are the card names
    nCards = len(Cards)                                 # number of cards in that edition
    
    r2 = random.randrange(0, nCards)                    # select a card at random
    
    Card = Cards[r2]                                    # assign card name to variable
    path = CardFolder + '/' + Card                      # path to card
    
    if Card in os.listdir(destination):                 # Checks if card is already in destination
        continue
    
    if Card in os.listdir(checkDest):
        continue
    
    copyfile(path, destination + '/' + Card)            # copy image file to destination folder
    
    