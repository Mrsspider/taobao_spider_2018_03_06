import re
import requests
from lxml import etree

from random import choice
import random
from time import sleep
from functings.spider_function import *
from settings.spider_setting import *

x = random.randint(1,3)

# 存档
def mywith(filename,result):
    try:
        with open(filename,'a',encoding='utf8') as f:
            f.writelines(result)
    except Exception as e:
        logbook = {'errorFunc':'mywrith','mywrith':e}
        with open('../logbook/logbook.txt','a',encoding='utf8') as f:
            f.writelines((str(logbook)+'\n'))


# 提取html页面
def gethtml(url):
    '''输入url,输出字符串respons.text'''
    # try:
    respons = requests.get(url,choice(getip()),headers=headers)
    respons.encoding
        # sleep(x)
    return respons.text
    # except Exception as e:
    #     logbook = {'errorFunc':'gethtml','errorType':e,'errorUrl':url,'errorHeaders':headers}
    #     mywith('../logbook/logbook.txt', str(logbook) + '\n')
    #     return None

# 使用xpath解析网页
def htmlparser(html):
    try:
        html = etree.HTML(html,parser=etree.HTMLParser())
        return html
    except Exception as e:
        logbook = {'errorFunc':'htmlparser','htmlparser':e}
        mywith('../logbook/logbook.txt', str(logbook) + '\n')





# 该函数测试ip是否可用，可用的ip作为列表输出
def test_ip(iplist):
    '''没有参数，输出可用[ip:port,...]列表'''
    prolist = []
    try:
        for ip in iplist:
            url = 'https://www.baidu.com/'
            pro = {'http':ip}
            head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
            test_num = requests.get(url,proxies=pro,headers=head).status_code
            if test_num == 200:
                prolist.append(ip+',')
            with open('../settings/proxy.txt','a',encoding='utf8') as f:
                f.writelines(prolist)
    except Exception as e:
        e = {'test_ip':e}
        with open('../logbook/logbook.txt','a',encoding='utf-8') as f:
            f.writelines(str(e))


# 该函数爬取速度小于3s的ip并写入proxy.text
def get_ip(num):
    '''输入爬取页数，把ip以逗号间隔写入proxy.txt首行'''
    url = 'https://www.kuaidaili.com/free/inha/'
    try:
        iplist = []
        for i in range(1,num):
            url = url + str(i)
            respons = requests.get(url).text
            pat = '<td data-title="IP">(.*?)</td>\s+<.*?>(\d+)</td>\s+<.*?>高匿名</td>\s+<.*?>.*?</td>\s+<.*?>.*?<.*?>\s+<.*?>(.*?)秒<'
            pattern = re.compile(pat)
            prolist = re.findall(pattern,respons)
            for pro in prolist:
                print(pro)
                if float(pro[2]) < 3:
                    pro = pro[0]+':'+pro[1]
                    iplist.append(pro)
        print('正在测试爬取到的ip',iplist)
        test_ip(iplist)
    except Exception as e:
        e = {'getip':e}
        with open('../logbook/logbook.txt','a',encoding='utf-8') as f:
            f.writelines(str(e))

def write_log(d):
    with open('../logbook/logbook.txt', 'a', encoding='utf-8') as f:
        f.writelines(str(d))


if __name__ == '__main__':
    get_ip(20)

