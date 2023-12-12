#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 23:26:42 2023

@author: kalliann
"""

def csv_path(self, topic):
    '''
    stores the filepath in a dictionary
    
    will have to change this path
    '''
    filepath = {'equity_score': '/Users/kalliann/Documents/Tree-Equity-Project/data sets/BOS_Tree_Equity_Score.csv',
              'parcels': '/Users/kalliann/Documents/Tree-Equity-Project/data sets/parcels.csv',
              'geoid_match': '/Users/kalliann/Documents/Tree-Equity-Project/data sets/matching_ids.csv',
              'dist_data': None,
              'census_block_groups':'/Users/kalliann/Documents/Tree-Equity-Project/data sets/Census2020_BlockGroups.shp',
              'open_spaces':'open-spaces.csv',
              'social_vulnerability': 'social_vulnerability.csv',
              'heat_report_shapes': 'Canopy_Change_Assessment%3A_Heat_Metrics.shp',
        }
    
    return filepath[topic]

def compare_geoids(topic_one, topic_two):
  """
  Finds matching IDs in two CSV files and saves them to a new file.

  Returns:
      A list of matching IDs.
  """
  
  with open(self.csv_path('geoid_match'), "w"):
      pass
  
  path_one = os.path.join(os.path.dirname(__file__), topic_one)
  path_two = os.path.join(os.path.dirname(__file__), topic_two)

  df1 = pd.read_csv(path_one)
  df2 = pd.read_csv(path_two)

  matching_ids = []

  for i, row1 in df1.iterrows():
    geoid1 = row1["GEOID"]

    try:
      j = df2.index[df2["GEOID"] == geoid1].tolist()[0]
      matching_ids.append((geoid1, j))
    except IndexError:
      pass

  df_matching_ids = pd.DataFrame(matching_ids, columns=["GEOID1", "GEOID2"])
  df_matching_ids.to_csv(self.csv_path('geoid_match'), index=False)

  # Optionally return the matching IDs
  return matching_ids