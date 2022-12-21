import socket

sock = socket.socket()
sock.bind(('', 50000))
sock.listen(2)
conn1, addr1 = sock.accept()
conn2, addr2 = sock.accept()
words = []

with open('data/words.txt', 'r', encoding='utf-8') as file:
    line = file.read().split()
    for i in line:
        words.append(i)


def check(word):
    global words
    if word not in words:
        return '2'
    else:
        return '1'


conn1.send('1'.encode('utf-8'))
conn2.send('2'.encode('utf-8'))

while True:
    word = conn1.recv(1024).decode('utf-8')
    conn1.send(check(word).encode('utf-8'))
    if check(word) == '1':
        conn2.send(word.encode('utf-8'))
        while True:
            input_word = conn2.recv(1024).decode('utf-8')
            conn2.send(check(input_word).encode('utf-8'))
