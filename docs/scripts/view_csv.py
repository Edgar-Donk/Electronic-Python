from tkinter import Tk, StringVar, font
from tkinter.ttk import Frame, Treeview , Label, Scrollbar, Style, Entry, Combobox, Notebook
import csv
from glob import glob
from tree import Tree

'''Loads treeview to view tables

    Tables are in csv format to be viewed as multicolumn data.
    Select required table from combobox field
    Delimiters are assumed to be "$",";" or ","
'''
ret='$'
def csvSel(event):
    global ret
    #print(csv_value.get())
    with open(csv_value.get()) as f:
        first_line = f.readline()
        print(first_line)
    if "$" in first_line:
        csvDelimiter="$"
    elif ";" in first_line:
        csvDelimiter=";"
    else:
        csvDelimiter = ','
    ret=csvDelimiter
    #print('csvSel',csv_value.get(),csvDelimiter)
    #Tree(page2,csv_value.get(),csvDelimiter) #,renew=True

def on_tab_changed(event):
        event.widget.update_idletasks()
        tab = event.widget.nametowidget(event.widget.select())
        event.widget.configure(height=tab.winfo_reqheight(),width=tab.winfo_reqwidth())

root = Tk()
root.wm_title("Arduino Tables")
root.wm_iconbitmap('../_static/ben1.ico')
root.geometry('+170+200')
s = Style()
s.theme_use('clam')

csvDelimiter = '$'
fr = Frame(root)
fr.pack(fill='both',expand=1)

nb = Notebook(fr)
nb.pack(fill='both', padx=2, pady=3,expand=1)
nb.bind("<<NotebookTabChanged>>", on_tab_changed)
nb.enable_traversal()

page1 = Frame(nb)
csvfiles = []
for file in glob("../csv/*.csv"):
    csvfiles.append(file)
#csv_value = StringVar()
#cb = Combobox(page1, values=csvfiles, state="readonly",
              #textvariable=csv_value, width=30)
#cb.set(csvfiles[0])
#cb.grid(column=0, row=1)
#cb.bind('<<ComboboxSelected>>', csvSel)

nb.add(page1, text="Commands",underline=0,sticky='ns',)

Tree(page1,csvfiles[0],'$')

page2=Frame(nb, name='page2')
Tree(page2,csvfiles[2],';')
nb.add(page2, text="Pin Numbers",underline=0)

page3 = Frame(nb, name='page3')
#print('ret',ret,csv_value.get(),'csv_value.get()')
Tree(page3,csvfiles[1],',')

nb.add(page3, text="Interrupt Numbers",sticky='ew',underline=0)

if __name__ == "__main__":
    fr.mainloop()
