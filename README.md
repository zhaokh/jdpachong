jdpachong
py3 用 urllib 代替 py2的urllib2，使用用urllib.request代替urllib2
py3 用http.cookiejar代替 cookielib
py3 使用requrest处理rul  运行pip install requests，按装requests库
官方文档：http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
安装 Beautiful Soup  运行 pip install beautifulsoup4，安装beautifulsoup库
官方文档：http://beautifulsoup.readthedocs.io/zh_CN/latest/


爬虫教程 https://blog.csdn.net/u012662731/article/details/78537432

动态加载的网站 强大的抓包工具就是Fiddler：

URL：http://www.telerik.com/fiddler  // 公司外网访问，直接报自由门，导致网络，真是诡异


v 0.2 抓取小说 章节标题 章节内容

v 1.0 整部小说下载，按章节，不可用的直接跳过

v 1.1 抓取豆瓣250部https，抓取图片自动并创建pic目录存储

安装 Anaconda, python的包管理器，通过它可以安装Scrapy，一个python的网络爬虫框架
然后运行conda install -c conda-forge scrapy来安装scrapy scrayp官方教程https://doc.scrapy.org/en/latest/intro/install.html
conda install -c conda-forge scrapy 安装scrapyr
运行 aconda navigator 会初始化环境安装若干依赖包


python三大神器：pip virtualenv fabric
 pip  --  python 包管理工具
 virtualenv --  创建虚拟python环境避免冲突
 fabric  --  基于ssh的部署工具包

 从远程分支（origin/master）提取到当前新建的分支  git checkout -b tmp origin/master

 添加 practice_jd, 爬京东手机图片

 运行 practice_jd.py
 需要先安装以下库： 
 pip install lxml
 pip install pandas
 pip install xlwt