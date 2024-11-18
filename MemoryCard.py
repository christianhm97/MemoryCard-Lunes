from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


app = QApplication([])


window = QWidget()
window.setWindowTitle('Tarjeta de memoria')


'''Interfaz para la aplicación de Tarjeta de memoria'''
btn_OK = QPushButton('Responder') # botón de responder
lb_Question = QLabel('Aquí irá nuestra pregunta') # texto de pregunta


RadioGroupBox = QGroupBox("Opciones de respuesta") # grupo en la pantalla para botones de radio con respuestas
rbtn_1 = QRadioButton('Respuesta 1')
rbtn_2 = QRadioButton('Respuesta 2')
rbtn_3 = QRadioButton('Respuesta 3')
rbtn_4 = QRadioButton('Respuesta 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

AnsGroupBox = QGroupBox("Resultado de prueba")
AnsGroupBox.hide()
lb_Result = QLabel("Correcto-Incorrecto")
lb_Correct = QLabel("Respuesta correcta")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment= Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # los verticales estarán dentro de los horizontales
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # dos respuestas en la primera columna
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # dos respuestas en la segunda columna
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # las columnas están en la misma línea


RadioGroupBox.setLayout(layout_ans1) # el “panel” con opciones de respuesta está listo 


layout_line1 = QHBoxLayout() # pregunta
layout_line2 = QHBoxLayout() # opciones de respuesta o resultados de prueba
layout_line3 = QHBoxLayout() # botón de “Responder”


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # el botón debería ser grande
layout_line3.addStretch(1)


# Ahora vamos a colocar las líneas que hemos creado una debajo de la otra:
layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # los espacios entre el contenido


window.setLayout(layout_card)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Siguiente Pregunta")


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Responder")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


def test():
    if btn_OK.text() == "Responder":
        show_result()
    else:
        show_question()

btn_OK.clicked.connect(test)

window.show()
app.exec()

