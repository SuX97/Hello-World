import requests
from bs4 import BeautifulSoup
import numpy
import socket
import time

link = 'https://wenku.baidu.com/view/89c4d71a79563c1ec5da718a.html?from=search'

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
						'Host':'wenku.baidu.com'
					}

r = requests.get(link,headers=headers,timeout=100)

print(r.text.replace(u'\xb3',u'').replace(u'\xf5',u''))