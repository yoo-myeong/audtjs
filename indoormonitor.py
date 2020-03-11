from tkinter import *
from tkinter import messagebox
import tkinter.font
import datetime
from threading import *
from tkinter import messagebox
import cv2
import sys
from PIL import Image,ImageTk
from face_recog import *
from camera import *

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
    
def livecheck():
    clear()
    cvFrame=Frame(window)
    cvFrame.place(x=0,y=0)

    lbl1=Label(cvFrame)
    lbl1.grid(row=0,column=0)
        
    def ExitButton():
        clear()
        back()
            

    btn=Button(cvFrame,text="Exit",command=lambda:ExitButton())
    btn.place(x=0,y=300)
    cap=cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,720)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,360)
    frame_size=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('frame_size=',frame_size)

    def show_frame():
        retval,frame=cap.read()
        frame=cv2.flip(frame,1)
        cv2image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
        img=Image.fromarray(cv2image)

        imgtk=ImageTk.PhotoImage(image=img)

        lbl1.imgtk=imgtk
        lbl1.configure(image=imgtk)

            

        window.after(10,show_frame)
    

    show_frame()
def settings():
    clear()
def interphornconnect():
    clear()
def open():
    clear()
def confirm():
    clear()
def reject():
    clear()
    back()
def recording():
    clear()      

def cameraon():
    cvFrame=Frame(window)
    cvFrame.place(x=0,y=130)

    lbl1=Label(cvFrame)
    lbl1.grid(row=0,column=0)
        
    def ExitButton():
            sys.exit()

    btn=Button(cvFrame,text="Exit")
    btn.place(x=0,y=300)
    cap=cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,352)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,288)
    frame_size=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('frame_size=',frame_size)
    

    def show_frame():
        retval,frame=cap.read()
        frame=cv2.flip(frame,1)
        cv2image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
        img=Image.fromarray(cv2image)

        imgtk=ImageTk.PhotoImage(image=img)

        lbl1.imgtk=imgtk
        lbl1.configure(image=imgtk)

            

        window.after(10,show_frame)
    

    show_frame()
def next():
    clear()
    
    labelText = StringVar()
    labelText.set("현재 시각: 00:00:00")
    label = Label(window, textvariable = labelText, width = 20)
    label.grid(row = 0, column = 0)
    label.place(x=50,y=50)
    

    updateTimer(labelText)

    cameraon()

    if correct==0:
        
        correct1=Label(window, text='일치하는 수배 얼굴이 없습니다.')
        correct1.place(x=500,y=100)
        
        button_interphornconnect = Button(window, text='인터폰연결', height=3, width=18, command=lambda:interphornconnect())
        button_interphornconnect.place(x=400, y=200)
        
        button_recording = Button(window, text='녹음본 출력', height=3, width=18, command=lambda:recording())
        button_recording.place(x=600, y=200)
        
        button_reject = Button(window, text='인터폰 거절', height=3, width=18, command=lambda:reject())
        button_reject.place(x=400, y=300)
        
        button_open = Button(window, text='문열기', height=3, width=18, command=lambda:open())
        button_open.place(x=600, y=300)
    elif correct>0:
        f=Frame(window,bg="black")
        
        correct2=Label(window, text='인식된 얼굴과 일치하는 수배 데이터를 찾았습니다.')
        correct2.place(x=500,y=100)
        
        button_confirm = Button(window, text='수배데이터 직접확인하기', height=3, width=18, command=lambda:confirm())
        button_confirm.place(x=400, y=200)
        
        button_interphornconnect = Button(window, text='인터폰연결', height=3, width=18, command=lambda:interphornconnect())
        button_interphornconnect.place(x=600, y=200)
        
        button_reject = Button(window, text='인터폰 거절', height=3, width=18, command=lambda:reject())
        button_reject.place(x=400, y=300)
        
        button_open = Button(window, text='문열기', height=3, width=18, command=lambda:open())
        button_open.place(x=600, y=300)
    
    
    
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

