import tkinter as tk
from tkinter import *
from tkinter import filedialog
from time import time,sleep
import os
import pyperclip
import ctypes
#from base64fontinstall import *
from compressor import *
sys32 = ctypes.windll.user32

pgrnm = "CODE COMPRESSOR v.10"
uif = 'Saira SemiCondensed SemiBold'
cof = "menlo"
gc1 = "#23efbc"
gc2 = "#1eea7f"
gc3 = "#05342e"
gc4 = "#112537"
gc5 =  "#0c9c76"
gc6 = "#00705e"
gc7 = "#0f1426"
gc8 = "#000404"
gc9 = "#000003"
tgc1 = "#032a2b"
wc1 = "#fff"
wc2 = "#ddd"
wc3 = "#999"
twc1 = "#1e4255"
twc2 = "#204349"
twc3 = "#2f5366"
twc4 = "#316477"
rc1 = "#d40e2f"
rc2 = "#fe5060"
rc3 = "#500a20"
rc4 = "#4c0a1f"
bgc = "#010a0a"
hdc = gc1
blc = "#000000"


b1bg = bgc
b1fg = wc1
b1fo = ("arial",12)
b1w = 6
b1h = 1
b1px =10
b1py = 5

mw = Tk()
mw.title(pgrnm)
mw.configure(bg=bgc)
mw.minsize(width = 1200,height=720)
mw.maxsize(width = 1200,height=720)
mw.geometry('1200x720+'+str(int(sys32.GetSystemMetrics(0)/2 - 600))+"+"+str(int(sys32.GetSystemMetrics(1)/2 - 350)))
mw.overrideredirect(1)
mw.wm_attributes("-topmost", False)
mw.wm_attributes("-disabled", False)
mw.attributes('-alpha', 0.95)
def mwclose():
    mw.destroy()

hhh = 60
ttlbr = Frame(mw,width=1200,height=hhh,bg =bgc )
ttlbr.pack(expand=0, fill=X)

def move_window(event):
    closealert()
    mw.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
    
ttlbr.bind('<B1-Motion>', move_window) 
header = Frame(ttlbr,width=400,height=60,bg = rc3)
header.place(x=400,y=-10)
header.bind('<B1-Motion>', move_window)

