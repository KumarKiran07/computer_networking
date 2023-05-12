import urllib.parse
url = 'https://www.yahoo.com:40/shop/abc.html?search=abc'
tpl = urllib.parse.urlparse(url)
print(tpl)
print('Schema = ',tpl.scheme)
print('Net Location = ', tpl.netloc)
print('Net Path = ',tpl.path)
print("Port Number ",tpl.port)
print("Whole URL : ",tpl.geturl())
