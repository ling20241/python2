import sys

from PyQt5.QtWidgets import  QWidget,QHBoxLayout,QPushButton,QApplication

Stylesheet="""
/*这里是通过设置，所有按钮都有效，不过后面的可以覆盖这个*/
QPushButton{
    border: none;/*去掉边框*/
    }
    
    /*
QPushButton#xxx
或者
#xx
都表示通过设置的objectName来指定
*/
QPushButton#RedButton {
    background-color: #f44336; /*背景颜色*/
}

#RedButton:hover{
background-color:#e57373;
}
/*注意pressed 一定要放在hover的后面，否则没有效果*/
#RedButton:pressed{
background-color: #ffcdd2;
}



"""


#继承窗体控件
class Window(QWidget):
# 表示可以接收任意的参数
    def __init__(self,*args,**kwargs):
        super(Window, self).__init__(*args,**kwargs)
        layout=QHBoxLayout(self)
        layout.addWidget(QPushButton("red button",self,objectName="RedButton",minimumHeight=48))
        layout.addWidget(QPushButton("green button", self, objectName="GreenButton", minimumHeight=48))
        layout.addWidget(QPushButton("blue button", self, objectName="BlueButton", minimumHeight=48))
        layout.addWidget(QPushButton("orange button",self,objectName="OrangeButton",minimumHeight=48))
        layout.addWidget(QPushButton("purple button", self, objectName="PurpleButton", minimumHeight=48))


if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setStyleSheet(Stylesheet)
    w=Window()
    w.show()
    sys.exit(app.exec_())