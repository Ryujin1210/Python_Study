from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget
import sys 
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QVBoxLayout

# 1. 생성
win = QWidget() # 부모 윈도우 
button = QPushButton("클릭", parent=win)

# 2. 배치
layout = QVBoxLayout()
layout.addWidget(button)

win.setLayout(layout)

# 3. 이벤트 처리
def on_click_event(self):
    print("버튼클릭")
    
button.clicked.connect(on_click_event)
