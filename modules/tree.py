#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
module -- tree.py

    Manages a specific instance of a tree.
    
"""

from parcel import Parcel
from neighborhood import Neighborhood
from pygris.geocode import geocode
import os

os.chdir('/Users/kalliann/Documents/Tree-Equity-Project/modules')

class Tree(Parcel):
    '''
    Data visualization tool based off of community data.
    
    attributes:
        self.location -- dict
            a dictionary containing latitude (abbrv. 'lat'), 
            longitude (abbrv. 'long'), & geoid.
            
    '''
    def __init__(self, species, maturation, health, last_seen, address, district, status=True):
        
        super().__init__(address, district)
        
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
        self.status = 'planned'
        return self.status
    
    def death(self):
        self.status = False
        return self.status
    
    def biodiversity(self):
        nbhd = Neighborhood(self.district)
        
        x = nbhd.species_dist()
        
        if self.species in x and x[self.species] > 10:
            return True
        else:
            return False
    
    def heat_vuln(self):
        
        at_risk = ['red maple', 'norther red oak']
        
        if self.species in at_risk:
            return True
        else:
            return False
    
    def __str__(self):
        return f"About this tree...\n" \
               f" \n"\
               f"  Species: {self.species}\n" \
               f"  Maturation: {self.maturation}\n" \
               f"  Health: {self.health}\n" \
               f"  Last Seen: {self.last_seen}\n" \
               f"  District: {self.get_district()}\n" \
               f"  Address: {self.get_address()}\n" \
               f"  Status: {'Planned' if self.status == 'planned' else 'Alive' if self.status else 'Dead'}"
    
    