trimg = PhotoImage(width=401,height=63,data=b'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')   
aiimg = PhotoImage(width=48,height=41,data=b'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')
climg = PhotoImage(width=122,height=63,data=b'iVBORw0KGgoAAAANSUhEUgAAAH4AAAA/CAMAAAAR+YxzAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAACHUExURQAAAEAAAEAAIFUAFVAQIE0NGkkJG1AIIE4HHE0NIEsMHUoLIE0JIEwMIEsLHkoLIE0KHkwJHk0LIE0KH0wKIEwJH00LH0wKIEsJH00LHkwKH0sKHkwKH0wKH0wKH0wJH0wKH0wKH0wKH0wJH0sKH0wKH0wKH0wKH0wKH0wKH0wKH0wKH0wKH9FL6ewAAAAsdFJOUwAECAwQFBwgJCgsMDhAREhMVGBkaGx0gIuPk5+rr7O/x8/T19/j5+vv8/f7mR1NdQAAAAlwSFlzAAAXEQAAFxEByibzPwAAAUhJREFUaEPt1zdyw0AQRFHQgBQFeoneG9AAuv/5lPx8G1Wt2kD78v7BZJPptj92e9KCMROjR047rFuyMZrSFuyYGO1IC6ZMjMou7bD8D04/oS3YMzHakhbMmBjdO7TD8icboxFtwYGJ0Ya0YM7E6NamHdZ7sfGph7QFRzZGa9KCbyZGF/30/Tcbn7qgLTixMVqRFiyYGF1atMMG/tNXn7TDWmc2RkvagiUTo3OD01dsfKoB7bDWhY3RgrZgxcToRFpQ1Gx83n3aYZFPv2ZidCQtGPpP/+rRDmvf2BjNaQs2TIwOpAUjJkZP/aHr3NkYzWgL4v7SEyZGZfqlJZF/6QcbozFtQfqlvRr80nEfuvRLezU4fdyHLv3SXk1+6bgP3X/+pQv/6d8ftMPSL+3V4JduX9kYfdEWpF/aq8EvHfehS7+0l3z6LPsFo/iFyKZI604AAAAASUVORK5CYII=')
climg2 = PhotoImage(width=122,height=63,data=b'iVBORw0KGgoAAAANSUhEUgAAAH4AAAA+CAMAAADapV/WAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAACTUExURQAAAL8AQN8AINUVK88QMNkNM9ULK9ESLtcQMNINLdUQMNYOLtUNL9MQMNYPMdUOLtMNL9YNMNUPLtUNMNUOL9MNLtUPL9QOL9MOMNQOL9QNL9UPMNQOL9QOL9QNMNMPL9QOL9QOL9MOLtQNL9QOL9MOL9QOL9QOL9QOL9QNL9QOL9QOL9QOL9QOL9QOL9QOL9QOLyYa9NYAAAAwdFJOUwAECAwQFBgcICgwODxAREhMUFRgbHR4fICDh4uTn6uvs7e7v8PHz9ff4+fr7/P3+/KCQuIAAAAJcEhZcwAAFxEAABcRAcom8z8AAAFDSURBVFhH7dfJUsJgFEThhEECiCKDogyiEUgMEN//6dycff+p6lQWybfvs7i7GwWb//kdaWuDnInRdURc2zNxWtLWXlg4fdLWhgUTo2JIXDswcVrQ1hYsnA60tdGViVE+IK4dmTjNaWtLFk572lpSw+mz8NOnTJxmtLUVC6cdbS25MTHK+sSl+MTEqJwS19ZMnLa0tfGdidGlR1xq+PQbJk4b2tqkZGJ0jolL8ZmJUTkhrn0wcXqlrU1rOP0p+PS9CxOj+5i4tmXitKatzVg4pbS1fsbE6JYQ13ZMnFa0tWcWTl+0tVY/dM3+0t1DZ1bhoavh9Hn46dv80DX8S3cPnVeFh+6HiVH5SFzrHjqv7qEL0vBD987E6Y221j10ZhUeuhpOnwafvtUP3RMLp2/aWvfQmVV46H6ZGBUPxLUmH7oo+gfydtCuqQO2+wAAAABJRU5ErkJggg==')

tr = Label(header,image=trimg,width=400,height=80,bg=bgc)
tr.place(x=0,y=-15)
tr.bind('<B1-Motion>', move_window) 

nmlb = Label(header,text="CODE  COMPRESSOR", bg = hdc, fg=blc,font=(uif, 18 ),width=16,height=1,anchor="w")
nmlb.place(x=130,y=14)
nmlb.bind('<B1-Motion>', move_window) 
aiim = Label(header,image=aiimg,width=48,height=41,bg=hdc)
aiim.place(x=70,y=12)
aiim.bind('<B1-Motion>', move_window)

clbtn = Button(mw,bd=0,anchor=S,relief="flat",
        font=(uif, 12 ),
        background=bgc, foreground=wc1,
        highlightbackground=bgc,highlightcolor=wc1,
        activebackground=bgc,activeforeground=wc1,
        image=climg,width=118,height=48,command=mwclose
        )
clbtn.place(x=795,y=0)
clbtn2 = Button(mw,bd=0,anchor=S,relief="flat",
        font=(uif, 12 ),justify=CENTER,
        background=rc4, foreground=rc1,
        highlightbackground=bgc,highlightcolor=wc1,
        activebackground=rc1,activeforeground=wc1,
        text="CLOSE",command=mwclose
        )
clbtn2.place(x=826,y=0)

def clsbtnhover(e):
    clbtn2['background'] = rc1
    clbtn2['foreground'] = wc1
    clbtn['image'] = climg2

