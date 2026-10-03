import sys
from PyQt6.QtWidgets import QApplication, QComboBox, QVBoxLayout, QWidget

app = QApplication(sys.argv)
window = QWidget()

# 1. 옵션 리스트 정의
options_list = ["Option 1", "Option 2", "Option 3"]

# 2. QComboBox 생성 및 항목 일괄 추가
combo = QComboBox()
combo.addItems(options_list)


def changed():
    selected = combo.currentText()
    print(selected)

combo.currentTextChanged.connect(changed)

# 3. 레이아웃 배치
layout = QVBoxLayout()
layout.addWidget(combo)

window.setLayout(layout)
window.show()

sys.exit(app.exec())