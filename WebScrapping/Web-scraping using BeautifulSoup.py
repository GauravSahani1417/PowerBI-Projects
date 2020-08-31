from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://en.wikipedia.org/wiki/Website"
html = urlopen(url)

soup = BeautifulSoup(html, "html.parser")

type(soup)

all_links = soup.findAll('div', {'class': 'mw-body'})
str_cells = str(all_links)

cleartext = BeautifulSoup(str_cells, "html.parser").get_text()

print(cleartext)