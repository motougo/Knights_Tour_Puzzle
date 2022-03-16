import requests
from bs4 import BeautifulSoup

word = input()
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
p = soup.find_all('p')

for x in p:
    if x.text.find(word) > 0:
        print(x.text)
        break
