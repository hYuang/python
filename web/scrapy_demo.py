import urllib.request

key="黄杨"
url="http://www.baidu.com/s?wd="
key_code=urllib.request.quote(key)
url_all=url+key_code
req=urllib.request.Request(url_all)
data=urllib.request.urlopen(req).read()
fhandle=open("./data/4.html","wb")
fhandle.write(data)
fhandle.close()
