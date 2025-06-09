
import dotenv
import os
from restaurantGet import get_restaurants
dotenv.load_dotenv()
res = os.getenv("RESTAURANTS").split(",")

map, foods = get_restaurants()
wanted_list = ""

for a in res:
    if a.strip() in foods.keys():
        wanted_list += a.strip() + "\n"
        wanted_list += foods[a.strip()]
        wanted_list += "\n"
    else:
        continue

print(wanted_list)