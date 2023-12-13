import unittest
from parcel import Parcel
from tree import Tree  # Import the Tree class

class TestParcelMethods(unittest.TestCase):

    def setUp(self):
        self.valid_number = "24"
        self.valid_streetname = "beacon st"
        self.valid_city = "boston"
        self.valid_state = "ma"
        self.valid_district = "beacon hill"

    def test_get_geoerror(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        self.assertFalse(parcel.get_geoerror())

    def test_get_address(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        address_df = parcel.get_address()
        self.assertFalse(address_df.empty)

    def test_get_longitude(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        self.assertIsNotNone(parcel.get_longitude())

    def test_get_latitude(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        self.assertIsNotNone(parcel.get_latitude())

    def test_set_geoid(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        parcel.set_geoid()
        self.assertIsNotNone(parcel.get_geoid())

    def test_get_geoid(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        self.assertIsNotNone(parcel.get_geoid())

    def test_get_equity_score(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        score = parcel.get_equity_score()
        self.assertIsNotNone(score)

    def test_get_heat_disparity(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        disparity = parcel.get_heat_disparity()
        self.assertIsNotNone(disparity)

    def test_get_trees(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        trees = parcel.get_trees()
        self.assertIsNotNone(trees)

    def test_get_planned(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        planned = parcel.get_planned()
        self.assertIsNotNone(planned)

    def test_planned_trees(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        parcel.planned_trees("Maple")
        planned = parcel.get_planned()
        self.assertIn("Maple", planned)

    def test_add_tree(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        tree = Tree(species="Oak", maturation="Mature", health="Good", last_seen="2023-01-01",
                    address=parcel.get_address(), district=self.valid_district, status=True)
        parcel.add_tree(tree)
        trees = parcel.get_trees()
        self.assertIn("Oak", trees)

    def test_tree_loss(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        # Assuming that there's an Oak tree that was added
        parcel.tree_loss("Oak", "Mature", parcel.get_address(), '2023-01-01')
        losses = parcel.losses.get("Oak", 0)
        self.assertEqual(losses, 0)

    def test_decline(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        # Adding a tree before declining
        tree = Tree(species="Oak", maturation="Mature", health="Good", last_seen="2023-01-01",
                    address=parcel.get_address(), district=self.valid_district, status=True)
        parcel.add_tree(tree)

        # Declining the tree
        parcel.decline("Oak", "Mature", parcel.get_address(), last_seen="2023-01-01")
        self.assertEqual(parcel.trees["Oak"][0].health, 'poor')

    def test_find_land_use(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        land_use = parcel.find_land_use()
        self.assertIsNotNone(land_use)

    def test_open_spaces(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        is_open_space = parcel.open_spaces()
        self.assertTrue(is_open_space)

    def test_tree_equity_score(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        score = parcel.tree_equity_score()
        self.assertEqual(score, None)

    def test_indicate_priority(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        priority = parcel.indicate_priority()
        self.assertIsNotNone(priority)

    def test_heat_index(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        heat_index = parcel.heat_index()
        self.assertEqual(heat_index, None)

    def test_too_hot(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        too_hot = parcel.too_hot()
        self.assertFalse(too_hot)

    def test_str(self):
        parcel = Parcel(f"{self.valid_number} {self.valid_streetname}, {self.valid_city}, {self.valid_state}", self.valid_district)
        string_representation = str(parcel)
        self.assertIsNotNone(string_representation)

if __name__ == '__main__':
    unittest.main()
