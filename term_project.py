import os
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox as messagebox


def quit_window(event=None):
    windows.quit()


def set_path():
    search_file(input_path.get(), 0)


def search_file(root_path, lst_idx):
    if lst_idx == 0:
        found_result_lstBox.delete(0, END)

    # 확장자 선택 안했을때 예외처리
    if found_extension.get() == '':
        messagebox.showerror("에러", "탐색 확장자를 설정해 주시오.")
        return

    if os.path.exists(root_path):
        files = os.listdir(root_path)
        for file in files:
            path = os.path.join(root_path, file)
            print(path)
            found_result_lstBox.insert(lst_idx, path)
            if os.path.isdir(path):
                search_file(path, lst_idx + 1)
            else:
                lst_idx += 1
    else:
        messagebox.showinfo("에러", "올바른 경로를 설정하시오.")
        return


windows = Tk()
windows.title("File_Manager")

# ---------------- 파일 검색 용 ------------
# 파일 확장자 설정
# 파일 확장자 선택을 위한 라디오 버튼
file_extension_frame = LabelFrame(text="Extension")
file_extension_frame.pack(side=RIGHT)

found_extension = StringVar()
txt_radioButton = Radiobutton(file_extension_frame, text="txt", value=".txt",
                              variable=found_extension)
jpg_radioButton = Radiobutton(file_extension_frame, text="jpg", value=".jpg",
                              variable=found_extension)
pptx_radioButton = Radiobutton(file_extension_frame, text="pptx", value=".pptx",
                               variable=found_extension)
txt_radioButton.pack()
jpg_radioButton.pack()
pptx_radioButton.pack()
# -------------------------------------------

# 탐색할 파일 입력 창

file_find_frame = Frame()
file_find_frame.pack(side=LEFT)
input_path = Entry(file_find_frame, width=50)
input_path.pack(side=LEFT)
find_button = Button(file_find_frame, text="찾기", command=set_path)
find_button.pack(side=RIGHT)

# 탐색 결과 리스트
found_result_lstBox = Listbox(selectmode='single', width=100)
found_result_lstBox.pack(side=BOTTOM)
found_result_lstBox.configure(background="skyblue", foreground="white", font='Aerial')

# 파일 삭제 기능

# 프로그램 종료 키워드
windows.bind("<Escape>", quit_window)
windows.mainloop()
