import unittest
from unittest.mock import patch, Mock
from tree import Tree

class TestTree(unittest.TestCase):

    def setUp(self):
        # Common setup for multiple test cases
        self.valid_species = 'Oak'
        self.valid_maturation = 5
        self.valid_health = 'Healthy'
        self.valid_last_seen = '2023-01-01'
        self.valid_address = '24 beacon st, boston, ma'
        self.valid_district = 'back bay'

    def test_constructor(self):
        # Test case for a valid tree
        valid_tree = Tree(self.valid_species, self.valid_maturation, self.valid_health, self.valid_last_seen,
                          self.valid_address, self.valid_district)
        # Assert that the attributes of the created tree match the expected values
        self.assertEqual(valid_tree.species, self.valid_species)
        self.assertEqual(valid_tree.maturation, self.valid_maturation)
        self.assertEqual(valid_tree.health, self.valid_health)
        self.assertEqual(valid_tree.last_seen, self.valid_last_seen)
        self.assertEqual(valid_tree.address, self.valid_address)
        self.assertEqual(valid_tree.get_district(), self.valid_district)
        self.assertTrue(valid_tree.get_status())

    def test_get_status(self):
        # Test case for getting the status of a tree
        valid_tree = Tree(self.valid_species, self.valid_maturation, self.valid_health, self.valid_last_seen,
                          self.valid_address, self.valid_district)
        # Assert that the status is True (alive) for a newly created tree
        self.assertTrue(valid_tree.get_status())

    def test_get_species(self):
        # Test case for getting the species of a tree
        valid_tree = Tree(self.valid_species, self.valid_maturation, self.valid_health, self.valid_last_seen,
                          self.valid_address, self.valid_district)
        # Assert that the returned species matches the expected species
        self.assertEqual(valid_tree.get_species(), self.valid_species)

    def test_get_maturation(self):
        # Test case for getting the maturation of a tree
        valid_tree = Tree(self.valid_species, self.valid_maturation, self.valid_health, self.valid_last_seen,
                          self.valid_address, self.valid_district)
        # Assert that the returned maturation matches the expected maturation
        self.assertEqual(valid_tree.get_maturation(), self.valid_maturation)

    def test_get_health(self):
        # Test case for getting the health of a tree
        valid_tree = Tree(self.valid_species, self.valid_maturation, self.valid_health, self.valid_last_seen,
                          self.valid_address, self.valid_district)
        # Assert that the returned health matches the expected health
        self.assertEqual(valid_tree.get_health(), self.valid_health)

    def test_get_last_seen(self):
        # Test case for getting the last seen date of a tree
        valid_tree = Tree(self.valid_species, self.valid_maturation, self.valid_health, self.valid_last_seen,
                          self.valid_address, self.valid_district)
        # Assert that the returned last seen date matches the expected last seen date
        self.assertEqual(valid_tree.get_last_seen(), self.valid_last_seen)

    def test_plan_tree(self):
        # Test case for planning a tree
        valid_tree = Tree(self.valid_species, self.valid_maturation, self.valid_health, self.valid_last_seen,
                          self.valid_address, self.valid_district)
        # Plan the tree and assert that the status is 'planned'
        valid_tree.plan_tree()
        self.assertEqual(valid_tree.get_status(), 'planned')

    def test_death(self):
        # Test case for marking a tree as dead
        valid_tree = Tree(self.valid_species, self.valid_maturation, self.valid_health, self.valid_last_seen,
                          self.valid_address, self.valid_district)
        # Mark the tree as dead and assert that the status is False
        valid_tree.death()
        self.assertFalse(valid_tree.get_status())

    @patch('tree.Neighborhood')
    def test_biodiversity(self, mock_neighborhood):
        # Test case for tree biodiversity
        # Mocking the Neighborhood instance and its spec_dist method
        mock_instance = mock_neighborhood.return_value
        mock_instance.spec_dist.return_value = {'Oak': 15, 'Maple': 8}
        valid_tree = Tree(self.valid_species, self.valid_maturation, self.valid_health, self.valid_last_seen,
                          self.valid_address, self.valid_district)
        # Check biodiversity based on the mocked data and assert True
        result = valid_tree.biodiversity()
        self.assertTrue(result)

    def test_heat_vuln(self):
        # Test case for tree heat vulnerability
        at_risk_species = ['red maple', 'northern red oak']
        valid_tree = Tree('red maple', self.valid_maturation, self.valid_health, self.valid_last_seen,
                          self.valid_address, self.valid_district)
        # Check heat vulnerability for a species considered at risk and assert True
        result = valid_tree.heat_vuln()
        self.assertTrue(result)

    def test_str(self):
        # Test case for the string representation of a tree
        valid_tree = Tree(self.valid_species, self.valid_maturation, self.valid_health, self.valid_last_seen,
                          self.valid_address, self.valid_district)
        # Get the string representation and assert that it is an instance of str
        result = str(valid_tree)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    # Run the tests if the script is executed directly
    unittest.main()
