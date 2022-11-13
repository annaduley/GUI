# This program creates labels in two different frames. 

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create two frames, one for the top of the
        # window, and one for the bottom.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window) 

        # Create three Label widgets for the
        # top frame.
        # these widgets are added to the self.top_frame widget
        # and not to the self.main_window widget
        
        self.label1 = tkinter.Label(self.top_frame,
                                    text='Winken')
        self.label2 = tkinter.Label(self.top_frame,
                                    text='Blinken')
        self.label3 = tkinter.Label(self.top_frame,
                                    text='Nod')

        # Pack the labels that are in the top frame.
        # Use the side='top' argument to stack them
        # one on top of the other.
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        # Create three Label widgets for the
        # bottom frame.
        self.label4 = tkinter.Label(self.bottom_frame,
                                    text='Winken')
        self.label5 = tkinter.Label(self.bottom_frame,
                                    text='Blinken')
        self.label6 = tkinter.Label(self.bottom_frame,
                                    text='Nod')


        # Pack the labels that are in the bottom frame.
        # Use the side='left' argument to arrange them
        # horizontally from the left of the frame.
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')


        # Create a Button widget. The text 'Click Me!'
        # should appear on the face of the Button. The
        # do_something method should be executed when
        # the user clicks the Button.
        self.my_button = tkinter.Button(self.main_window,text='Click Me!',command=self.do_something)

        
        # Pack the 'click me' button.
        self.my_button.pack(side='right')




        self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)

        # what happens if you change it from main_window.destroy to bottom_frame.destroy?
        #self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.bottom_frame.destroy)

        


        # Pack the 'quit' button
        self.quit_button.pack(side='right')

        

        # Yes, we have to pack the frames too!
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()



    def do_something(self):
        # Display an info dialog box.

        tkinter.messagebox.showinfo('Response','Thanks for clicking the button.')


       

# Create an instance of the MyGUI class.
my_gui = MyGUI()

