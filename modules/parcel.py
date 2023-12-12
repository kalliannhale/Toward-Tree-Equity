#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
module -- parcel.py
    
    Assesses canopy and land use trends in predetermined 
        environmental justice communities, with the 
        hope of facilitating efforts to organize 
        equitable resource distribution.
        
"""
import os
import pandas as pd
from neighborhood import Neighborhood
from pygris.geocode import geocode

class Parcel(Neighborhood):
    '''
    Manages a specific address.
    '''
    
    unique_parcels = {}
    
    def __init__(self, address, district):
        
        super().__init__(district)
        
        address = address.lower()
        
        if address in Parcel.unique_parcels:
            existing_parcel = Parcel.unique_parcels[address]
            self.__dict__ = existing_parcel.__dict__
            # accesses __dict__ attribute to copy all existing attribute info at given address to the new instance
        else:
            Parcel.unique_parcels[address] = self
        
        try:
            self.geoerror = False
            self.raw_address = address
            self.address = geocode(address)
            self.longitude = self.address.iat[0, 0]
            self.latitude = self.address.iat[0, 1]
            self.geoid = float(self.address.iat[0, 2])
            self.equity_score = self.tree_equity_score()
            self.heat_disparity = self.heat_index()
            self.trees = {}
            self.planned = []
            self.losses = {}
        
        except Exception as e:
            print()
            print(f"Geocoding failed for address '{address}': {e}")
            print()
            
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
    
    def get_trees(self):
        return self.trees
    
    def get_planned(self):
        return self.planned
    
    def planned_trees(self, tree):
        self.planned.append(tree)
    
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
    
    def tree_loss(self, species, maturation, address):
        
        if species not in self.losses:
            self.losses[species] = 0
        
        for t in self.trees[species]:
            if t.species == species and t.maturation == maturation and t.address == address:
                t.status = False
                self.losses[species] += 1
                break
    
    def decline(self, species, maturation, address):
        
        for t in self.trees[species]:
            if t.species == species and t.maturation == maturation and t.address == address:
                t.health = 'poor'
                break
            
    def find_land_use(self):
        land_use = self.landuse(self)
        return land_use
    
    def open_spaces(self):
        pathway = '/Users/kalliann/Documents/Tree-Equity-Project/modules/open_spaces_real.csv'
        df = pd.read_csv(pathway)
        # Check if the address is present in the "ADDRESS" column
        match_found = any(df['ADDRESS'] == self.address)
        
        if match_found is not None:
            return True
        else:
            return False
    
    def tree_equity_score(self):
        
        pathway = '/Users/kalliann/Documents/Tree-Equity-Project/modules/BOS_Tree_Equity_Score.csv'
        pd.read_csv(pathway)
        
        if self.geoerror == False:
            
            df = pd.read_csv(pathway)
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
        if self.geoerror == False:
            self.set_geoid()
            
            pathway = '/Users/kalliann/Documents/Tree-Equity-Project/modules/BOS_Tree_Equity_Score.csv'
            df = pd.read_csv(pathway)
            df = df.loc[df['GEOID'] == self.geoid]
            df = df.reset_index()
            
            heat_disparity = df['temp_diff'][0]
        
            return heat_disparity
        
        else:
            return None
        
    def too_hot(self):
        
        if self.heat_disparity > 20:
            return True
        else:
            return False
    
    def __str__(self):
        
        if self.geoerror:
            return f"Your attempt to record a parcel has created a geocoding error...\n" \
                   f'Some methods of analysis are not available.'\
                   f"  Address: {self.address}\n" 
                   
        else:
            return f"About this land parcel...\n" \
                   f" \n"\
                   f"  Land Use: {self.find_land_use()}\n"\
                   f"  {'This is an open space!' if self.open_spaces() else ''}\n"\
                   f"  Trees planned: {len(self.planned)}\n"\
                   f"  Equity Score: {self.equity_score}\n" \
                   f"  Heat Disparity: {self.heat_disparity}\n"\
                   f"  Priority Determination: {'Highest Need!' if self.indicate_priority() else 'Need is higher in more vulnerable communities.'}\n" \
                   f" \n"\
                   f"{self.address}\n"