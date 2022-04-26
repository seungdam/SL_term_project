import tkinter


def exit(event=None):
    windows.quit()


windows = tkinter.Tk()
windows.title("File_Manager")

windows.bind("<Escape>", exit)
windows.mainloop()
