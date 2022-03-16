import requests
from bs4 import BeautifulSoup
import sys

languages = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese',
             'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']

args = sys.argv
if len(args) > 1:
    lang_from = 1 + languages.index(args[1].title())
    if args[2] == 'all':
        lang_to = 0
    else:
        try:
            lang_to = 1 + languages.index(args[2].title())
        except ValueError:
            print("Sorry, the program doesn't support", args[2])
            quit()

    word = args[3]
else:
    print("Hello, you're welcome to the translator. Translator supports:")
    for count, value in enumerate(languages):
        print(count+1, '. '+value, sep='')

    lang_from = int(input('Type the number of your language: '))
    lang_to = int(input("Type the number of a language you want to translate to or '0' "
                        "to translate to all languages: "))
    word = input('Type the word you want to translate: ')

url_base = 'https://context.reverso.net/translation/'
headers = {'User-Agent': 'Mozilla/5.0'}

language = []
word_to = []
if lang_to != 0:
    language.insert(0, languages[lang_from - 1].lower()+'-'+languages[lang_to - 1].lower()+'/')
    word_to.insert(0, languages[lang_to - 1])
else:
    count = 0
    for lang in languages:
        if languages[lang_from - 1].lower() != lang.lower():
            language.insert(count, languages[lang_from - 1].lower()+'-'+lang.lower()+'/')
            word_to.insert(count, lang)
        count += 1

word_count = 0
file_input = ""
for lang in language:
    url = url_base + lang + word
    while True:
        page = requests.get(url, headers=headers)
        if page.status_code == 200:
            # print(page.status_code, page.reason)
            break
        elif page.status_code == 404:
            print('Sorry, unable to find', word)
            quit()
        else:
            print('Something wrong with your internet connection')
            quit()
            
    soup = BeautifulSoup(page.content, 'html.parser')
    trans_tags = soup.find_all('a', class_='translation')

    example_src_tags = soup.find_all('div', class_='src')
    example_trg_tags = soup.find_all('div', class_='trg')

    print('\n' + word_to[word_count] + ' Translations:')
    file_input = file_input + word_to[word_count] + ' Translations:' + '\n'

    count = 0
    for i in trans_tags:
        if i.text.strip() != 'Translation':
            print(i.text.strip())
            file_input = file_input + i.text.strip() + '\n'
            count += 1
            if count == 1:
                break

    print('\n' + word_to[word_count] + ' Examples:')
    file_input = file_input + '\n' + word_to[word_count] + ' Examples:' + '\n'
    word_count += 1

    count = 0
    for i, j in zip(example_src_tags, example_trg_tags):
        count += 1
        print(i.text.strip())
        file_input = file_input + i.text.strip() + '\n'
        print(j.text.strip())
        file_input = file_input + j.text.strip() + '\n'
        file_input = file_input + '\n'
        if count == 1:
            break
        else:
            print('\n')

filename = word + '.txt'
file = open(filename, 'w', encoding='utf-8')
file.write(file_input)
file.close()
