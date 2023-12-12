#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:54:33 2023

@author: kalliann
"""

from community import Community
from parcel import Parcel
from tree import Tree
from user_input import user_info, decision, species, area_of_interest, maturation, health, last_seen, address
from neighborhood import Neighborhood

def main():
    
    cdb = "community_database.db"
    community = Community(cdb)
    
    user_name, affiliation = user_info()
    community.add_user(user_name, affiliation)
    community.get_user_info()
    print()

    while True:
        print("\n=== Toward Tree Equity: An Accountability Mapping Tool ===")
        print()
        print("1. Visualize Need")
        print("2. Plan a Tree")
        print("3. Record Existing/Planted Tree")
        print("4. Report Tree Loss/Declining Health")
        print("5. View Volunteer Data")
        print("6. Exit")
        print()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print("\n=== Visualize Need ===")
            
            
        elif choice == "2":
            print("\n=== Plan a Tree ===")
            
            print()
            d = area_of_interest()
            print()
            nbhd = Neighborhood(d)
            print(nbhd)
            
            print()
            a = address()
            parcel = Parcel(a, d)
            print(parcel)
            print()
            
            m = maturation()
            print()
            h = 'good'
            l = 0000-00-00
            
            s = species()
            print()
            
            tree = Tree(s, m, h, l, a, d, status='planned')
            if tree.biodiversity:
                print("The concentration of this species is already too high in this neighborhood.")
                print()
            if tree.heat_vuln() and parcel.too_hot():
                print("This species is vulnerable to extreme heat.")
                print("This block experiences high heat.")
                print()
            
            print("Would you like to record this plan?")
            answer = decision()
            print()
            
            if answer == 'y':
                tree.plan_tree()
                parcel.planned_trees(tree)
                nbhd.store_parcel()
                community.add_neighborhood()
                community.add_tree()
            print("Tree planned successfully!")

        elif choice == "3":
            print("\n=== Record Existing/Planted Tree ===")
            
            print()
            d = area_of_interest()
            print()
            a = address()
            print()
            s = species()
            print()
            m = maturation()
            print()
            h = health()
            print()
            l = last_seen()
            print()
            
            nbhd = Neighborhood(d)
            parcel = Parcel(a, d)
            tree = Tree(s, m, h, l, a, d)
            
            nbhd.store_parcel(parcel)
            parcel.add_tree(tree)
            
            community.add_tree(tree)
            community.add_neighborhood(nbhd.dist_id)
            
            print("Tree successfully recorded.")

        elif choice == "4":
            print("\n=== Report Tree Loss/Declining Health ===")
            
            print()
            d = area_of_interest()
            print()
            a = address()
            print()
            s = species()
            print()
            m = maturation()
            print()

            print("Has this tree died?")
            print()
            answer = decision()
            
            parcel = Parcel(a, d)
            
            if answer == 'y':
                parcel.tree_loss(s, m, a)
                community.remove_tree(s, m, a)
                
            if answer == 'n':
                parcel.decline(s, m, a)
            
            print("Thank you for reporting.")
            
        elif choice == "5":
            print("\n=== View Volunteer Data ===")
            
            print()
            d = area_of_interest()
            print()
            nbhd = Neighborhood(d)
            print(nbhd)
            print()
            
            print("Would you like to investigate a specific address?")
            answer = decision()
            
            if answer == 'y':
                print()
                a = address()
                print()
                parcel = Parcel(a, d)
                print(parcel)
                print()
                
            print("Would you like to view the data logged by our community?")
            answer = decision()
            print()
            
            if answer == 'y':
                print("Addresses logged by our volunteers...")
                print()
                community.print_parcels()

                print("Trees recorded...")
                print()
                community.print_trees()
                print()


        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()