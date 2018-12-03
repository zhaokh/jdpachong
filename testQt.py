import os,sys
from PyQt5 import QtCore,QtWidgets,QtGui

class test():

    def setUI(self,w):
        #设置工具窗口的大小
        w.setGeometry(100,200,800,400)
        #设置工具窗口的标题
        w.setWindowTitle("经咚爬虫")
        #设置窗口的图标
        w.setWindowIcon(QtGui.QIcon('icon.png'))
        #设置提示框中文本的字体样式，大小
        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif',20))

        #添加文本标签
        self.label = QtWidgets.QLabel(w)
        #设置标签的左边距，上边距，宽，高
        self.label.setGeometry(QtCore.QRect(60, 20, 120, 45))
        #设置文本标签的字体和大小，粗细等
        self.label.setFont(QtGui.QFont("Roman times",20,QtGui.QFont.Bold))
        
        self.label.setText("Name：")
        #为窗口添加提示
        w.setToolTip('这是Window关机工具')
        w.show()

if __name__=='__main__': 
    #创建应用程序和对象
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    ui = test()
    ui.setUI(w)
    sys.exit(app.exec_())