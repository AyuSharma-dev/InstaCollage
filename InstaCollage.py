from tkinter import *
from tkinter import filedialog
import os
from PIL import Image,ImageTk,ImageFilter
import random as rnd
from tkinter import colorchooser
import re


class pictures():
    
    def fileinfo(self,win):
        global p,Img_list,s
        s = []
        a = []
        Img_list=[]
        files = filedialog.askdirectory()
        p = os.listdir(files)
        for i in range(len(p)):
            
                a.append(files+'/'+str(p[i]))
                if re.search('.jpg$',a[i]) or re.search('.png$',a[i]):
                    locals()['img'+str(i)]=Image.open(a[i])
                    Img_list.append(locals()['img'+str(i)])
                else:
                    pass
       
    def show(self,win):
        global Img_list,s,imgg,V
        G = 1
        c = []
        d = []
        img_list = [i for i in range(len(Img_list))]
        r,g,b = 0,0,0
        imgg = Image.new("RGBA",(1400,780),(0,0,0,92))  
        for i in range(len(Img_list)):
            x = rnd.randrange(-20,1300)
            y = rnd.randrange(-20,760)
            if 10>G>0:
                w = rnd.randrange(600,800)
                h = rnd.randrange(600,800)
            elif 20>G>10:
                w = rnd.randrange(400,600)
                h = rnd.randrange(400,600)
            elif G>20:
                w = rnd.randrange(100,400)
                h = rnd.randrange(100,400)
            
            angle = rnd.randrange(0,10)        
        
            c.append(x)
            d.append(y)
            
            
            if x in c and y in d:
                x += 20
                
                y += 20
            
            if len(s)<= len(p):
                Img_list[i] = Img_list[i].rotate(angle,expand=1).resize((w,h))
                s.append(1)
                
            Img_list[i] = Img_list[i].convert('RGBA')
            r,g,b,a = Img_list[i].split()
            try:
                v = V
            except:
                v= 0
                
            if v==1:
                #Img_list[i] = Img_list[i].convert('cnyk')
                img_list[i] = Image.merge('RGBA',(b,g,r,a))
            if v==2:
                #Img_list[i] = Img_list[i].convert('L')
                img_list[i] = Image.merge('RGBA',(b,r,g,a))
            if v==3:
                img_list[i] = Image.merge('RGBA',(g,b,r,a))
            if v==4:
                img_list[i] = Image.merge('RGBA',(r,b,g,a))
            if v==0:
                img_list[i] = Image.merge('RGBA',(r,g,b,a))
            if angle%6==0:
                img_list[i] = Img_list[i].transpose(Image.FLIP_LEFT_RIGHT)
            imgg.paste(img_list[i],(x,y),img_list[i])
            G+=1
            
        
        
        #imgg.show()
        can = Canvases()
        can.printpic(win,imgg)
        
    def saveimage(self):
            global imgg
            filename = filedialog.asksaveasfilename()
            imgg.save(str(filename)+'.jpg','JPEG')
    
class buttons():

    #def button(self,win):
    def __init__(self,win): 
        to = IntVar()
        pic = pictures()
        can = Canvases()
        def direct():
            pic.fileinfo(win)
            pic.show(win)
            
        def T_again():
            pic.show(win)
        
        def backcolor():
            
            #color,colorr = colorchooser.askcolor()
            can.canvas(win,ask= True)
           
        def savefile():
            pic.saveimage()
        
        def tools(): 
            
            global V
            V = to.get()
        
        def undo():
            can.undoo()

        
#==============================================================================
        self.openff = Image.open('icons/open.png')
        self.save = Image.open('icons/save.png')
        self.undoo = Image.open('icons/ayush.png')
        self.rf = Image.open('icons/refresh.png')
        self.bbcolor = Image.open('icons/colors.png')
        self.openf2 = ImageTk.PhotoImage(self.openff)
        self.save = ImageTk.PhotoImage(self.save)
        self.undoo = ImageTk.PhotoImage(self.undoo)
        self.rf = ImageTk.PhotoImage(self.rf)
        self.bbcolor = ImageTk.PhotoImage(self.bbcolor)
        
        self.bgr = Image.open('icons/bgr.png')
        self.brg = Image.open('icons/brg.png')
        self.gbr = Image.open('icons/gbr.png')
        self.rbg = Image.open('icons/rbg.png')
        self.normal = Image.open('icons/normal.png')
        self.bgr = ImageTk.PhotoImage(self.bgr)
        self.brg = ImageTk.PhotoImage(self.brg)
        self.gbr = ImageTk.PhotoImage(self.gbr)
        self.rbg = ImageTk.PhotoImage(self.rbg)
        self.normal = ImageTk.PhotoImage(self.normal)
        


