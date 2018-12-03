import requests
url="https://img13.360buyimg.com/n7/jfs/t3391/79/1963324994/297093/187de6d4/583ced0fN27e50577.jpg"
res=requests.get(url=url, verify=False)

with open("jd1.jpg","wb") as fd:
    fd.write(res.content)

import re
url="https://p.3.cn/prices/mgets?callback=jQuery6775278&skuids=J_5089253"
res=requests.get(url, verify=False)
print(res.text)
pat='"p":"(.*?)"}'
price=re.compile(pat).findall(res.text)
print(price)

url="https://list.jd.com/list.html?cat=9987,653,655"
res=requests.get(url, verify=False)
imagepat='<img width="220" height="220" data-img="1" data-lazy-img="//(.*?)">'
imagelist=re.compile(imagepat).findall(res.text)
print(imagelist)

x=1
for imageurl in imagelist:
    imagename="jdpic\\"+str(x)+".jpg"
    x+=1
    imageurl="http://"+imageurl
    res=requests.get(imageurl, verify=False)
    with open(imagename,'wb') as fd:
        fd.write(res.content)