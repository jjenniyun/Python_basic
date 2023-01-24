import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("HY GUI")
root.geometry("640x360") # 가로 * 세로

values = [str(i)+"일" for i in range(1,32)] # 1~31까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최조 목록 제목 설정

read_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # 읽기 전용
read_combobox.current(0) # 0번쨰 인덱스 값 선택
read_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(read_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()