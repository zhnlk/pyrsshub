# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author: zhnlk


import requests

domain = 'https://app.jiucaigongshe.com/jystock-app/api/v2/article/community'

cookies = {
    'SESSION': 'NGE0NDdmM2MtYTg1MC00Y2U0LTllMWEtOGQ5YWM3OGEzOTBh',
    'UM_distinctid': '17f608807f08c2-0ede015138b24a-37677109-1aeaa0-17f608807f2782',
}

headers = {
    'Host': 'app.jiucaigongshe.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
    'content-type': 'application/json',
    'accept': 'application/json, text/plain, */*',
    'timestamp': '1646597391980',
    'platform': '3',
    'token': '7392940b976998584d6abcc267b3f3d8',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://www.jiucaigongshe.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.jiucaigongshe.com/',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
}


def parse(post):
    item = {}
    item['title'] = post['title']
    item['description'] = post['content']
    item['link'] = 'https://www.jiucaigongshe.com/action/detail/' + str(post['article_id'])
    item['pubDate'] = str(post['create_time'])
    item['author'] = post['user_id']
    return item


def ctx(start):
    data = '{"category_id":"","limit":15,"order":1,"start":' + start + ',"type":0,"back_garden":0}'
    posts = requests.post(domain, headers=headers, cookies=cookies, data=data).json()['data']['result']

    # pprint(response.json()['data']['result'])
    # for i in response.json()['data']['result']:
    #     print(i['content'])

    return {
        'title': '基本面挖掘的社群文章',
        # 'link': f'{domain}//lists/{category}.html',
        'link': 'https://www.jiucaigongshe.com/',
        'description': '韭菜公社',
        'author': 'ccat',
        'items': list(map(parse, posts))
    }
