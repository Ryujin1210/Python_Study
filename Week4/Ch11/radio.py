import sys 
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QPushButton, QRadioButton
from PyQt6.QtWidgets import QVBoxLayout

def order():
    if r_btn1.isChecked():
        print("A런치 주문")
    elif r_btn2.isChecked():
        print("B런치 주문")
    elif r_btn3.isChecked():
        print("C런치 주문")
        
app = QApplication(sys.argv)
win = QWidget()
win.resize(200,200)

r_btn1 = QRadioButton("A런치")
r_btn2 = QRadioButton("B런치")
r_btn3 = QRadioButton("C런치")

r_btn2.setChecked(True)

btn_order = QPushButton("주문")
btn_order.clicked.connect(order)

layout = QVBoxLayout()
layout.addWidget(r_btn1)
layout.addWidget(r_btn2)
layout.addWidget(r_btn3)
layout.addWidget(btn_order)

win.setLayout(layout)
win.show()
sys.exit(app.exec())