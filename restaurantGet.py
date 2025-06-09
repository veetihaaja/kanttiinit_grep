#Fetch and compile dictionary of restaurants from the database
import requests
import json
import time

def get_restaurants():
    #Get the full list of restaurants from the kanttiinit.fi API, along with their menus.
    #The API is not documented, so this is a best-effort attempt to scrape the data.
    url1 = "https://kitchen.kanttiinit.fi/restaurants/"
    url2 = "/menu"

    map = {} #Mapping of restaurant names to their IDs, if needed
    foods = {}  #Actual food items, indexed by restaurant name

    for i in range(1, 100):  # Assuming there are at max 100 restaurants (as is the case 9/6/25):

        time.sleep(0.1) #Add small delay to avoid overwhelming the server

        try:
            url = url1+str(i)+url2
            response = requests.get(url)
            response.raise_for_status()
            data = response.json() 

            map[data['name'].strip()] = int(data['id'])
            if data['menus']:
                #If a menu exists, add its relevant items to the foods dictionary as a print-ready string
                ruokalista = "" #Construct a printable list of food items with their properties

                for item in data['menus'][0]['courses']: #Assuming we only want the first menu
                    ruokalista += item['title'] + " "
                    ruokalista += ", ".join(item['properties']) 
                    ruokalista += "\n"
                foods[data['name'].strip()] = ruokalista
            else:
                foods[data['name'].strip()] = "Ei ruokaa tänään\n"
        except (requests.RequestException, ValueError):
            continue  
    
    res = ""
    for key in map.keys():
        res += f"{key.strip()}\n"
    with open("restaurants.txt", "w", encoding="utf-8") as f:
        f.write(res)

    return (map, foods)