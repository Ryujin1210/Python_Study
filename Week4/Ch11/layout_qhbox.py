from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout
import sys 

# 1. 생성
app = QApplication(sys.argv)
win = QWidget() # 부모 윈도우 
win.resize(300,200)

button1 = QPushButton("Push1")
button2 = QPushButton("Push2")
button3 = QPushButton("Push3")

# 2. 배치
layout = QGridLayout()
layout.addWidget(button1, 0, 1)
layout.addWidget(button2, 1, 0)
layout.addWidget(button3, 1, 2)
win.setLayout(layout)

# 4. 윈도우 표시 및 이벤트 루프 실행
win.show() 
sys.exit(app.exec()) 


