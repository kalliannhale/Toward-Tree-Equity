"""
module -- community.py
    
    Adds to and manages a dynamic set of volunteer 
        field data; intended to streamline sharing between 
        community actors and stakeholders involved in 
        local development initiatives which may benefit 
        from neighborhood tree data.
        
"""

from neighborhood import Neighborhood
from parcel import Parcel
from tree import Tree

import sqlite3

class Community:
    
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
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
                district_id INTEGER,
                FOREIGN KEY (district_id) REFERENCES neighborhoods (id)
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

        self.connection.commit()

    def add_neighborhood(self, district):
        cursor = self.connection.cursor()

        cursor.execute('SELECT id FROM neighborhoods WHERE district=?', (district,))
        existing_neighborhood = cursor.fetchone()

        if existing_neighborhood:
            neighborhood_id = existing_neighborhood[0]
        else:
            cursor.execute('INSERT INTO neighborhoods (district) VALUES (?)', (district,))
            neighborhood_id = cursor.lastrowid
        
        # only stores unique districts

        self.connection.commit()

        return neighborhood_id
        

    def add_parcel(self, address, district_id):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO parcels (address, district_id) VALUES (?, ?)', (address, district_id))
        self.connection.commit()

    def add_tree(self, tree):
        cursor = self.connection.cursor()

        cursor.execute('SELECT id, district_id FROM parcels WHERE address=?', (tree.address,))
        existing_parcel = cursor.fetchone()

        if existing_parcel:
            parcel_id, district_id = existing_parcel
        else:
            cursor.execute('INSERT INTO parcels (address, district_id) VALUES (?, ?)', (tree.address, tree.district_id))
            parcel_id = cursor.lastrowid
            district_id = tree.district_id
            
        # only stores unique addresses

        cursor.execute('''
            INSERT INTO trees (status, species, maturation, health, last_seen, parcel_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (tree.status, tree.species, tree.maturation, tree.health, tree.last_seen, parcel_id))

        # trees are stored in parcels of the same address
        
        if existing_parcel:
            neighborhood_id = district_id
        else:
            neighborhood_id = self.add_neighborhood(tree.district)
            tree.parcel = Parcel(tree.address, tree.district)
            tree.parcel.add_tree(tree)

        self.connection.commit()
