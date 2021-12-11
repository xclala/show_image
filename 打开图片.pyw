try:
    from tkinter import *
    from tkinter import messagebox
    from threading import Thread
    from os import getcwd
    root = Tk()
    root.title("打开图片")
    root.geometry("1500x30")

    def on_closing():
        if messagebox.askokcancel("退出", "你确定要退出吗？"):
            root.destroy()

    def open_image():
        from cv2 import imread, imshow
        imshow(image.get(), imread(image.get()))

    class MyThread(Thread):

        def __init__(self, func, *args):
            super().__init__()
            self.func = func
            self.args = args
            self.setDaemon(True)
            self.start()

        def run(self):
            self.func(*self.args)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    Label(text='请把照片放在'+str(getcwd())).pack(side=LEFT)
    image = Entry()
    image.pack(side=LEFT, expand=True, fill=X)
    Button(text="打开", command=lambda :MyThread(open_image)).pack(side=RIGHT)
    mainloop()
except Exception as e:
    print(e)
