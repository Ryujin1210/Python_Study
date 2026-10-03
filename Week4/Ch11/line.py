from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel,QLineEdit
import sys 

# 1. 생성
app = QApplication(sys.argv)
win = QWidget() # 부모 윈도우 
win.resize(300,200)

entry = QLineEdit()
label1 = QLabel()

# 동적 실시간 바인딩
entry.textChanged.connect(label1.setText)

# 2. 배치
layout = QVBoxLayout()
layout.addWidget(entry)
layout.addWidget(label1)

win.setLayout(layout)

# 4. 윈도우 표시 및 이벤트 루프 실행
win.show() 
sys.exit(app.exec()) 


