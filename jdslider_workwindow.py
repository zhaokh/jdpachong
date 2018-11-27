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

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.comboBox.addItems(["大家电","厨房家电"])

        self.comboBox_2.addItems(["电视机","冰箱"])
        
        self.pushButton.clicked.connect(self.onGetClicked)

        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)

        column_name = [
            'ETH/BIC',
            'column1',
            'column2',
            'column3',
            'column4',
        ]
        self.tableWidget.setHorizontalHeaderLabels(column_name)  # 设置列名称

    def insertItemData(self,itemData):
        print(itemData)
        """
        itemCount = self.tableWidget.rowCount
        self.tableWidget.insertRow(itemCount)
        self.tableWidget.setItem(itemCount,0,"111")
        self.tableWidget.setItem(itemCount,1,"222")
        self.tableWidget.setItem(itemCount,2,"333")       
        """

    def onGetClicked(self):
        print("开启爬虫")
        self.update_data_thread = UpdateData()
        self.update_data_thread.update_date.connect(self.insertItemData)  # 链接信号
        self.update_data_thread.start()


def getItemData(self):
    jdInfoAll = DataFrame()
    for i in range(1,2):
        url="https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
        res=requests.get(url, verify=False)
        res.encoding='utf-8'
        root=etree.HTML(res.text)
        name=root.xpath('//li[@class="gl-item"]//div[@class="p-name"]/a/em/text()')
        for i in range(0,len(name)):
            name[i]=re.sub('\s','',name[i])

        #sku
        sku=root.xpath('//li[@class="gl-item"]/div/@data-sku')

        #价格
        price=[]
        comment=[]
        for i in range(0,len(sku)):
            thissku=sku[i]
            priceurl="https://p.3.cn/prices/mgets?callback=jQuery6775278&skuids=J_"+str(thissku)
            pricedata=requests.get(priceurl, verify=False)
            pricepat='"p":"(.*?)"}'
            thisprice=re.compile(pricepat).findall(pricedata.text)   
            price=price+thisprice

            commenturl = "https://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds="+str(thissku)
            commentdata = requests.get(commenturl)
            commentpat = '"CommentCount":(.*?),"'
            thiscomment = re.compile(commentpat).findall(commentdata.text)
            comment = comment + thiscomment

            #self.tableWidget.insertRow(i)

            #self.tableWidget.setItem( i , 0 , QTableWidgetItem('Hello'))

            self.update_date.emit(str(i))  # 发射信号

            print(i)
            #self.tableWidget.setItem( i , 0 , new QTableWidgetItem(name))
            #self.tableWidget.setItem( i , 1 , new QTableWidgetItem(price))
            #self.tableWidget.setItem( i , 2 , new QTableWidgetItem(comment))
            #self.tableWidget.

        #商家名称
        shopname=root.xpath('//li[@class="gl-item"]//div[@class="p-shop"]/@data-shop_name')
        print(shopname)

        jdInfo = DataFrame([name,price,shopname,comment]).T
        jdInfo.columns=['产品名称','价格','商家名称','评论数']
    jdInfoAll = pd.concat([jdInfoAll,jdInfo]) 

class UpdateData(QtCore.QThread):
    """更新数据类"""
    update_date = pyqtSignal(str)  # pyqt5 支持python3的str，没有Qstring

    def run(self):
        print(self)
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

    
