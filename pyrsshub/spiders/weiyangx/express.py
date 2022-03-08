import requests
import json
from parsel import Selector
from pyrsshub.utils import default_headers

domain = 'https://www.weiyangx.com'


def parse(post):
    item = {}
    item['title'] = post['post_title']
    item['description'] = post['post_content']
    post_id = post['post_id']
    item['link'] = f'{domain}/{post_id}.html'
    item['pubDate'] = post['post_date'][0] + '-' + \
        post['post_date'][1] + '-' + \
        post['post_date'][2]
    return item


def ctx():
    url = f'https://www.weiyangx.com/category/express'
    res = requests.get(url, headers=default_headers)
    res = Selector(res.text)
    posts = res.css('script::text')[-4].extract().split('=')[-1]
    posts = json.loads(posts)
    items = list(map(parse, posts))
    return {
        'title': f'快讯 - 未央网',
        'description': f'快讯 - 未央网',
        'link': f'{domain}/category/express',
        'author': f'hillerliao',
        'items': items
    }
