from PIL import ImageTk
from tkinter import Tk, Label, PhotoImage, Frame

import time
from lcd_pil import pilpointer
from lcd_tk import LCD
from lcd_pil_rev import lcd_pil

def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print (f.__name__, 'took', end - start, 'time')
        return result
    return f_timer

@timefunc
def pil(root,select,val):
    image=pilpointer(select,val)
    tki=ImageTk.PhotoImage(image)
    l=Label(root,image=tki)
    l.image=tki
    l.grid()

@timefunc
def tk(fr,select=4,colour='red',unit='Luminosity'):
    l1=LCD(fr,select=4,colour='red',unit='Luminosity')
    l1.grid(row=0,column=0,sticky='nsew')
    oldval=1023//2
    #val=100
    l1.lcd_pointer(val,oldval)

@timefunc
def pil_rev(root,lp,val):
    im=lp.pilpointer(val)
    tki=ImageTk.PhotoImage(im)
    l2=Label(root,image=tki)
    l2.image=tki
    l2.grid()

root=Tk()
fr=Frame(root)
fr.grid(row=0,column=0,sticky='nsew')
# select 1,2,3,4 -30:70,0:100,0:255,0:1023
select=4
# val value to be shown
val=100
res=pil(root,select,val)

result=tk(fr,select=4,colour='red',unit='Luminosity')

lp=lcd_pil(select)
pil_rev(root,lp,val)

root.mainloop()
'''
pil took 0.06304216384887695 time
tk took 0.024517536163330078 time
#######
pil took 0.0665440559387207 time
tk took 0.029016971588134766 time
pil_rev took 0.017513036727905273 time
'''