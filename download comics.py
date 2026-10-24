#! python3
# download comics

import requests, os, bs4

url = 'https://www.oglaf.com'       # starting url
os.makedirs('OGLAF', exist_ok=True) # make ./OGLAF for storing comics
while True:
    # download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # find url of comic image
    comic_elem = soup.select('#strip') #############
    if comic_elem == []:
        print('Could not find comic image')
    else:
        comic_url = comic_elem[0].get('src')
        # download comic
        print('Downloading image %s...' % (comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()
        # save image to ./OGLAF
        image_file = open(os.path.join('OGLAF', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
    # get prev button's url
    try:
        prev_link = soup.select('a[rel="prev"]')[0]
    except:
        break
    url = 'https://www.oglaf.com' + prev_link.get('href')

print('Done.')