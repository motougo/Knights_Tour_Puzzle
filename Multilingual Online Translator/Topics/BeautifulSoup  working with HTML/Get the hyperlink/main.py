import requests
from bs4 import BeautifulSoup


i = input()
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
a = soup.find_all('a')
for x in a:
    if x.text == 'ACT ' + i:
        print(x.get('href'))
