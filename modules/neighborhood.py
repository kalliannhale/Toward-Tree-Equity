<<<<<<< HEAD
'''module -- neighborhood.py    Incorporates US Census, MassGIS, & Tree Equity Score         data & methodological parameters to manage         “official,” municipal data sets that are immutable,         but accessible to analyze so-called “priority         zones” with three or more indicators.        '''import pandas as pdimport matplotlib.pyplot as pltclass Neighborhood:    '''    Analyzes "official" municipal data to determine a        priority zone.    '''        def __init__(self, district):        self.district = district        self.data = self.district_data(district)        self.canopy = []        def get_district(self):        return self.district        def district_data(self, district):        '''        stores district data in a dictionary        '''        pass        def csv_path(self, topic):        '''        stores the filepath in a dictionary        '''        filepath = {'equity_score': '/Users/kalliann/Documents/Tree-Equity-Project/data sets/BOS_Tree_Equity_Score.csv',                  'parcels': '/Users/kalliann/Documents/Tree-Equity-Project/data sets/parcels.csv',                  'geoid_match': '/Users/kalliann/Documents/Tree-Equity-Project/data sets/matching_ids.csv',                  'district': None,                  'census_block_groups':'/Users/kalliann/Documents/Tree-Equity-Project/data sets/2020_Census_Block_Groups_in_Boston.csv',                  'open_spaces':'/Users/kalliann/Documents/Tree-Equity-Project/data sets/open-spaces.csv',                  'social_vulnerability': '/Users/kalliann/Documents/Tree-Equity-Project/data sets/social_vulnerability.csv'            }                return filepath[topic]        def analyze_parcels(self, filepath):        data['ST_NUM'] = data['ST_NUM'].str.extract('(\d+)')        addresses = []        for index, row in data.iterrows():            address = f"{row['ST_NUM']} {row['ST_NAME']}, {row['ST_NAME_SU']}, Boston, MA"            addresses.append(address.lower())        return pd.DataFrame({'Address': addresses})        def open_spaces(self, district):        pass        def canopy(self):        pass        def compare_geoids(topic_one, topic_two):      """      Finds matching IDs in two CSV files and saves them to a new file.      Returns:          A list of matching IDs.      """            with open(self.csv_path('geoid_match'), "w"):          pass      df1 = pd.read_csv(self.csv_path(topic_one))      df2 = pd.read_csv(self.csv_path(topic_two))      matching_ids = []      for i, row1 in df1.iterrows():        geoid1 = row1["GEOID"]        try:          j = df2.index[df2["GEOID"] == geoid1].tolist()[0]          matching_ids.append((geoid1, j))        except IndexError:          pass      df_matching_ids = pd.DataFrame(matching_ids, columns=["GEOID1", "GEOID2"])      df_matching_ids.to_csv(self.csv_path('geoid_match'), index=False)      # Optionally return the matching IDs      return matching_ids      def __str__(self):        pass
=======
'''
module -- neighborhood.py

    Incorporates US Census, MassGIS, & Tree Equity Score 
        data & methodological parameters to manage 
        “official,” municipal data sets that are immutable, 
        but accessible to analyze so-called “priority 
        zones” with three or more indicators.
        
'''
import pandas as pd
import matplotlib.pyplot as plt

class Neighborhood:
    '''
    Analyzes "official" municipal data to determine a
        priority zone.
    '''
    
    def __init__(self, district):
        self.district = district
        self.data = self.district_data(district)
    
    def get_district(self):
        return self.district
    
    def district_data(self, district):
        '''
        stores district data in a dictionary
        '''
        pass
    
    def csv_path(self, topic):
        '''
        stores the filepath in a dictionary
        '''
        filepath = {'equity_score': '/Users/kalliann/Documents/Tree-Equity-Project/data sets/BOS_Tree_Equity_Score.csv',
                  'parcels': '/Users/kalliann/Documents/Tree-Equity-Project/data sets/parcels.csv',
                  'geoid_match': '/Users/kalliann/Documents/Tree-Equity-Project/data sets/matching_ids.csv',
                  'district': None,
                  'census_block_groups':'/Users/kalliann/Documents/Tree-Equity-Project/data sets/2020_Census_Block_Groups_in_Boston.csv',
                  'open_spaces':'/Users/kalliann/Documents/Tree-Equity-Project/data sets/open-spaces.csv',
                  'social_vulnerability': '/Users/kalliann/Documents/Tree-Equity-Project/data sets/social_vulnerability.csv'
            }
        
        return filepath[topic]
    
    def analyze_parcels(self, filepath):
        data['ST_NUM'] = data['ST_NUM'].str.extract('(\d+)')
        addresses = []
        for index, row in data.iterrows():
            address = f"{row['ST_NUM']} {row['ST_NAME']}, {row['ST_NAME_SU']}, Boston, MA"
            addresses.append(address.lower())
        return pd.DataFrame({'Address': addresses})
    
    def open_spaces(self, district):
        pass
    
    def canopy(self):
        pass
    
    def compare_geoids(topic_one, topic_two):
      """
      Finds matching IDs in two CSV files and saves them to a new file.

      Returns:
          A list of matching IDs.
      """
      
      with open(self.csv_path('geoid_match'), "w"):
          pass

      df1 = pd.read_csv(self.csv_path(topic_one))
      df2 = pd.read_csv(self.csv_path(topic_two))

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
  
    def __str__(self):
        pass
>>>>>>> 815a69dff1c40609a3981a0b0ade5e81c75326f3
