#! python3
# flickr_saver - saves X amount of images of searched thing from flickr

import requests, bs4, logging, sys
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of the program.')

def download(name, amount):
    logging.debug('Start of "download".')
    # search for "name"
    name = name.replace(' ', '%20')
    url = "https://www.flickr.com/search/?text=" + name
    logging.info('Url of your search result: ' + url)
    # get url of page of image
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    img_p_elem = soup.select('#yui_3_16_0_1_1627924401607_920')
    # crits if nothing found
    if soup == '':
        logging.critical('No soup!!!')
        sys. exit()
    if img_p_elem == []:
        logging.critical('Nothing found in soup :(')
        sys.exit()
    # download image
    for i in range(0, amount):
        img_p_url = img_p_elem[i].get('href')
        print(img_p_url)

download('king quail', 3)
loggin.debug('End of the program.')

#'.sizes .Original a'