#Label 배우기 (로그인창 만들기)
# get() - 라벨안의 문자열반환
# set() - 라벨안의 문자열 설정
# place(x,y) - 라벨안의 텍스트 위치 설정

from tkinter import*

top = Tk()
top.geometry("350x250")
top.configure(bg="black")

id = Label(top, text = "아이디").place(x=30,y=20) # 전에는 grid(row,column)으로 위치설정 해줬지만 이거는 place(x,y)로 x,y좌표 설정
el = Entry(top, width=20).place(x=100, y=20)

pwd = Label(top, text= "패스워드").place(x=30, y=90)
e2 = Entry(top, width=20, show= '*').place(x=100, y=90) #여기서 width는 entry의 폭을 뜻함

btn = Button(top, text= "로그인").place(x=30, y=130)

top.mainloop()

