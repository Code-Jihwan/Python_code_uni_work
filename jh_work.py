import random
from cProfile import label
from tkinter import *
from pyrsistent import b
from sympy import root

root = Tk()ㅎ
root.title("근로내용")  # 타이틀 적기
root.geometry("700x400+600+300")  # 창 크기 설정(가로*세로 + x좌표 +y좌표)

# 라벨1
label = Label(root, text="근로내용 출력")
label.pack()

#라벨2
labe2 = Label(root, text="(한번 누르고 다시 고르고 싶으면, 초기화 누르고 다시 누르기!)")
labe2.pack()

#텍스트박스
txt = Text(root, width=85, height=4)
txt.pack()

#누르는 버튼의 기능
def workbtn():
  with open ('work.txt', "r") as f:
    r = list(f.readlines())
  pickRandomLine = random.choice(r).splitlines() [0] #랜덤하게 원소 하나 뽑음
  pickRandomLine2 = random.choice(r).splitlines() [0] #랜덤하게 원소 하나 뽑음

  txt.insert(END, pickRandomLine + ". " + pickRandomLine2)

  print("+----------------------------------------------------------------------------------------------------+")
  print("|                                          근로 내용                                                  ")
  print("|")
  print("| >> "+pickRandomLine +". "+ pickRandomLine2 +".")
  print("+----------------------------------------------------------------------------------------------------+")

#누르기 버튼
btn = Button(root, width=5, height=2, fg="blue", text="눌러봐", command=workbtn)    # padx, pady는 여백, width, height도 가능 # fg는 글자색, bg는 배경색
btn.pack()

#초기화 버튼 기능
def workbtn2():
  txt.delete("1.0", END)  #1 : 첫번째 라인, 0 : 0번째 column 위치

#초기화 버튼
btn2 = Button(root, width=5, height=2, fg="green", text="초기화", command=workbtn2)
btn2.pack()

#종료 버튼 기능
def workbtn3():
  root.destroy()

#종료 버튼
btn3 = Button(root, width=5, height=2, fg="red", text="종료", command=workbtn3)
btn3.pack()

root.mainloop()   #화면 유지 시키도록



  # with ... as 구문을 사용하게 되면 파일을 열고 해당 구문이 끝나면 자동으로 닫힘
  # with open(파일 경로, 모드) as 파일 객체: 
  # close함수가 없지만 with as 구문을 빠져나가게 되면 자동으로 close() 함수를 호출하여 파일을 닫음 (자동으로 close 객체 생성)
  # with as 를 쓰면 파일을 열고 자동으로 닫아준다

  # f 는 file object. open 메서드의 리턴 값

  # 줄 단위로 문자열을 변환하는 함수 splitlines()

  # (1) readline() - 파일의 한 줄을 가져와 문자열로 반환합니다. 파일 포인터는 그 다음줄로 이동합니다.
  # (2) readlines() - 파일 내용 전체를 가져와 리스트로 반환합니다. 각 줄은 문자열 형태로 리스트의 요소로 저장됩니다.
  # 예를들어 5줄짜리 파일을 readlines() 로 읽게 되면 문자열 5개를 요소로 갖는 리스트가 반환
  # (3) read() - 파일 내용 전체를 가져와 문자열로 반환합니다