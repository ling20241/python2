# -*- coding: utf-8 -*-
# @File:DeleteCustomItem.py
# @Author : 灵
# @Time : 2024/5/10 17:26
# @Software: PyCharm

# 可删除的列表


from PyQt5.QtCore import QSize,pyqtSignal
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QLineEdit,QPushButton,\
    QListWidgetItem,QVBoxLayout,QListWidget,QApplication


class ItemWidget(QWidget):
    # itemDeleted的自定义信号，它继承自
    # PyQt5.QtCore.pyqtSignal，并且可以传递一个
    # QListWidgetItem类型的对象作为参数。这意味着当这个信号被触发时，
    # 它可以传递一个列表项对象给所有连接到这个信号的槽函数。
    itemDeleted=pyqtSignal(QListWidgetItem)

    def __init__(self,text,item,*args,**kwargs):
        super(ItemWidget, self).__init__(*args,**kwargs)
        self._item=item # 保留list item 的对象引用
        layout=QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(QLineEdit(text,self))
        layout.addWidget(QPushButton('x',self,clicked=self.doDeleteItem))

    def doDeleteItem(self):
        self.itemDeleted.emit(self._item)


    def sizeHint(self):
        # 决定item的高度
        return QSize(200,40)


class Window(QWidget):

    def __init__(self,*args,**kwargs):
        super(Window, self).__init__(*args,**kwargs)
        layout=QVBoxLayout(self)

        # 列表
        self.listWindget=QListWidget(self)
        layout.addWidget(self.listWindget)

        # 清空按钮
        self.clearBth=QPushButton('清空',self,clicked=self.doClearItem)
        layout.addWidget(self.clearBth)

        # 添加测试数据
        self.testData()

    def doDeleteItem(self,item):
        # 根据 item得到他对应的行数
        row=self.listWindget.indexFromItem(item).row()
        # 删除item
        item=self.listWindget.takeItem(row)
        # 删除widget
        self.listWindget.removeItemWidget(item)


    def doClearItem(self):
        # 清空所有Item
        for _ in range(self.listWindget.count()):
            # 删除item
            # 一直是0的原因是一直从第一行删,删掉第一行后第二行变成了第一行
            # 这个和删除list [] 里面的数据是一个道理
            item=self.listWindget.takeItem(0)
            # 删除widget
            self.listWindget.removeItemWidget(item)
            del item


    def testData(self):
        # 生成测试数据
        for i in range(100):
            item =QListWidgetItem(self.listWindget)
            widget=ItemWidget('item: {}'.format(i),item, self.listWindget)
            # 绑定删除信号
            widget.itemDeleted.connect(self.doDeleteItem)
            self.listWindget.setItemWidget(item,widget)


if __name__ == '__main__':
    import sys
    import cgitb
    cgitb.enable(format='text')

    app=QApplication(sys.argv)
    w=Window()
    w.show()
    sys.exit(app.exec_())
