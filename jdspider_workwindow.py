from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import requests,re
import time
import threading
from lxml import etree
from pandas import DataFrame
import pandas as pd
from Ui_jdjiadianui import Ui_MainWindow
from PyQt5.QtCore import QObject, pyqtSignal
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.itemurlDic = initsmallCatelog(self)

        self.comboBox.addItems(["大家电"])

        self.comboBox_2.addItems(self.itemurlDic.keys())
    
        self.pushButton.clicked.connect(self.onGetClicked)

        column_name = [
            '手机名称',
            '价格',
            '商家名称',
            '评论数'
        ]

        self.tableWidget.setColumnCount(len(column_name))

        self.tableWidget.setHorizontalHeaderLabels(column_name)  # 设置列名称

    def insertItemData(self,itemData):

        itemCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(itemCount);
        for i in range(0, len(itemData)):
            self.tableWidget.setItem(itemCount,i,QTableWidgetItem(itemData[i]))             


    def onGetClicked(self):
        print("开启spider")
        base = "https://list.jd.com"

        #for key,value in self.itemurlDic.items():
        #    print(key + " : " + base + value)

        # 在 initsmallCatelog中初始化 itemurlDic
        url = base + self.itemurlDic[self.comboBox_2.currentText()]

        self.update_data_thread = UpdateData(url)  # 启动线程 ，传递 url参数
        self.update_data_thread.update_date.connect(self.insertItemData)  # 链接信号，在线程中 emit信号，调用self.insertItemData
        self.update_data_thread.start()


def initsmallCatelog(self):
    url = "https://list.jd.com/list.html?cat=737,794,13701"
    res=requests.get(url, verify=False)
    res.encoding='utf-8'
    root=etree.HTML(res.text)

    names = root.xpath('/html/body//div[@class="crumbs-nav-item"][last()]//ul[@class="menu-drop-list"]/li/a/text()')
    urls = root.xpath('/html/body//div[@class="crumbs-nav-item"][last()]//ul[@class="menu-drop-list"]/li/a/@href')
    itemurldic = dict(zip(names,urls))
    return itemurldic

def getItemData(self):
    jdInfoAll = DataFrame()
    for i in range(1,4):
        url= self._url + "&page="+str(i)
        print("url : " + url )
        res=requests.get(url, verify=False)
        res.encoding='utf-8'
        root=etree.HTML(res.text)
        items=root.xpath('//li[@class="gl-item"]')
        priceurl_base = "https://p.3.cn/prices/mgets?callback=jQuery6775278&skuids=J_"
        commenturl_base = "https://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds="

        for item in items:
            name = item.xpath('.//div[@class="p-name"]/a/em/text()')
            name = name[0]
            name = re.sub('\s','',str(name))
            sku=item.xpath('./div/@data-sku')
            sku = sku[0]
            priceurl = priceurl_base + str(sku)
            pricedata=requests.get(priceurl, verify=False)
            pricepat='"p":"(.*?)"}'
            price = re.compile(pricepat).findall(pricedata.text)
            price = price[0]
           

            commenturl = commenturl_base + str(sku)
            commentdata = requests.get(commenturl, verify=False)
            commentpat = '"CommentCount":(.*?),"'
            comment = re.compile(commentpat).findall(commentdata.text)
            comment = comment[0]           
            self.update_date.emit([name,price,"xxx",comment])  # 发射信号
        pass
    pass
pass

class UpdateData(QtCore.QThread):
    """更新数据类"""

    update_date = pyqtSignal(list)  # pyqt5 支持python3的str，没有Qstring

    def __init__(self, url):
        super().__init__()
        self._url = url

    def run(self):
        #print(self.parent().urls)
        pass  # pass 无意义
        getItemData(self)

        """
        cnt = 0
        count = 10
        while cnt < count:
            cnt += 1
            self.update_date.emit(str(cnt))  # 发射信号
            time.sleep(0.5)
            print(cnt)
        """

    
