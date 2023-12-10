#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
module -- parcel.py
    
    Assesses canopy and land use trends in predetermined 
        environmental justice communities, with the 
        hope of facilitating efforts to organize 
        equitable resource distribution.
        
"""

import pandas as pd
from neighborhood import Neighborhood
from pygris.geocode import geocode

class Parcel(Neighborhood):
    '''
    Manages a specific address.
    '''
    
    unique_parcels = set()
    
    def __init__(self, address, district):
        
        super().__init__(district)
        
        address = address.lower()
        
        if address in Parcel.unique_parcels:
            raise ValueError(f"Duplicate address found: {address}")
            
        Parcel.unique_parcels.add(address)
        
        try:
            self.geoerror = False
            self.address = geocode(address)
            self.longitude = self.address.iat[0, 0]
            self.latitude = self.address.iat[0, 1]
            self.geoid = float(self.address.iat[0, 2])
            self.equity_score = self.tree_equity_score()
            self.heat_disparity = self.heat_index()
            self.trees = {}
            self.planned = {}
            # self.land_use = self.findlanduse(address)
        
        except Exception as e:
            print()
            print(f"Geocoding failed for address '{address}': {e}")
            print()
            print("This project is limited to Boston, MA.")
            print("Please format address accordingly: 'number name street, Boston, MA'")
            print("Include commas; do not include unit numbers.")
            print("Street abbreviations such as '100 Wilmer Ave, Boston, MA' are acceptable.")
            self.address = address
            self.latitude = None
            self.longitude = None
            self.geoid = None
            self.equity_score = None
            self.geoerror = True
    
    def get_geoerror(self):
        return self.geoerror
    
    def get_address(self):
        return self.address
    
    def get_longitude(self):
        return self.longitude
    
    def get_latitude(self):
        return self.latitude
    
    def set_geoid(self):
        self.geoid = float(int(self.geoid/10**3))
    
    def get_geoid(self):
        return self.geoid
    
    def get_equity_score(self):
        return self.equity_score
    
    def get_heat_disparity(self):
        return self.heat_disparity
    
    def get_land_use(self):
        # return self.land_use
        pass
    
    def get_trees(self):
        return self.trees
    
    def get_planned(self):
        return self.planned
    
    def planned_trees(self, tree):
        
        if tree.species not in self.planned:
            self.planned[tree.species] = [tree]
        else:
           self.planned[tree.species].append(tree)
    
    def add_tree(self, tree):
        '''
        stores trees at this address in dict with species as key
        
        returns: None
        '''
        species = tree.species
        
        if tree.status == True:
            if species not in self.trees:
                self.trees[tree.species] = [tree]
            self.trees[tree.species].append(tree)
            
        elif tree.status == 'planned':
            self.plan_tree(tree, tree.species)
    
    def remove_tree(self, species):
        
        for t in self.trees[species]:
            if t.status == False:
                self.trees[species].remove(t)
            
    def find_landuse(self, address):
        # filepath = self.csv_path('parcels')
        # df = pd.read_csv(filepath)
        # df = df.loc[df['']]
        pass
    
    def tree_equity_score(self):
        
        if self.geoerror == False:
            
            filepath = self.csv_path('equity_score')
            df = pd.read_csv(filepath)
            df = df.loc[df['GEOID'] == float(int(self.geoid/10**3))]
            # matching up geoid across csv files
            
            if not df.empty:
                return df['tes'].iloc[0]
            
        else:
            return None
    
    def indicate_priority(self):
        '''

        returns True if this is a priority area,
        False otherwise.

        '''
        if self.geoerror == False:
            if self.equity_score < 70:
                return True
            elif self.equity_score >= 70:
                return False
        else:
            return None
        
    def heat_index(self):
        '''

        grabs heat index from tes data

        '''
        
        self.set_geoid()
        
        filepath = self.csv_path('equity_score')
        df = pd.read_csv(filepath)
        df = df.loc[df['GEOID'] == self.geoid]
        df = df.reset_index()
        
        self.heat_disparity = df['temp_diff'][0]
        
        return self.heat_disparity
    
    def __str__(self):
        
        if self.geoerror:
            return f"Your attempt to record a parcel has created a geocoding error...\n" \
                   f"  Address: {self.address}\n" 
                   
        else:
            return f"About this land parcel...\n" \
                   f" \n"\
                   f"  Trees planned: {len(self.planned)}\n"\
                   f"  Equity Score: {self.equity_score}\n" \
                   f"  Heat Disparity: {self.heat_disparity}\n"\
                   f"  Priority Determination: {'Highest Need!' if self.indicate_priority() else 'Need is higher in more vulnerable communities.'}\n" \
                   f" \n"\
                   f"{self.address}\n"
                   #f"  Land Use: {self.land_use}\n" \