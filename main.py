from tkinter.constants import CENTER
from vidstream import *
import tkinter as tk
import socket
import threading

local_ip_address = socket.gethostbyname(socket.gethostname())

server = StreamingServer(local_ip_address, 9999)
receiver = AudioReceiver(local_ip_address, 8888)

def listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()
    
def camara():
    camara_client = CameraClient(text_target_ip.get(1.0, 'end-1c'), 7777)
    t3 = threading.Thread(target=camara_client.start_stream)
    t3.start()

def screen():
    screen_client = ScreenShareClient(text_target_ip.get(1.0, 'end-1c'), 7777)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()

def audio():
    audio_sender = AudioSender(text_target_ip.get(1.0, 'end-1c'), 6666)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()    



# GUI

root = tk.Tk()
root.title("Zoom Clone")
root.geometry('600x500')
root.wm_iconbitmap("zoom1.ico")

label_target_ip = tk.Label(root, text="target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(root, height=1)
text_target_ip.pack()


bt_listen = tk.Button(root, text="Start Listening", width=50, bg="Steelblue1", command=listening)
bt_listen.pack(anchor=CENTER, expand=True)


bt_camara = tk.Button(root, text="Start Camara", width=50, bg="Steelblue1", command=camara)
bt_camara.pack(anchor=CENTER, expand=True)


bt_screen = tk.Button(root, text="Start Screen Sharing", width=50, bg="Steelblue1", command=screen)
bt_screen.pack(anchor=CENTER, expand=True)


bt_audio = tk.Button(root, text="Start Audio", width=50, bg="Steelblue1", command=audio)
bt_audio.pack(anchor=CENTER, expand=True)


root.mainloop()