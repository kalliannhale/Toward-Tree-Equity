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

import pandas as pd
from neighborhood import Neighborhood
from pygris.geocode import geocode

class Parcel(Neighborhood):
    '''
    class -- Parcel:
        manages a specific address.
        
    attributes:
        unique_parcels -- a class attribute to keep track
            of unique parcels by their addresses.

    methods:
        __init__:
            constructs an instance of the Parcel class.
        get_geoerror :
            returns the geocoding error status.
        get_address: 
            returns the geocoded address.
        get_longitude: 
            returns the longitude of the parcel.
        get_latitude: 
            returns the latitude of the parcel.
        set_geoid: 
            sets the geoid by removing the last three digits.
        get_geoid: 
            returns the geoid value.
        get_equity_score: 
            returns the equity score.
        get_heat_disparity:
            returns the heat disparity value.
        get_trees: 
            returns the dictionary of trees associated
            with the parcel.
        get_planned: 
            returns the list of planned trees for
            the parcel.
        planned_trees:
            adds a tree to the list of planned trees.
    '''

    # a class attribute to keep track of unique parcels by their addresses.
    unique_parcels = {}

    def __init__(self, address, district):
        '''
        constructor:
            initializes a new instance of the Parcel class.

        parameters:
            address -- a string representing the address of the parcel.
            district -- a string representing the district to which
                the parcel belongs.
        '''
        
        super().__init__(district)
        # inherits district attribute from Neighborhood

        address = address.lower()
        # standardizes characters to prevent error

        if address in Parcel.unique_parcels:
            existing_parcel = Parcel.unique_parcels[address]
            self.__dict__ = existing_parcel.__dict__
        else:
            Parcel.unique_parcels[address] = self
        # stores the information entered abt each address on record
        # avoids duplicates by recopying information using __dict__

        try:
            # for addresses that geocode according to Tree Equity Data:
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
            # handles errant addresses out of scope:
            print()
            print(f"Geocoding failed for address '{address}': {e}")
            print()

            self.geoerror = True
            self.raw_address = address
            self.address = address
            self.latitude = None
            self.longitude = None
            self.geoid = None
            self.equity_score = None
            self.heat_disparity = None
            self.trees = {}
            self.planned_trees = []

    def get_geoerror(self):
        '''
        method -- get_geoerror:
            returns the geocoding error status.

        returns -- bool
            True if geocoding failed, False otherwise.
        '''
        return self.geoerror

    def get_raw_address(self):
        '''
        method -- get_address:
            returns the input address; useful for indexing
            and locating information in data frames
            based on address.
        '''
        return self.raw_address
    
    def get_address(self):
        '''
        method -- get_address:
            returns the geocoded address.
        '''
        return self.address

    def get_longitude(self):
        '''
        method -- get_longitude:
            returns the longitude of the parcel.
        '''
        return self.longitude

    def get_latitude(self):
        '''
        method -- get_latitude:
            returns the latitude of the parcel.
        '''
        return self.latitude

    def set_geoid(self):
        '''
        method -- set_geoid:
            sets the geoid by removing the last three digits.
            modifies the geoid attribute in place.
        '''
        self.geoid = float(int(self.geoid / 10**3))

    def get_geoid(self):
        '''
        method -- get_geoid:
            returns the geoid value.
        '''
        return self.geoid

    def get_equity_score(self):
        '''
        gets the equity score.
        '''
        return self.equity_score

    def get_heat_disparity(self):
        '''
        gets the heat disparity; returns a float.
        '''
        return self.heat_disparity

    def get_trees(self):
        '''
        gets the dictionary of trees associated with the parcel.
        '''
        return self.trees

    def get_planned(self):
        '''
        gets the list of planned trees for the parcel.
        '''
        return self.planned

    def planned_trees(self, tree):
        '''
        method -- planned_trees()
            adds a tree to the list of planned trees. Useful for
            counting the total number of recorded trees, not just
            planned trees.

        parameters:
            tree -- Tree
                The type of tree to be added.
        '''
        self.planned.append(tree)
    
    def add_tree(self, tree):
        '''
        method -- add_tree()
            stores trees at this address in dict with 
            species as key.
        
        returns: None
        '''
        species = tree.species
        
        if tree.status == True:
            if species not in self.trees:
                self.trees[tree.species] = [tree]
                
            self.trees[tree.species].append(tree)
            
        elif tree.status == 'planned':
            self.plan_tree(tree, tree.species)
    
    def tree_loss(self, species, maturation, address, last_seen):
        '''
        method -- tree_loss:
            counts the number of tree deaths; changes 
            the status of a tree which matches the 
            specified species, maturation and address. 
            updates the date last accessed.
    
        parameters:
            species -- str
            maturation -- str
            address -- str
    
        returns -- None
        '''
        if species not in self.losses:
            self.losses[species] = 0
            return None
        
        for t in self.trees[species]:
            if t.species == species and t.maturation == maturation and t.address == address:
                t.status = False
                t.last_seen = last_seen
                self.losses[species] += 1
                return None

    def decline(self, species, maturation, address, last_seen):
        '''
        method -- decline:
            simulates a decline in the health of a 
            tree at a specific address; changes the health of
            a tree that matches the specified species, maturation,
            and address and updates the date last accessed.
        
        parameters:
            species -- str
            maturation -- str
            address -- str
            last_seen -- str
        '''
        if species not in self.trees:
            return None
        
        for t in self.trees[species]:
            if t.species == species and t.maturation == maturation and t.address == address:
                t.health = 'poor'
                t.last_seen = last_seen
                break
            
    def find_land_use(self):
        '''
        method -- find_land_use:
            retrieves the general land use information 
            for the specific parcel instance
    
        returns:
            land_use -- the land use information.
                i.e., "Residential"
        '''
        land_use = self.landuse(self)
        return land_use
    
    def open_spaces(self):
        '''
        method -- open_spaces:
            checks if the parcel is designated as open space, 
            which implies right of way land use.
    
        returns -- bool
            True if the parcel is designated as open space, 
            False otherwise.
        '''
        pathway = '/Users/kalliann/Documents/Tree-Equity-Project/modules/open_spaces_real.csv'
        df = pd.read_csv(pathway)
        df = df['ADDRESS'].str.lower()
    
        m = df.loc[df == self.raw_address]
        
        if not m.empty:
            return True
        else:
            return False
    
    def tree_equity_score(self):
        '''
        method -- tree_equity_score:
            retrieves the tree equity score for the identified parcel.
    
        returns -- int
            the tree equity score.
        '''
        pathway = '/Users/kalliann/Documents/Tree-Equity-Project/modules/BOS_Tree_Equity_Score.csv'
        pd.read_csv(pathway)
        
        if self.geoerror == False:
            
            df = pd.read_csv(pathway)
            df = df.loc[df['GEOID'] == float(int(self.geoid/10**3))]
            
            if not df.empty:
                return df['tes'].iloc[0]
            
        else:
            return None
    
    def indicate_priority(self):
        '''
        method -- indicate_priority:
            if the equity score is less than 70, then the
            area takes priority.
    
        returns -- bool
            True if the parcel is a priority area, False otherwise.
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
        method -- heat_index:
            retrieves the heat index for the parcel.
    
        returns -- float
            the heat index value.
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
        '''
        method -- too_hot:
            checks if the parcel's heat disparity is greater than 20.
    
        returns -- bool
            True if the parcel's heat disparity is 
            greater than 20, False otherwise.
        '''
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
                   f"  General land use: {self.find_land_use()}\n"\
                   f"  {'This is an open space!' if self.open_spaces() else ''}\n"\
                   f"  Trees planned: {len(self.planned)}\n"\
                   f"  Trees lost: {sum(self.losses.values())}\n"\
                   f"  Equity Score: {self.equity_score}\n" \
                   f"  Heat Disparity: {self.heat_disparity}\n"\
                   f"  Priority Determination: {'Highest Need!' if self.indicate_priority() else 'Need is higher in more vulnerable communities.'}\n" \
                   f" \n"\
                   f"{self.address}\n"