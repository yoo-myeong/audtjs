from tkinter import*
from tkinter import messagebox
top = Tk()
top.title("도어락으로 만들기")
top.geometry("200x300")
top.configure(bg="blue")
top.resizable(False, False)

def b_press(val): #입력받기
    display.insert("end",val) #display 입력창의 맨끝에 매개변수값을 입력

def b_correct():
    val = Entry.get(display)
    answer =1234
    number = val
    if int(number) == answer:
        return messagebox.showinfo("확인", "정답입니다.")
    else:
        display.delete(0,END)
        return messagebox.showinfo("확인","틀렸습니다.")



display = Entry(top, width= 15, justify ="right", show = '*') # justify = "right" 숫자가 오른쪽으로부터

b_1 = Button(top, text = '1', width =5, command = lambda:b_press('1'))
b_2 = Button(top, text = '2', width =5, command = lambda:b_press('2'))
b_3 = Button(top, text = '3', width =5, command = lambda:b_press('3'))

b_4 = Button(top, text = '4', width =5, command = lambda:b_press('4'))
b_5 = Button(top, text = '5', width =5, command = lambda:b_press('5'))
b_6 = Button(top, text = '6', width =5, command = lambda:b_press('6'))

b_7 = Button(top, text = '7', width =5, command = lambda:b_press('7'))
b_8 = Button(top, text = '8', width =5, command = lambda:b_press('8'))
b_9 = Button(top, text = '9', width =5, command = lambda:b_press('9'))

b_0 = Button(top, text = '0', width =5, command = lambda:b_press('0'))
b_last = Button(top, text = "확인", command = b_correct )


display.grid(row=6,column=0, columnspan =4)

b_1.grid(row=1, column=0, pady=8, padx=10)  
b_2.grid(row=1, column=1, padx=10 )
b_3.grid(row=1, column=2, padx=10 )

b_4.grid(row=2, column=0, pady=8, padx=10)
b_5.grid(row=2, column=1 , padx=10)
b_6.grid(row=2, column=2 , padx=10)

b_7.grid(row=3, column=0, pady=8, padx=10)
b_8.grid(row=3, column=1, padx=10)
b_9.grid(row=3, column=2, padx=10)

b_0.grid(row=4, column=1, pady=8, padx=10)
b_last.grid(row=5, column=1,pady=8)

top.mainloop()