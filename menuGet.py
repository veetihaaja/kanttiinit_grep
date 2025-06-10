#Fetch and compile dictionary of restaurants from the database
import requests
import json
import time

def get_menus(wanted):
    url1 = "https://kitchen.kanttiinit.fi/restaurants/"
    url2 = "/menu"

    menus = {} 

    entries =  {}
    with open("restaurants.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                a, b = line.split(",")
                entries[a.strip()] = int(b.strip())

    for a in wanted:  

        time.sleep(0.1) 

        try:
            url = url1+str(entries[a.strip()])+url2
            response = requests.get(url)
            response.raise_for_status()
            data = response.json() 

            if data['menus']:
                #If a menu exists, add its relevant items to the foods dictionary as a print-ready string
                ruokalista = "" #Construct a printable list of food items with their properties

                for item in data['menus'][0]['courses']: #Assuming we only want the first menu
                    ruokalista += item['title'] + " "
                    ruokalista += ", ".join(item['properties']) 
                    ruokalista += "\n"
                menus[data['name'].strip()+":\n"] = ruokalista
            else:
                menus[data['name'].strip()+":\n"] = "Ei ruokaa tänään\n"
        except (requests.RequestException, ValueError):
            continue  
    
    return(menus)