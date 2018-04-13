from functings.spider_function import gethtml

url = 'https://s.taobao.com/search?q=%E5%A5%B3%E8%A3%85&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180306&ie=utf8'
html = gethtml(url)
print(html)