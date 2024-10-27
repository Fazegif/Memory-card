from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
question = QLabel('Какую фразу чаще всего используют дотеры против девушек?')
btn_answer1 = QRadioButton('хук на кухню')
btn_answer2 = QRadioButton('фу женщина')
btn_answer3 = QRadioButton('женщина посудомойка')
btn_answer4 = QRadioButton('иди мой посуду')
answer = QPushButton('Ответить')
layout_main = QVBoxLayout()


RadioGroupBox = QGroupBox('Варианты')
layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()
layout4 = QHBoxLayout()
layout5 = QHBoxLayout()
layout6 = QHBoxLayout()
layout2.addWidget(btn_answer1)
layout2.addWidget(btn_answer2)
layout3.addWidget(btn_answer3)
layout3.addWidget(btn_answer4)
layout4.addWidget(question)
layout5.addWidget(answer)
layout1.addLayout(layout2)
layout1.addLayout(layout3)


RadioGroupBox.setLayout(layout1)
layout6.addWidget(RadioGroupBox)
layout_main.addLayout(layout4)
layout_main.addLayout(layout6)

layout_main.setSpacing(10)

AnsGroup = QGroupBox('Результат:')
RadioGroupBox.hide()
AnsGroup.show()
text = QLabel('правильно/неправильно')
text2 = QLabel('Правильный ответ')
layout7 = QVBoxLayout()
layout7.addWidget(text, alignment = Qt.AlignVCenter)
layout7.addWidget(text2, alignment = Qt.AlignHCenter )
AnsGroup.setLayout(layout7)
layout_main.addWidget(AnsGroup)
layout_main.addLayout(layout5)

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

def show_result():
    RadioGroupBox.hide()
    AnsGroup.show()
    answer.setText('следующий вопрос')

def show_question():
    AnsGroup.hide()
    RadioGroupBox.show()
    answer.setText('ответить')
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if 'ответить'==answer.text():
        show_result()
    else:
        show_question()

answers = [btn_answer1,btn_answer2,btn_answer3,btn_answer4]

class myquestion():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
q1 = myquestion('Самый популярный шип стримеров','Дипинс x Жожо', 'Крид x Дипинс', 'Жожо x Некоглай', 'Дипинс x Некоглай')
question_list.append(q1)
q2 = myquestion('Какой рост у Дипинса?', '190+', '185', '156', '168')
question_list.append(q2)
q3 = myquestion('Сколько Дипинсу будет лет в этом году?', '22', '19', '26', '21')
question_list.append(q3)
q4 = myquestion('В каком городе родился Ваня Дипинс?', 'Омск', 'Петербург', 'Москва', 'Ярославль')
question_list.append(q4)
q5 = myquestion('как зовут Альфу?','Денис','Андрей','Артём','Даня')
question_list.append(q5)
q6 = myquestion('Почему люди уходят с комьюнити zen?','неадекватный фандом','плохая задумка','админ адьюз','малолетки')
question_list.append(q6)
q7 = myquestion('Кем создат сервер ру комьюнити zen?','lrey','order','arstan','zombiak')
question_list.append(q7)


def ask(q: myquestion):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    text2.setText(q.right_answer)
    show_question()

def show_correct(res):
    text.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked or answers[3].isChecked():
            show_correct('Неправильно')
    print('Статистика')
    print('Всего вопросов:', main_win.total)
    print('Правильных ответов:', main_win.score)
    print('Рейтинг:', (main_win.score/main_win.total)*100)

def next_question():
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    main_win.total += 1
    ask(q)
    print('Статистика')
    print('Всего вопросов:', main_win.total)
    print('Правильных ответов:', main_win.score)

def click_OK():
    if answer.text() == 'ответить':
        check_answer()
    else:
        next_question()

main_win.cur_question = -1
answer.clicked.connect(click_OK)

main_win.total = 0
main_win.score = 0

main_win.setLayout(layout_main)
main_win.show()
app.exec_()