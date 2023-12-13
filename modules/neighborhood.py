'''
Analyzes "official" municipal data to determine a
priority zone.

'''
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

class Neighborhood:
    
    def __init__(self, district):
        '''
        constructor:
          initializes a new instance of the Neighborhood class.
    
       attributes:
          district:
              a string representing the name of the neighborhood.
          parcels:
              a dictionary storing Parcel objects with addresses as keys.
          dist_id: 
              an integer representing the district ID.
          priority_plantings: 
              an integer representing the number of trees planted in priority areas.
        '''
        self.district = district
        self.parcels = {}
        self.dist_id = self.find_dist_id()
        self.priority_plantings = 0
        
    def get_district(self):
        '''
        method -- get_district
          returns the name of the neighborhood.
        '''
        return self.district
    
    def get_dist_id(self):
        '''
        method -- get_dist_id
          returns the district ID.
        '''
        return self.dist_id
        
    def get_parcels(self):
        '''
        method -- get_parcels
          returns the dictionary of Parcel objects.
        '''
        return self.parcels
        
    def find_dist_id(self):
        '''
        method -- find_dist_id
          retrieves the district ID for the given neighborhood.
    
        returns -- int
          returns the district ID.
          
        raises -- ValueError
          raises an exception if the district does not exist.
        '''
        
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
        '''
        method -- dist_data
          reads the district data from the 
          'district_data_v.csv' file.
    
        returns -- DataFrame
          returns the district data as a pandas DataFrame.
        '''
        
        pathway = 'district_data_v.csv'
        df = pd.read_csv(pathway)
        return df
    
    def priority_planting(self, species):
        '''
        method -- priority_planting
          counts the number of trees recorded in
          parcels for which equity scores are lower than
          70; i.e., priority areas where trees have 
          been either recorded 
    
        parameters -- species: str
          the species for which the priority 
          plantings are calculated.
        '''
        
        for parcel in self.parcels.values():
            if parcel.indicate_priority():
                for t in parcel.trees.values():
                    self.priority_plantings += len(parcel.trees[species])
    
    def loss_or_gain(self):
        '''
        method -- loss_or_gain
          calculates the net loss or gain in acres 
          for the given district from 2014 to 2019.
    
        returns -- str
          returns a string describing the net acreage change.
        '''
        
        data = self.dist_data()
        dist_stat = data[data['DIST_ID'] == self.dist_id]
        r = dist_stat['NET'].iloc[0]
        q = dist_stat['LOSS'].iloc[0]
        p = dist_stat['GROWTH'].iloc[0]
        
        acreage = abs(p - q)
        
        return f"Experienced a net {r} of {acreage} acres from 2014-2019."
    
    def plot_gain_loss(self):
        '''
        method -- plot_gain_loss
          plots the growth and loss for a given 
          district ID using a bar chart.
        '''
        
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
        '''
        method -- plot_age_dist
          plots the age distribution for 
          a given district ID.
        '''
        
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
        '''
        method -- plot_genus_dist
          plots the genus distribution for 
          a given district ID.
        '''
        
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
        '''
        method -- plot_species_dist
          plots the species distribution for 
          a given district ID.
        '''
        
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
    
    def percent_sp(self):
        '''
        method -- spec_dist
          retrieves the species distribution by 
          percentage for a given district ID and 
          stores them in a dictionary.
        
        returns -- dict
          returns a dictionary containing species 
          and their corresponding percentages.
        '''
        
        data = self.dist_data()
        district_data = data[data['DIST_ID'] == self.dist_id]
        species_dist = district_data['SPEC_DIST'].apply(eval).apply(pd.Series)
        
        percent_species = []
        for column in species_dist.columns:
            total_percentage = species_dist[column].sum() * 100
            percent_species.append((column, total_percentage))
        
        return dict(percent_species)

    def plot_heat_index(self):
        '''
        method -- plot_heat_index
          plots the heat index using data 
          from a shapefile supplied by the 
          City of Boston (Analyze Boston).
        '''
        
        pathway = 'Canopy_Change_Assessment%3A_Heat_Metrics.shp'
        heat = gpd.read_file(pathway)
        heat.plot(cmap='hsv', edgecolor='black')
        
    def plot_vulnerability(self):
        '''
        method -- plot_vulnerability
          plots the vulnerability index using 
          data from a shapefile supplied by the 
          City of Boston (Analyze Boston).
        '''
        
        pathway = 'social_vulnerability.shp'
        heat = gpd.read_file(pathway)
        heat.plot(cmap='hsv', edgecolor='black')
    
    def store_parcel(self, parcel):
        '''
        method -- store_parcel
          stores parcels recorded within the district
          in a dictionary by address.
    
        parameters:
          parcel -- a Parcel object representing 
          the parcel to be stored.
        '''
        
        address = parcel.address
        
        if address not in self.parcels:
            self.parcels[address] = parcel
    
    def official_addresses(self):
        '''
        method -- official_addresses
          retrieves addresses of officially recorded land parcels 
          from a CSV file supplied by the City of Boston 
          (Analyze Boston).
    
        returns -- DataFrame
          returns a DataFrame with a validated address and
          index that can be used to locate other variables
          in the file.
        '''
        
        pathway = 'parcels.csv'
        data = pd.read_csv(pathway, low_memory=False)
        
        data['ST_NUM'] = data['ST_NUM'].str.extract('(\d+)')
        addresses = []
        for index, row in data.iterrows():
            address = f"{row['ST_NUM']} {row['ST_NAME']} {row['ST_NAME_SU']}, Boston, MA"
            addresses.append(address.lower())
            
        return pd.DataFrame({'ADDRESS': addresses})
    
    def landuse(self, parcel):
        '''
        method -- landuse
          retrieves land use information for parcels stored in
          a municipal database.
    
        parameters:
          parcel -- a Parcel object representing the parcel.
    
        returns -- str
          ex. 'Residential' or 'Commercial'
        '''
        
        pathway = 'parcels.csv'
        data = pd.read_csv(pathway, low_memory=False)
        
        df = self.official_addresses()
        df = df.loc[df['ADDRESS'] == parcel.raw_address]
        
        if not df.empty:
            match = df.index[0]
            land_use = data.loc[df.index[0], 'LU_GENERAL']
        else:
            land_use = 'Unspecified or not found.'
        return land_use
    
    def __str__(self):
        return (
            f"Neighborhood: {self.district}\n"
            f"District ID: {self.dist_id}\n"
            f"{self.loss_or_gain()}\n"
            f"Total addresses recorded by community: {len(self.parcels)}\n"
            f"Number of trees planted or verified in priority areas: {self.priority_plantings}"
        )
