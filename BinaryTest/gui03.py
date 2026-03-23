import tkinter as tk
from tkinter import messagebox




def clicked():
    print("버튼을 클릭했네요?")
    input_value=entry.get().strip()
    if input_value == "":
        result_label.config(text = "입력된 값이 없습니다.", fg = "red")
        return
    try:
        if len(input_value) != 8:
            messagebox.showerror("에러", "8자리의 숫자를 입력해주세요")
            return
        elif not set(input_value).issubset({"0", "1"}): 
            messagebox.showerror("에러", "0과 1로만 입력해주세요")
            return
        result_label.config(text = f" 결과 : {int(input_value,2)}")
        
    except Exception as e:
        result_label.config(text = "숫자만 입력 가능합니다.", fg = "red")



if __name__ == "__main__" :
    root = tk.Tk()
    root.title("변환기")
    root.geometry("400x200")
    
    label = tk.Label(root, text="2 진수를 10진수로 변환")
    label.pack(pady=20)
    
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    entry.focus()
    
    btn = tk.Button(root, text="변환", command=clicked, width=10, bg="lightgray")
    btn.pack(pady=15)

    result_label = tk.Label(root, text="결과...")
    result_label.pack(pady=20)
    
    root.mainloop()
