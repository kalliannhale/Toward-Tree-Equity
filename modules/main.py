#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
file - main.py
    demonstrates usage
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
            
            if tree.biodiversity == True:
                print("The concentration of this species is already too high in this neighborhood.")
                print()
            if tree.heat_vuln() and parcel.too_hot():
                print("This species is vulnerable to extreme heat.")
                print("This block experiences high heat.")
                print()
                #Checks if a tree species known for its heat 
                #vulnerability is being planned in an area 
                #with high heat disparity.
            
            print("Would you like to record this plan?")
            answer = decision()
            print()
            
            if answer == 'y':
                tree.plan_tree()
                parcel.planned_trees(tree)
                nbhd.store_parcel(parcel)
                
                community.add_neighborhood(nbhd.dist_id, nbhd.district)
                community.add_tree(tree)
            print("Tree planned successfully!")

        elif choice == "3":
            print("\n=== Record Existing/Planted Tree ===")
            
            print()
            d = area_of_interest()
            print()
            a = address()
            parcel = Parcel(a, d)
            print()
            s = species()
            print()
            m = maturation()
            print()
            h = health()
            print()
            l = last_seen()
            print()
            
            print("Is this tree alive?")
            answer = decision()
            if answer == 'n':
                tree = Tree(s, m, h, l, a, d)
                tree.death()
                parcel.tree_loss(s, m, a)
            else:
                tree = Tree(s, m, h, l, a, d)
            
            nbhd = Neighborhood(d)
            
            
            nbhd.store_parcel(parcel)
            parcel.planned_trees
            parcel.add_tree(tree)
            
            community.add_neighborhood(nbhd.dist_id, nbhd.district)
            community.add_tree(tree)
            
            print("Tree successfully recorded.")

        elif choice == "4":
            print("\n=== Report Loss/Declining Health ===")
            print()
            print("Is this tree already recorded?")
            print()
            
            answer = decision()
            
            if answer == 'y':
                
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
                l = last_seen()
                print()
                
                parcel = Parcel(a, d)
                
                if answer == 'y':
                    parcel.tree_loss(s, m, a, l)
                    community.remove_tree(s, m, a, l)
                    
                if answer == 'n':
                    parcel.decline(s, m, a)
                    
                print("Thank you for reporting.")
                
            if answer == 'n':
                print()
                print("Please enter '3' to capture this tree.")
                continue
            
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
            print()
            print("Thank you for contributing to our community database!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
