# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 01:47:22 2020

@author: Zubin
"""
import os
from CardNames import Cards
import requests
import shutil
import time

path = r'Z:/MTG'                                                               #Path to save card Images

api = 'https://api.scryfall.com/cards/'                                        # api url that contains card images

    
for key in Cards.keys():                                                       # Loop through the Editions
    
    
    
    newpath = path + "\\" + key                                                # Path for Edition
    
    if not os.path.exists(newpath):                                            # Check if Edition directory exists
        
        os.makedirs(newpath)                                                   # Create new Edition Directory
        
    os.chdir(newpath)                                                          # Change working path to newly created directory
    
    for card in Cards[key]:                                                    # Loop through every card in Edition
        
        
        name = card[0]                                                         # Extract Card Name
        ID = card[3]                                                           # Extract unique Card ID
        
        if '"' in name:                                                        # Remove any characters not allowed in file names
            name = name.replace('"', '')
        
        if '/' in name:
            name = name.replace('/', '-')
            
        if '?' in name:
            name = name.replace('?', '')
            
        if os.path.exists(newpath + "\\" + name + '-' + ID + ".png"):          # Check if Card Image already recorded 
            
            print('{} : {}, image already recorded, continuing...'
                  .format(key, name))
            continue
        
        
        response = requests.get(api + ID, params =                             # Search api for Card Image based on ID
                                {'format' : 'image', 'version' : 'png'},
                                stream = True)
        
        
        image = requests.get(response.url, stream = True)                      # Extract Image from api response
        
        with open(name + '-' + ID + '.png', 'wb') as out_file:                 # Write Image to file named with card name and ID
            shutil.copyfileobj(image.raw, out_file)
            
        print('{} : {}, image has been recorded'.format(key, name ))           # Print Confirmation 
            
        time.sleep(.1)                                                         # Wait as to not flood api with requests
        
        
        