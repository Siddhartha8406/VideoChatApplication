from http import client
import os
os.system('clear')

#-------Main Code starts here-------
import socket
import cv2
import threading
import pickle
import struct

#---Host Creation---
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = "SERVER"
HOST_IP = '192.168.29.8'
HOST_PORT = 6969
print(f"[{HOST_NAME}][{HOST_IP}]")

soc.bind((HOST_IP,HOST_PORT))

soc.listen(2)
print(f"[{HOST_NAME}]: Waiting for incomming connections.......")


while True:
    client_socket, client_addr = soc.accept()
    print(f"[{client_addr}]: CONNECTED TO SERVER")
    if client_socket:
        vid = cv2.VideoCapture(0)
    
        while(vid.isOpened()):
            ret,image = vid.read()
            img_serialize = pickle.dumps(image)
            message = struct.pack("Q",len(img_serialize))+img_serialize
            client_socket.sendall(message)
            
            cv2.imshow('Video from Server',image)
            key = cv2.waitKey(10) 
            if key ==13:
                client_socket.close()