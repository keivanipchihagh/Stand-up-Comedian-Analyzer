# Transcripts URLs
urls = [
    'https://scrapsfromtheloft.com/2017/05/06/louis-ck-oh-my-god-full-transcript/',
    'https://scrapsfromtheloft.com/2017/04/11/dave-chappelle-age-spin-2017-full-transcript/',
    'https://scrapsfromtheloft.com/2018/03/15/ricky-gervais-humanity-transcript/',
    'https://scrapsfromtheloft.com/2017/08/07/bo-burnham-2013-full-transcript/',
    'https://scrapsfromtheloft.com/2017/05/24/bill-burr-im-sorry-feel-way-2014-full-transcript/',
    'https://scrapsfromtheloft.com/2017/04/21/jim-jefferies-bare-2014-full-transcript/',
    'https://scrapsfromtheloft.com/2017/08/02/john-mulaney-comeback-kid-2015-full-transcript/',
    'https://scrapsfromtheloft.com/2017/10/21/hasan-minhaj-homecoming-king-2017-full-transcript/',
    'https://scrapsfromtheloft.com/2017/09/19/ali-wong-baby-cobra-2016-full-transcript/',
    'https://scrapsfromtheloft.com/2017/08/03/anthony-jeselnik-thoughts-prayers-2015-full-transcript/',
    'https://scrapsfromtheloft.com/2018/03/03/mike-birbiglia-my-girlfriends-boyfriend-2013-full-transcript/',
    'https://scrapsfromtheloft.com/2017/08/19/joe-rogan-triggered-2016-full-transcript/'
    ]


# Imports
from bs4 import BeautifulSoup
import requests

def get_transcript(url):
    ''' Get paragraph contents of the URL in the spesified Div element'''
    
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    texts = [p.text for p in soup.find(class_ = 'elementor-widget-theme-post-content').find_all('p')]
    
    print('Got contents for "{0}"'.format(url))
    return texts

# Get transcrpts for all the URLs
transcripts = [get_transcript(url) for url in urls]
print('Scraping completed.')

names = [
    'Lousic C.K.',
    'Dave Chappelle',
    'Ricky Gervais',
    'Bo Burham',
    'Bill Burr',
    'Jim Jefferies',
    'John Mulaney',
    'Hasan Minhaj',
    'Ali Wong',
    'Anthony Jeselnik',
    'Mike Birbiglia',
    'Joe Rogan'
]


# Imports
import pickle

all_data = dict(zip(names, transcripts))

with open('saves/transcripts_data.json', 'wb') as file:
    pickle.dump(all_data, file)
