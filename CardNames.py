# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:44:45 2020

@author: Zubin
"""

import json


with open('AllPrintings.json', encoding = 'utf-8') as file:                    # Open JSON file containing Card Info
    Data = file.read()
    
    
CardData = json.loads(Data)                                                    # Assigning Data
CardData = CardData['data']
    
# Alternate Method to opbtain card listing
"""
params = {'format' : 'json', 'pretty' : True}                                  

response = requests.get('https://api.scryfall.com/catalog/card-names',
                        params = params)
"""
Cards = {}                                                                     # Initializing Card Dict.

for Edition in CardData:                                                       # Looping through Editions in CardData
    
    name = CardData[Edition]['name']                                           # Extract Edition Name
       
    name = name.replace(':', '-')                                              # Remove problem characters
    name = name.replace('.', '-')
    name = name.replace('/', '-')
    
    temp = CardData[Edition]['cards'].copy()                                   # Extract cards from edition
    temp.extend(CardData[Edition]['tokens'])                                   # Add token cards with the rest
    
    for Card in temp:                                                          # Loop through cards
        
        if name not in Cards.keys():                                           # Check if Edition is key in Cards Dict.
            
            Cards[name] = [(Card['name'], Edition, Card['type'],               # Create new Edition key and add first card info
                            Card['identifiers']['scryfallId'], Card['uuid'])]
            
        else :
            
            Cards[name].append((Card['name'], Edition, Card['type'],           # add card info to edition key
                                Card['identifiers']['scryfallId'],
                                Card['uuid']))
            
