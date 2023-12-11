#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:32:52 2023

@author: kalliann
"""

district_ids = {'allston': 1, 'allston-brighton': 1, 'allston brighton': 1, 
                'brighton': 1, 'back bay': 2, 'beacon hill': 3, 
                'charlestown': 4, 'central': 5, 'dorchester': 6, 
                'east boston': 7, 'fenway': 8, 'longwood': 8, 
                'hyde park': 10, 'jamaica plain': 11, 'mattapan': 12, 
                'mission hill': 13, 'roslindale': 14, 'roxbury': 15, 
                'south boston':16, 'south end': 17, 'west roxbury': 18
                }

def area_of_interest():
    
    districts = ['Allston-Brighton', 'Back-Bay', 'Beacon Hill', 
                 'Charlestown', 'Central', 'Dorchester',
                 'East Boston', 'Fenway', 'Longwood', 
                 'Hyde Park', 'Jamaica Plain', 'Mattapan'
                 'Mission Hill', 'Roslindale', 'Roxbury',
                 'South Boston', 'South End', 'West Roxbury'
        ]
    
    d = input("Type the name of the neighborhood you're interested in:")
    print()
    for dist in districts:
        print(d)
    
    return d

def plan_tree():
    '''
    facilitates planning a tree

    '''
    disrict = input("What neighborhood are you interested in? ")
    
    print()
    
    for d in districts:
        print(d)
