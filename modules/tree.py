#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
module -- tree.py

    Manages a specific instance of a tree.
    
"""

import geopandas as gpd
import matplotlib.pyplot as plt
from parcel import Parcel
from pygris.geocode import geocode

class Tree(Parcel):
    '''
    Data visualization tool based off of community data.
    
    attributes:
        self.location -- dict
            a dictionary containing latitude (abbrv. 'lat'), 
            longitude (abbrv. 'long'), & geoid.
            
    '''
    def __init__(self, species, maturation, health, last_seen, status=True, district, address):
        
        super().__init__(district, address)
        
        self.status = status
        self.species = species
        self.maturation = maturation
        self.health = health
        self.address = address
        self.last_seen = last_seen
        self.status = status
        
    def get_status(self):
        return self.status
    
    def get_species(self):
        return self.species
    
    def get_maturation(self):
        return self.maturation
    
    def get_health(self):
        return self.health
    
    def get_last_seen(self):
        return self.last_seen
    
    def plan_tree(self):
        self.status = 'planned'
        return self.status
    
    def tree_loss(self):
        self.status = False
        return self.status
    
    def __str__(self):
        pass
    
    