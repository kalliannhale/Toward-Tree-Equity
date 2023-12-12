'''
module -- neighborhood.py

    Incorporates US Census, MassGIS, & Tree Equity Score 
        data & methodological parameters to manage 
        “official,” municipal data sets that are immutable, 
        but accessible to analyze so-called “priority 
        zones” with three or more indicators.
        
'''
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

class Neighborhood:
    '''
    Analyzes "official" municipal data to determine a
        priority zone.
    '''
    
    def __init__(self, district):
        
        self.district = district
        self.parcels = {}
        self.dist_id = self.find_dist_id()
        self.priority_plantings = 0
        
    def get_district(self):
        return self.district
    
    def get_dist_id(self):
        return self.dist_id
        
    def get_parcels(self):
         return self.parcels
        
    def find_dist_id(self):
        
        district_ids = {'allston brighton': 1, 'back bay': 2, 'beacon hill': 3, 
                        'charlestown': 4, 'central': 5, 'dorchester': 6, 
                        'east boston': 7, 'fenway': 8, 'longwood': 8, 
                        'hyde park': 10, 'jamaica plain': 11, 'mattapan': 12, 
                        'mission hill': 13, 'roslindale': 14, 'roxbury': 15, 
                        'south boston':16, 'south end': 17, 'west roxbury': 18
                        }
        
        if self.district in district_ids:
            return district_ids[self.district]
        else:
            raise ValueError("This district does not exist.")
    
    def dist_data(self):
        """
        Reads the district data from the 'district_data_v.csv' file.
        """
        pathway = '/Users/kalliann/Documents/Tree-Equity-Project/modules/district_data_v.csv'
        df = pd.read_csv(pathway)
        return df
    
    def priority_plantings(self, address):
        # Locate the corresponding parcel
        parcel = self.parcels.get(address)

        for parcel in self.parcels.values():
            for t in parcel.get_trees().values():
                if parcel.indicate_priority():
                self.priority_plantings += len(trees_list)
    
    def loss_or_gain(self):
        data = self.dist_data()
        dist_stat = data[data['DIST_ID'] == self.dist_id]
        r = dist_stat['NET'].iloc[0]
        q = dist_stat['LOSS'].iloc[0]
        p = dist_stat['GROWTH'].iloc[0]
        
        acreage = abs(p - q)
        
        return f"Experienced a net {r} of {acreage} acres from 2014-2019."
    
    def plot_gain_loss(self):
        """
        Plots the growth and loss for a given district ID using a bar chart.
        """
        data = self.dist_data()
        district_data = data[data['DIST_ID'] == self.dist_id]
        agg_data = district_data[['GROWTH', 'LOSS']].sum()
        
        plt.figure(figsize=(8, 6))
        plt.bar(['Growth', 'Loss'], agg_data.values, color=['green', 'red'])
        plt.xlabel('Outcome')
        plt.ylabel('Acres')
        plt.title(f'Growth and Loss for District ID {self.district}')
        plt.show()

    def plot_age_dist(self):
        """
        Plots the age distribution for a given district ID.
        """
        data = self.dist_data()
        district_data = data[data['DIST_ID'] == self.dist_id]
        agg_data = district_data['AGE_DIST'].apply(eval).apply(pd.Series).sum()
        agg_data *= 100
        
        plt.figure(figsize=(10, 6))
        agg_data.plot(kind='bar', color='orange')
        plt.xlabel('Age Distribution')
        plt.ylabel('Percentage')
        plt.title(f'Age Distribution for District ID {self.district}')
        plt.show()

    def plot_genus_dist(self):
        """
        Plots the genus distribution for a given district ID.
        """
        data = self.dist_data()
        district_data = data[data['DIST_ID'] == self.dist_id]
        agg_data = district_data['GENUS_DIST'].apply(eval).apply(pd.Series).sum()
        agg_data *= 100
        
        plt.figure(figsize=(12, 8))
        agg_data.plot(kind='bar', color='purple')
        plt.xlabel('Genus Distribution')
        plt.ylabel('Percentage')
        plt.title(f'Genus Distribution for District ID {self.district}')
        plt.show()
        
    def plot_species_dist(self):
        """
        Plots the species distribution for a given district ID.
        """
        data = self.dist_data()
        district_data = data[data['DIST_ID'] == self.dist_id]
        agg_data = district_data['SPEC_DIST'].apply(eval).apply(pd.Series).sum()
        agg_data *= 100
        
        plt.figure(figsize=(12, 8))
        agg_data.plot(kind='bar', color='skyblue')
        plt.xlabel('Species')
        plt.ylabel('Percentage')
        plt.title(f'Species Distribution for District ID {self.district}')
        plt.show()
        
        # if percent_species > 0.1, recommend against

    def species_dist(self):
        """
        Retrieves the species dist by percentage for a 
        given district ID and stores them in a list.
        """
        data = self.dist_data()
        district_data = data[data['DIST_ID'] == self.dist_id]
        species_dist = district_data['SPEC_DIST'].apply(eval).apply(pd.Series)

        percent_species = []
        for column in species_dist.columns:
            total_percentage = species_dist[column].sum() * 100
            percent_species.append((column, total_percentage))

        return dict(percent_species)
    
    def plot_heat_index(self):
        pathway = os.path.join(os.path.dirname(__file__), 'Canopy_Change_Assessment%3A_Heat_Metrics.shp')
        heat = gpd.read_file(pathway)
        heat.plot(cmap = 'hsv', edgecolor = 'black')
        
    def plot_vulnerability(self):
        pathway = os.path.join(os.path.dirname(__file__), 'social_vulnerability.shp')
        heat = gpd.read_file(pathway)
        heat.plot(cmap = 'hsv', edgecolor = 'black')
    
    def store_parcel(self, parcel):
        '''
        stores parcels
        '''
       
        address = parcel.address
        
        if address not in self.parcels:
            self.parcels[address] = parcel
    
    def official_addresses(self):
        
        pathway = '/Users/kalliann/Documents/Tree-Equity-Project/modules/parcels.csv'
        
        data = pd.read_csv(pathway, low_memory=False)
        
        data['ST_NUM'] = data['ST_NUM'].str.extract('(\d+)')
        addresses = []
        for index, row in data.iterrows():
            address = f"{row['ST_NUM']} {row['ST_NAME']} {row['ST_NAME_SU']}, Boston, MA"
            addresses.append(address.lower())
            
        return pd.DataFrame({'ADDRESS': addresses})
    
    def landuse(self, parcel):
        
        pathway = '/Users/kalliann/Documents/Tree-Equity-Project/modules/parcels.csv'
        
        data = pd.read_csv(pathway, low_memory=False)
        
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
  
    def __str__(self):
        return (
            f"Neighborhood: {self.district}\n"
            f"District ID: {self.dist_id}\n"
            f"{self.loss_or_gain()}\n"
            f"Number of Recorded Parcels: {len(self.parcels)}"
        )