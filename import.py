# from binhex import openrsrc
# from curses import window
import json
import qrcode
import docx
# import tempfile
# import img2pdf
import qrcode.image.svg

# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPDF

#from PIL import Image
from tkinter import messagebox as mbox

# import win32api
# import win32print

from tkinter import *
from tkinter import filedialog
# from tkinter import ttk

# from tkinter.filedialog import askopenfilename
# from tkinter.messagebox import showerror
# from tkinter.messagebox import showinfo

import os

filepath = ''
imgpath = ''
# svgpath = ''
# pdfpath = ''




# Opening JSON file
def qr(filepath):
	f = open(filepath)
	data = json.load(f)
	# for i in data:
	# 	print(i)
	f.close()
	img=qrcode.make(data["SignedQRCode"])
	#os.startfile(imgpath, 'print')
	#img = img.resize((500, 500))
	global imgpath
	imgpath = filepath + '_qr.png'
	img.save(imgpath)

	doc = docx.Document()

	docpath = imgpath + ".docx"

	doc.add_picture(imgpath, width=docx.shared.Inches(2),height=docx.shared.Cm(5))
	doc.save(docpath)


	# method = "path"

	# if method == 'basic':
	# 	factory = qrcode.image.svg.SvgImage
	# elif method == 'fragment':
	# 	factory = qrcode.image.svg.SvgFragmentImage
	# elif method == 'path':
	# 	factory = qrcode.image.svg.SvgPathImage

	# row = data["SignedQRCode"]
	# img = qrcode.make(row, image_factory = factory)
	# global svgpath
	# svgpath = filepath + ".svg"
	# img.save(svgpath)
	# drawing = svg2rlg(svgpath)
	# global pdfpath
	# pdfpath = filepath + ".pdf"
	# renderPDF.drawToFile(drawing, pdfpath)

	# os.startfile(pdfpath, "print")
	answer = mbox.askyesnocancel ('Print','Do you want to print now? Cancel to "delete and exit"')
	print(answer)
	if(answer == True):
		os.startfile(docpath, "print")
	elif(answer == None):
		os.remove(docpath)
		os.remove(imgpath)
		exit()








def openFile():
	filepath = filedialog.askopenfilename(title="Locate the JSON file for E-Invoice",
	filetypes=(("JSON","*.json"),
	("all files","*.*")))
	#showinfo(title='Converting JSON to QR',message='Please Wait')
	#print(filepath)
	qr(filepath)




root = Tk()
root.title('Select JSON & Print QR-code')
l = Label(text='Select the JSON File ',bg='gray')
l.pack(fill=X)
btn_select = Button(text='Select File',width=15,bg='dark green',command=openFile).pack()
l1 = Label(text='')
l1.pack(fill=X)


# btn = Button(root,text='Print',width=15,command=locprinter).pack()
root.mainloop()







