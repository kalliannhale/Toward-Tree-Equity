#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
module -- tree.py

Manages a specific instance of a tree.

"""

from parcel import Parcel
from neighborhood import Neighborhood
from pygris.geocode import geocode

class Tree(Parcel):
    '''
    Data visualization tool based on community data.

    attributes:
        self.location -- dict
            A dictionary containing latitude (abbrv. 'lat'),
            longitude (abbrv. 'long'), & geoid.

    '''

    def __init__(self, species, maturation, health, last_seen, address, district, status=True):
        '''
        constructor:
            Initializes a new instance of the Tree class.

        parameters:
            species -- str
                The species of the tree.
            maturation -- str
                The maturation stage of the tree.
            health -- str
                The health status of the tree.
            last_seen -- str
                The last recorded date the tree was observed.
            address -- str
                The address of the tree.
            district -- str
                The district in which the tree is located.
            status -- bool or str, optional
                The status of the tree. Defaults to True.

        '''
        
        super().__init__(address, district)

        self.status = status
        self.species = species
        self.maturation = maturation
        self.health = health
        self.address = address
        self.last_seen = last_seen

    def get_status(self):
        '''
        method -- get_status
            Returns the status of the tree.

        returns -- bool or str
                The status of the tree.
        '''
        return self.status

    def get_species(self):
        '''
        method -- get_species
            Returns the species of the tree.

        returns -- str
                The species of the tree.
        '''
        return self.species

    def get_maturation(self):
        '''
        method -- get_maturation
            Returns the maturation stage of the tree.
        '''
        return self.maturation

    def get_health(self):
        '''
        method -- get_health
            Returns the health status of the tree.
        '''
        return self.health

    def get_last_seen(self):
        '''
        method -- get_last_seen
            Returns the last recorded date the tree was observed
            as a string.
        '''
        return self.last_seen

    def plan_tree(self):
        '''
        method -- plan_tree
            Changes the status of the tree to 'planned'.
        '''
        self.status = 'planned'
        return self.status

    def death(self):
        '''
        method -- death
            Represents the death of a tree by changing its 
            status to False.

        returns -- bool
                The updated status of the tree.
        '''
        self.status = False
        return self.status

    def biodiversity(self):
        '''
        method -- biodiversity
            Checks if a particular tree species exceeds the recommended
            concentration of 10% in a given neighborhood.

        returns -- bool
                True if the species is over-concentrated, 
                False otherwise.
        '''
        nbhd = Neighborhood(self.district)
        x = nbhd.percent_sp()

        if (self.species in x) and (x[self.species] > 10):
            return True
        else:
            return False

    def heat_vuln(self):
        '''
        method -- heat_vuln
            Checks if a tree species is vulnerable to 
            high heat.

        returns -- bool
                True if vulnerable, False otherwise
        '''
        at_risk = ['red maple', 'northern red oak']

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
    
    