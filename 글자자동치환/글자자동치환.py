from tkinter import *
from words import * #words 딕셔너리 가져오기  


#gui
win = Tk()  #창 생성
win.geometry("525x350")  #창의 크기
win.title("글자자동치환")     #창 제목
win.option_add("*Font", "나눔고딕 15")   #글꼴 설정
win.resizable(False, False) #창 크기 고정


#명령어
def clear(event) :
    #개행문자가 포함되어있었다~
    if upText.get(1.0,"end-1c") == "여기에 입력하세요":  
        upText.delete(1.0,END)


def default(event) :
    if upText.get(1.0,"end-1c")== "" :
        upText.insert(END,"여기에 입력하세요")

def convert() :
    
    #체크 안됐을 때
    if status.get() == 0 :
        temp = upText.get(1.0,"end-1c").split()

        for i in range(len(temp)) :
            for i2 in range(len(words)) :
                temp[i] = temp[i].replace(words[i2],words[i2]+"("+transWords[i2]+")")
        
        #아래쪽에 텍스트 추가        
        downText.delete(1.0,END)
        for i3 in range(len(temp)) :
            downText.insert(END,temp[i3]+" ")
            
            
    #체크 됐을 때
    if status.get() == 1 :
        temp = upText.get(1.0,"end-1c").split()

        for i in range(len(temp)) :
            for i2 in range(len(words)) :
                temp[i] = temp[i].replace(words[i2],transWords[i2])
        
        #아래쪽에 텍스트 추가        
        downText.delete(1.0,END)
        for i3 in range(len(temp)) :
            downText.insert(END,temp[i3]+" ")
    
    


            

###컴포넌트 생성

#상단 입력창
upText = Text(win, width=30, height=5)

#entry에서는 0, text에서는 0대신 END 사용 =(Tk.End)
upText.insert(END,"여기에 입력하세요")   
upText.bind("<Button-1>", clear)
upText.bind("<Leave>", default)
upText.pack()



#체크박스 상태 저장 0 or 1
status = IntVar()
##중앙체크박스
chk = Checkbutton(win, text="전부 번역",variable=status)
chk.pack()


#버튼 컴포넌트
b = Button(win,text="실행",command=convert)
b.pack()


#하단 변환된 텍스트
downText = Text(win, width=30, height=5)
downText.insert(END,"여기에 결과가 나옵니다")
downText.pack()


#디버깅
#print(status.get())

#창 실행
win.mainloop()