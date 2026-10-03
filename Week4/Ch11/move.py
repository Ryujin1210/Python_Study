from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout
import sys 

# 1. 생성
app = QApplication(sys.argv)
win = QWidget() # 부모 윈도우 
win.resize(300,200)

button1 = QPushButton("Push1", win)
button2 = QPushButton("Push2", parent = win)
button3 = QPushButton("Push3", win)

# 2. 배치
button1.move(10, 60)
button2.move(140, 60)
button3.move(80, 10)

# 4. 윈도우 표시 및 이벤트 루프 실행
win.show() 
sys.exit(app.exec()) 


