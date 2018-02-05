#!/usr/bin/python
# coding:utf-8

import requests

# r = requests.get('https://www.douban.com/')  # 豆瓣首页
# print r.status_code
# print r.text

# 对于带参数的URL，传入一个dict作为params参数：
# r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# print r.url
# requests自动检测编码，可以使用encoding属性查看：
# print r.encoding

# 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
# print r.content

# requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：
# r = requests.get\
#     ('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print r.json()

# 需要传入HTTP Header时，我们传入一个dict作为headers参数：
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print r.text

# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

# # requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头：
# print  r.headers
# # {Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Content-Encoding': 'gzip', ...}
# print r.headers['Content-Type']
# # 'text/html; charset=utf-8'
# # requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
#
# print r.cookies['ts']
# 'example_cookie_12345'