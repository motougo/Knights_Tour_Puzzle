import requests
from bs4 import BeautifulSoup

i = int(input())
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
headings = soup.find_all('h2')
print(headings[i].text)
