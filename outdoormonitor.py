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



"""
import RPi.GPIO as GPIO
import time
"""

window = Tk()
window.geometry("780x450")
window.configure(bg="black")


def cameraon():
    cvFrame=Frame(window)
    cvFrame.place(x=100,y=75)

    lbl1=Label(cvFrame)
    lbl1.grid(row=0,column=0)
        
    def ExitButton():
            sys.exit()

    btn=Button(cvFrame,text="Exit")
    btn.place(x=0,y=300)
    cap=cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,448)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,350)
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
def clear():
    mylist = window.place_slaves()
    for i in mylist:
        i.destroy()

def doorlock():
    clear()

    button_7 = Button(window, text='7', height=2, width=7, command=lambda: button_press('7'))
    button_8 = Button(window, text='8', height=2, width=7, command=lambda: button_press('8'))
    button_9 = Button(window, text='9', height=2, width=7, command=lambda: button_press('9'))

    button_4 = Button(window, text='4', height=2, width=7, command=lambda: button_press('4'))
    button_5 = Button(window, text='5', height=2, width=7, command=lambda: button_press('5'))
    button_6 = Button(window, text='6', height=2, width=7, command=lambda: button_press('6'))

    button_1 = Button(window, text='1', height=2, width=7, command=lambda: button_press('1'))
    button_2 = Button(window, text='2', height=2, width=7, command=lambda: button_press('2'))
    button_3 = Button(window, text='3', height=2, width=7, command=lambda: button_press('3'))

    button_0 = Button(window, text='0', height=2, width=7, command=lambda: button_press('0'))
    button_dat = Button(window, text='*', height=2, width=7, command=lambda: ce())
    button_equal = Button(window, text='#', height=2, width=7, command=lambda: b_correct('#'))

    button_7.place(x=460, y=140)
    button_8.place(x=550, y=140)
    button_9.place(x=640, y=140)

    button_4.place(x=460, y=200)
    button_5.place(x=550, y=200)
    button_6.place(x=640, y=200)

    button_1.place(x=460, y=260)
    button_2.place(x=550, y=260)
    button_3.place(x=640, y=260)

    button_dat.place(x=460, y=320)
    button_0.place(x=550, y=320)
    button_equal.place(x=640, y=320)

    Button(window, text='뒤로가기', width=20, command=lambda:cal('화면을 터치해주세요')).place(x=502, y=100)

    display = Entry(window, width=20, justify="right", show='*')  # justify = "right" 숫자가 오른쪽으로부터
    display.place(x=505, y=50)
    cameraon()

    def button_press(val):  # 입력받기
        display.insert("end", val)  # display 입력창의 맨끝에 매개변수값을 입력

    def b_correct(val):
        val = Entry.get(display)
        answer = 1234
        number = val
        if int(number) == answer:
            back()
            return messagebox.showinfo("확인", "문이 열립니다")


            """
            pin = 18
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(pin, GPIO.OUT)
            p = GPIO.PWM(pin, 50)
            p.start(0)
            cnt = 0        button_4 = Button(window, text='4', height=2, width=

            p.ChangeDutyCycle(12.5)
            time.sleep(5)

            p.ChangeDutyCycle(2.5)
            time.sleep(1)

            p.stop()
            GPIO.cleanup()
            """
        else:
            display.delete(0, END)
            return messagebox.showinfo("확인", "틀렸습니다.")

    def ce():  # 마지막 입력 지우기
        ms = Entry.get(display)
        x = ''  # 문자를 저장할 변수
        if len(ms) == 1:
            display.delete(0, END)
        for i in range(len(ms) - 1):  # range(0,5,2)는 0,2,4
            # len(객체)는 객체의 갯수를 뜻한다.
            x += ms[i]
            display.delete(0, END)
            display.insert('end', x)
            if len(ms)==1 :
                display.delete(0, END)


call = PhotoImage(file = "call.gif")
pass2 = PhotoImage(file ="pass2.gif")

def cal(key):
    if key=="화면을 터치해주세요":
        clear()

        window.configure(bg="black")

        c_i = Button(window,height =120, width =120, image = call, command=lambda:interphone())
        c_i.place(x=600, y=70)

        p_i = Button(window,height =120, width =120, image=pass2, command=lambda:doorlock())
        p_i.place(x=600, y=250)
        cameraon()

def back():
    clear()
    button1 = Button(window, text='터치해주세요', font=font, bg='black', fg='white', bd=-1,
                     command=lambda: cal('화면을 터치해주세요')).place(x=290, y=180)


end_call = PhotoImage(file = "end_call.gif")

def RunControl():
    os.system("chat_server.py")

def RunControl2():
    os.system("chat_client.py")

def close():
    os.system('taskkill /f /im py.exe')


def interphone():
    clear()
    th1 = Thread(target=RunControl)
    th1.start()
    th2 = Thread(target=RunControl2)
    th2.start()
    
    label=Label(window, text='---연결중입니다---',bd=0, bg='black', fg='white', font=font2)
    label.place(x=582, y=150)
    e_i = Button(window, height = 120, width = 120, bd=-1, image = end_call,command = back)
    e_i.place(x=600,y=250)
    cameraon()

   

def back2():
    clear()
    close()
    cameraon()
    button1 = Button(window, text='터치해주세요', font=font, bg='black', fg='white', bd=-1,
                     command=lambda: cal('화면을 터치해주세요')).place(x=290, y=180)


font=tkinter.font.Font(family="맑은 고딕", size=20, slant="italic")
font2=tkinter.font.Font(family="맑은 고딕", size=15)

button1 = Button(window, text='터치해주세요', font=font, bg='black', fg='white', bd=-1,
                 command=lambda: cal('화면을 터치해주세요')).place(x=290,y=180)




window.mainloop()