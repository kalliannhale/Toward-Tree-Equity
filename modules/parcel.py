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
    
    def __init__(self, address, district):
        
        super().__init__(district)
        
        try:
            self.geoerror = False
            self.address = geocode(address)
            self.longitude = self.address.iat[0, 0]
            self.latitude = self.address.iat[0, 1]
            self.geoid = float(self.address.iat[0, 2])
            self.equity_score = self.tree_equity_score()
            self.heat_index = heat_index
        
        except Exception as e:
            print(f"Geocoding failed for address '{address}': {e}")
            print("Please format address accordingly: 'streetaddress streetname, city, state'")
            print("Do not include unit numbers.")
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
    
    def get_geoid(self):
        return self.geoid
    
    def get_equity_score(self):
        return self.equity_score
    
    def get_heat_index(self):
        return heat_index
    
    def land_use(self):
        filepath = self.csv_path('parcels')
        df = pd.read_csv(filepath)
        df = df.loc[df['']]
    
    def tree_equity_score(self):
        
        if self.geoerror == False:
            
            filepath = self.csv_path('equity_score')
            df = pd.read_csv(filepath)
            df = df.loc[df['GEOID'] == float(int(self.geoid/10**3))]
            # matching up geoid across csv files
            
            if not df.empty:
                return df['tes'].iloc[0]
            
        else:
            pass
    
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
            pass
        
    def heat_event_hours(self):
        pass
    
    def trees_added(self):
        pass
    
    def trees_lost(self):
        pass
    
    def __str__(self):
        pass