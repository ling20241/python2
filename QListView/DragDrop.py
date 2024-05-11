import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("商品管理系统")
        self.setGeometry(100, 100, 400, 200)  # 位置和大小

        # 创建一个垂直布局和主窗口
        self.layout = QVBoxLayout(self)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        # 商品名称标签和输入框
        self.label_name = QLabel("商品名称：", self)
        self.layout.addWidget(self.label_name)
        self.line_edit_name = QLineEdit(self)
        self.layout.addWidget(self.line_edit_name)

        # 入库时间标签和输入框
        self.label_time = QLabel("入库时间：", self)
        self.layout.addWidget(self.label_time)
        self.line_edit_time = QLineEdit(self)
        self.layout.addWidget(self.line_edit_time)

        # 商品RFID标签和输入框
        self.label_rfid = QLabel("商品RFID：", self)
        self.layout.addWidget(self.label_rfid)
        self.line_edit_rfid = QLineEdit(self)
        self.layout.addWidget(self.line_edit_rfid)

        # 读取按钮
        self.button_read = QPushButton("读取", self)
        self.button_read.clicked.connect(self.read_rfid)
        self.layout.addWidget(self.button_read)

        # 保存按钮
        self.button_save = QPushButton("保存", self)
        self.button_save.clicked.connect(self.save_data)
        self.layout.addWidget(self.button_save)

        # 关闭按钮
        self.button_close = QPushButton("关闭", self)
        self.button_close.clicked.connect(self.close)
        self.layout.addWidget(self.button_close)

    def read_rfid(self):
        # 这里可以添加读取RFID的逻辑
        print("RFID读取按钮被点击")

    def save_data(self):
        # 这里可以添加保存数据的逻辑
        print("保存按钮被点击")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())