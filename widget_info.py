# -*- coding: utf-8 -*-

"""
Author: Fallen
Email: sigernmenz_he@henu.edu.cn
Date: 2022/3/3
Desc: 信息板块
"""

from PySide2.QtWidgets import (QGroupBox, QLabel, QWidget, QVBoxLayout)


class WidgetInfo(QWidget):
    def __init__(self):
        super(WidgetInfo, self).__init__()

        vbox = QVBoxLayout()

        self.label_fps = QLabel('FPS: ')
        vbox.addWidget(self.label_fps)

        box = QGroupBox()
        box.setLayout(vbox)

        _vbox = QVBoxLayout()
        _vbox.setContentsMargins(0, 0, 0, 0)
        _vbox.addWidget(box)
        self.setLayout(_vbox)

    def update_fps(self, fps):
        self.label_fps.setText(f'FPS: { "" if fps <= 0 else round(fps, 1)}')
