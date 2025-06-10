#Map all restaurants to their IDs. Used later to not spam API with requests.
import requests
import json
import time

def get_restaurants():
    url1 = "https://kitchen.kanttiinit.fi/restaurants/"
    url2 = "/menu"

    map = {}

    for i in range(1, 100):  # Assuming there are at max 100 restaurants (as is the case 9/6/25):

        time.sleep(0.1) #Add small delay to avoid overwhelming the server

        try:
            url = url1+str(i)+url2
            response = requests.get(url)
            response.raise_for_status()
            data = response.json() 

            map[data['name'].strip()] = int(data['id'])
        except (requests.RequestException, ValueError):
            continue  
    
    res1 = ""
    for key,val in map.items():
        res1 += f"{key.strip()},{val}\n"
    with open("restaurants.txt", "w", encoding="utf-8") as f:
        f.write(res1)

if __name__ == "__main__":
    get_restaurants()