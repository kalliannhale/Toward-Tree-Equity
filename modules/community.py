from parcel import Parcel
from datetime import datetime
import sqlite3

class Community:

    def __init__(self, database_file):
        '''
        constructor:
          initializes a new instance of the Community class.
    
        parameters:
          database_file:
              a string representing the path 
              to the SQLite3 database file.
        '''
        with sqlite3.connect(database_file) as connection:
            self.connection = connection
            self.create_tables()

    def create_tables(self):
        '''
        method -- create_tables
          creates the necessary tables in the SQLite3 database.
        '''
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
        '''
        method -- add_user
          adds a user to the database.
    
        parameters:
          user_name -- a string representing the name of the user.
          affiliation -- a string representing the affiliation of the user.
        '''
        if user_name and affiliation:
            entry_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute('INSERT INTO users (name, affiliation, entry_date) VALUES (?, ?, ?)',
                               (user_name, affiliation, entry_date))
    
    def get_user_info(self):
        '''
        method -- get_user_info
          retrieves information about the latest user 
          added to the database.
    
        returns -- tuple
          returns a tuple containing the user's name, 
          affiliation, and entry date.
        '''
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute('SELECT name, affiliation, entry_date FROM users ORDER BY entry_date DESC LIMIT 1')
            user_info = cursor.fetchone()
            return user_info
    
    def add_neighborhood(self, dist_id, district_name=None):
        '''
        method -- add_neighborhood
          adds a neighborhood to the database.
    
        parameters:
          dist_id:
              an integer representing the district ID.
          district_name:
              a string representing the name of the 
              district (default is None).
        
        returns -- int
          returns the ID of the added or existing neighborhood.
        '''
        with self.connection:
            cursor = self.connection.cursor()
    
            cursor.execute('SELECT id FROM neighborhoods WHERE id=?', (dist_id,))
            existing_neighborhood = cursor.fetchone()
    
            if existing_neighborhood:
                return existing_neighborhood[0]
            else:
                # provide a default value for district_name if not provided
                district_name = district_name or f'District {dist_id}'
    
                # neighborhood doesn't exist, add a new neighborhood with a district name
                cursor.execute('INSERT INTO neighborhoods (id, district) VALUES (?, ?)', (dist_id, district_name))
    
                return cursor.lastrowid
                # returns id
    
    def add_parcel(self, address, dist_id):
        '''
        method -- add_parcel
          adds a parcel to the database.
    
        parameters:
            
          address:
              a string representing the address of 
              the parcel.
          dist_id:
              an integer representing the district 
              ID of the parcel.
        '''
        
        with self.connection:
            
            cursor = self.connection.cursor()
            cursor.execute('SELECT id FROM neighborhoods WHERE id=?', (dist_id,))
            existing_neighborhood = cursor.fetchone()
    
            if existing_neighborhood:
                neighborhood_id = existing_neighborhood[0]
            else:
                cursor.execute('INSERT INTO neighborhoods (id) VALUES (?)', (dist_id,))
                neighborhood_id = cursor.lastrowid
                # uses existing neighborhoods or creates a new one
    
            cursor.execute('INSERT INTO parcels (address, dist_id) VALUES (?, ?)', (address, neighborhood_id))
            # adds parcels using neighborhood ids
    
    def add_tree(self, tree):
        '''
        method -- add_tree
          adds a tree to the database.
    
        parameters:
          tree -- Tree
              a Tree object representing the tree to be added.
        '''
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute('SELECT id FROM parcels WHERE address=? AND dist_id=?', (tree.address, tree.dist_id))
            existing_parcel = cursor.fetchone()
            # checking for existing parcels
    
            if existing_parcel:
                parcel_id = existing_parcel[0]
            else:
                parcel_id = self.add_parcel(tree.address, tree.dist_id)
                # creating a new parcel
    
            cursor.execute('''
                INSERT INTO trees (status, species, maturation, health, last_seen, parcel_id)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (tree.status, tree.species, tree.maturation, tree.health, tree.last_seen, parcel_id))
            # inserting tree data
    
    def remove_tree(self, species, maturation, address):
        '''
        method -- remove_tree
          removes a tree from the database.
    
        parameters:
            
          species:
              a string representing the species 
              of the tree.
          maturation:
              a string representing the maturation 
              stage of the tree.
          address: 
              a string representing the address 
              of the tree.
        '''
        with self.connection:
            cursor = self.connection.cursor()
    
            # select tree_id based on species, maturation, and address
            cursor.execute(
                'SELECT id FROM trees WHERE species=? AND maturation=? AND address=? LIMIT 1',
                (species, maturation, address)
            )
    
            tree_id = cursor.fetchone()
    
            if tree_id:
                tree_id = tree_id[0]
    
                cursor.execute('DELETE FROM trees WHERE id=?', (tree_id,))
                # deletes trees
    
    def print_parcels(self):
        '''
        method -- print_parcels
          prints information about all parcels in the database.
        '''
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM parcels')

    def print_trees(self):
        '''
        method -- print_trees
          prints information about all trees in the database.
        '''
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM trees')
            trees = cursor.fetchall()

            print("\nTrees:")
            for tree in trees:
                print(f"ID: {tree[0]}, Status: {tree[1]}, Species: {tree[2]},"
                      f"Maturation: {tree[3]}, Health: {tree[4]},"
                      f"Date Last Seen: {tree[5]}, Parcel ID: {tree[6]}")
