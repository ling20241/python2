# -*- coding: utf-8 -*-
# @File:DragDrop.py
# @Author : 灵
# @Time : 2024/5/11 10:05
# @Software: PyCharm


from PyQt5.QtCore import Qt,QSize,QRect,QPoint
from PyQt5.QtGui import QColor,QPixmap,QDrag,QPainter,QCursor
from PyQt5.QtWidgets import QListWidget,QListWidgetItem,QLabel,QRubberBand,QApplication


class DropListWidget(QListWidget):

