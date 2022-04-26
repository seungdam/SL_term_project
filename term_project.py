import logging
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText


def quit_window(event=None):
    windows.quit()


def found_extension_value():
    logging.debug(found_extension.get())


windows = Tk()
windows.title("File_Manager")

# ---------------- 파일 검색 용 ------------
# 파일 확장자 설정
# 파일 확장자 선택을 위한 라디오 버튼

file_extension_frame = LabelFrame(text="Extension")
file_extension_frame.pack()

found_extension = StringVar()
txt_radioButton = Radiobutton(file_extension_frame, command=found_extension_value, text="txt", value=".txt",
                              variable=found_extension)
jpg_radioButton = Radiobutton(file_extension_frame, command=found_extension_value, text="jpg", value=".jpg",
                              variable=found_extension)
txt_radioButton.pack()
jpg_radioButton.pack()

windows.bind("<Escape>", quit_window)
windows.mainloop()
