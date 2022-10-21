import requests
from bs4 import BeautifulSoup
import random
import concurrent.futures



def getProxies():
    r = requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('tbody')
    proxies= []
    for row in table:
        if row.find_all('td')[4].text =='elite proxy':
            proxy= ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
            proxies.append(proxy)
        else:
            pass
    return proxies
def extract(proxy):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'} 
    try:
        
        r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http' : proxy, 'https' : proxy}, timeout=1)
        print(r.json(), r.status_code)
    except:
        pass
    return proxy

proxylist = getProxies()
print(len(proxylist))
# print(proxylist)
for i in proxylist:
    print(i)
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract, proxylist)