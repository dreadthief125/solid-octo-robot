import socket
from threading import Thread
nickname=input("Username?")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_aderess='127.0.0.1'
port=8000
client.connect(((ip_aderess,port)))
print("Connected to the quiz game! Please enjoy your stay.")
def recive():
  while True:
    try:
      message=client.recv(2048).decode('utf-8')
      if message=='nickname':
        client.send(nickname.encode('utf-8'))
      else:
        print(message)
    except:
      print("ErR 404!11!!1 ERROR! error id: recive function misrun")
      client.close()
      break
def write():
  while True:
    message='{}: {}'.format(nickname,input(''))
    client.send(message.encode('utf-8'))
recive_thread=Thread(target=recive)
recive_thread.start()
write_thread=Thread(target=write)
write_thread.start()


