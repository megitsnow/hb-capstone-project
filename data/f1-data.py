from bs4 import BeautifulSoup
import urllib
import regex as re
import requests
import pprint



drivers_txt = open('drivers.txt')

drivers = {}

for line in drivers_txt:
    line = line.rstrip().replace('"', '')
    driverId, driverRef,number,code,forename,surname,dob,nationality,url  = line.split(",")
    drivers[driverId] = {"driverRef": driverRef, "number": number, "code": code,
    "forename": forename, "surname": surname, "dob": dob, "nationality": nationality, "url": url}

# print(drivers['1']['url'])

def get_main_wiki_image(wiki_url):
    urlpage =  wiki_url
    page = requests.get(urlpage).text

    soup = BeautifulSoup(page, 'html.parser')
    for raw_img in soup.find_all('img'):
        link = raw_img.get('src')
        
        if re.search('wikipedia/.*/thumb/', link) and not re.search('.svg', link):
            break
    return link

for driver in drivers.keys():
    img_url = get_main_wiki_image(drivers[driver]['url'])
    drivers[driver]['img'] = img_url

print(drivers)



    




