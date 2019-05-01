

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import firstpage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    firstpage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    firstpage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("646x411")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.firstframe = tk.Frame(top)
        self.firstframe.place(relx=0.046, rely=0.049, relheight=0.912
                , relwidth=0.906)
        self.firstframe.configure(relief='groove')
        self.firstframe.configure(borderwidth="2")
        self.firstframe.configure(relief="groove")
        self.firstframe.configure(background="#61d4d8")
        self.firstframe.configure(width=585)

        self.PLACEMENT = tk.Label(self.firstframe)
        self.PLACEMENT.place(relx=0.068, rely=0.08, height=54, width=517)
        self.PLACEMENT.configure(background="#61d4d8")
        self.PLACEMENT.configure(disabledforeground="#a3a3a3")
        self.PLACEMENT.configure(font="-family {Sylfaen} -size 22 -weight bold")
        self.PLACEMENT.configure(foreground="#000000")
        self.PLACEMENT.configure(text='''PLACEMENT OFFICE DSATM''')

        self.loginas = tk.Label(self.firstframe)
        self.loginas.place(relx=0.12, rely=0.533, height=41, width=141)
        self.loginas.configure(background="#61d4d8")
        self.loginas.configure(disabledforeground="#a3a3a3")
        self.loginas.configure(font="-family {@Microsoft JhengHei UI} -size 16 -weight bold")
        self.loginas.configure(foreground="#000000")
        self.loginas.configure(text='''LOGIN AS:''')

        self.ADMIN = tk.Button(self.firstframe)
        self.ADMIN.place(relx=0.41, rely=0.533, height=33, width=81)
        self.ADMIN.configure(activebackground="#ececec")
        self.ADMIN.configure(activeforeground="#000000")
        self.ADMIN.configure(background="#d9d9d9")
        self.ADMIN.configure(disabledforeground="#a3a3a3")
        self.ADMIN.configure(foreground="#000000")
        self.ADMIN.configure(highlightbackground="#d9d9d9")
        self.ADMIN.configure(highlightcolor="black")
        self.ADMIN.configure(pady="0")
        self.ADMIN.configure(text='''ADMIN''')
        self.ADMIN.configure(width=81)

        self.STUDENT = tk.Button(self.firstframe)
        self.STUDENT.place(relx=0.598, rely=0.533, height=33, width=76)
        self.STUDENT.configure(activebackground="#ececec")
        self.STUDENT.configure(activeforeground="#000000")
        self.STUDENT.configure(background="#d9d9d9")
        self.STUDENT.configure(disabledforeground="#a3a3a3")
        self.STUDENT.configure(foreground="#000000")
        self.STUDENT.configure(highlightbackground="#d9d9d9")
        self.STUDENT.configure(highlightcolor="black")
        self.STUDENT.configure(pady="0")
        self.STUDENT.configure(text='''STUDENT''')

if __name__ == '__main__':
    vp_start_gui()





