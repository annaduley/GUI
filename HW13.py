import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('700x300')
        self.main_window.title('Pizza To-Go Order')

        self.topframe = tkinter.Frame(self.main_window)
        self.topframe2 = tkinter.Frame(self.main_window)
        self.middleframe = tkinter.Frame(self.main_window)
        self.middleframe2 = tkinter.Frame(self.main_window)
        self.middleframe3 = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

 

        self.prompt_label = tkinter.Label(self.topframe,text='Please enter your email:')
        self.prompt_label.pack(side='left')
        self.email_entry = tkinter.Entry(self.topframe,width=10)
        self.email_entry.pack(side='left')


        self.label1 = tkinter.Label(self.middleframe, text='\n\nSelect your sauce:')
        self.label1.pack()

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
        

        self.rb1 = tkinter.Radiobutton(self.middleframe, text='Marinara $10', variable=self.radio_var, value=10)
        self.rb2 = tkinter.Radiobutton(self.middleframe, text='Alfredo $11', variable=self.radio_var, value=11)
        self.rb3 = tkinter.Radiobutton(self.middleframe, text='BBQ Sauce $12', variable=self.radio_var, value=12)


        
        self.rb1.pack(side='left')
        self.rb2.pack(side='left')
        self.rb3.pack(side='left')



        self.label2 = tkinter.Label(self.topframe2, text='\n\nSelect your toppings:')
        self.label2.pack()



        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        self.cb_var8 = tkinter.IntVar()
        self.cb_var9 = tkinter.IntVar()
        
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        self.cb_var8.set(0)
        self.cb_var9.set(0)
        
        self.cb1 = tkinter.Checkbutton(self.middleframe2,
                                       text='Pepperoni $1.50',
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.middleframe2,
                                       text='Sausage $1.50',
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.middleframe2,
                                       text='Bacon $1.50',
                                       variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.middleframe2,
                                       text='Ham $1.50',
                                       variable=self.cb_var4)

        self.cb5 = tkinter.Checkbutton(self.middleframe3,
                                       text='Onions $1.00',
                                       variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.middleframe3,
                                       text='Mushrooms $1.00',
                                       variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.middleframe3,
                                       text='Olives $1.00',
                                       variable=self.cb_var7)

        self.cb8 = tkinter.Checkbutton(self.middleframe3,
                                       text='Bell Peppers $1.00',
                                       variable=self.cb_var8)
        self.cb9 = tkinter.Checkbutton(self.middleframe3,
                                       text='Pineapple $1.00',
                                       variable=self.cb_var9)
        # Pack the Checkbuttons.
        self.cb1.pack(side='left')
        self.cb2.pack(side='left')
        self.cb3.pack(side='left')
        self.cb4.pack(side='left')
        self.cb5.pack(side='left')
        self.cb6.pack(side='left')
        self.cb7.pack(side='left')
        self.cb8.pack(side='left')
        self.cb9.pack(side='left')



        self.topframe.pack()
        self.middleframe.pack()
        self.topframe2.pack()
        self.middleframe2.pack()
        self.middleframe3.pack()
        self.bottomframe.pack()


        self.calc_button = tkinter.Button(self.main_window,text="Place Order", command=self.show_choice)
        self.quitbutton = tkinter.Button(self.main_window,text="Quit",command= self.main_window.destroy)

        
        self.calc_button.pack(side='bottom')
        self.quitbutton.pack(side='bottom')

        tkinter.mainloop()




    def show_choice(self):
        price = self.radio_var.get()
        if self.cb_var1.get() == 1:
            price += 1.50
        if self.cb_var2.get() == 1:
            price += 1.50
        if self.cb_var3.get() == 1:
            price += 1.50
        if self.cb_var4.get() == 1:
            price += 1.50
        if self.cb_var5.get() == 1:
            price += 1.00
        if self.cb_var6.get() == 1:
            price += 1.00
        if self.cb_var7.get() == 1:
            price += 1.00
        if self.cb_var8.get() == 1:
            price += 1.00
        if self.cb_var9.get() == 1:
            price += 1.00
        tkinter.messagebox.showinfo('Selection', 'Your order is placed. Your total will be $' +
                                    str(price))

myGUI = MyGUI()

