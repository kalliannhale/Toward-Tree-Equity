#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
module -- tree.py

    Manages a specific instance of a tree.
    
"""

import geopandas as gpd
import matplotlib.pyplot as plt
from community import Parcel

class Tree:
    '''
    Data visualization tool based off of community data.
    
    attributes:
        self.location -- dict
            a dictionary containing latitude (abbrv. 'lat'), 
            longitude (abbrv. 'long'), & geoid.
            
    '''
    def __init__(self, status, species, maturation, health, address, last_seen):
        self.status = status
        self.species = species
        self.maturation = maturation
        self.health = health
        self.address = address
        self.last_seen = last_seen
        
    def get_status(self):
        return self.status
    
    def get_species(self):
        return self.species
    
    def get_maturation(self):
        return self.maturation
    
    def get_health(self):
        return self.health
    
    def get_address(self):
        return self.address
    
    def get_last_seen(self):
        return self.last_seen
    
    def get_latitude(self):
        location = geocoder.geocode(self.address)
        self.location = {'lat': location}
    
    def record_tree(self):
        # adds to Parcel
        pass
    
    def report_loss(self):
        pass
    
    def __str__(self):
        pass
    
    