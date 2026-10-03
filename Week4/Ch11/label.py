from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
import sys 

# 1. 생성
app = QApplication(sys.argv)
win = QWidget() # 부모 윈도우 
win.resize(300,200)
# setStyleSheet(): QT위젯의 모양을 꾸밀때 
label1 = QLabel("라벨1")
label1.setStyleSheet("background-color:red; color:white;")
label2 = QLabel("라벨2")
label2.setStyleSheet("background-color:green; color:white;")
label3 = QLabel("라벨3")
label3.setStyleSheet("background-color:blue; color:white;")

# 2. 배치
layout = QVBoxLayout()
layout.addWidget(label1)
layout.addWidget(label2)
layout.addWidget(label3)

win.setLayout(layout)

# 4. 윈도우 표시 및 이벤트 루프 실행
win.show() 
sys.exit(app.exec()) 


