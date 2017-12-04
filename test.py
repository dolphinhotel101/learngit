import requests

html = requests.get('http://www.baidu.com')
print(html.text)
