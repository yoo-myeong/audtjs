from tkinter import*
import random

window=Tk()
window.title("도어락")
window.configure(bg="white")
window.geometry("450x400")

number = '1357'

def cal(key):
    if key == "#" :
        result = str(label.get())
        label.delete(0,END)
        if result == number :
            label.insert(END, "문이 열립니다")
        else :
            label.insert(END,"*를 누르고 다시 입력하시오")

    elif key=="*":
        label.delete(0,END)

def button_press(val):
    label.insert(END, val)
        

label=Entry(window, width=55, justify='right')
label.grid(row=0, column=0, columnspan=2, pady=10, padx=4)

button_7 = Button(window, text='7', width=20, command=lambda:button_press('7'))
button_8 = Button(window,text='8', width=20, command=lambda:button_press('8'))
button_9 = Button(window, text='9',width=20, command=lambda:button_press('9'))

button_4 = Button(window,text='4', width=20, command=lambda:button_press('4'))
button_5 = Button(window, text='5',width=20, command=lambda:button_press('5'))
button_6 = Button(window, text='6',width=20, command=lambda:button_press('6'))

button_1 = Button(window, text='1',width=20, command=lambda:button_press('1'))
button_2 = Button(window,text='2', width=20, command=lambda:button_press('2'))
button_3 = Button(window,text='3', width=20, command=lambda:button_press('3'))

button_0 = Button(window,text='0', width=20, command=lambda:button_press('0'))
button_dat = Button(window, text='*',width=20, command=lambda:cal('*'))
button_equal = Button(window,text='#', width=20, command=lambda:cal('#'))


label.grid(row=0,column=0,columnspan=3,pady=10,padx=4)

button_7.grid(row=1,column=0,pady=3)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_4.grid(row=2,column=0,pady=3)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_1.grid(row=3,column=0,pady=3)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_dat.grid(row=4,column=0,pady=3)
button_0.grid(row=4,column=1)
button_equal.grid(row=4,column=2)


window.mainloop()
