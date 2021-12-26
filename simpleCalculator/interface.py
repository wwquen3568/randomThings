from tkinter import *

#gui
def win() :   
    win = Tk()  #창 생성
    win.geometry("350x350")  #창의 크기
    win.title("계산기")     #창 제목
    win.option_add("*Font", "나눔고딕 15")   #글꼴 설정
    
    components(win)    #컴포넌트 추가(tkinter매개변수) - 버튼,레이블
    
    win.mainloop()  #창 실행


#컴포넌트 생성 및 설정
def components(win) :
    #계산 과정 창 
    visualbar = Label(win)
    visualbar.config(text = "계산현황")
    visualbar.grid(column=0, row=0, columnspan=4, padx=50, pady=10)

    #입력창
    userInput = Entry(win)
    userInput.config(justify = "center")
    userInput.grid(column=0, row=1, columnspan=4, padx=50, pady=10)

    #기록1
    log1 = Label(win)
    log1.config(text = "기록1")
    log1.grid(column=0, row=2, padx=20, pady=10)

    #기록2
    log2 = Label(win)
    log2.config(text = "기록2")
    log2.grid(column=0, row=3, padx=20, pady=10)

    #기록3
    log3 = Label(win)
    log3.config(text = "기록3")
    log3.grid(column=0, row=4, padx=20, pady=10)

    #기록1 값 불러오기
    getLog1 = Button(win)
    getLog1.config(width = 2, bg="yellow")
    getLog1.grid(column=1, row=2, padx=10, pady=10)

    #기록2 값 불러오기
    getLog1 = Button(win)
    getLog1.config(width = 2, bg="yellow")
    getLog1.grid(column=1, row=3, padx=10, pady=10)

    #기록3 값 불러오기
    getLog1 = Button(win)
    getLog1.config(width = 2, bg="yellow")
    getLog1.grid(column=1, row=4, padx=10, pady=10)

    #+버튼
    plus = Button(win)
    plus.config(text = "+",width = 3)
    plus.grid(column=2, row=2, padx=10, pady=10)

    #-버튼
    plus = Button(win)
    plus.config(text = "-",width = 3)
    plus.grid(column=3, row=2, padx=10, pady=10)

    #*버튼
    plus = Button(win)
    plus.config(text = "×",width = 3)
    plus.grid(column=3, row=3, padx=10, pady=10)

    #/버튼
    plus = Button(win)
    plus.config(text = "÷",width = 3)
    plus.grid(column=2, row=3, padx=10, pady=10)

    #=버튼
    plus = Button(win)
    plus.config(text = "=",width = 10)
    plus.grid(column=2, row=4,columnspan=3, padx=10, pady=10)
    