def clsbtnhout(e):
    clbtn2['background'] = rc4
    clbtn2['foreground'] = rc1
    clbtn['image'] = climg

clbtn.bind("<Enter>",clsbtnhover)
clbtn.bind("<Leave>",clsbtnhout)
clbtn2.bind("<Enter>",clsbtnhover)
clbtn2.bind("<Leave>",clsbtnhout)

wb = 1
wbc = gc1
Frame(mw,width=1200,height=wb,bg = wbc).place(x=0,y=0)
Frame(mw,width=1200,height=wb,bg = wbc).place(x=0,y=720-wb)
Frame(mw,width=wb,height=720,bg = wbc).place(y=0,x=0)
Frame(mw,width=wb,height=720,bg = wbc).place(y=0,x=1200-wb)

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]
        self.bind("<Enter>", self.on_enterb1)
        self.bind("<Leave>", self.on_leaveb1)

    def on_enterb1(self, e):
        self['background'] = self['highlightbackground']
        self['foreground'] = self['highlightcolor']

    def on_leaveb1(self, e):
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground

class seloptcl(tk.Button):
    def __init__(self,master,**kw):
        tk.Button.__init__(self,master=master,**kw)
        self.abg = self['background']
        self.afg = self['foreground']

        self.bind("<Enter>", self.hover)
        self.bind("<Leave>", self.hout)
        self.bind("<Button-1>",self.clicked)

    def hover(self,e):
        self['background'] = self['highlightbackground']
        self['foreground'] = self['highlightcolor']

    def hout(self,e):
        self['background'] = self.abg
        self['foreground'] = self.afg

    def clicked(self,e):
        x = self['text']
        opsel['text'] = x
        if x=="J S":
            t2 = "O N"
            bg = resc['activebackground']
            fg = resc['activeforeground']
        else:
            t2 = "O F F";
            bg = resc['highlightbackground']
            fg = resc['highlightcolor']
        resc['background'] = bg
        resc['foreground'] = fg
        resc['text'] = t2
        clsselfn()

def selopt(txt,y,com=None,tp=0,pr=mw):
    st = {0:{"bg":twc1,"fg":wc2,"hbg":twc4,"hfg":gc1,"abg":gc1,"afg":wc1},1:{"bg":gc6,"fg":wc2,"hbg":gc1,"hfg":wc1,"abg":gc2,"afg":bgc},2:{"bg":rc3,"fg":rc1,"hbg":rc2,"hfg":wc1,"abg":rc1,"afg":wc1}
    }
    st = st[0]
    btn = seloptcl(pr, text=txt, font=(uif, 12 ),width=15, height=1,justify=CENTER,bd = 0,relief="flat",
        background=st["bg"], foreground=st["fg"], highlightbackground=st["hbg"],highlightcolor=st["hfg"],
        activebackground=st["abg"],activeforeground=st["afg"])
    btn.place(x=-230,y=y)
    return btn

def opnselfn():
    cssbt.place(x=230)
    jsbt.place(x=230)
    phpbt.place(x=230)
    htmlbt.place(x=230)
    closealert()

def clsselfn():
    cssbt.place(x=-230)
    jsbt.place(x=-230)
    phpbt.place(x=-230)
    htmlbt.place(x=-230)

class Tglbutn(tk.Button):
    def __init__(self,master,**kw):
        tk.Button.__init__(self,master=master,**kw)        
        self.bind("<Button-1>",self.clicked)

    def clicked(self,e):
        t2 = "O N"
        bg = self['activebackground']
        fg = self['activeforeground']
        if("O N"==self['text']):
            t2 = "O F F";
            bg = self['highlightbackground']
            fg = self['highlightcolor']
        self['background'] = bg
        self['foreground'] = fg
        self['text'] = t2
        closealert()
        clsselfn()

