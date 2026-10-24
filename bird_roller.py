#! python3
# bird_roller - randomly chooses a bird species, opens its Wikiedia page
#               and downloads its images via flickr_saver

import bs4, random, requests, webbrowser

# random choice of lists to use
bird_list = ["List_of_birds_of_Asia", "List_of_birds_of_Europe",
             "List_of_birds_of_North_America", "List_of_birds_of_Africa",
             "List_of_birds_of_South_America"]
chosen_url = "https://en.wikipedia.org/wiki/" + random.choice(bird_list)
# get wiki page
res = requests.get(chosen_url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# search for links to species and choose one, ensure it's animal
animal_elem = soup.select('.div-col a')
if chosen_url == "https://en.wikipedia.org/wiki/List_of_birds_of_South_America":
    del animal_elem[:12] # jakies kraje randomowe tam są, oby nikt tego kurwa nie edytował na wiki bo mi sie kod zesra
while True:
    animal = random.choice(animal_elem)
    name = animal.get('title')
    if name.startswith('List') or name.startswith('Lists') or name.startswith('Fauna') or name.startswith('Birds') or name.startswith('The'):
        continue
    break
print('Your bird of the day is %s!' % name)
# open link to their Wiki
link = "https://en.wikipedia.org" + animal.get('href')
webbrowser.open(link)