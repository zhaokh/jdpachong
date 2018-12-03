import sys
from PyQt5 import QtWidgets
from Ui_jdjiadianui import Ui_MainWindow  #导入创建的GUI类

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
     #__init__:析构函数，也就是类被创建后就会预先加载的项目。
     # 马上运行，这个方法可以用来对你的对象做一些你希望的初始化。
    def __init__(self):
         #这里需要重载一下mywindow，同时也包含了QtWidgets.QMainWindow的预加载项。
         super(mywindow, self).__init__()
         self.setupUi(self)

    def update(self):
        self.comboBox_2.addItem(["222","111"])




if __name__=='__main__': 
    #创建应用程序和对象
    app = QtWidgets.QApplication(sys.argv)
    w = mywindow()
    w.update()
    w.show()
    sys.exit(app.exec_())