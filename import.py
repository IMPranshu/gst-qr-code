import json
import qrcode
import docx
import qrcode.image.svg

from tkinter import *
from tkinter import messagebox as mbox
from tkinter import filedialog

import os

filepath = ''
imgpath = ''


# Opening JSON file
def qr():
	f = open(filepath)
	data = json.load(f)
	# for i in data:
	# 	print(i)
	f.close()
	img=qrcode.make(data["SignedQRCode"])
	global imgpath
	imgpath = filepath + '_qr.png'
	img.save(imgpath)

	doc = docx.Document()

	docpath = imgpath + ".docx"

	doc.add_picture(imgpath, width=docx.shared.Inches(2),height=docx.shared.Cm(5))
	doc.save(docpath)
	answer = mbox.askyesnocancel ('Print','Do you want to print now? Cancel to "delete and exit"')
	print(answer)
	if(answer == True):
		os.startfile(docpath, "print")
	elif(answer == None):
		os.remove(docpath)
		os.remove(imgpath)
		exit()


def openFile():
	global filepath
	filepath = filedialog.askopenfilename(title="Locate the JSON file for E-Invoice",
	filetypes=(("JSON","*.json"),
	("all files","*.*")))
	qr()


root = Tk()
root.title('Select JSON & Print QR-code')
l = Label(text='Select the JSON File ',bg='gray')
l.pack(fill=X)
btn_select = Button(text='Select File',width=15,bg='dark green',command=openFile).pack()
l1 = Label(text='')
l1.pack(fill=X)
root.mainloop()







