from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

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
        check_answer()
        show_result()
    else:
        next_question()

btn_OK.clicked.connect(test)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask (q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    lb_Result.setText(res)


def check_answer():
    if answers[0].isChecked():
        show_correct('Correcto')
    else:
        show_correct('Incorrecto')


def next_question():
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)


question_list = []
q1 = Question('¿Cuál es la capital de España?', 'Madrid', 'Sevilla', 'Toledo', 'Valencia')
question_list.append(q1)
q2 = Question('¿Qué idioma se habla en Argentina?', 'Español', 'Argentino', 'Inglés', 'Portugués')
question_list.append(q2)
q3 = Question('¿Cuánto es nueve mil noventa y nueve más uno?', '9100', '9999', '10000', '9909')
question_list.append(q3)
q4 = Question('¿Cuál es mamífero?', 'Murciélago', 'Atún', 'Serpiente', 'Caracol')
question_list.append(q4)
q5 = Question('¿Qué planeta es el más cercano al Sol?', 'Mercurio', 'Marte', 'Tierra', 'SagitarioA*')
question_list.append(q5)


next_question()
window.show()
app.exec()
