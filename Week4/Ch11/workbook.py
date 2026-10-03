import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QPushButton
from PyQt6.QtWidgets import QVBoxLayout

def receipt():
    selected = []
    total = 0
    
    for chk, name, price in pizza_checks:
        if chk.isChecked():
            selected.append(name)
            total += price
    print(f"주문내역: {', '.join(selected)}\n총 가격: {total}원")       

app = QApplication(sys.argv)
win = QWidget()
win.resize(400, 300)
win.setWindowTitle("조각 피자 주문 프로그램")

pizza_label = QLabel("피자")

pizza_menu = {
    "페퍼로니 피자": 3000,
    "치즈피자": 3200,
    "콤비네이션 피자": 3500,
    "불고기 피자": 3600,
    "해산물 피자": 3800
}

pizza_order = QPushButton("주문")
pizza_order.clicked.connect(receipt)

layout = QVBoxLayout()

layout.addWidget(pizza_label)

pizza_checks = []

for name, price in pizza_menu.items():
    chk = QCheckBox(f"{name} - {price} 원")
    pizza_checks.append((chk, name, price))
    layout.addWidget(chk)

layout.addWidget(pizza_order)

win.setLayout(layout)
win.show()
sys.exit(app.exec())