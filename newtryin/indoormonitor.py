from tkinter import *
from tkinter import messagebox
import tkinter.font
import datetime
from threading import *
from tkinter import messagebox
import cv2
import sys
from PIL import Image,ImageTk
import os
import socket
import numpy
from queue import Queue
from _thread import *

def runcontrol() :
    os.system("inserver.py")
def runcontrol2() :
    os.system("inclient.py")

    
th = Thread(target=runcontrol)  # inserver ip겹쳐서 port 바꿔놨음
th.start()
th1 = Thread(target=runcontrol2)  # inserver ip겹쳐서 port 바꿔놨음
th1.start()



"""
import RPi.GPIO as GPIO
import time
"""

window = Tk()
window.geometry("780x450")
window.configure(bg="black")

timer = None
visit=2
correct=0
def visitant():
    if visit>=1:
        t = datetime.datetime.now()
        
def updateTimer(labelText):  #시간 나타내기
    global timer
    t = datetime.datetime.now()
    labelText.set("현재 시각: {:02d}:{:02d}:{:02d}".format(t.hour, t.minute, t.second))
    timer = Timer(1.0, updateTimer, [labelText])
    timer.start()

def clear():  #화면 다지우기
    mylist = window.place_slaves()
    for i in mylist:
        i.destroy()


    def button_press(val):  # 입력받기
        display.insert("end", val)  # display 입력창의 맨끝에 매개변수값을 입력
        
def visitdata():
    clear()
    visitant()
    

def cameraon() :    
    cvFrame=Frame(window)
    cvFrame.place(x=30,y=75)

    lbl1=Label(cvFrame)
    lbl1.grid(row=0,column=0)
    
    def recvall(sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf


    HOST = '192.168.35.39'
    PORT = 9999

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

    client_socket.connect((HOST, PORT))
    
    while True: 
        message = '1'
        client_socket.send(message.encode()) 
          
        length = recvall(client_socket,16)
        stringData = recvall(client_socket, int(length))
        data = numpy.frombuffer(stringData, dtype='uint8') 

        frame=cv2.imdecode(data,1) # 여기까지 카메라 소켓코드. 이미지들을 소켓을통해 frame에 받는것 까지만 이용
        frame=cv2.flip(frame,1) # 여기서부터는 frame에 이미지 넣는 코드, 소켓을 통해 받는 이미지를 frame에 맞게 변환해서 넣고 그것을 while문으로 반복하면 영상이 된다.
        cv2image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
        img=Image.fromarray(cv2image)

        imgtk=ImageTk.PhotoImage(image=img)

        lbl1.imgtk=imgtk
        lbl1.configure(image=imgtk)
            
        key = cv2.waitKey(1)
        if key == 27:
            break  


def next():
    clear()
    
    labelText = StringVar()
    labelText.set("현재 시각: 00:00:00")
    label = Label(window, textvariable = labelText, width = 20)
    label.grid(row = 0, column = 0)
    label.place(x=50,y=50)
    

    updateTimer(labelText)

    if correct==0:
        
        correct1=Label(window, text='일치하는 수배 데이터가 없습니다.')
        correct1.place(x=500,y=100)
        
        button_reject = Button(window, text='인터폰 종료', height=3, width=18, command=lambda:reject())
        button_reject.place(x=400, y=300)
        
        button_open = Button(window, text='문열기', height=3, width=18, command=lambda:open())
        button_open.place(x=600, y=300)
    elif correct>0:
        f=Frame(window,bg="black")
        
        correct2=Label(window, text='인식된 얼굴과 일치하는 수배 데이터를 찾았습니다.')
        correct2.place(x=500,y=100)
        
        button_confirm = Button(window, text='수배데이터 직접확인하기', height=3, width=18, command=lambda:confirm())
        button_confirm.place(x=400, y=200)
        
        button_reject = Button(window, text='인터폰 거절', height=3, width=18, command=lambda:reject())
        button_reject.place(x=500, y=300)
        
        button_open = Button(window, text='문열기', height=3, width=18, command=lambda:open())
        button_open.place(x=600, y=300)

    th3=Thread(target=cameraon)
    th3.start()
    
    
def back():
    labelText = StringVar()
    labelText.set("현재 시각: 00:00:00")
    label = Label(window, textvariable = labelText, width = 20)
    label.grid(row = 0, column = 0)
    label.place(x=300,y=100)


    updateTimer(labelText)

    button_visitdata = Button(window, text='방문기록', height=3, width=10, command=lambda:visitdata())
    button_visitdata.place(x=100, y=300)

    button_livecheck = Button(window, text='실시간확인', height=3, width=10, command=lambda:livecheck())
    button_livecheck.place(x=330, y=300)

    button_settings = Button(window, text='설정', height=3, width=10, command=lambda:settings())
    button_settings.place(x=550, y=300)
    button_next = Button(window, text='다음', height=3, width=10, command=lambda:next())
    button_next.place(x=700, y=400)

    
        
        
        

    
    





labelText = StringVar()
labelText.set("현재 시각: 00:00:00")
label = Label(window, textvariable = labelText, width = 20)
label.grid(row = 0, column = 0)
label.place(x=300,y=100)


updateTimer(labelText)
button_visitdata = Button(window, text='방문기록', height=3, width=10, command=lambda:visitdata())
button_visitdata.place(x=100, y=300)

button_livecheck = Button(window, text='실시간확인', height=3, width=10, command=lambda:livecheck())
button_livecheck.place(x=330, y=300)

button_settings = Button(window, text='설정', height=3, width=10, command=lambda:settings())
button_settings.place(x=550, y=300)
button_next = Button(window, text='다음', height=3, width=10, command=lambda:next())
button_next.place(x=700, y=400)





window.mainloop()
timer.cancel()

