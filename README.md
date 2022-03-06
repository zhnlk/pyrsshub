# pyrsshub

> 🍰 万物皆可 RSS

RSSHub 是一个轻量、易于扩展的 RSS 生成器，可以给任何奇奇怪怪的内容生成 RSS 订阅源

本项目是
[原RSSHub](https://github.com/DIYgod/RSSHub)的Python实现。  
[原RSSHub-python](https://github.com/hillerliao/RSSHub-python)的重构版本
pyrsshub base RSSHub-python which based RSSHub

**其实用Python写爬虫要比JS更方便:p**


## RSS过滤

你可以通过以下查询字符串来过滤RSS的内容：

- include_title: 搜索标题
- include_description: 搜索描述
- exclude_title: 排除标题
- exclude_description: 排除描述
- limit: 限制条数

## 贡献RSS方法

1. fork这份仓库
2. 在spiders文件夹下创建新的爬虫目录和脚本，编写爬虫
3. 在blueprints的main.py中添加对应的路由（按照之前路由的格式）
4. 在templates中的main目录下的feeds.html上写上说明文档，同样可参照格式写
5. 提pr

## 部署

### 搭建

``` bash
git clone https://github.com/zhnlk/pyrsshub
cd pyrsshub
pip install -r ./requirements.txt
```

### 运行

``` bash
flask run
```

### Docker 部署

制作镜像文件 `docker image build -t rsshub_python .`

创建docker容器 `docker run -dit -p 6666:6666 --name rsshub rsshub_python`
