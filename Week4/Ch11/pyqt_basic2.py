from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys 

app = QApplication(sys.argv)

# 1. 생성
win = QWidget() # 부모 윈도우 

win.setGeometry(100, 100, 400, 300)

# 크기 조절 800,600
win.resize(800, 600)

# 위치 이동 
win.move(100, 200)

button = QPushButton("클릭", parent=win)

# 3. 이벤트 처리
def on_click_event(self):
    print("버튼클릭")
    
button.clicked.connect(on_click_event)


# 2. 배치
layout = QVBoxLayout()
layout.addWidget(button)
win.setLayout(layout)

# 4. 윈도우 표시 및 이벤트 루프 실행
win.show() 
sys.exit(app.exec()) 


