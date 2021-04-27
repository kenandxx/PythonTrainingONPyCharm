# BeautifulSoup用于从HTML中提取信息的时候比正则表达式好很多
# 虽然叫BeautifulSoup，但是importbs4

import requests, bs4

res = requests.get('http://nostarch.com')  # download homepage
try:
    res.raise_for_status()
except Exception as exc:
    print('Got issue when download Homepage')

noStarchSoup = bs4.BeautifulSoup(res.text)  # 将响应结果的text属性传递给bs4.BeautifulSoup
type(noStarchSoup)  # <class 'bs4.BeautifulSoup'>

print(noStarchSoup)

# or you can open an HTML file like follows
"""
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)
print(exampleSoup)
"""

# 11.5.2 用select()方式寻找元素
# 用method（）方法，传入一个字符串作为CSS选择器，这样就可以取得Web页面元素了哦。@选择器就像正则表达式：它们指定了要寻找的模式，在这个例子里，
# 是在HTML页面中寻找，而不是普通的文本字符串。
# 本书不完整地讨论CCS选择器，请在http://nostarch.com/automatestuff/学习
#
