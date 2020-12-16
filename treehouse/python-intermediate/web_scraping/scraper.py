from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://isbnsearch.org/isbn/9780743277464')
soup = BeautifulSoup(html.read(), 'html.parser')

print(soup.title)

divs = soup.find_all('div', {'class': 'featured'})
for div in divs:
    print(div)


print(soup.prettify())