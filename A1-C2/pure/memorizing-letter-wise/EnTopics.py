import requests as r
from bs4 import BeautifulSoup as BS

base_url = 'https://langeek.co'
url = 'https://langeek.co/en/grammar/'
topics = [
    '2/pronouns',
    '3/tenses',
    '6/nouns',
    '5/verbs',
    '22/moods',
    '4/modals',
    '21/adjectives',
    '7/adverbs',
    '8/determiners',
    '10/prepositions-and-conjunctions',
    '19/grammatical-functions',
    '20/phrases-and-clauses',
    '9/sentences',
    '12/punctuation-and-spelling',
    '17/etymology-and-morphology',
    '18/misc',
]

for topic in topics:
    topic_url = f'{url}{topic}'
    print(topic_url)
    html = r.get(topic_url).text
    bs = BS(html, 'html.parser')
    links = bs.find_all('a')
    print([base_url+link.get('href') for link in links if \
                link.get('href') and link.get('href').startswith('/en/grammar/course/')
                # and link.get('href')[...] in '0123456789'
          ])
    print('-'*79)
