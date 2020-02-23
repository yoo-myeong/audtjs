from tkinter import*

window=Tk()
window.title("502번째 확진자 유명선")
window.configure(bg="white")
window.geometry("240x240")

def cal(key):
    if key == "=" :
        result = str(eval(label.get()))
        label.delete(0,END)
        label.insert(END, result)

    elif key=="C":
        label.delete(0,END)

    else :
        label.insert(END, key)

def button_press(val):
    label.insert(END, val)
 

label=Entry(window, width=22, justify='right')
label.grid(row=0, column=0, columnspan=3, pady=10, padx=4) #padx는 상하여백, pady는 좌우여백

button_c = Button(window, text='C', width=5, command=lambda:cal('C'))

button_7 = Button(window, text='7', width=5, command=lambda:button_press('7'))
button_8 = Button(window,text='8', width=5, command=lambda:button_press('8'))
button_9 = Button(window, text='9',width=5, command=lambda:button_press('9'))
button_dash = Button(window, text='/', width=5, command=lambda:cal('/'))

button_4 = Button(window,text='4', width=5, command=lambda:button_press('4'))
button_5 = Button(window, text='5',width=5, command=lambda:button_press('5'))
button_6 = Button(window, text='6',width=5, command=lambda:button_press('6'))
button_mul = Button(window, text='*', width=5, command=lambda:cal('*'))

button_1 = Button(window, text='1',width=5, command=lambda:button_press('1'))
button_2 = Button(window,text='2', width=5, command=lambda:button_press('2'))
button_3 = Button(window,text='3', width=5, command=lambda:button_press('3'))
button_minus = Button(window, text='-',width=5, command=lambda:cal('-'))

button_0 = Button(window,text='0', width=5, command=lambda:button_press('0'))
button_dat = Button(window, text='.',width=5, command=lambda:button_press('.'))
button_equal = Button(window,text='=', width=5, command=lambda:cal('='))
button_plus = Button(window,text='+', width=5, command=lambda:cal('+'))
 


label.grid(row=0,column=0,columnspan=3,pady=10,padx=4)

button_c.grid(row=0,column=3)

button_7.grid(row=1,column=0,pady=3)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_dash.grid(row=1,column=3)

button_4.grid(row=2,column=0,pady=3)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_mul.grid(row=2,column=3)

button_1.grid(row=3,column=0,pady=3)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_minus.grid(row=3,column=3)

button_0.grid(row=4,column=0,pady=3)
button_dat.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_plus.grid(row=4,column=3)


window.mainloop()
