import tkinter as tk
import sys


def clicked():
    print("클릭 이벤트 발생")
    num1 = int(name_entry.get())
    if 0 < num1 < 255:
        label2.config(text = f"입력한 수: {num1}")
        label3.config(text = f"2진수로 변환한 수: {num1:08b}")
    else:
        print("0~255사이로 입력해주세요")
        sys.exit()
        
        
        
if __name__ == "__main__" :
    
    root = tk.Tk()
    root.title("나의 APP")
    root.geometry("400x400")
    # 레이블
    label = tk.Label(root, text="안녕하세요! python GUI 입니다")
    label.pack(pady=20)
    # 입력창
    name_entry = tk.Entry(root, font = ("Arial", 12))
    name_entry.pack(pady = 5)
    name_entry.focus() #포커스주기
    # 버튼                             command <--- 함수 집어넣으면댐 버튼 이벤트발생시 함수호출
    btn = tk.Button(root, text="전송", command = clicked , width = 10, bg = "lightgray")
    btn.pack(pady = 15)
    label2 = tk.Label(root, text = "결과... ")
    label2.pack(pady = 20)
    label3 = tk.Label(root, text = "결과... ")
    label3.pack(pady = 20)
    #루프
    root.mainloop()