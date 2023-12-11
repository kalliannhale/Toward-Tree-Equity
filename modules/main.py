#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:54:33 2023

@author: kalliann
"""

from community import Community
from parcel import Parcel
from tree import Tree
from user_input import user_info, species, area_of_interest, maturation, health, last_seen, address
from neighborhood import Neighborhood

def main():
    
    cdb = "community_database.db"
    community = Community(cdb)
    
    user_name, affiliation = user_info()
    community.add_user(user_name, affiliation)
    community.get_user_info
    print()

    while True:
        print("\n=== Boston Urban Forestry Accountability Mapping Tool ===")
        print("1. Plan a Tree")
        print("2. Record Existing/Planted Tree")
        print("3. Report Tree Loss")
        print("4. Analyze Land Use")
        print("5. Access Information")
        print("6. Determine Priority")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            
            # Call the user input functions and assign the returned values
            print()
            d = area_of_interest()
            print()
            s = species()
            print()
            m = maturation()
            print()
            h = health()
            print()
            l = 0000-00-00
            print()
            a = address()
            
            nbhd = Neighborhood(a)
            
            x = species_dist(nbhd.dist_id)
            
            if s in x and s > 0.1:
                print("This species currently exceeds the recommended limit in this area.")
            
            parcel = Parcel(a, d)
            tree = Tree(s, m, h, l, a, d, status='planned')
            
            community.add_tree(tree)
            print("Tree planned successfully!")
            
        elif choice == "2":
            print()
            s = species()
            print()
            m = maturation()
            print()
            h = health()
            print()
            l = last_seen()
            print()
            a = address()
            print()
            d = area_of_interest()
            
            parcel = Parcel(a, d)
            tree = Tree(s, m, h, l, a, d)
            
            community.add_tree(tree)

        elif choice == "3":
            pass
            # print()
            # s = species()
            # print()
            # m = maturation()
            # print()
            # h = health()
            # print()
            # l = last_seen()
            # print()
            # a = address()
            # print()
            # d = area_of_interest()
            
            # parcel = Parcel(a, d)
            # tree = Tree(s, m, h, l, a, d, status='planned')
            
            # community.add_tree(tree)

        elif choice == "4":
            print("\n=== View Canopy Trends ===")
            # implement visualizations

        elif choice == "5":
            print("\n=== Prioritize Environmental Justice Communities ===")
            # determine priority


        elif choice == "6":
            print("\n=== Analyze Land Use ===")
            # analyze trends / access data


        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()