import dotenv
import os
from menuGet import get_menus
from time import strftime, localtime

fetch_time = strftime('%d-%m %H:%M', localtime())

dotenv.load_dotenv()
res = os.getenv("RESTAURANTS").split(",")

menus = get_menus(res)

textWrapLength = 55

total = ""
for index,(key,val) in enumerate(menus.items()):
    if index == 0:
        total += f"{str(key).strip("\n")} (Haettu {fetch_time}):\n"
        total += str(val)
        total += "\n"
    else:
        total += str(key).strip("\n") + ":\n"
        total += str(val)
        total += "\n"

for line in total.split("\n"):
    if len(line) > textWrapLength:
        total = total.replace(line, line[:textWrapLength] + "-\n" + line[textWrapLength:])

print(total.strip("\n"))