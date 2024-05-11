# -*- coding: utf-8 -*-
# @File:BottomLine.py
# @Author : 灵
# @Time : 2024/5/6 14:38
# @Software: PyCharm


import  sys

from random import randint

from PyQt5.QtCore import QTimer,QThread,pyqtSignal
from PyQt5.QtGui import QPainter,QColor,QPen
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget,QVBoxLayout



# 设置颜色

StyleSheet="""
PushButtonLine{
color:white;
border:none;
min-height:48px;
background-color:#90caf9;
}
"""

# 多线程,继承QT多线程，重写方法
class LoadingThread(QThread):
    valueChanged=pyqtSignal(float)

    def __init__(self,*args,**kwargs):
        super(LoadingThread, self).__init__(*args,**kwargs)
        self.totalValue=randint(100,200)

    def run(self) :

        for i in range(self.totalValue+1):
            if self.isInterruptionRequested():
                break
            self.valueChanged.emit(i/self.totalValue)
            QThread.msleep(randint(50,100))



# 定义button 类 继承QTBuuton

class PushButtonLine(QPushButton):

    lineColor=QColor(0,150,136)

    def __init__(self,*args,**kwargs):
        self._waitText=kwargs.pop("waitText","等待中")
        super(PushButtonLine, self).__init__(*args,**kwargs)
        self._text=self.text()
        self._percent=0

        # 定时器
        self._time=QTimer(self,timeout=self.update)

        # 按键点击事件
        self.clicked.connect(self.start)


    def __del__(self):
        # 结束
        self.stop()


    def paintEvent(self,event):
        super(PushButtonLine, self).paintEvent(event)
        if not self._time.isActive():
            return

        painter=QPainter(self)
        pen=QPen(self.lineColor)
        pen.setWidth(4)
        painter.setPen(pen)
        painter.drawLine(0,self.height(),self.width()
                         * self._percent,self.height())

    def start(self):

        if hasattr(self,"loadingThread"):
            return self.stop()

        self.loadingThread=LoadingThread(self)
        self.loadingThread.valueChanged.connect(self.setParent)
        self._time.start(100)
        self.loadingThread.start()
        self.setText(self._waitText)


    def stop(self):
        try:
            if hasattr(self,"loadingThread"):
                if self.loadingThread.isRunning():
                    self.loadingThread.requestInterruption()
                    # 停止
                    self.loadingThread.quit()
                    # 等待执行完毕
                    self.loadingThread.wait(2000)
                    # 删除对象
                del self.loadingThread
        except RuntimeError:
            pass
        try:
            self._percent=0
            self._time.stop()
            self.setText(self._text)
        except RuntimeError:
            pass

    def setParent(self,v):
        self._percent=v
        if v==1:
            self.stop()
            self.update()


    def setLineColor(self,color):
        self.lineColor=QColor(color)
        return self



class Window(QWidget):

    def __init__(self,*args,**kwargs):
        super(Window, self).__init__(*args,**kwargs)
        layout=QVBoxLayout(self)
        layout.addWidget(PushButtonLine("点击加载"))
        layout.addWidget(PushButtonLine("点击加载").setLineColor('#ef5350'))
        layout.addWidget(PushButtonLine("点击加载").setLineColor('#ffc107'))


if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    w=Window()
    w.show()
    sys.exit(app.exec_())






