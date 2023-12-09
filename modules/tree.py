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
    def __init__(self, status, species, maturation, health, last_seen, district, address):
        
        super().__init__(district, address)
        
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
    
    def get_last_seen(self):
        return self.last_seen
    
    def plan_tree(self):
        pass
    
    def record_trees(self):
        # adds to Parcel
        pass
    
    def report_loss(self):
        pass
    
    def __str__(self):
        pass
    
    