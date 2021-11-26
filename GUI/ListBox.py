import tkinter as tk


root = tk.Tk()
root.title('BaiGame')

root.title('test')
root.geometry('400x300')
td = {
    "hong": 1,
    "hou": 2,
    "he": 3
}
lb = tk.Listbox(root)
for i in td:
    print(i)
    lb.insert('end', i)
lb.pack()

var1 = tk.StringVar()
l = tk.Label(root, bg='green', fg='yellow', font=('Arial', 12), width=10, textvariable=var1)
l.pack()

def print_selection():
    key = lb.get(lb.curselection())
    var1.set(td[key])

btn = tk.Button(root, text='print value', width=15, height=2, command=print_selection)
btn.pack()
root.mainloop()