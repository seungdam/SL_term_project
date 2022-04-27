import os
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText


def quit_window(event=None):
    windows.quit()


def set_path():
    search_file(input_path.get(), 0)


def search_file(root_path, lst_idx):
    found_result_lstBox.delete(0, END)
    files = os.listdir(root_path)
    for file in files:
        path = os.path.join(root_path, file)
        found_result_lstBox.insert(lst_idx, path)
        if os.path.isdir(path):
            search_file(path, lst_idx + 1)


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
pdf_radioButton = Radiobutton(file_extension_frame, text="pdf", value=".jpg",
                              variable=found_extension)
txt_radioButton.pack()
jpg_radioButton.pack()
pdf_radioButton.pack()
# -------------------------------------------

# 탐색할 파일 설정

file_find_frame = Frame()
file_find_frame.pack()
input_path = Entry(file_find_frame, width=30)
input_path.pack(side=LEFT)

find_button = Button(file_find_frame, text="찾기", command=set_path)
find_button.pack(side=RIGHT)

# 탐색 결과 리스트

found_result_lstBox = Listbox(selectmode='single', width=50)
found_result_lstBox.pack(side=BOTTOM)
windows.bind("<Escape>", quit_window)
windows.mainloop()
