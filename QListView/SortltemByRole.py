# -*- coding: utf-8 -*-
# @File:SortltemByRole.py
# @Author : 灵
# @Time : 2024/5/10 10:57
# @Software: PyCharm
from random import choice

from PyQt5.QtCore import QSortFilterProxyModel,Qt  # 排序模块，自定义规则
from PyQt5.QtGui import QStandardItem,QStandardItemModel # 表格处理模块
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QListView,QPushButton


class SortFilterProxyModel(QSortFilterProxyModel):


    def __init__(self,*args,**kwargs):
        super(SortFilterProxyModel, self).__init__(*args,**kwargs)
        self._topIndex=0


    def setSortIndex(self,index):
        self._topIndex=index
        print("在最前面的序号为:",index)


    def lessThan(self,source_left,source_right):
        if not source_left.isValid() or not source_right.isValid():
            return False


        if self.sortRole()==ClassifyRole and \
            source_left.column()==self.sortColumn() and \
            source_right.column()==self.sortColumn():

            leftIndex=source_left.data(ClassifyRole)
            rightIndex=source_right.data(ClassifyRole)


            # 升序

            if self.sortOrder() ==Qt.AscendingOrder:
                # 保持在最前面
                if leftIndex ==self._topIndex:
                    leftIndex=-1
                if rightIndex ==self._topIndex:
                    rightIndex=-1

                return leftIndex<rightIndex

        return super(SortFilterProxyModel, self).lessThan(source_left,source_right)



NameDict={
    '唐':['Tang',0],
    '宋':['Song',1],
    '元':['Yuan',2],
    '明':['Ming',3],
    '清':['Qing',4],
}

IndexDict = {
    0:'唐',
    1:'宋',
    2:'元',
    3:'明',
    4:'清',
}

IdRole=Qt.UserRole+1 # 用于恢复排序
ClassifyRole=Qt.UserRole+2 # 用于按照分类序号排序

class Window(QWidget):

    def __init__(self,*args,**kwargs):
        super(Window, self).__init__(*args,**kwargs)
        self.resize(600,400)
        layout=QVBoxLayout(self)
        self.listView=QListView(self)
        self.listView.setEditTriggers(QListView.NoEditTriggers)
        layout.addWidget(self.listView)
        layout.addWidget(QPushButton('恢复默认顺序',self,clicked=self.restoreSort))
        layout.addWidget(QPushButton('唐',self,clicked=self.sortByClassify))
        layout.addWidget(QPushButton('宋',self,clicked=self.sortByClassify))
        layout.addWidget(QPushButton('元',self,clicked=self.sortByClassify))
        layout.addWidget(QPushButton('明',self,clicked=self.sortByClassify))
        layout.addWidget(QPushButton('清',self,clicked=self.sortByClassify))
        self._initItems()

    def restoreSort(self):
        # 恢复默认排序
        self.fmodel.setSortRole(IdRole) # 必须设置排序角色为ID
        self.fmodel.sort(0) # 排序第一列按照ID升序


    def sortByClassify(self):

        self.fmodel.setSortIndex(NameDict.get(
            self.sender().text(), ['', 100])[1])
        self.fmodel.setSortRole(IdRole)

        self.fmodel.setSortRole(ClassifyRole)
        self.fmodel.sort(0)


    def _initItems(self):

        self.dmodel=QStandardItemModel(self.listView)
        self.fmodel=SortFilterProxyModel(self.listView)
        self.fmodel.setSourceModel(self.dmodel)
        self.listView.setModel(self.fmodel)

        keys=list(NameDict.keys())
        print(keys)  # ['清'],['元‘]
        classifies=[v[1] for v in NameDict.values()]
        for i in range(5):
            # 添加5-100，用于模拟没有分类，排序的时候就显示在最后面
            classifies.append(100)
        print(classifies)

        # 生成50个 Item
        for i in range(50):

            item=QStandardItem()
            # 设置ID角色
            item.setData(i,IdRole)
            # 设置分类角色
            c=choice(classifies)
            item.setData(c,ClassifyRole)
            # 设置显示内容
            item.setText('Name:{}\t\tId: {}\t\tClassify: {}'.format(IndexDict.get(c,'其它'),i,c))
            self.dmodel.appendRow(item)



if __name__ == '__main__':
    import sys
    import cgitb
    cgitb.enable(format='text')
    app=QApplication(sys.argv)
    w=Window()
    w.show()
    sys.exit(app.exec_())



