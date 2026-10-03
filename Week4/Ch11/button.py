from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
import sys 

# 1. 생성
app = QApplication(sys.argv)
win = QWidget() # 부모 윈도우 
win.resize(300,200)

button1 = QPushButton("Push1", parent=win)
button2 = QPushButton("Push2", parent=win)
button3 = QPushButton("Push3", parent=win)

label = QLabel("라벨")

# 2. 배치
layout = QVBoxLayout()
# layout = QHBoxLayout()
layout.addWidget(label)
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
win.setLayout(layout)

# 4. 윈도우 표시 및 이벤트 루프 실행
win.show() 
sys.exit(app.exec()) 


