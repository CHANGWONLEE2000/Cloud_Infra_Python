# BinaryTest/gui02.py

# ui ToolKit 을 사용할수 있는 interface 객체 import 하기 
import tkinter as tk
from tkinter import messagebox

def clicked():
    print("버튼을 클릭했네요?")
    # Entry(입력창) 에 입력한 문자열 읽어오기
    input_value=entry.get().strip() # 좌우 공백 제거 strip()
    # 빈값일 경우 안내 문구 
    if input_value == "":
        result_label.config(text = "입력된 값이 없습니다.", fg = "red")
        return
    try:
        if 0 <= int(input_value) <= 255:
            pass
        else:
            messagebox.showerror("에러", "0~255 사이의 숫자를 입력해 주세요.")
            return
        result_label.config(text = f" 결과 : {int(input_value):08b}")
    except Exception as e:
        result_label.config(text = "숫자만 입력 가능합니다.", fg = "red")
        
   

if __name__ == "__main__" :
    # root 창 생성
    root = tk.Tk()
    # 제목 설정 
    root.title("나의 App")
    # 창의 크기
    root.geometry("400x200")

    # 레이블
    label = tk.Label(root, text="10 진수를 2진수로 변환")
    # pady => padding y => y축 padding => 위아래 padding
    label.pack(pady=20)

    # 입력창 
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    entry.focus() # 포커스 주기

    # 버튼
    btn = tk.Button(root, text="변환", command=clicked, width=10, bg="lightgray")
    btn.pack(pady=15)

    result_label = tk.Label(root, text="결과...")
    result_label.pack(pady=20)

    # 창이 닫힐때 까지 무한 대기
    root.mainloop()
