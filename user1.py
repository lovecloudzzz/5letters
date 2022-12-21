import socket
import threading
from PyQt6.QtWidgets import QApplication
from back.players import Player1, Player2


def receive():
    while True:
        window.messages.append(sock.recv(1024).decode('utf-8'))
        if window.number == 2:
            if len(window.messages[0]) == 1:
                flag = window.sock.recv(1024).decode('utf-8')
                if flag == '1':
                    window.mistake.setText('')
                    for j in range(len(window.word)):
                        if window.word[j] == window.input[j].lower():
                            window.massive[window.i - 5 + j].setStyleSheet("background-color:#ffb833; border-radius: 10px")
                            window.flag += 1
                        elif window.input[j].lower() not in window.word:
                            window.massive[window.i - 5 + j].setStyleSheet("background-color:#9c9c9c; color:#c7c7c7")
                    if window.flag == 5:
                        window.mistake.setText('Победа!')
                        window.Play.setEnabled(False)
                    else:
                        window.input = ''
                        window.flag = 0
                        window.words += 1
                        if window.words == 6:
                            window.mistake.setText(
                                f'Вы проиграли,\n попытки исчерпаны\nПравильное слово - {window.word}')
                            window.input = 'aaaaa'
                            window.Play.setEnabled(False)
                else:
                    window.mistake.setText('Такого слова нет в словаре,\nпопробуйте другое')
            else:
                window.word = window.messages[0]
                window.Play.clicked.connect(window.check)
                window.Play.setEnabled(True)
            window.messages.pop()


if __name__ == '__main__':
    app = QApplication([])
    sock = socket.socket()
    sock.connect(('localhost', 50000))
    number = sock.recv(1024).decode('utf-8')
    if number == '1':
        window = Player1(sock)
        window.Play.setEnabled(True)
    else:
        window = Player2(sock)
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    window.show()
    app.exec()
