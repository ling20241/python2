
# -*- coding: utf-8 -*-
# @File:CustomWidgetltem.py
# @Author : 灵
# @Time : 2024/5/6 17:09
# @Software: PyCharm

# 时间排序和名字排序

import string
from random import choice,randint

from time import time


from PyQt5.QtCore import QSortFilterProxyModel,Qt ,QSize
from PyQt5.QtGui import QStandardItem,QStandardItemModel
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QListView,\
    QHBoxLayout,QLineEdit,QApplication

def randomChar(y):
    # 返回随机字符串
    return ''.join(choice(string.ascii_letters)for _ in range(y))


# 模板 view 里面显示的内容

class CustomWidget(QWidget):
    def __init__(self,text,*args,**kwargs):
        super(CustomWidget, self).__init__(*args,**kwargs)
        layout=QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(QLineEdit(text,self))
        layout.addWidget(QPushButton("x",self))


    def sizeHint(self):
        # 决定item的高度
        return QSize(200,40)


# 模型，过滤数据，用户定义规则来进行排序和过滤
class SortFilterProxyModel(QSortFilterProxyModel):

    def lessThan(self,source_left,source_right):
        if not source_left.isValid() or not source_right.isValid():
            return

        leftData=self.sourceModel().data(source_left)
        rightData=self.sourceModel().data(source_right)
        if self.sortOrder() == Qt.DescendingOrder:
            # 按照时间倒序排序
            leftData=leftData.split('-')[-1]
            rightData=rightData.split('-')[-1]

            return leftData < rightData
        return super(SortFilterProxyModel, self).lessThan(source_left,source_right)



class Window(QWidget):

    def __init__(self,*args,**kwargs):
        super(Window, self).__init__(*args,**kwargs)
        self.resize(800,600)
        layout=QVBoxLayout(self)
        layout.addWidget(QPushButton('以名字升序',self,clicked=self.sortByName))
        # 时间倒序
        layout.addWidget(QPushButton('以时间倒序',self,clicked=self.sortByTime))
        # listview
        self.listview=QListView(self)
        layout.addWidget(self.listview)

        # 数据模型
        self.dmodel=QStandardItemModel(self.listview)
        # 排序代理模型
        self.fmodel=SortFilterProxyModel(self.listview)
        self.fmodel.setSourceModel(self.dmodel)
        self.listview.setModel(self.fmodel)

        #模拟生成50条数据
        for _ in range(50):
            name=randomChar(5)
            times=time()+randint(0,30)
            value='{}-{}'.format(name,times)
            item=QStandardItem(value)

            self.dmodel.appendRow(item)

            # 索引
            index=self.fmodel.mapFromSource(item.index())
            # 自定义的widget
            widget=CustomWidget(value,self)
            item.setSizeHint(widget.sizeHint())
            self.listview.setIndexWidget(index,widget)


    def sortByTime(self):
        # 按照时间排序
        self.fmodel.sort(0,Qt.DescendingOrder)


    def sortByName(self):

        # 按照名子升序排序
        self.fmodel.sort(0,Qt.AscendingOrder)


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    w=Window()
    w.show()
    sys.exit(app.exec_())



        