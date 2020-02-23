from tkinter import*    # 원래는 tkinter.Tk()라고 라이브러리 이름을 불러줘야 하지만 이걸 쓰면 이 프로젝트내에서 불러들임 없이 tkinter 모듈을 사용할 수 있다.

canvasHeight = 400
canvasWidth = 600
canvasColour = "black"

picX = canvasWidth/2
picY = canvasHeight/2       # 캔버스의 중앙에 위치하도록 절반으로 나눔
picColour = "green"
lineWidth = 5
lineLength = 5




def picmoveUp(event) : # event = 버튼이 클릭되는것 같은 일이 발생되는것
    global picY
    canvas.create_line(picX, picY, picX, (picY-lineLength), width = lineWidth, fill = picColour)
    picY = picY - lineLength

def picmoveDown(event) :
    global picY
    canvas.create_line(picX, picY, picX, (picY+lineLength), width = lineWidth, fill = picColour)
    picY = picY + lineLength
    
def picmoveRight(event) :
    global picX
    canvas.create_line(picX, picY, (picX+lineLength), picY, width = lineWidth, fill = picColour)
    picX = picX +lineLength
    
def picmoveLeft(event) :
    global picX
    canvas.create_line(picX, picY, (picX-lineLength), picY, width = lineWidth, fill = picColour)
    picX = picX -lineLength



window = Tk()
window.title("MySketch")
canvas = Canvas(bg = canvasColour, height=canvasHeight, width = canvasWidth, highlightthickness=0)
canvas.pack()



window.bind("<Up>", picmoveUp)  #   .bind("이벤트", 함수)를 하면 이벤트가 발생할때 실행할 함수를 설정할 수 있다.
window.bind("<Down>", picmoveDown)
window.bind("<Right>", picmoveRight)
window.bind("<Left>", picmoveLeft)


    

window.mainloop()
