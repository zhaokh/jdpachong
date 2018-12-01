import requests,sys,json,time,os
from bs4 import BeautifulSoup
from contextlib import closing
from requests.packages import urllib3


class get_protos:

     def __init__(self):
          self.protoes_id = []
          self.download_server = 'https://unsplash.com/photos/xxx/download?force=trues'
          self.next_page = 'https://unsplash.com/napi/photos?page=xxx&per_page=10&order_by=latest ' # 每页10张图片
          self.target = 'http://unsplash.com/napi/feeds/home'
          self.headers = {'authorization':'Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626'}

     def get_ids(self):


          #req = requests.get(url=self.target, headers=self.headers, verify=False)
          #html = json.loads(req.text)
          #for each in html:
          #     self.protoes_id.append(each['id'])
          #time.sleep(1)


          for i in range(5):
               next_page = self.next_page.replace('xxx', str(i+1))
               print(next_page)
               req = requests.get(url=next_page, verify=False)
               html = json.loads(req.text)
               for each in html:
                    self.protoes_id.append(each['id'])
               time.sleep(1)
     
     def download(self,photo_id, filename):
          headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
          target = self.download_server.replace('xxx', photo_id)
          dir = os.getcwd () + "\\pics\\"
          if not os.path.exists(dir):
               os.makedirs(dir)
             
          with closing(requests.get(url=target, stream=True, verify = False, headers = self.headers)) as r:
                #closing(object) 创建上下文管理器，在执行过程离开with语句体时自动执行object.close()。
                with open(dir+'%d.jpg' % filename, 'ab+') as f:
                    # open() 函数用于打开一个文件，创建一个 file 对象, ab+ 以二进制打开yi个文件用于追加
                    for chunk in r.iter_content(chunk_size = 1024):
                         if chunk:
                              f.write(chunk)
                              f.flush()
     
if __name__ == '__main__':
     urllib3.disable_warnings()
     gp = get_protos()
     print('获取图片链接中：')
     gp.get_ids()
     print('图片下载中：')
     for i in range(len(gp.protoes_id)):
          print("正在下载第%d张图片" % (i+1))
          gp.download(gp.protoes_id[i],(i+1))





