import sys 
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QPushButton, QCheckBox
from PyQt6.QtWidgets import QVBoxLayout

def order():
    selected_items= []
    if chk1.isChecked():
        selected_items.append("아메리카노")
    if chk2.isChecked():
        selected_items.append("라떼")
    if chk3.isChecked():
        selected_items.append("카푸치노")
    if chk4.isChecked():
        selected_items.append("에스프레소")
    
    if selected_items:
        print(f"주문 항목: {', '.join(selected_items)}")
    else:
        print("선택한 메뉴가 없습니다.")
        
app = QApplication(sys.argv)
win = QWidget()
win.resize(200,200)

chk1 = QCheckBox("아메리카노")
chk2 = QCheckBox("라떼")
chk3 = QCheckBox("카푸치노")
chk4 = QCheckBox("에스프레소")

btn_order = QPushButton("주문")
btn_order.clicked.connect(order)

layout = QVBoxLayout()
layout.addWidget(chk1)
layout.addWidget(chk2)
layout.addWidget(chk3)
layout.addWidget(chk4)
layout.addWidget(btn_order)

win.setLayout(layout)
win.show()
sys.exit(app.exec())