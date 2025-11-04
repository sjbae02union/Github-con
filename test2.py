# GUI 제작을 위한 기본 설정
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("메인 애플리케이션")
        self.root.geometry("800x600")
        
        # 메인 프레임 생성
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 제목 라벨
        self.title_label = ttk.Label(self.main_frame, text="GUI 애플리케이션", font=("Arial", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # 버튼들
        self.button1 = ttk.Button(self.main_frame, text="버튼 1", command=self.button1_click)
        self.button1.grid(row=1, column=0, padx=5, pady=5)
        
        self.button2 = ttk.Button(self.main_frame, text="버튼 2", command=self.button2_click)
        self.button2.grid(row=1, column=1, padx=5, pady=5)
        
    def button1_click(self):
        messagebox.showinfo("알림", "버튼 1이 클릭되었습니다!")
        
    def button2_click(self):
        messagebox.showinfo("알림", "버튼 2가 클릭되었습니다!")

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()