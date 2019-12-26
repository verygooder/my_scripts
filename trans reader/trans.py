import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
from caiyun import Translator
import json


class App(tk.Tk):
    """docstring for App"""

    def __init__(self):
        super().__init__()
        self.title("trans reader")
        # self.geometry("600x600")
        self.resizable = False
        self.config(background='gray')
        self.translator = Translator()
        self.setupUI()

    def setupUI(self):
        # menu
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.markmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label="open file", command=self.load_file)
        self.menubar.add_cascade(label='Save', menu=self.markmenu)
        self.markmenu.add_command(label="save marker", command=self.save_marker)
        # function area
        self.reader = scrolledtext.ScrolledText(self, width=60, height=30, wrap=tk.WORD)
        self.click_trans = tk.Button(self, text='translate', command=self.trans_and_show)
        self.shower = scrolledtext.ScrolledText(self, width=60, height=5)
        # pack
        self.config(menu=self.menubar)
        self.reader.pack()
        self.click_trans.pack()
        self.shower.pack()

        # test
        self.test_button = tk.Button(self, text='test', command=self.test)
        self.test_button.pack()

    def trans_and_show(self):
        self.shower.delete(1.0, tk.END)
        select_text = self.reader.selection_get()
        if select_text:
            trans_text = self.translator.trans_paragraph(select_text)
            self.shower.insert(1.0, trans_text)

    def load_file(self):
        target_file = filedialog.askopenfile(title='open txt file', filetypes=[("文本文件", "*.txt")])
        self.filename = target_file.name
        data = target_file.read()
        self.reader.delete(1.0, tk.END)
        self.reader.insert(1.0, data)
        # load bookmark
        with open('./history/history.txt', 'r') as f:
            history = f.read()
            history = json.loads(history)
        if self.filename in history:
            pos = history[self.filename]
        else:
            pos = '0.0'
        self.reader.mark_set('insert', pos)
        self.reader.see('insert')
        self.reader.configure(state='disabled')
        target_file.close()

    def save_marker(self):
        if self.filename:
            name = self.filename
            pos = self.reader.index(tk.INSERT)
            # load history and change
            with open('./history/history.txt', 'r') as f:
                history = f.read()
                history = json.loads(history)
            history[name] = pos
            # save changes
            with open('./history/history.txt', 'w') as f:
                save_content = json.dumps(history)
                f.write(save_content)

    def test(self):
        pos = self.reader.index(tk.INSERT)
        print(pos, type(pos))


if __name__ == '__main__':
    app = App()
    app.mainloop()
