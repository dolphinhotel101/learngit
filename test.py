import requests

html = requests.get('http://www.baidu.com')
print(html.text)

# it's python3, ofcourse.
