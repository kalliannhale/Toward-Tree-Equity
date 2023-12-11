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

districts = ['Allston-Brighton', 'Back-Bay', 'Beacon Hill', 
             'Charlestown', 'Central', 'Dorchester',
             'East Boston', 'Fenway', 'Longwood', 
             'Hyde Park', 'Jamaica Plain', 'Mattapan'
             'Mission Hill', 'Roslindale', 'Roxbury',
             'South Boston', 'South End', 'West Roxbury'
    ]

def plan_tree():
    '''
    facilitates planning a tree

    '''
    dist_id = input("What neighborhood are you interested in?")
    
    neighborhood_instance = Neighborhood(dist_id)
    community.add_neighborhood(neighborhood_instance)

