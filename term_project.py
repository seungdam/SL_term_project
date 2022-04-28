import os
import re

from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText

import PIL.Image
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox

path_list = []
cnt = 0


def quit_window(event=None):
    windows.quit()


def set_path():
    search_file(input_path.get(), 0)


def remove_file():
    # 리스트 커서를 선택하지 않은 경우
    if not len(found_result_lstBox.curselection()):
        messagebox.showinfo("경고", " 리스트를 체크해 주세요")
        return
    remove_file_path = path_list[found_result_lstBox.curselection()[0]]
    if os.path.exists(remove_file_path):
        os.remove(remove_file_path)
        path_list.remove(remove_file_path)

    found_result_lstBox.delete(found_result_lstBox.curselection()[0], found_result_lstBox.curselection()[0])
    found_result_lstBox.update()


def set_preview():
    if not len(found_result_lstBox.curselection()):
        messagebox.showinfo("경고", " 리스트를 체크해 주세요")
        return
    preview_file_path = path_list[found_result_lstBox.curselection()[0]]
    if os.path.exists(preview_file_path):
        if re.search(".png", preview_file_path):
            print(preview_file_path)
            prev_img = Image.open(preview_file_path)
            resized_img = prev_img.resize((160, 160))
            photo = ImageTk.PhotoImage(resized_img)
            preview_label.configure(image=photo)
            preview_label.image = photo
        elif re.search(".txt", preview_file_path):
            prev_img = ImageTk.PhotoImage(Image.open(r"C:\Users\OH.S.D\Desktop\preview.png").resize((160, 160)))
            preview_label.configure(image=prev_img)
            preview_label.image = prev_img
            txt_read = open(preview_file_path, 'r')
            messagebox.showinfo("텍스트 파일 내용", txt_read.read())
            txt_read.close()

    else:
        return


def search_file(root_path, lst_idx):
    # 매 검색마다 리스트를 초기화 시켜줌
    if lst_idx == 0:
        path_list.clear()
        found_result_lstBox.delete(0, END)

    # 확장자 선택 안했을때 예외처리
    if found_extension.get() == '':
        messagebox.showerror("경고", "탐색 확장자를 설정해 주시오.")
        return

    if os.path.exists(root_path):
        files = os.listdir(root_path)
        for file in files:
            path = os.path.join(root_path, file)
            if re.search(found_extension.get(), path):
                found_result_lstBox.insert(lst_idx, os.path.basename(path))
                path_list.append(path)
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
file_extension_frame.pack(side=RIGHT, fill=BOTH)

found_extension = StringVar()
txt_radioButton = Radiobutton(file_extension_frame, text="txt", value=".txt",
                              variable=found_extension)

png_radioButton = Radiobutton(file_extension_frame, text="png", value=".png",
                              variable=found_extension)
txt_radioButton.pack()
png_radioButton.pack()
# -------------------------------------------

# 탐색할 파일 입력 창

file_find_frame = Frame()
file_find_frame.pack(side=TOP)
input_path = Entry(file_find_frame, width=50)
input_path.pack(side=LEFT)
find_button = Button(file_find_frame, text="찾기", command=set_path)
find_button.pack(side=RIGHT)

# 탐색 결과 리스트 위젯
result_frame = Frame()

found_result_lstBox = Listbox(selectmode='single', width=40)
found_result_lstBox.configure(background="skyblue", foreground="white", font='Aerial')
found_result_lstBox.pack(side=LEFT, fill=BOTH)

# 미리보기 위젯
img = ImageTk.PhotoImage(Image.open(r"C:\Users\OH.S.D\Desktop\preview.png").resize((160, 160)))
preview_label = Label(result_frame, image=img)
preview_label.configure(background="WHITE")
preview_label.pack(side=RIGHT, fill=BOTH)
result_frame.pack()

# 파일 삭제, 미리보기 버튼 기능
manipulate_btn_frame = LabelFrame(text="파일 작업")
delete_btn = Button(manipulate_btn_frame, text="삭제", command=remove_file)
delete_btn.pack(side=LEFT)
preview_btn = Button(manipulate_btn_frame, text="미리보기", command=set_preview)
preview_btn.pack(side=RIGHT)
manipulate_btn_frame.pack()


# 프로그램 종료 키워드
windows.bind("<Escape>", quit_window)
windows.mainloop()
