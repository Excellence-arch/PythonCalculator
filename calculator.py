from tkinter import Entry, Label, Button, Tk, Frame
from tkinter.messagebox import *
class Calculator:
	def __init__(self):
		self.root = Tk()
		self.root.config(bg='black')
		self.root.title("Calculator")
		self.root.iconbitmap('icons8_Calculator.ico')
		self.frame1 = Frame(self.root, bg='black')
		self.frame1.pack()
		self.screen = Entry(self.frame1, width=40, text="", background='gray50', foreground='white')
		self.screen.pack(side='left', ipady=13, pady=5)

		self.frame2 = Frame(self.root, bg='black')
		self.frame2.pack(pady=5)
		Button(self.frame2, width=7, bg='spring green', text="7", command=lambda: self.write("7")).pack(side='left', padx=5, ipady=10)
		Button(self.frame2, width=7, bg='spring green', text="8", command=lambda: self.write("8")).pack(side='left', padx=5, ipady=10)
		Button(self.frame2, width=7, bg='spring green', text="9", command=lambda: self.write("9")).pack(side='left', padx=5, ipady=10)
		Button(self.frame2, width=7, bg='spring green', text="+", command=self.add).pack(side='left', padx=5, ipady=10)

		self.frame3 = Frame(self.root, bg='black')
		self.frame3.pack(pady=3)
		Button(self.frame3, bg='spring green', width=7, text="4", command=lambda: self.write("4")).pack(side='left', padx=5, ipady=10)
		Button(self.frame3, bg='spring green', width=7, text="5", command=lambda: self.write("5")).pack(side='left', padx=5, ipady=10)
		Button(self.frame3, bg='spring green', width=7, text="6", command=lambda: self.write("6")).pack(side='left', padx=5, ipady=10)
		Button(self.frame3, bg='spring green', width=7, text="-", command=self.sub).pack(side='left', padx=5, ipady=10)

		self.frame4 = Frame(self.root, bg='black')
		self.frame4.pack(pady=5)
		Button(self.frame4, bg='spring green', width=7, text="1", command=lambda: self.write("1")).pack(side='left', padx=5, ipady=10)
		Button(self.frame4, bg='spring green', width=7, text="2", command=lambda: self.write("2")).pack(side='left', padx=5, ipady=10)
		Button(self.frame4, bg='spring green', width=7, text="3", command=lambda: self.write("3")).pack(side='left', padx=5, ipady=10)
		Button(self.frame4, bg='spring green', width=7, text="*", command=self.mul).pack(side='left', padx=5, ipady=10)

		self.frame5 = Frame(self.root, bg='black')
		self.frame5.pack(pady=5)
		Button(self.frame5, bg='orange red', width=7, text="C", command=self.clear).pack(side='left', padx=5, ipady=10)
		Button(self.frame5, bg='spring green', width=7, text="0", command=lambda: self.write("0")).pack(side='left', padx=5, ipady=10)
		Button(self.frame5, bg='spring green', width=7, text=".", command=lambda: self.write(".")).pack(side='left', padx=5, ipady=10)
		Button(self.frame5, bg='spring green', width=7, text="/", command=self.div).pack(side='left', padx=5, ipady=10)

		self.frame6 = Frame(self.root, bg='black')
		self.frame6.pack(pady=5)
		Button(self.frame6, width=37, bg='grey10', fg='snow', text="=", command=self.equal).pack(ipady=7)
		self.root.mainloop()

	def write(self, num):
		self.num = num
		inp = self.screen.get()
		num = inp+num
		self.screen.delete(0, len(inp))
		self.screen.insert(0, num)

	def clear(self):
		self.screen.delete(0, len(self.screen.get()))

	def equal(self):
		s_val = self.screen.get()
		s_num = s_val[1:]
		if s_val[0] == '+':
			addition = float(self.f_num) + float(s_num)
			self.screen.delete(0, len(self.screen.get()))
			self.screen.insert(0, str(addition))
		elif s_val[0] == '-':
			addition = float(self.f_num) - float(s_num)
			self.screen.delete(0, len(self.screen.get()))
			self.screen.insert(0, str(addition))
		elif s_val[0] == '/':
			try:
				addition = float(self.f_num) / float(s_num)
			except:
				addition = 'Math Error'
			self.screen.delete(0, len(self.screen.get()))
			self.screen.insert(0, str(addition))
		else:
			addition = float(self.f_num) * float(s_num)
			self.screen.delete(0, len(self.screen.get()))
			self.screen.insert(0, str(addition))

	def add(self):
		self.f_num = self.screen.get()
		self.screen.delete(0, len(self.screen.get()))
		self.screen.insert(0, '+')

	def sub(self):
		self.f_num = self.screen.get()
		self.screen.delete(0, len(self.screen.get()))
		self.screen.insert(0, '-')

	def mul(self):
		self.f_num = self.screen.get()
		self.screen.delete(0, len(self.screen.get()))
		self.screen.insert(0, '*')

	def div(self):
		self.f_num = self.screen.get()
		self.screen.delete(0, len(self.screen.get()))
		self.screen.insert(0,  '/')

start = Calculator()