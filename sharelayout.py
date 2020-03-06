from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("800x480")


def clear():
    mylist = window.place_slaves()
    for i in mylist:
        i.destroy()


def doorlock():
    mylist = window.place_slaves()
    for i in mylist:
        i.destroy()

        button_7 = Button(window, text='7', height=2, width=10, command=lambda: button_press('7'))
        button_8 = Button(window, text='8', height=2, width=10, command=lambda: button_press('8'))
        button_9 = Button(window, text='9', height=2, width=10, command=lambda: button_press('9'))

        button_4 = Button(window, text='4', height=2, width=10, command=lambda: button_press('4'))
        button_5 = Button(window, text='5', height=2, width=10, command=lambda: button_press('5'))
        button_6 = Button(window, text='6', height=2, width=10, command=lambda: button_press('6'))

        button_1 = Button(window, text='1', height=2, width=10, command=lambda: button_press('1'))
        button_2 = Button(window, text='2', height=2, width=10, command=lambda: button_press('2'))
        button_3 = Button(window, text='3', height=2, width=10, command=lambda: button_press('3'))

        button_0 = Button(window, text='0', height=2, width=10, command=lambda: button_press('0'))
        button_dat = Button(window, text='delete', height=2, width=10, command=lambda:ce())
        button_equal = Button(window, text='#', height=2, width=10, command=lambda: b_correct('#'))

        button_7.place(x=600, y=140)
        button_8.place(x=690, y=140)
        button_9.place(x=780, y=140)

        button_4.place(x=600, y=240)
        button_5.place(x=690, y=240)
        button_6.place(x=780, y=240)

        button_1.place(x=600, y=340)
        button_2.place(x=690, y=340)
        button_3.place(x=780, y=340)

        button_dat.place(x=600, y=440)
        button_0.place(x=690, y=440)
        button_equal.place(x=780, y=440)

        Button(window, text='뒤로가기', width=20, command=lambda: cal('화면을 터치해주세요')).place(x=650, y=100)

        display = Entry(window, width=20, show='*', justify="right")  # justify = "right" 숫자가 오른쪽으로부터
        display.place(x=652, y=50)

    def button_press(val):  # 입력받기
        display.insert("end", val)  # display 입력창의 맨끝에 매개변수값을 입력

    def b_correct(val):
        val = Entry.get(display)
        answer = 1234
        number = val
        if int(number) == answer:
            return messagebox.showinfo("확인", "정답입니다.")

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


def cal(key):
    if key == "화면을 터치해주세요":
        mylist = window.place_slaves()
        for i in mylist:
            i.destroy()

            window.configure(bg="black")

            pass2 = Button(window, text='pass', width=5, command=doorlock)
            pass2.place(x=600, y=300)


button1 = Button(window, text='화면을 터치해주세요', command=lambda: cal('화면을 터치해주세요')).place(x=330, y=220)

Label(window, text="xx동 xx호").place(x=360, y=150)

window.mainloop()
