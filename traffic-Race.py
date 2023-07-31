from tkinter import *
from PIL import ImageTk,Image
from random import randint ,choice

   
width = 220
height = 100
window = Tk() # Create a window
window.title("Adarsh-Racing-Game") # S
window.iconbitmap(r'car.ico')

class start:
    def __init__(self):
       

        self.canvas = Canvas(window, width = 520, height = 800)
        self.canvas.pack()

        # Bind canvas with key events
        self.canvas.bind("<Up>", self.up)
        self.canvas.bind("<Down>", self.down)
        self.canvas.bind("<Left>", self.left)
        self.canvas.bind("<Right>", self.right)
        self.canvas.bind("<Button-1>", self.on)
        self.canvas.focus_set()
        self.x=55
        self.y=55

        self.img1=ImageTk.PhotoImage(Image.open('11.png').resize((60,100)))
        self.img22=ImageTk.PhotoImage(Image.open('22.png').resize((60,100)))
        self.img3=ImageTk.PhotoImage(Image.open('33.png').resize((60,100)))
        self.img4=ImageTk.PhotoImage(Image.open('44.png').resize((60,100)))
        self.img5=ImageTk.PhotoImage(Image.open('55.png').resize((70,120)))
        self.img6=ImageTk.PhotoImage(Image.open('66.png').resize((60,100)))
        self.img=ImageTk.PhotoImage(Image.open('car.png').resize((60,90)))
        self.car=self.canvas.create_image(270,700,anchor=NW,image=self.img,tags='car')
        self.img2=ImageTk.PhotoImage(Image.open('road.jpg').resize((520,540)))
        self.road=self.canvas.create_image(0,-400,anchor=NW,image=self.img2,tags='road')
        self.road=self.canvas.create_image(0,0,anchor=NW,image=self.img2,tags='road')
        self.road=self.canvas.create_image(0,500,anchor=NW,image=self.img2,tags='road')
        self.road=self.canvas.create_image(0,700,anchor=NW,image=self.img2,tags='road')
        self.canvas.lift('car')
        self.carscor=self.canvas.coords('car')
        '''
        self.first=self.canvas.create_rectangle(70,0,170,100,fill='red',tags='red')
        self.sec=self.canvas.create_rectangle(200,0,300,100,fill='green',tags='green')
        self.thr=self.canvas.create_rectangle(330,0,430,100,fill='blue',tags='blue')
        '''
        self.list1=[1,2,3,4,5,6]
        self.list2=[self.img1,self.img22,self.img3,self.img4,self.img5,self.img6]
        self.one=0
        self.last=100
        self.equation=[]
        self.tags=[]
        self.mainmark=0
        self.text=self.canvas.create_text(250,250,text= 'Start',fill='black',font=('Time',80),tags='start')
        
        self.text=self.canvas.create_text(430,50,text= 'Total-Score',fill='black',font=('Time',20),tags='total')
        self.score=self.canvas.create_text(430,100,text= '0',fill='White',font=('Time',20,'bold'),tags='score')
        
        self.key=1
        #self.motion()
        
    def up(self, event):
      if self.key==1:
        self.cord=self.canvas.coords('car')
        print(self.cord)
        if self.cord[1]>70:
        
        
            self.canvas.move('car',0,-90)
            self.carscor=self.canvas.coords('car')
            self.canvas.lift('car')
    def on(self, event):
        if  self.mainmark==0:
            self.canvas.move('car',0,0)
            self.carscor=self.canvas.coords('car')
            self.canvas.lift('car')
            self.canvas.delete('start')
            self.key=1
            self.canvas.delete('end')
            self.canvas.delete('cars')
            self.canvas.delete('car')
            self.car=self.canvas.create_image(270,700,anchor=NW,image=self.img,tags='car')
            self.equation=[]
            self.tags=[]
            self.one=0
            self.mainmark=1
            self.motion()
        

    def down(self, event):
      if self.key==1:
        self.cord=self.canvas.coords('car')
        print(self.cord)
        if self.cord[1]<700:
               self.canvas.move('car',0,90)
               self.carscor=self.canvas.coords('car')
               self.canvas.lift('car')
                

    def left(self, event):
     if self.key==1:
        self.cord=self.canvas.coords('car')
        print(self.cord)
        if self.cord[0]>0:
                self.canvas.move('car', -90,00)
                self.carscor=self.canvas.coords('car')
                self.canvas.lift('car')
        

    def right(self, event):
     if self.key==1:
        self.cord=self.canvas.coords('car')
        print(self.cord)
        if self.cord[0]<450:
            self.canvas.move('car', 90,00)
            self.carscor=self.canvas.coords('car')
            self.canvas.lift('car')
    def motion(self):
     self.canvas.delete('wow')
     if self.mainmark==0:
         self.text=self.canvas.create_text(250,450,text= 'Restart',fill='black',font=('Time',80),tags='start')
     if  self.mainmark:  
       
        
        
        self.one+=5
        self.canvas.itemconfigure('score',text=str(self.one))
       
        self.canvas.move('road',0,20)
        number=100;
        if self.one>5000:
            number=50
        if self.one>10000:
            number=25
        if self.one>50000:
            number=10
        if self.one%number==0:
            self.road=self.canvas.create_image(0,-400,anchor=NW,image=self.img2,tags='road')
            self.road=self.canvas.create_image(0,0,anchor=NW,image=self.img2,tags='road')
            self.road=self.canvas.create_image(0,500,anchor=NW,image=self.img2,tags='road')
            self.road=self.canvas.create_image(0,700,anchor=NW,image=self.img2,tags='road')
            
            self.canvas.lower('road')  
            val=choice(self.list1)
            iii=choice(self.list2)
           
            
            if val==1:
                tagg='1'+str(self.one)+'tag'
                self.cars=self.canvas.create_image(0,-30,anchor=NW,image=iii,tags=('cars',tagg))
               
                self.equation.append(tagg)
            if val==2:
                tagg='2'+str(self.one)+'tag'
                self.cars=self.canvas.create_image(90,-30,anchor=NW,image=iii,tags=('cars',tagg))
             
                self.equation.append(tagg)
            if val==3: 
                tagg='3'+str(self.one)+'tag'
                self.cars=self.canvas.create_image(180,-30,anchor=NW,image=iii,tags=('cars',tagg))
             
                self.equation.append(tagg)
            if val==4:
                tagg='4'+str(self.one)+'tag'
                self.cars=self.canvas.create_image(270,-30,anchor=NW,image=iii,tags=('cars',tagg))
             
                self.equation.append(tagg)
            if val==5:
                tagg='5'+str(self.one)+'tag'
                self.cars=self.canvas.create_image(360,-30,anchor=NW,image=iii,tags=('cars',tagg))
              
                self.equation.append(tagg)
            if val==6:  
                tagg='6'+str(self.one)+'tag'
                self.cars=self.canvas.create_image(450,-30,anchor=NW,image=iii,tags=('cars',tagg))
               
                self.equation.append(tagg)
           
       
        n=len(self.equation)
       # print(self.equation)
        
        for i in range(n):
            t=self.equation[i]
   
            
            tagval=self.canvas.coords(str(t))
           
            
           
             
           
            def linearSearch (expression, target):
             for i in range(len(expression)):
              
                   if (expression[i][0] == target):
                       return i
             return -1
         
         
            
            taga=t
              
            target = taga
            ans = linearSearch(self.tags, target)
          
            
           
            if(ans == -1):  
                 array1=[]
                 array1.append(str(t))
                 array1.append(tagval)
                 
                 self.tags.append(array1) 
              
            else: 
                 
                 xyz=self.tags[i][1][1] 
                # print(xyz)
                 if xyz<800:
                     array1=[]
                     array1.append(str(t))
                     array1.append(tagval)
                     self.tags[i]=array1
                
                  
                     
             
         
            
                         
                       
            
                
                
                
      
      #  print(self.tags)    
        length=len(self.tags)
        ppp=len(self.tags)
        for i in range(ppp):
            
            xyz=self.tags[i][1]
            self.carscor=self.canvas.coords('car')
           # print(self.carscor)
            
           
            
            #empty list
            sub_list = []
            
            #two lists are passed to zip 
            zip_object = zip( self.carscor,xyz)
            
            #loop to find diff of each element
            for list1_i, list2_i in zip_object:
                sub_list.append(list1_i - list2_i)
            
            x=sub_list[0]
            y=sub_list[1]
           # print(x)
          #  #print(y)
            
            if x==00 and y<100 and y>-90:
               # print('crash')
                qw='Total Score :- '+str(self.one)
                end=self.canvas.create_text(250,200,text= 'Game Over',fill='red',font=('Time',42),tags='end')
                end=self.canvas.create_text(250,300,text=qw ,fill='White',font=('Time',32,'bold'),tags='end')
                self.canvas.lift('end')
                self.key=0
                self.mainmark=0
             
        self.carscor=self.canvas.coords('car')
        timer=10
        if self.one>5000:
            timer=20
        if self.one>10000:
                timer=50
        if self.one>50000:
                timer=100
        self.canvas.lift('cars')
        self.canvas.move('cars',0,timer)
        
            
        self.canvas.lift('end')
        self.canvas.lift('final')
        self.canvas.after(10,self.motion)
     
mm=start()
window.mainloop()