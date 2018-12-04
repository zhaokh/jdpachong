# -*- coding:utf-8 -*-
'''
Created on 2015年8月4日

@author: DXL

Copyright (C) 2004-2012 Shandong Leadom Software Development Co.,Ltd

'''
import os,sys
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication

class TableWidgetHelper(QtCore.QObject):
    def __init__(self,parent,del_column=None):
        QtCore.QObject.__init__(self,parent)
        if not isinstance(parent,QtWidgets.QTableWidget) or parent.columnCount()<=0:
            print ( "Parent of TableWidgetHelper must is QTableWidget and its has one column at last.")
            self._parent = None
        else:
            self._parent = parent
            self._parent.currentCellChanged.connect(self.onItemChanged)
            self._parent.cellClicked.connect(self.onClickedItem)
            self._parent.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
            #self._addActions = []
        if isinstance(del_column,int) or del_column is None:
            self._del_column = del_column
            if self._del_column is not None and self._parent:
                if not self._parent.rowCount(): 
                    self.onItemChanged(0,0)
                del_all_action = QAction(u"清空",self._parent)
                del_all_action.triggered.connect(self.onDelAll)
                del_select_action = QAction(u"删除所选",self._parent)
                del_select_action.triggered.connect(self.onDelSelect)
                insert_action = QAction(u"增加一行",self._parent)
                insert_action.triggered.connect(self.onAddItem)
                self._parent.addAction(del_all_action)
                self._parent.addAction(del_select_action)
                self._parent.addAction(insert_action)
        else:
            print ('Variant of del_column hast unexcept type.')
            self._del_column = None

    def onDelAll(self):
        if self._parent:
            self._parent.setRowCount(0)
        pass

    def onAddItem(self):
        if self._parent:
            r = self._parent.rowCount()-1 if self._parent.rowCount() else 0
            self.onItemChanged(r, 0)
        pass

    def onDelSelect(self):
        select_rows = set()
        for rg in self._parent.selectedRanges():
            for i in range(rg.topRow(),rg.bottomRow()+1):
                select_rows.add(i)
        select_rows = list(select_rows)
        select_rows.sort(reverse=True)
        for index in select_rows:
            self._parent.removeRow(index)
        pass

    def onClickedItem(self,r,c):
        if self._del_column is None or not self._parent:
            return
        if  c == self._del_column:
            ret = QtGui.QMessageBox.warning(self._parent, u'警告', u'是否删除第%s行?'%(r+1,), QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
            if ret == QtGui.QMessageBox.Yes:
                self._parent.removeRow(r)
                return
            else:
                return

    def  onItemChanged(self,r,c):
        if self._del_column is None or not self._parent:
            return
        if r + 1 >= self._parent.rowCount():
            #for i in range(self._parent.columnCount()):
            self._parent.insertRow(self._parent.rowCount()) 
            item = QtWidgets.QTableWidgetItem(QtGui.QIcon(':/icon/del.png'),'')
            self._parent.setItem(self._parent.rowCount()-1,self._del_column,item)  



if __name__ == "__main__":
    a = QtWidgets.QApplication([])
    w = QtWidgets.QTableWidget()
    w.setColumnCount(5)
#     w.setRowCount(10)
#     for i in range(10):
#         for j in range(5):
#             insert_str = "(%s,%s)"%(i,j)
#             item = QtGui.QTableWidgetItem(insert_str)
#             w.setItem(i,j,item)

    w_helper = TableWidgetHelper(w,4)
    w.show()
    a.exec_()
