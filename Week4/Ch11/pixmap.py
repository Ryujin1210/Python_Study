import sys 
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtGui import QPixmap

app = QApplication(sys.argv)
win = QWidget()
win.resize(200,200)

# 상대 경로 주소 복사 
pixmap = QPixmap("cat.jpg")
label = QLabel(win)
label.setPixmap(pixmap)
label.move(-400, -400)

button1 = QPushButton("Push1", win)
button2 = QPushButton("Push2", parent = win)
button3 = QPushButton("Push3", win)

# layout = QVBoxLayout()
# layout.addWidget(label)

button1.move(10, 60)
button2.move(140, 60)
button3.move(80, 10)

# win.setLayout(layout)
win.show()
sys.exit(app.exec())