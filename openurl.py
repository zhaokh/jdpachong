#cookie
import requests, sys,time
from bs4 import BeautifulSoup
 
class downloader(object):

    # 初始化参数
    def __init__(self):
        self.server = 'http://www.biqukan.com'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.names = [] #存放章节名
        self.urls = [] #存放章节链接
        self.nums = 0 #章节数

    # 获取下载链接
    def get_download_url(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html, "html.parser")
        div = div_bf.find_all('div',class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]),"html.parser")
        a = a_bf.find_all('a')
        self.nums = len(a[15:])
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))
    
    # 获取章节内容
    def get_content(self,target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html,'html.parser')
        texts = bf.find_all("div",class_ = 'showtxt')
        if(len(texts) > 0):
            texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts
    
    # 将爬取的文章内容写入文件
    def writer(self, name, path, text):
        write_flag = True
        with open(path,'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('《一年永恒》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], "一念永恒.txt",dl.get_content(dl.urls[i]))
        sys.stdout.write(dl.names[i] + "  url:  " + dl.urls[i] + '\n');
        sys.stdout.write('  已下载：%.3f' % float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《一年永恒》下载完成')