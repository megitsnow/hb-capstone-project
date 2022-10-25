from bs4 import BeautifulSoup
import urllib
import regex as re
import requests


constructors_txt = open('constructors.txt')

constructors = {}

for line in constructors_txt:
    line = line.rstrip().replace('"', '')
    constructorId, constructorRef, name, nationality, url  = line.split(",")
    constructors[constructorId] = {"constructorRef": constructorRef, 
    "name": name, "nationality": nationality, "url": url}



def get_main_wiki_image(wiki_url):
    urlpage =  wiki_url
    page = requests.get(urlpage).text

    soup = BeautifulSoup(page, 'html.parser')
    for raw_img in soup.find_all('img'):
        link = raw_img.get('src')
        
        if re.search('wikipedia/.*/thumb/', link) and not re.search('.svg', link):
            break
    return link

for constructor in constructors.keys():
    img_url = get_main_wiki_image(constructors[constructor]['url'])
    constructors[constructor]['img'] = img_url

print(constructors['1']['img'])
print(constructors['2']['img'])
print(constructors['3']['img'])
print(constructors['4']['img'])