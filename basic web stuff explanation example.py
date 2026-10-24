import webbrowser, requests

# open link in your browser
url = "https://www.google.com"
webbrowser.open(url)

# download txt (or smth else) and save into file
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
play_file = open('RomeoAndJuliet.txt', 'wb') #notice 'wb' instead of 'w'
for chunk in res.iter_content(100000):
    play_file.write(chunk)
play_file.close()


'''e==element

soup.select('div') - es named <div>

soup.select('#author') - e with an id attribute of author

soup.select('.notice') - es that use a CSS class attribute named notice

soup.select('div span') - es named <span> that are within an e named <div>

soup.select('div > span') - es named <span> that are directly within an e named 
                            <div> with no other element in between

soup.select('input[name]') - es named <input> that have a name attribute with 
                             any value

soup.select('input[type="button"]') - es named <input> that have an attribute named
                                      type with value button'''