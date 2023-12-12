"""
module -- user_input.py

Creates functions to aid the collection of user input in main.

"""

from pygris.geocode import geocode

def user_info():
    '''
    function -- user_info
        collects user name and organizational affiliation.

    returns -- tuple
        two variables: user_name, affiliation
    '''
    user_name = input("Enter your name: ")
    affiliation = input("Enter your organizational affiliation: ")
    return user_name, affiliation

def decision():
    '''
    function -- decision
        collects a user decision, attempts to valid input.

    returns -- str
        'y' for yes or 'n' for no.
    '''
    while True:
        user_input = input("Type 'Y' for yes or 'N' for no: ").upper()
        print()
        d = user_input.strip().lower()

        if d == 'y' or d == 'n':
            print("Got it, thanks!")
            return d
        else:
            print("Invalid input. Please type 'Y' for yes or 'N' for no.")
            print()

def species():
    '''
    function -- species
        allows user to choose from a list of top 
        tree species, input a new one, and ensures valid input.

    returns -- str
        The selected tree species.
    '''
    sp = ['littleleaf linden', 'norway maple', 'crabapple spp',
          'hedge maple', 'red maple', 'green ash', 'japanese zelkova',
          'norther red oak', 'japanese tree lilac', 'american sycamore',
          'honeylocust', 'pin oak', 'sweetgum', 'london planetree',
          'ginko', 'american elm', 'kwanzan cherry', 'accolade elm',
          'other'
          ]

    s = input("What species are you interested in? ")

    while s.lower().strip() not in sp:
        print()
        for x in sp:
            print(x)
        print()
        s = input("Please choose from one of the above: ")

    print("Got it, thanks!")
    print()

    if s == 'other':
        return input("What is the name of the species you would like to record?")

    return s.lower().strip()

def area_of_interest():
    '''
    function -- area_of_interest
        determines the district a user is
        interested in; ensures valid input.

    returns -- str
        the selected neighborhood.
    '''
    districts = ['allston brighton', 'back bay', 'beacon hill',
                 'charlestown', 'central', 'dorchester',
                 'east boston', 'fenway', 'longwood',
                 'hyde park', 'jamaica plain', 'mattapan',
                 'mission hill', 'roslindale', 'roxbury',
                 'south boston', 'south end', 'west roxbury'
                 ]

    r = input("Type the name of the neighborhood you're interested in: ")

    while r.lower().strip() not in districts:
        print()
        for d in districts:
            print(d)
        print()
        r = input("Please choose from one of the above: ")

    print()
    print("Got it, thanks!")
    print()

    return r.lower().strip()

def maturation():
    '''
    function -- maturation
        prompts user to select the maturation stage of a 
        tree, validates input.
        
    returns -- str
        the selected tree maturation.
    '''
    maturation = ['seedling', 'young', 'establishing', 'maturing', 'mature']

    print("Identify the maturation of your tree:")
    print()
    print("seedling - just planted/less than 1")
    print("young - less than 6 years old")
    print("establishing - less than 18 years old")
    print("maturing - less than 24 years old")
    print("mature - 25 years or older")
    print()

    m = input("How old is your tree? ")

    while m.lower().strip() not in maturation:
        print()
        for x in maturation:
            print(x)
        print()
        m = input("Type one of the above: ")

    print()
    print("Got it, thanks!")
    print()

    return m.lower().strip()

def health():
    '''
    function -- health
         allows user to record either 'good' for a
         healthy/normal tree, or 'poor' for a tree
         of exceptionally bad health.

    returns -- str
        the tree health status selected.
    '''
    health = ['good', 'poor']

    print("Tree Health:")
    print()
    print("Unless your tree is on the decline, indicate 'good' for good health.")
    print("If your tree is clearly declining, indicate 'poor.'")
    print()

    h = input("Is your tree's health good or poor? ")

    while h.lower().strip() not in health:
        print()
        for h in health:
            print(h)
        print()
        h = input("Type one of the above: ")

    print()
    print("Got it, thanks!")
    print()

    return h.lower().strip()

def address():
    '''
    function -- address
        Attempts to geocode the address input; user has
        four attempts, and is warned on the third attempt 
        that if this geocoding fails, a raw address 
        with limited features of analysis will be stored.

    returns -- str
        some address.
    '''
    for attempt in range(4):
        print('Where is this tree?')
        a = input('Enter address: ')

        try:
            geocode(a)
            return a

        except Exception as e:
            print()
            print(f"Geocoding failed for address '{address}': {e}")
            print()

            print('Please format addresses accordingly:')
            print("100 Wilmer Ave, Boston, MA")
            print('Make sure to include commas; do not include unit numbers.')
            print()

            if attempt < 2:
                print("Please try again.")
                print()
            elif attempt == 2:
                print("This is your last attempt.")
                print()
            else:
                print('Geocoding is not possible at this address.')
                print('Some features of analysis may not be available.')
                print(f"The address you've entered is: {a}.")

                return a.lower().strip()

def last_seen():
    '''
    function -- last_seen
        Collects user input for the date 
        when the tree was recorded.

    returns -- str
        the recorded date in the format YYYY-MM-DD.
    '''
    date = input("When did you record this tree? "
                 "Use the following format: YYYY-MM-DD "
                 )
    
    while len(date) < 8:
        print()
        print("Sorry. Wrong format.")
        date = input('Please try again: ')
        date.strip()
        print()

    print()
    print("Got it, thanks!")
    print()

    return date
