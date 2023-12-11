'''
module -- neighborhood.py

    Incorporates US Census, MassGIS, & Tree Equity Score 
        data & methodological parameters to manage 
        “official,” municipal data sets that are immutable, 
        but accessible to analyze so-called “priority 
        zones” with three or more indicators.
        
'''
import pandas as pd

class Neighborhood:
    '''
    Analyzes "official" municipal data to determine a
        priority zone.
    '''
    
    def __init__(self, district):
        
        self.district = district
        #self.dist_stats = self.dist_data(district)
        self.parcels = {}
        #self.dist_id = ...
    
    def get_district(self):
        return self.district
    
    def get_dist_stats(self):
       # return self.dist_stats
       pass
    
    def get_dist_id(self):
        pass
        #return self.dist_id
    
    def dist_data(self, district):
        '''
        creates a data frame from district data
        '''
        
        df = pd.read_csv(self.csv_path('dist_data'))
        df = df.loc[district]
        pass
    
    def species_dist(self):
        pass
    
    def genus_dist(self):
        pass
    
    def age_dist(self):
        pass
    
    def get_parcels(self):
        return self.parcels
    
    def store_parcel(self, parcel):
        '''
        stores parcels
        '''
        address = parcel.address
        self.parcels[address] = parcel
        
    def open_spaces(self, district):
        pass
    
    def official_addresses(self):
        
        data = pd.read_csv(self.csv_path('parcels'), low_memory=False)
        
        data['ST_NUM'] = data['ST_NUM'].str.extract('(\d+)')
        addresses = []
        for index, row in data.iterrows():
            address = f"{row['ST_NUM']} {row['ST_NAME']} {row['ST_NAME_SU']}, Boston, MA"
            addresses.append(address.lower())
            
        return pd.DataFrame({'ADDRESS': addresses})
    
    def landuse(self, parcel):
        
        data = pd.read_csv(self.csv_path('parcels'), low_memory=False)
        
        df = self.official_addresses()
        df = df.loc[df['ADDRESS'] == parcel.raw_address]
        
        if not df.empty:
            match = df.index[0]
            land_use = data.loc[df.index[0], 'LU_GENERAL']
        
        else:
            land_use = 'Not Found'
        
        return land_use
    
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
                  'heat_report_shapes': 'Canopy_Change_Assessment%3A_Heat_Metrics.shp'
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
