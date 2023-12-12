from parcel import Parcel
from datetime import datetime
import sqlite3

class Community:

    def __init__(self, database_file):
        with sqlite3.connect(database_file) as connection:
            self.connection = connection
            self.create_tables()

    def create_tables(self):
        with self.connection:
            cursor = self.connection.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS neighborhoods (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    district TEXT NOT NULL
                )
            ''')
            # creating Neighborhood table

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS parcels (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    address TEXT NOT NULL,
                    dist_id INTEGER,
                    FOREIGN KEY (dist_id) REFERENCES neighborhoods (id)
                )
            ''')
            # creating Parcel table

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS trees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    status TEXT,
                    species TEXT,
                    maturation TEXT,
                    health TEXT,
                    last_seen TEXT,
                    parcel_id INTEGER,
                    FOREIGN KEY (parcel_id) REFERENCES parcels (id)
                )
            ''')
            # creating Tree table

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    affiliation TEXT NOT NULL,
                    entry_date TEXT NOT NULL
                )
            ''')

    def add_user(self, user_name, affiliation):
        if user_name and affiliation:
            entry_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute('INSERT INTO users (name, affiliation, entry_date) VALUES (?, ?, ?)',
                               (user_name, affiliation, entry_date))

    def get_user_info(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute('SELECT name, affiliation, entry_date FROM users ORDER BY entry_date DESC LIMIT 1')
            user_info = cursor.fetchone()
            return user_info

    def add_neighborhood(self, dist_id, district_name=None):
        with self.connection:
            cursor = self.connection.cursor()
    
            cursor.execute('SELECT id FROM neighborhoods WHERE id=?', (dist_id,))
            existing_neighborhood = cursor.fetchone()
    
            if existing_neighborhood:
                return existing_neighborhood[0]
            else:
                # Provide a default value for district_name if not provided
                district_name = district_name or f'District {dist_id}'
    
                # Neighborhood doesn't exist, add a new neighborhood with a district name
                cursor.execute('INSERT INTO neighborhoods (id, district) VALUES (?, ?)', (dist_id, district_name))
    
                # Return the newly added neighborhood's id
                return cursor.lastrowid

    def add_parcel(self, address, dist_id):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute('SELECT id FROM neighborhoods WHERE id=?', (dist_id,))
            existing_neighborhood = cursor.fetchone()
            # checks to see if nbhd with identical dist_id exists

            if existing_neighborhood:
                # Use the existing neighborhood
                neighborhood_id = existing_neighborhood[0]
            else:
                # Create a new neighborhood
                cursor.execute('INSERT INTO neighborhoods (id) VALUES (?)', (dist_id,))
                neighborhood_id = cursor.lastrowid

            # Now add the parcel with the determined neighborhood_id
            cursor.execute('INSERT INTO parcels (address, dist_id) VALUES (?, ?)', (address, neighborhood_id))

    def add_tree(self, tree):
        with self.connection:
            # Check if the parcel exists, or add it
            cursor = self.connection.cursor()
            cursor.execute('SELECT id FROM parcels WHERE address=? AND dist_id=?', (tree.address, tree.dist_id))
            existing_parcel = cursor.fetchone()

            if existing_parcel:
                parcel_id = existing_parcel[0]
            else:
                # Create a new parcel
                parcel_id = self.add_parcel(tree.address, tree.dist_id)

            # Insert tree data
            cursor.execute('''
                INSERT INTO trees (status, species, maturation, health, last_seen, parcel_id)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (tree.status, tree.species, tree.maturation, tree.health, tree.last_seen, parcel_id))

    def remove_tree(self, species, maturation, address):
        with self.connection:
            cursor = self.connection.cursor()

            # Select tree_id based on species, maturation, and address
            cursor.execute(
                'SELECT id FROM trees WHERE species=? AND maturation=? AND address=? LIMIT 1',
                (species, maturation, address)
            )

            tree_id = cursor.fetchone()

            if tree_id:
                tree_id = tree_id[0]

                # Delete the tree
                cursor.execute('DELETE FROM trees WHERE id=?', (tree_id,))

                # Check if the corresponding parcel is now empty, and if so, remove it
                cursor.execute('SELECT parcel_id FROM trees WHERE id=?', (tree_id,))
                parcel_id = cursor.fetchone()[0]

                cursor.execute('SELECT COUNT(*) FROM trees WHERE parcel_id=?', (parcel_id,))
                tree_count = cursor.fetchone()[0]

                if tree_count == 0:
                    cursor.execute('DELETE FROM parcels WHERE id=?', (parcel_id,))

    def print_parcels(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM parcels')
            parcels = cursor.fetchall()

            print("\nParcels:")
            for parcel in parcels:
                print(f"ID: {parcel[0]}, Address: {parcel[1]}, District ID: {parcel[2]}")

    def print_trees(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM trees')
            trees = cursor.fetchall()

            print("\nTrees:")
            for tree in trees:
                print(f"ID: {tree[0]}, Status: {tree[1]}, Species: {tree[2]},"
                      f"Maturation: {tree[3]}, Health: {tree[4]},"
                      f"Date Last Seen: {tree[5]}, Parcel ID: {tree[6]}")
