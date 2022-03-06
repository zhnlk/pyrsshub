from rsshub.utils import default_headers
from rsshub.utils import fetch

domain = 'http://www.jintiankansha.me'


def parse(post):
    item = {}
    item['description'] = item['title'] = post.css('a::text').extract_first()
    item['link'] = post.css('a::attr(href)').extract_first()
    return item


def ctx(category=''):
    url = f'{domain}/column/{category}'
    default_headers.update({'Host': 'www.jintiankansha.me'})
    tree = fetch(url, headers=default_headers)
    posts = tree.css('.cell.item')
    items = list(map(parse, posts))

    column_title = tree.css('title::text').extract_first()
    return {
        'title': f'{column_title}',
        'description': f'{category}',
        'link': url,
        'author': f'hillerliao',
        'items': items
    }
