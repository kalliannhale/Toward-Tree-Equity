import unittest
from unittest.mock import Mock, patch
from neighborhood import Neighborhood
import pandas as pd
 
class TestNeighborhood(unittest.TestCase):
 
    def setUp(self):
        # Set up a Neighborhood instance for testing
        self.neighborhood = Neighborhood('back bay')
 
    def test_get_district(self):
        # Test the get_district method
        result = self.neighborhood.get_district()
        self.assertEqual(result, 'back bay')
 
    def test_get_dist_id(self):
        # Test the get_dist_id method
        result = self.neighborhood.get_dist_id()
        self.assertEqual(result, 2)
 
    def test_get_parcels(self):
        # Test the get_parcels method
        result = self.neighborhood.get_parcels()
        self.assertEqual(result, {})
 
    def test_find_dist_id(self):
        # Test the find_dist_id method
        self.neighborhood.district = 'central'
        result = self.neighborhood.find_dist_id()
        self.assertEqual(result, 5)
 
    @patch('neighborhood.pd.read_csv')
    def test_dist_data(self, mock_read_csv):
        # Test the dist_data method with a mock for pd.read_csv
        mock_read_csv.return_value = Mock()
        result = self.neighborhood.dist_data()
        mock_read_csv.assert_called_once_with('C:/Users/sneha/Downloads/Toward-Tree-Equity-main/district_data_v.csv')
 
    def test_priority_planting(self):
        # Test the priority_planting method
        species = 'oak'
        parcel = Mock()
        parcel.indicate_priority.return_value = True
        parcel.trees = {species: [1, 2, 3]}
        self.neighborhood.parcels = {'24 Beacon St, Boston, MA': parcel}
        self.neighborhood.priority_planting(species)
        self.assertEqual(self.neighborhood.priority_plantings, len(parcel.trees[species]))
 
    @patch('neighborhood.pd.DataFrame')
    def test_loss_or_gain(self, mock_dataframe):
        # Test the loss_or_gain method with a mock for pd.DataFrame
        mock_dataframe.return_value = Mock()
        result = self.neighborhood.loss_or_gain()
        self.assertIn('Experienced a net', result)
 
    @patch('neighborhood.plt.show')
    @patch('neighborhood.pd.DataFrame')
    def test_plot_gain_loss(self, mock_dataframe, mock_show):
        # Test the plot_gain_loss method with mocks for pd.DataFrame and plt.show
        mock_dataframe.return_value = Mock()
        self.neighborhood.plot_gain_loss()
        mock_show.assert_called_once()
 
    @patch('neighborhood.plt.show')
    @patch('neighborhood.pd.DataFrame')
    def test_plot_age_dist(self, mock_dataframe, mock_show):
        # Test the plot_age_dist method with mocks for pd.DataFrame and plt.show
        mock_dataframe.return_value = Mock()
        self.neighborhood.plot_age_dist()
        mock_show.assert_called_once()
 
    @patch('neighborhood.plt.show')
    @patch('neighborhood.pd.DataFrame')
    def test_plot_genus_dist(self, mock_dataframe, mock_show):
        # Test the plot_genus_dist method with mocks for pd.DataFrame and plt.show
        mock_dataframe.return_value = Mock()
        self.neighborhood.plot_genus_dist()
        mock_show.assert_called_once()
 
    @patch('neighborhood.plt.show')
    @patch('neighborhood.pd.DataFrame')
    def test_plot_species_dist(self, mock_dataframe, mock_show):
        # Test the plot_species_dist method with mocks for pd.DataFrame and plt.show
        mock_dataframe.return_value = Mock()
        self.neighborhood.plot_species_dist()
        mock_show.assert_called_once()
 
    @patch('neighborhood.pd.read_csv')
    def test_species_dist(self, mock_read_csv):
        # Test the species_dist method with a mock for pd.read_csv
        mock_read_csv.return_value = Mock()
        result = self.neighborhood.species_dist()
        self.assertIsInstance(result, dict)
 
    @patch('neighborhood.gpd.read_file')
    @patch('neighborhood.plt.show')
    def test_plot_heat_index(self, mock_show, mock_read_file):
        # Test the plot_heat_index method with mocks for gpd.read_file and plt.show
        self.neighborhood.plot_heat_index()
        mock_show.assert_called_once()
 
    @patch('neighborhood.gpd.read_file')
    @patch('neighborhood.plt.show')
    def test_plot_vulnerability(self, mock_show, mock_read_file):
        # Test the plot_vulnerability method with mocks for gpd.read_file and plt.show
        self.neighborhood.plot_vulnerability()
        mock_show.assert_called_once()
 
    @patch('neighborhood.pd.read_csv')
    def test_store_parcel(self, mock_read_csv):
        # Test the store_parcel method with a mock for pd.read_csv
        mock_read_csv.return_value = Mock()
        parcel = Mock(address='24 Beacon St, Boston, MA')
        self.neighborhood.store_parcel(parcel)
        self.assertEqual(self.neighborhood.parcels, {'24 Beacon St, Boston, MA': parcel})
 
    @patch('neighborhood.pd.read_csv')
    def test_official_addresses(self, mock_read_csv):
        # Test the official_addresses method with a mock for pd.read_csv
        mock_read_csv.return_value = Mock()
        result = self.neighborhood.official_addresses()
        self.assertIsInstance(result, pd.DataFrame)
 
    @patch('neighborhood.pd.read_csv')
    def test_landuse(self, mock_read_csv):
        # Test the landuse method with a mock for pd.read_csv
        mock_read_csv.return_value = Mock()
        parcel = Mock(raw_address='24 Beacon St, Boston, MA')
        result = self.neighborhood.landuse(parcel)
        self.assertIsInstance(result, str)
 
    @patch('neighborhood.pd.DataFrame')
    def test_str(self, mock_dataframe):
        # Test the __str__ method with a mock for pd.DataFrame
        mock_dataframe.return_value = Mock()
        result = str(self.neighborhood)
        self.assertIsInstance(result, str)
