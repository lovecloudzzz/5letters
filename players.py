from PyQt6.QtWidgets import QMainWindow

import front.player2 as player2
import front.player1 as player1


class Player1(QMainWindow, player1.Ui_MainWindow):
    def __init__(self, sock):
        super(Player1, self).__init__()
        self.setupUi(self)
        self.sock = sock
        self.number = 1
        self.Play.clicked.connect(self.check)

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.check()

    def check(self, ):
        word = self.word.text()
        if len(word) != 5:
            self.mistake.setText('Попробуйте другое слово')
        else:
            word = word.lower()
            self.sock.send(word.encode('utf-8'))
            flag = self.sock.recv(1024).decode('utf-8')
            if flag == '1':
                print(flag)
                self.mistake.setText('Слово загадано')
                self.Play.setEnabled(False)
            else:
                self.mistake.setText('Попробуйте другое слово')


class Player2(QMainWindow, player2.Ui_MainWindow):
    def __init__(self, sock):
        self.sock = sock
        self.number = 2
        self.messages = []
        super(Player2, self).__init__()
        self.setupUi(self)
        self.massive = [0, self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, self.s7, self.s8, self.s9,
                        self.s10, self.s11, self.s12, self.s13, self.s14, self.s15, self.s16, self.s17, self.s18,
                        self.s19, self.s20, self.s21, self.s22, self.s23, self.s24, self.s25, self.s26, self.s27,
                        self.s28, self.s29, self.s30]
        self.i = 1
        self.alph = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.input = ''
        self.flag = 0
        self.words = 0


    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.check()
        if event.key() > 1039 and event.key() < 1072 and len(self.input) != 5:
            self.massive[self.i].setText(self.alph[event.key() - 1040])
            self.i += 1
            self.input = self.input + self.alph[event.key() - 1040]
        if event.key() == 1025 and self.flag != 5:
            self.massive[self.i].setText('Ё')
            self.input = self.input + 'Ё'
            self.i += 1
        if event.key() == 16777219 and len(self.input) > 0:
            self.i = self.i - 1
            self.massive[self.i].setText('')
            self.input = self.input[0:len(self.input) - 1]

    def check(self):
        if len(self.input) != 5:
            self.mistake.setText('Неполное слово')
        else:
            self.sock.send(self.input.lower().encode('utf-8'))