def addbtn(txt,x,y,com=None,tp=0,pr=mw):
	st = {0:{"bg":twc1,"fg":wc2,"hbg":twc4,"hfg":gc1,"abg":gc1,"afg":wc1},1:{"bg":gc6,"fg":wc2,"hbg":gc1,"hfg":wc1,"abg":gc2,"afg":bgc},2:{"bg":rc3,"fg":rc1,"hbg":rc2,"hfg":wc1,"abg":rc1,"afg":wc1}
	}
	st = st[tp]
	btn = HoverButton(pr, text=txt, command=com, font=(uif, 11 ),width=16, height=1,justify=CENTER,bd = 0,relief="flat",
		background=st["bg"], foreground=st["fg"], highlightbackground=st["hbg"],highlightcolor=st["hfg"],
		activebackground=st["abg"],activeforeground=st["afg"])
	btn.place(x=x,y=y)
	return btn

def addtgbtn(txt,x,y,tp=0,pr=mw):
	lb = Label(pr,text=txt,font=(uif, 10 ),width=20, height=1, anchor=W, bd = 0,relief="flat", bg=bgc, fg=wc3)
	lb.place(x=x,y=y)
	bg = twc2;
	fg=wc2;
	t = "O F F"
	if(tp):bg = gc5;fg=bgc;t = "O N"
	btn = Tglbutn(pr,text=t, font=(uif, 10 ),width=10, height=1,justify=CENTER,bd = 0,relief="flat",
		background=bg, foreground=fg, highlightbackground=twc2, highlightcolor=wc2, activebackground=gc5,activeforeground=bgc)
	btn.place(x=x,y=y+25);return btn;
        
def addtxtbox(x,y,tp=0,pr=mw):
    w=534
    h=480
    lb = Frame(pr,width=w, height=h,bg=tgc1)
    lb.place(x=x,y=y)
    btn = Text(lb, font=(cof, 10 ),width=62, height=13,bd = 0,relief="flat",background=bgc, foreground=wc2,padx=17,pady=10)
    btn.place(x=2,y=2)
    btn.config(spacing1=10)
    btn.config(spacing2=10)
    btn.config(spacing3=10)
    return btn
    
def gettxt(t):
    return (t.get("1.0",END))

def showalert(a,b=0):
    clsselfn()
    clsselfn()
    al['text'] = a
    alf.place(x=40,y=250)
    if(b):
        alf['height'] = 163
        al2['height'] = 3        
        if(b==1):alnxt.place(x=243,y = 100)
        else:alnxt2.place(x=243,y = 100)
    
def closealert():
    al['text'] = ""
    al2['height'] = 2
    alf['height'] = 112
    alf.place(x=40,y=-250)
    alnxt.place(x = -300, y=0)
    alnxt2.place(x = -300, y=0)

def tglbutnvl(b):
    x = b['text']
    if(x=="O N"):x = 1
    else:x= 0
    return x

notcompressed = ""
compressed = ""

def copy2():
    global compressed    
    closealert()
    clsselfn()
    pyperclip.copy(compressed)

def paste2():
    global notcompressed
    closealert()
    clsselfn()
    x = pyperclip.paste()
    notcompressed = x
    inptxt.delete("1.0",END);inptxt.insert("1.0",x)
    if tglbutnvl(atcm):
        cmpbtn()

sc0 = ["html","css","php"]
sc1 = ["js"]

def compress_with_ui(tx1,sc=0,insp=1,dp=1):
    global compressed
    if tx1:
        if insp:inptxt.delete("1.0",END);inptxt.insert("1.0",tx1)
        x = code_cmpr(tx1,sc)
        compressed = x
    if(dp):outtxt.delete("1.0",END);outtxt.insert("1.0",x)
    return x

def cmpbtn():
    global notcompressed
    closealert()
    clsselfn()
    f = open("CODE.txt","w+",encoding='utf-8')
    f.write(notcompressed)
    f.seek(0)   
    f1 =f.read()
    f.close()
    os.remove("CODE.txt")
    compress_with_ui(f1,tglbutnvl(resc),0)
    if tglbutnvl(atcl):copy2()
    if tglbutnvl(clwd):mwclose()

