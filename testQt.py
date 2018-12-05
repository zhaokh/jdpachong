import os,sys
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import *


class Table(QWidget):
    def __init__(self):
        super(Table,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QTableWidget例子")
        self.resize(400,300)
        self.move(100, 100)  # 移动
        layout=QHBoxLayout()

        #实现的效果是一样的，四行三列，所以要灵活运用函数，这里只是示范一下如何单独设置行列
        TableWidget=QTableWidget(4,3)

        # TableWidget = QTableWidget()
        # TableWidget.setRowCount(4)
        # TableWidget.setColumnCount(3)



        #设置水平方向的表头标签与垂直方向上的表头标签，注意必须在初始化行列之后进行，否则，没有效果
        TableWidget.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])
        #Todo 优化1 设置垂直方向的表头标签
        #TableWidget.setVerticalHeaderLabels(['行1', '行2', '行3', '行4'])

        #TODO 优化 2 设置水平方向表格为自适应的伸缩模式
        ##TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #TODO 优化3 将表格变为禁止编辑
        #TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #TODO 优化 4 设置表格整行选中
        #TableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        #TODO 优化 5 将行与列的高度设置为所显示的内容的宽度高度匹配
        #QTableWidget.resizeColumnsToContents(TableWidget)
        #QTableWidget.resizeRowsToContents(TableWidget)

        #TODO 优化 6 表格头的显示与隐藏
        #TableWidget.verticalHeader().setVisible(False)
        #TableWidget.horizontalHeader().setVisible(False)

        #TOdo 优化7 在单元格内放置控件
        # comBox=QComboBox()
        # comBox.addItems(['男','女'])
        # comBox.addItem('未知')
        # comBox.setStyleSheet('QComboBox{margin:3px}')
        # TableWidget.setCellWidget(0,1,comBox)
        #
        # searchBtn=QPushButton('修改')
        # searchBtn.setDown(True)
        # searchBtn.setStyleSheet('QPushButton{margin:3px}')
        # TableWidget.setCellWidget(0,2,searchBtn)


        #添加数据
        newItem=QTableWidgetItem('张三')
        TableWidget.setItem(0,0,newItem)

        newItem=QTableWidgetItem('男')
        TableWidget.setItem(0,1,newItem)

        newItem=QTableWidgetItem('160')
        TableWidget.setItem(0,2,newItem)

        layout.addWidget(TableWidget)

        self.setLayout(layout)

    def update_item_data(self, data):
        """更新内容"""
        self.setItem(0, 0, QTableWidgetItem(data)) # 设置表格内容(行， 列) 文字

class test():

    def setUI(self,w):

        height_combox = 30
        width_combo = 100

        heigcht_label = 30
        width_label = 100

        font_size = 12

        #设置工具窗口的大小
        w.setGeometry(100,200,800,400)
        #设置工具窗口的标题
        w.setWindowTitle("经咚家电spider")
        #设置窗口的图标
        w.setWindowIcon(QtGui.QIcon('/pic/544257.png'))

        w.setStyleSheet("background-image: url(/pic/544257.png)")

        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif',10))
        w.setToolTip('这是经咚spider')


        self.label_largecatelog = QtWidgets.QLabel(w)
        self.label_largecatelog.setGeometry(QtCore.QRect(40, 20, width_label, heigcht_label))
        self.label_largecatelog.setFont(QtGui.QFont("Roman times",font_size))
        self.label_largecatelog.setText("大类别:")

        self.combx_largecatelog = QtWidgets.QComboBox(w)
        self.combx_largecatelog.setGeometry(QtCore.QRect(140,20,width_combo, height_combox))
        self.combx_largecatelog.setFont(QtGui.QFont("Roman times",font_size))
        self.combx_largecatelog.addItems(["12","11"])


        self.label_smallcatelog = QtWidgets.QLabel(w)
        self.label_smallcatelog.setGeometry(QtCore.QRect(300, 20, width_label, heigcht_label))
        self.label_smallcatelog.setFont(QtGui.QFont("Roman times",font_size))
        self.label_smallcatelog.setText("小类别:")

        self.combx_smallcatelog = QtWidgets.QComboBox(w)
        self.combx_smallcatelog.setGeometry(QtCore.QRect(400,20,width_combo,height_combox))
        self.combx_smallcatelog.setFont(QtGui.QFont("Roman times",font_size))
        self.combx_smallcatelog.addItems(["12","11"])



        #添加提交按钮和单击事件
        self.btn = QtWidgets.QPushButton(w)
        #设置按钮的位置大小
        self.btn.setGeometry(QtCore.QRect(600,20,150,30))
        #设置按钮的位置，x坐标,y坐标
        self.btn.setText("  获  取  ")
        self.btn.setFont(QtGui.QFont("Roman times",font_size))
        #为按钮添加单击事件
        self.btn.clicked.connect(self.getText)

        self.jdtable = Table()

        w.show()

    def getText(self):
        name = self.text.text()
        if name:
            try:
                self.label2.setText("你输入的名字是%s" % name)
                self.text.clear()
            except:
                self.label2.setText("请输入名字")

if __name__=='__main__': 
    #创建应用程序和对象
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    ui = test()
    ui.setUI(w)
    sys.exit(app.exec_())