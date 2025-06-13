
import dotenv
import os
from menuGet import get_menus
dotenv.load_dotenv()
res = os.getenv("RESTAURANTS").split(",")

menus = get_menus(res)

total = ""
for key,val in menus.items():
    total += str(key)
    total += str(val)
    total += "\n"

print(total)