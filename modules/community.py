#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
module -- community.py
    
    Adds to and manages a dynamic set of volunteer 
        field data; intended to streamline sharing between 
        community actors and stakeholders involved in 
        local development initiatives which may benefit 
        from neighborhood tree data.
        
"""

import pandas as pd
from neighborhood import Neighborhood
from pygris.geocode import geocode

class Community:
    '''
    Manages a specific address.
    '''
    
    def __init__(self, address, district):
        
        super().__init__(district)
    
    def trees_added(self):
        pass
    
    def trees_lost(self):
        pass
    
    def visualize_canopy(self):
        pass
    
    def __str__(self):
        pass