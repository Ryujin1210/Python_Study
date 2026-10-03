from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget
import sys 
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QVBoxLayout

app = QApplication(sys.argv)

# 1. 생성
win = QWidget() # 부모 윈도우 
button = QPushButton("클릭")

# 3. 이벤트 처리
def order(self):
    print("주문하세요")
button.clicked.connect(order)


# 2. 배치
layout = QVBoxLayout()
layout.addWidget(button)

win.setLayout(layout)

win.show
sys.exit