import requests
import json
from pyrsshub.utils import default_headers

domain = 'https://techcrunch.com'

def parse(post):
    item = {}
    item['title'] = post['title']['rendered']
    item['description'] = post['content']['rendered']
    item['link'] = post['link']
    item['pubDate'] = post['date_gmt']
    return item

def ctx(category=''):
    url = f'{domain}/wp-json/tc/v1/magazine?tags={category}'
    res = requests.get(url, headers=default_headers)
    res = json.loads(res.text)
    posts = res 
    items = list(map(parse, posts))
    return {
        'title': f'{category} - tag - Techcrunch',
        'description': f'{category} - tag - Techcrunch',
        'link': f'f{domain}/tag/fintech/',
        'author': f'hillerliao',
        'items': items
    }