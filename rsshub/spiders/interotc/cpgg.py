import requests
from rsshub.utils import default_headers

domain = 'https://www.interotc.com.cn'


def parse(post):
    item = {}
    end_date = ''
    if '东兴证券' in post['TITLE']:
        end_date = post['CONTENT'].split('存续期到期日')[1].split('。')[0]
    item['title'] = post['TITLE'] + ' (' + post['CPDM'] + ', ' + end_date +  ', ' + post['CPMC'] + ')'    
    item['description'] = post['CONTENT']
    item['link'] = f'{domain}/portal/newportal/cpggDetail.html?bdid=' + str(post['BDID'])
    item['pubDate'] = post['FBSJ']
    return item 


def ctx(category=''):
    default_headers.update({'Host': 'www.interotc.com.cn'})
    url = f'{domain}/zzjsInterface/interface/fixedIncome/lettersListNew.json'
    # req_params = {'pageSize': '10','startDate':'-1', 'keyword': category, 'pageIndex': '1'}
    # posts = requests.post(url, \
    #         data=req_params, headers=default_headers)
    req_params = f'?keyword={category}&pageSize=150'
    posts = requests.get(url+req_params)
    import json
    posts = json.loads(posts.text)['resultSet']           
    return {
        'title': f'{category} - 产品公告 - 机构间市场',
        'link': f'{domain}/portal/newportal/cpgg.html',
        'description': f'{category}的产品公告',
        'author': 'hillerliao',
        'items': list(map(parse, posts))
    }