def cmpfile(fn):
    global sc0,sc1
    f = str(fn)
    ft = f.split(".")[len(f.split(".")) - 1].lower()
    sc = 0 
    if (ft in sc1): sc = 2
    elif (ft in sc0):sc = 1
    if(sc):
        sc-=1
        fl = open(f,"r",encoding='utf-8')
        flt = fl.read()
        fl.close()
        inptxt.delete("1.0",END);
        inptxt.insert("1.0",flt)
        nt = compress_with_ui(flt,sc)        
        f2 = open(f, "w",encoding='utf-8')
        f2.write(nt)
        f2.close()
        return 1

def cmpfilebtn1():
    clsselfn()
    closealert()
    showalert("FILE BACKUP BEFORE COMPRESS",1)

def cmpfilebtn():
    clsselfn()
    closealert()
    fn = filedialog.askopenfilename()
    global sc1,sc0
    if fn:
        f = str(fn)
        ft = f.split(".")[len(f.split(".")) - 1].lower()
        if (ft in sc0) or (ft in sc1):
            if(cmpfile(fn)):showalert("F I L E   C O M P R E S S E D")
        else:showalert("U N S U P P O R T E D   F I L E")   
    
def cmpfolderbtn1():
    closealert()
    clsselfn()
    showalert("FOLDER BACKUP BEFORE COMPRESS",2)

def cmpfolde():
    global sc0,sc1
    closealert()
    clsselfn()
    fd = filedialog.askdirectory()
    cprdc = 0
    if fd:
        for fn in os.listdir(fd):
            f = str(fn)
            ft = f.split(".")[len(f.split(".")) - 1].lower()
            if (ft in sc0) or (ft in sc1):
                if(cmpfile(fd+"/"+fn)):cprdc+=1
        if(cprdc):
            if cprdc==1:st = "ONE FILE"
            else:st = str(cprdc)+ " "+"FILES"
            showalert(st+ " "+"COMPRESSED")
        else:showalert("THEIR AREN'T SUPPORTED FILES",2)
        

addbtn("PASTE", 25,70,paste2)
opsel = addbtn("SELECT   FILE   TYPE", 226,70,opnselfn)
addbtn("COMPRESS", 427,70,cmpbtn)
addbtn("COPY", 640,70,copy2)
addbtn("BROWSE   FILE",839 ,70,cmpfilebtn1,1)
addbtn("BROWSE   FOLDER", 1038,70,cmpfolderbtn1,1)

resc = addtgbtn("ROW  END  SEMICOLAN",25,140)
atcm = addtgbtn("AUTO  COMPRESS",435,140)
atcl = addtgbtn("AUTO  COPY",640,140)
clwd =addtgbtn("CLOSE  WHEN  DONE",1050,140)

inptxt = addtxtbox(25,220)
outtxt = addtxtbox(640,220)
inptxt['background'] ="#000003"
inptxt['foreground'] = rc2
outtxt['background'] = "#000404"
outtxt['foreground'] = gc1

alf = Frame(mw,width=611,height=112,bg=gc1)
al2 = Label(alf,width=34, height=2,bg=gc8,fg=gc1,font=(uif, 25 ),justify=CENTER)
al2.place(x=25,y=2)
al = Label(alf,width=34, height=2,bg=gc8,fg=gc1,font=(uif, 25 ),justify=CENTER)
al.place(x=25,y=2)

alnxt = addbtn("N  E  X  T", -243,-110,cmpfilebtn,1,pr = alf)
alnxt2 = addbtn("N  E  X  T", -243,-110,cmpfolde,1,pr = alf)

cssbt = selopt("C S S",30)
jsbt = selopt("J S",70)
phpbt = selopt("P H P",110)
htmlbt = selopt("H T M L",150)

mw.mainloop()
