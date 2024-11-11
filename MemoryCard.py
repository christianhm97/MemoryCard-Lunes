from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

aplicacion = QApplication([])
ventana = QWidget()
ventana.show()
ventana.setWindowTitle('Memory Card')

lb_Question = QLabel('Aquí veremos la pregunta')
btn_Ok = QPushButton('Responder')

RadioGroupBox = QGroupBox('Opciones de respuesta')

rbtn_1 = QRadioButton('Respuesta 1')
rbtn_2 = QRadioButton('Respuesta 2')
rbtn_3 = QRadioButton('Respuesta 3')
rbtn_4 = QRadioButton('Respuesta 4')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_Ok, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)

layout_card.setSpacing(5)

ventana.setLayout(layout_card)

aplicacion.exec_()
