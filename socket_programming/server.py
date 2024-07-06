# 2019007892
# 박준성
import os
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 8080))
serverSocket.listen(1)
print('클라이언트의 접속을 기다리고 있습니다 . . . ')

# 3개의 클라이언트 연결 반복
for i in range(3):
    pid = os.fork()  # 자식 프로세스 생성
    if pid == 0:    # 자식 프로세스 (각 클라이언트와 연결하여 작업 후 종료)
        connectionSocket, addr = serverSocket.accept()
        # 연결된 클라이언트 정보 출력
        print(str(addr), '에서 접속하였습니다.')
        while True:
            # client가 보낸 데이터 receive
            data = connectionSocket.recv(1024)
            # 클라이언트가 quit을 입력하여 연결 종료시 break
            if not data:
                print(str(addr), '에서 연결을 종료하였습니다')
                break
            # 클라이언트가 보낸 메시지 출력
            print(str(addr), '의 메시지 : ', data.decode('utf-8'))
            # 클라이언트에게 수신 확인 메시지 send
            connectionSocket.send('메시지를 정상적으로 받았습니다'.encode('utf-8'))

        # connection 소켓 close
        connectionSocket.close()
        print(str(addr), '와의 연결 소켓을 닫았습니다.')
        # fork exit
        os._exit(0)
# 부모 프로세스가 3개 자식 프로세스 종료까지 wait
for i in range(3):
    os.wait()
# 서버 소켓 close
serverSocket.close()
print('서버 소켓을 닫았습니다.')
