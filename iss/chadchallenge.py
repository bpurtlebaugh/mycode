#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Accessing Open APIs with Python"""

# standard library
import json

# 3rd party library
import requests

# Define URL as a global constant (this will not change)
MAJORTOM = 'https://anapioficeandfire.com/api/books'

def main():
    """making API requests"""
    
    # Call the web service
    resp = requests.get(MAJORTOM)  # sends an HTTP GET
    
    # strip JSON data off response and convert
    # to python data types
    data = resp.json()
     
    numbooks = len(data)
    print(f"There are {numbooks} books in the series. They are:")
    print()

     
    # display our Pythonic data
    for book in data:
        print(book.get('name'))
    
    
    #astros = data.get('people') # people is a list of dict
    #print(astros) # this is the list of dict

    # for-loop across astros
    # display names of those in space
    #for astro in astros:
       # print(f"Riding on the {astro['craft']} is:", astro['name'])

if __name__ == '__main__':
    main()
