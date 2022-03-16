import requests
from bs4 import BeautifulSoup


letter = 'S'
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
a = soup.find_all('a')
answer = []
for x in a:
    if x.text.startswith(letter):
        http = x.get('href')
        if (http.find('topics') > 0 or http.find('entity') > 0) and len(x.text) > 1:
            answer.append(x.text)

print(answer)