#         self.fb = PhotoImage('facebook.png')    
#         self.save = PhotoImage('save.png')    
#        self.openf = PhotoImage('open.png')    
#         self.undo = PhotoImage('udno.png') 
#         self.rf = PhotoImage('refresh.png')    
#         self.bbcolor = PhotoImage('colors.png')    
#==============================================================================
        button1 = Button(win,text = 'OPEN',image=self.openf2,bg = 'blue',bd=4,command = direct)
        button1.place(x = 20,y = 8)
        button2 = Button(win,text = 'SAVE',bg = 'pink',image = self.save,bd=4,command = savefile)
        button2.place(x = 80,y=8)
        button3 = Button(win,text='REFRESH',bg='red',image = self.rf,bd=4,height = 40,width = 40,command= T_again)
        button3.place(x = 200,y=8)
        button4 = Button(win,text = 'BACKGROUND',bg='aqua',image = self.bbcolor,height = 40,width = 40,bd=4,command= backcolor)
        button4.place(x = 260 ,y=8)
        button5 = Button(win,text = 'UNDO',bg='gold',image = self.undoo,bd=4,command= undo)
        button5.place(x = 140,y=8)
        
        
        Rbutton1 = Radiobutton(win,text='effect1',image= self.bgr,variable=to,value=1,bd=4,indicatoron=0,command=tools).place(x=900,y=8)
        Rbutton2 = Radiobutton(win,text='effect2',image= self.brg,variable=to,value=2,bd=4,indicatoron=0,command = tools).place(x=970,y=8)
        Rbutton3 = Radiobutton(win,text='effect3',image= self.gbr,variable=to,value=3,bd=4,indicatoron=0,command = tools).place(x=1040,y=8)
        Rbutton4 = Radiobutton(win,text='effetc4',image= self.rbg,bd=4,variable=to,value=4,indicatoron=0,command = tools).place(x=1110,y=8)
        Rbutton4 = Radiobutton(win,text='effetc4',image= self.normal,bd=4,variable=to,value=0,indicatoron=0,command = tools).place(x=1180,y=8)
       

class Canvases():
    
    
    def canvas(self,win,ask='False'):
        
        #global imgg
        global Plot,colorr
        if ask == True:
            color,colorr = colorchooser.askcolor()
        try:
            Plot = Canvas(win,bg=colorr,height = 760,width = 1400)
            Plot.place(x=0,y = 60)
        except:
            Plot = Canvas(win,bg='black',height = 760,width = 1400)
            Plot.place(x=0,y = 60)
        
        
    def printpic(self,win,imgg,clear = True):
        global Plot,colorr
        d = Plot.find_all()
        #Plot.config(bg = colorr)
        try:
            Plot.create_rectangle(0,0,1400,820,fill=colorr)
        except:
            Plot.create_rectangle(0,0,1400,820,fill='black')
        if len(d)>7:
            print('ayush')
            Plot.delete('all')
        
        
        #print('no')
        picc = Image.open('D:/images/gokuvegeta.jpg')
        image = ImageTk.PhotoImage(imgg)
        iss = Plot.create_image(650,330,image = image)
        
        win.mainloop()
    def undoo(self):
        global Plot
        c = Plot.find_all()
        if len(c) >0:
            Plot.delete(c[-1])
            Plot.delete(c[-2])

        
class main():
    def __init__(self):
        
        win = Tk()
        DspW = 1400
        DspH = 820
        
        win.geometry(str(DspW)+'x'+str(DspH)+'+100+100')
        win.title('Insta Collage')
        #tkinter.Tk.iconphoto
        
        win.iconbitmap('collage_maker.ico')
        but = buttons(win)
        #but.button(win)
        can = Canvases()
        can.canvas(win)
        
        win.mainloop()
        
if __name__ == '__main__':
    a = main()
