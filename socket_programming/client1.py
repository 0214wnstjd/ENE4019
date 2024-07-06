# 2019007892
# 박준성
from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
# 서버와 연결
clientSocket.connect(('127.0.0.1', 8080))
print('서버와 연결 되었습니다.')

print('메시지를 입력하시고, 종료하시려면 quit을 입력하십시오')
while True:
    message = input('>>>')  # 메시지 입력
    if message == 'quit':   # quit 입력시 break
        break
    clientSocket.send(message.encode('utf-8'))  # 서버에게 send
    data = clientSocket.recv(1024)  # 서버로부터 receive
    print('서버 : ', data.decode('utf-8'))
clientSocket.close()  # socket close
print('클라이언트 소켓을 닫았습니다')
print('서버와의 연결을 종료하였습니다.')
