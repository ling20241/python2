# -*- coding: utf-8 -*-
# @File:SignalsExample.py
# @Author : 灵
# @Time : 2024/5/6 15:46
# @Software: PyCharm


from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QPlainTextEdit



class Window(QWidget):
    def __init__(self,*args,**kwargs):

        super(Window, self).__init__(*args,**kwargs)
        layout=QVBoxLayout(self)

        btn1=QPushButton("按钮点击信号",self)
        btn1.setObjectName("ClickBut")
        btn1.clicked.connect(self.onClicked)
        layout.addWidget(btn1)

        btn2=QPushButton("按钮按下信号",self)
        btn2.setObjectName("PressBut")
        btn2.pressed.connect(self.onPressed)
        layout.addWidget(btn2)

        btn3=QPushButton("按钮点击信号",self)
        btn3.setObjectName("ReleaseBut")
        btn3.released.connect(self.onReleased)
        layout.addWidget(btn3)

        btn4=QPushButton("按钮点击信号",self)
        btn4.setObjectName("ToggleBut")
        btn4.setCheckable(True)
        btn4.toggled.connect(self.onToggled)
        layout.addWidget(btn4)

        self.resultview=QPlainTextEdit(self)
        # 文本设置成为只读模式
        self.resultview.setReadOnly(True)

        layout.addWidget(self.resultview)


    def onClicked(self):

        self.resultview.appendPlainText(
            '按钮{0}被点击'.format(self.sender().objectName()))

    def onPressed(self):

        self.resultview.appendPlainText(
            '按钮{0}被按下'.format(self.sender().objectName()))

    def onReleased(self):

        self.resultview.appendPlainText(
            '按钮{0}被释放'.format(self.sender().objectName()))

    def onToggled(self,checked):

        self.resultview.appendPlainText(
            '按钮{0}被选中：{1}'.format(self.sender().objectName(),checked))


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    w=Window()
    w.show()
    sys.exit(app.exec_())