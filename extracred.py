import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('300x200')
        self.main_window.title('InputBox Demo')



        self.firstframe = tkinter.Frame(self.main_window)
        self.topframe = tkinter.Frame(self.main_window)
        self.middleframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)


        self.Label1 = tkinter.Label(self.topframe,text='Enter the score for test 1:')
        self.Score1 = tkinter.Entry(self.topframe,width=10)


        self.Label1.pack(side='left')
        self.Score1.pack(side='left')

        self.Label3 = tkinter.Label(self.middleframe,text='Enter the score for test 2:')
        self.Score2= tkinter.Entry(self.middleframe,width=10)


        self.Label3.pack(side='left')
        self.Score2.pack(side='left')


        self.Label5 = tkinter.Label(self.bottomframe,text='Enter the score for test 3:')
        self.Score3 = tkinter.Entry(self.bottomframe,width=10)


        self.Label5.pack(side='left')
        self.Score3.pack(side='left')

        self.topframe.pack()
        self.middleframe.pack()
        self.bottomframe.pack()


        self.calcButton = tkinter.Button(self.main_window,text="Convert", command=self.do_something)
        self.quitbutton = tkinter.Button(self.main_window,text="Quit",command= self.main_window.destroy)

        self.calcButton.pack(side='left')
        self.quitbutton.pack(side='right')

        tkinter.mainloop()

    def do_something(self):
        avg=float((float(self.Score1.get()) + float(self.Score2.get()) + float(self.Score3.get()))/3)
        tkinter.messagebox.showinfo("Results",str(avg)+' is the average')
        tkinter.mainloop()





myGUI = MyGUI()

print('Hi there')