import urllib.request
from time import strftime, localtime
import sys

def gethtml(url):

    try:
        req = urllib.request.urlopen(url)
        rawhtml = req.read()
        htmlstr = rawhtml.decode("utf8")
        req.close()
    except:
        print("Error fetching the URL, stopping script")
        htmlstr = ""
        sys.exit()
    return htmlstr

def parseFoodData(htmlstr, restaurantsToDisplay):
    """
    Parses the HTML string from the Kanttiinit website and extracts food data for specified restaurants.
    returns a dictionary with restaurant names as keys and their food items as a string.
    """

    #dictionary for final data
    foodRawData = {i:"" for i in restaurantsToDisplay}
    foodFinalData = {i:"" for i in restaurantsToDisplay}

    # used for parsing
    urldict = {"Chemicum":"https://unicafe.fi/restaurants/chemicum/",
               "Exactum":"https://unicafe.fi/restaurants/exactum/",
               "Chemicum Opettajien ravintola":"https://unicafe.fi/restaurants/chemicum-opettajien-ravintola/"}
    
    #split by restaurant header
    dataList = htmlstr.split("<h3>")

    #get desired restaurants
    for data in dataList:
        for restaurant in restaurantsToDisplay:
            if urldict[restaurant] in data:
                foodRawData[restaurant]=data
    
    #check for "ei ruokalistaa"
    for restaurant in foodRawData.keys():
        if "Ei ruokalistaa." in foodRawData[restaurant]:
            foodFinalData[restaurant] = "Ei ruokalistaa."
            foodRawData[restaurant] = ""

    #split by list item:
    for restaurant in foodRawData.keys():
        if foodRawData[restaurant] != "":
            foodRawData[restaurant] = foodRawData[restaurant].split("<li>")
            foodRawData[restaurant] = foodRawData[restaurant][1:]

    for restaurant in foodRawData.keys():
        if foodRawData[restaurant] != "":
            for i in range(len(foodRawData[restaurant])):
                foodRawData[restaurant][i] = foodRawData[restaurant][i].split("(")
                foodRawData[restaurant][i][0] = foodRawData[restaurant][i][0].strip()

    for restaurant in foodRawData.keys():
        if foodRawData[restaurant] != "":
            for i in range(len(foodRawData[restaurant])):
                foodFinalData[restaurant] += foodRawData[restaurant][i][0]
                for flag in foodRawData[restaurant][i][1:]:
                    if "vegan" in flag:
                        foodFinalData[restaurant] += " V"
                    if "gluten-free" in flag:
                        foodFinalData[restaurant] += " G"
                    if "lactose-free" in flag:
                        foodFinalData[restaurant] += " L"
                foodFinalData[restaurant] += "\n"

    return foodFinalData

restaurantsToDisplay = ["Chemicum", "Exactum", "Chemicum Opettajien ravintola"]

htmlstr = gethtml("https://folio.kanttiinit.fi/fi/area/7")
foodToDisplay = parseFoodData(htmlstr, restaurantsToDisplay)

index = 0
#print fetch time with the first restaurant name
for restaurant in foodToDisplay.keys():
    if index ==0:
        print(f"{restaurant}: (haettu {strftime('%d-%m %H:%M', localtime())})")
    else: 
        print(f"{restaurant}:")

    if foodToDisplay[restaurant] == "Ei ruokalistaa.":
        print(foodToDisplay[restaurant])
        print()
    else:
        print(foodToDisplay[restaurant])

    index += 1