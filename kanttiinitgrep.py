import urllib.request

fp = urllib.request.urlopen("https://folio.kanttiinit.fi/fi/area/7")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

mystr = mystr.split("<h3>")

mystr = mystr[1:]

ravintolat = ["Chemicum"]

copystr = ""

for i, val in enumerate(mystr):
    if val[0:8] in ravintolat:
        copystr = mystr[i]
        break

copystr = copystr.split("<li>")


copystr2 = []

for i in copystr[1:]:
    copystr2.append(i.split("("))

print("Chemicum:")
for i in copystr2:
    print(i[0])