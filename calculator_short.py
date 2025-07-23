
import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title('Scientific Calculator')
        self.root.configure(bg='#0000FF')
        self.root.resizable(False, False)
        self.current = ''
        self.inp_value = True

        self.entry = tk.Entry(root, bg='#ADD8E6', fg='#000080', font=('Arial', 25), borderwidth=10, justify="right")
        self.entry.grid(row=0, columnspan=10, padx=10, pady=10, sticky='nsew')
        self.entry.insert(0, '0')

    def update_entry(self, val): self.entry.delete(0, 'end'); self.entry.insert(0, val)
    def get_val(self): return self.entry.get()

    def enter_num(self, num):
        self.current = str(num) if self.inp_value else self.get_val() + str(num)
        self.inp_value = False
        self.update_entry(self.current)

    def operate(self, val):
        try:
            self.update_entry(str(eval(self.get_val()))) if val == '=' else self.update_entry(self.get_val()+val)
        except: self.update_entry('Error')
        self.inp_value = False

    def clear(self): self.inp_value = True; self.current = '0'; self.update_entry('0')

    def apply_func(self, func):
        try: self.update_entry(func(float(self.get_val())))
        except: self.update_entry('Error')

    def build_buttons(self):
        FONT = ('Arial', 10, 'bold')
        nums = "789456123"
        i = 0
        for r in range(2, 5):
            for c in range(3):
                b = tk.Button(self.root, text=nums[i], font=FONT, fg="red", width=6, height=2,
                              highlightbackground='#ADD8E6', highlightthickness=2,
                              command=lambda x=nums[i]: self.enter_num(x))
                b.grid(row=r, column=c, sticky='nsew', padx=10, pady=10)
                i += 1

        ops = {
            'CE': self.clear, '√': lambda: self.apply_func(math.sqrt),
            '+': lambda: self.operate('+'), '-': lambda: self.operate('-'),
            '*': lambda: self.operate('*'), '/': lambda: self.operate('/'),
            '=': lambda: self.operate('='), '.': lambda: self.operate('.'),
            '0': lambda: self.enter_num('0'), 'π': lambda: self.update_entry(math.pi),
            'e': lambda: self.update_entry(math.e), 'Deg': lambda: self.apply_func(math.degrees),
            'Rad': lambda: self.apply_func(math.radians), 'Exp': lambda: self.apply_func(math.exp),
            'x!': lambda: self.apply_func(math.factorial), 'sin': lambda: self.apply_func(lambda x: math.sin(math.radians(x))),
            'cos': lambda: self.apply_func(lambda x: math.cos(math.radians(x))),
            'tan': lambda: self.apply_func(lambda x: math.tan(math.radians(x))),
            'sinh': lambda: self.apply_func(lambda x: math.sinh(math.radians(x))),
            'cosh': lambda: self.apply_func(lambda x: math.cosh(math.radians(x))),
            'tanh': lambda: self.apply_func(lambda x: math.tanh(math.radians(x))),
            'ln': lambda: self.apply_func(math.log), 'log2': lambda: self.apply_func(math.log2),
            'log10': lambda: self.apply_func(math.log10), 'x²': lambda: self.apply_func(lambda x: x**2),
            'x³': lambda: self.apply_func(lambda x: x**3), '10ⁿ': lambda: self.apply_func(lambda x: 10**x),
            '1/x': lambda: self.apply_func(lambda x: 1/x), 'Abs': lambda: self.apply_func(abs)
        }

        positions = [
            ('CE', 1, 0, 2), ('√', 1, 2), ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3), ('0', 5, 0, 2),
            ('.', 5, 2), ('=', 5, 3), ('π', 1, 4), ('e', 1, 5), ('Deg', 1, 6), ('Exp', 2, 4), ('x!', 2, 5),
            ('Rad', 2, 6), ('sin', 3, 4), ('cos', 3, 5), ('tan', 3, 6), ('sinh', 4, 4), ('cosh', 4, 5),
            ('tanh', 4, 6), ('ln', 5, 4), ('log2', 5, 5), ('log10', 5, 6), ('x²', 1, 7), ('x³', 2, 7),
            ('10ⁿ', 3, 7), ('1/x', 4, 7), ('Abs', 5, 7)
        ]

        for (text, r, c, cs) in [(*p, 1) if len(p) == 3 else p for p in positions]:
            b = tk.Button(self.root, text=text, font=FONT, width=5, height=2, fg="#000000",
                          highlightbackground='#ADD8E6', highlightthickness=2, command=ops[text])
            b.grid(row=r, column=c, columnspan=cs, sticky='nsew', padx=10, pady=10)

if __name__ == '__main__':
    root = tk.Tk()
    app = Calculator(root)
    app.build_buttons()
    root.mainloop()
