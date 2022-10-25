from bs4 import BeautifulSoup
import urllib
import regex as re
import requests

def get_main_wiki_image(title):
  person_url = []
  urlpage =  'https://en.wikipedia.org/wiki/' + title
  # query the website and return the html to the variable 'page'
  page = requests.get(urlpage).text
  # parse the html using beautiful soup and store in variable 'soup'
  soup = BeautifulSoup(page, 'html.parser')
  for raw_img in soup.find_all('img'):
   link = raw_img.get('src')
   # The first image on the page with the URL strucutre below is usually 
   # the image inside the infobox. We exlcude any .svg images, as they are 
   # vector graphics common to all Wikipedia pages
   if re.search('wikipedia/.*/thumb/', link) and not re.search('.svg', link):
     person_url = [title, link]
     # Once the first image has been found, we break out of the loop and search the next page
     break
  return person_url

title_urls = []
for title in names['title']:
  person_url = get_main_wiki_image(title)
  if person_url:
    title_urls.append(person_url)
    
# Save the results to a dataframe
title_urls_df = pd.DataFrame(title_urls, columns = ['title', 'url'])

# Upload results to BigQuery table 'titles_urls'
dataset_ref = bqclient.dataset('wikipedia')
table_ref = dataset_ref.table('title_urls')
bqclient.load_table_from_dataframe(title_urls_df, table_ref).result()