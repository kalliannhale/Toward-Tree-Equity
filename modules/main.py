#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:54:33 2023

@author: kalliann
"""

from community import Community
from neighborhood import Neighborhood
from parcel import Parcel
from tree import Tree

def main():
    
    cdb = "community_database.db"  # Replace with your actual database file name
    community = Community(cdb)

    while True:
        print("\n=== Boston Urban Forestry Accountability Mapping Tool ===")
        print("1. Plan a Tree")
        print("2. Record Existing/Planted Tree")
        print("3. Report Tree Loss")
        print("4. View Canopy Trends")
        print("5. Priority")
        print("6. Analyze Land Use")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            
            pass

        elif choice == "2":
            address = input("Enter parcel address: ")
            dist_id = input("Enter district ID: ")
            parcel = Parcel(address, dist_id)
            community.add_parcel(parcel_instance)
            print("Parcel added successfully!")

        elif choice == "3":
            species = input("Enter tree species: ")
            maturation = input("Enter tree maturation: ")
            health = input("Enter tree health: ")
            last_seen = input("Enter last seen date: ")
            address = input("Enter tree address: ")
            dist_id = input("Enter district ID: ")

            tree = Tree(species, maturation, health, last_seen, address, dist_id)
            
            community.add_tree(tree_instance)
            print("Tree added successfully!")

        elif choice == "4":
            print("\n=== View Canopy Trends ===")
            # Implement functionality to view canopy trends
            # Example: community.view_canopy_trends()

        elif choice == "5":
            print("\n=== Prioritize Environmental Justice Communities ===")
            # Implement functionality to prioritize environmental justice communities
            # Example: community.prioritize_ej_communities()

        elif choice == "6":
            print("\n=== Analyze Land Use ===")
            # Implement functionality to analyze land use
            # Example: community.analyze_land_use()

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()