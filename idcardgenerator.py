#coding:utf-8
import os
import Image as PImage
import ImageFont,ImageDraw
from Tkinter import * 
from ttk import *
from tkFileDialog import *
from tkMessageBox import *

if getattr(sys, 'frozen', None):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(__file__)


def generator():
    name = ename.get()
    sex = esex.get()
    nation = enation.get()
    year = eyear.get()
    mon = emon.get()
    day = eday.get()
    org = eorg.get()
    life = elife.get()
    addr = eaddr.get()
    idn = eidn.get()
    
    fname = askopenfilename(parent=root,initialdir=os.getcwd(),title=u'选择头像')
    #print fname
    im = PImage.open(os.path.join(base_dir, 'empty.png'))
    avatar = PImage.open(fname) #500x670

    name_font = ImageFont.truetype(os.path.join(base_dir,'hei.ttf'),72)
    other_font = ImageFont.truetype(os.path.join(base_dir,'hei.ttf'),60)
    bdate_font = ImageFont.truetype(os.path.join(base_dir,'fzhei.ttf'),60)
    id_font = ImageFont.truetype(os.path.join(base_dir,'ocrb10bt.ttf'),72)
    

    draw = ImageDraw.Draw(im)  
    draw.text((630,690),name, fill=(0,0,0),font=name_font)
    draw.text((630,840),sex, fill=(0,0,0),font=other_font)
    draw.text((1030,840),nation, fill=(0,0,0),font=other_font)
    draw.text((630,980),year, fill=(0,0,0),font=bdate_font)
    draw.text((950,980),mon, fill=(0,0,0),font=bdate_font)
    draw.text((1150,980),day, fill=(0,0,0),font=bdate_font)
    start = 0
    loc = 1120
    while start+11<len(addr):
        draw.text((630,loc),addr[start:start+11], fill=(0,0,0),font=other_font)
        start += 11
        loc += 100
    draw.text((630,loc),addr[start:], fill=(0,0,0),font=other_font)
    draw.text((950,1475),idn, fill=(0,0,0),font=id_font)
    draw.text((1050,2750),org, fill=(0,0,0),font=other_font)
    draw.text((1050,2895),life, fill=(0,0,0),font=other_font)

    im.paste(avatar,(1500,690),mask=avatar)

    im.save('color.png')
    im.convert('L').save('bw.png')

    showinfo(u'成功',u'文件已生成到目录下,黑白bw.png和彩色color.png')
    

root = Tk()
root.title(u'AIRobot身份证图片生成器')
#root.geometry('640x480')
root.resizable(width=False, height=False)
Label(root, text=u'姓名:').grid(row=0,column=0,sticky=W,padx=3,pady=3)
ename = Entry(root,width=8)
ename.grid(row=0,column=1,sticky=W,padx=3,pady=3)
Label(root, text=u'性别:').grid(row=0,column=2,sticky=W,padx=3,pady=3)
esex = Entry(root,width=8)
esex.grid(row=0,column=3,sticky=W,padx=3,pady=3)
Label(root, text=u'民族:').grid(row=0,column=4,sticky=W,padx=3,pady=3)
enation = Entry(root,width=8)
enation.grid(row=0,column=5,sticky=W,padx=3,pady=3)
Label(root, text=u'出生年:').grid(row=1,column=0,sticky=W,padx=3,pady=3)
eyear = Entry(root,width=8)
eyear.grid(row=1,column=1,sticky=W,padx=3,pady=3)
Label(root, text=u'月:').grid(row=1,column=2,sticky=W,padx=3,pady=3)
emon = Entry(root,width=8)
emon.grid(row=1,column=3,sticky=W,padx=3,pady=3)
Label(root, text=u'日:').grid(row=1,column=4,sticky=W,padx=3,pady=3)
eday = Entry(root,width=8)
eday.grid(row=1,column=5,sticky=W,padx=3,pady=3)
Label(root, text=u'住址:').grid(row=2,column=0,sticky=W,padx=3,pady=3)
eaddr = Entry(root,width=32)
eaddr.grid(row=2,column=1,sticky=W,padx=3,pady=3,columnspan=5)
Label(root, text=u'证件号码:').grid(row=3,column=0,sticky=W,padx=3,pady=3)
eidn = Entry(root,width=32)
eidn.grid(row=3,column=1,sticky=W,padx=3,pady=3,columnspan=5)
Label(root, text=u'签发机关:').grid(row=4,column=0,sticky=W,padx=3,pady=3)
eorg = Entry(root,width=32)
eorg.grid(row=4,column=1,sticky=W,padx=3,pady=3,columnspan=5)
Label(root, text=u'有效期限:').grid(row=5,column=0,sticky=W,padx=3,pady=3)
elife = Entry(root,width=32)
elife.grid(row=5,column=1,sticky=W,padx=3,pady=3,columnspan=5)
Button(root, text=u'生成',width=32,command=generator).grid(row=6,column=1,sticky=W,padx=3,pady=3,columnspan=4)

root.iconbitmap(os.path.join(base_dir,'ico.ico'))
root.mainloop()

