import urllib.request
try:
    # if you want to download from internet than use like
    file = urllib.request.urlopen("https://www.python.org")
    #file = urllib.request.urlopen("file:///Z://New Folder//FOW//SetInterval.html")
    content = file.read()
    print(content)
except urllib.error.HTTPError as httpErr:
    print(httpErr)
    exit()
except Exception as ex:
    print(ex)
    exit()
f = open('myfile.html','wb')
f.write(content)
f.close()
