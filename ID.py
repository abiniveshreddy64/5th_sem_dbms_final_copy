from tkinter import *
from PIL import ImageFont,ImageTk, Image,ImageDraw
import pymysql,re,time,yagmail,random,sys,pyautogui
tit_font=ImageFont.truetype(r'F:\5th sem dbms mini project\Comfortaa-VariableFont_wght.ttf', 70)
connection = pymysql.connect(host="localhost",user="root",password="Chinnu@123",database="miniproject",autocommit=True)
a=re.compile('[\d]{1}[\w]{2}[\d]{2}[\w]{2}[\d]{3}')
em=re.compile('[\d]{1}[\w]{2}[\d]{2}[\w]{2}[\d]{3}[@bmsit.in]')
cur = connection.cursor()
yag = yagmail.SMTP("Tryingout64@gmail.com","raelgzgecldyogle")
#-----------------------------
choice=''
no=''
otp=''
usnn=''
f=''
table=''
count=3
usnn1=''
pa=''
bran=''
#-----------------------------
def goto(sen):
    if sen=='Welcome Student.....':
        starting1()
    elif sen=='Welcome Teacher.....':
        starting2()
    elif sen=='Loading Student Register Page.....':
        registering1()
    elif sen=='Loading Student Login Page.....':
        logging1()
    elif sen=='Loading Teacher Register Page.....':
        registering2()
    elif sen=='Loading Teacher Login Page.....':
        logging2()
    elif sen=='Student Registering.....':
        logging1()
    elif sen=='Teacher Registering.....':
        logging2()
    elif sen=='Student Logging in.....':
        start1(usnn)
    elif sen=='Teacher Logging in.....':
        start2(usnn)
    elif sen=='Enter USN.....':
        forgot("student","#02fac8","reg_student","usn")
    elif sen=='Enter ID.....':
        forgot("teacher",'#f0fc00',"reg_teacher","t_id")
    elif sen=='Student ID card created':
        one()
    elif sen=='Teacher ID card created':
        one()
#-----------------------------
def splash(sen,color):
    root=Tk()
    root.config(bg='black')
    root.overrideredirect(True)
    root.geometry('300x200')
    root.eval('tk::PlaceWindow . center')
    j=0
    l=[]
    fin=''
    for i in sen:
        fin+=i
        l.append(fin)
    def conti():
        global j
        if not j+1>len(l):
            l1.config(text=l[j])
            j+=1
            root.after(30,conti)
        else:
            root.after(1000)
            root.destroy()
            goto(sen)
    l1=Label(root,text='',bg='black',fg=color,font=(tit_font,15))
    l1.pack(ipady=80)
    root.after(300,conti)
    root.mainloop()

#----------------------------
def one():
    top = Tk()
    top.title("Welcome")
    #top.state('zoomed')
    top.attributes('-fullscreen', True)
    top.config(bg='black')
    frame1 = Frame(top)
    frame1.place(x=850,y=180)
    img1 = ImageTk.PhotoImage((Image.open(r"F:\5th sem dbms mini project\education1.png")).resize((150,100)),master=top)
    label1 = Label(frame1,bg='black', image = img1)
    label1.pack()
    frame2 = Frame(top)
    frame2.place(x=850,y=340)
    img2 = ImageTk.PhotoImage((Image.open(r"F:\5th sem dbms mini project\teacher.png")).resize((150,100)),master=top)
    label2 = Label(frame2,bg='black', image = img2)
    label2.pack()
    top.title("WELCOME")
    top.geometry('1200x600')
    def but(x,y,text,fcolor,bcolor,w,h):
        def submit():
            global choice
            choice=text

            if choice == 'Student':
                global j,l,fin
                j=0
                l=[]
                fin=''
                top.destroy()
                top.after(1000,splash('Welcome Student.....','#00ffea'))
            elif choice == 'Teacher':
                #global j
                j=0
                l=[]
                fin=''
                top.destroy()
                top.after(1000,splash('Welcome Teacher.....','#ffff80'))
            else:
                j=0
                l=[]
                fin=''
                top.destroy()
                top.after(1000,splash('Thank You!!','red'))
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=w, height =h,activeforeground=bcolor,activebackground=fcolor,command=lambda:submit())
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(600,180,'Student','black','#99ebff',20,4)
    but(600,340,"Teacher",'black','#00ccff',20,4)
    but(1300,20,"X",'black','red',2,1)
    top.mainloop()
#---------------------
def starting1():
    start = Tk()
    #start.state('zoomed')
    start.attributes('-fullscreen', True)
    start.config(bg='black')
    start.title("WELCOME")
    start.geometry('1200x600')
    def but(x,y,text,fcolor,bcolor):
        def check():
            if choice=='Register':
                global j,l,fin
                j=0
                l=[]
                fin=''
                start.after(1000,splash('Loading Student Register Page.....','#00ffea'))
            elif choice=='Login':
                j=0
                l=[]
                fin=''
                start.after(1000,splash('Loading Student Login Page.....','#00ffea'))
            else:
                start.destroy
                one()
        def submit():
            global choice
            choice=text
            start.destroy()
            check()
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(start,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:submit())
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(600,180,'Register','black','#02fac8')
    but(600,360,'Login','black','#02cdfa')
    but(600,540,'Back','black','#03a1fc')
    start.mainloop()
def starting2():
    start = Tk()
    #start.state('zoomed')
    start.attributes('-fullscreen', True)
    start.config(bg='black')
    start.title("WELCOME")
    start.geometry('1200x600')
    def but(x,y,text,fcolor,bcolor):
        def check():
            if choice=='Register':
                global j,l,fin
                j=0
                l=[]
                fin=''
                start.after(1000,splash('Loading Teacher Register Page.....','#ffff80'))
            elif choice=='Login':
                j=0
                l=[]
                fin=''
                start.after(1000,splash('Loading Teacher Login Page.....','#ffff80'))
            else:
                start.destroy
                one()
        def submit():
            global choice
            choice=text
            start.destroy()
            check()
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(start,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:submit())
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(600,180,'Register','black','#c3ff00')
    but(600,360,'Login','black','#f0fc00')
    but(600,540,'Back','black','#facd02')
    start.mainloop()
#----------------------------------
def registering1():
    top = Tk()
    top.config(bg='black')
    #top.state('zoomed')
    top.attributes('-fullscreen', True)
    top.title("Register")
    l1=Label(top,text="USN:",bg='black',fg='#02fac8', font=(tit_font,15), anchor = 'center')
    usn = Entry(top,bg='#02fac8',font=(tit_font,15),width=30)
    l2=Label(top,text="Password: ",bg='black',fg='#02fac8', font=(tit_font,15), anchor = 'center')
    pas = Entry(top,bg='#02fac8',show='*',font=(tit_font,15), width=30)
    l3=Label(top,text="Email-id: ",bg='black',fg='#02fac8', font=(tit_font,15), anchor = 'center')
    email = Entry(top,bg='#02fac8',font=(tit_font,15), width=30)
    l4=Label(top,text=None,bg='black',fg='#02fac8', font=(tit_font,15), anchor = 'center')
    l4.place(x=550,y=250)
    l=Label(top,text="REGISTER HERE!!",bg='black',fg='#02fac8',font=(tit_font,25), anchor='center')
    l.pack()
    def but(x,y,text,fcolor,bcolor,cmd):
        global val
        val=cmd
        def submit():
            usn_val = usn.get()
            pass_val = pas.get()
            email_val = email.get()
            if re.findall(a,usn_val)==[]:
                l4.config(text="Enter usn properly")
            elif len(pass_val)<8:
                l4.config(text="Minimum password length is 8")
            elif re.findall(em,email_val)==[]:
                l4.config(text="Enter valid email-id")
            else:
                new=(usn_val.upper(),email_val,pass_val)
                try:
                    cur.execute("insert into reg_student(usn,email,password) values {}".format(new))
                    top.destroy()
                    global j,l,fin
                    j=0
                    l=[]
                    fin=''
                    top.after(1000,splash('Student Registering.....','#02cdfa'))
                except:
                    l4.config(text="Account already exists please login")
        def nothing(val):
            if val=='submit':
                submit()
            elif val=='log':
                top.destroy()
                global j,l,fin
                j=0
                l=[]
                fin=''
                top.after(1000,splash('Loading Student Login Page.....','#02cdfa'))
            else:
                top.destroy()
                starting1()
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:nothing(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(600,280,'Register','black','#02fac8','submit')
    but(600,420,'Login','black','#02cdfa','log')
    but(600,560,'Back','black','#03a1fc','back')
    l1.place(x=350,y=100)
    usn.place(x=500,y=100)
    l2.place(x=350,y=150)
    pas.place(x=500,y=150)
    l3.place(x=350,y=200)
    email.place(x=500,y=200)
    top.mainloop()
#---------------------
def registering2():
    top = Tk()
    top.config(bg='black')
    #top.state('zoomed')
    top.attributes('-fullscreen', True)
    top.title("Register")
    l1=Label(top,text="ID:",bg='black',fg='#c3ff00',font=(tit_font,15), anchor = 'center')
    usn = Entry(top,bg='#c3ff00',font=(tit_font,15),width=30)
    l2=Label(top,text="Password: ",bg='black',fg='#c3ff00', font=(tit_font,15), anchor = 'center')
    pas = Entry(top,bg='#c3ff00',font=(tit_font,15),show='*', width=30)
    l3=Label(top,text="Email-id: ",bg='black',fg='#c3ff00', font=(tit_font,15), anchor = 'center')
    email = Entry(top,bg='#c3ff00',font=(tit_font,15), width=30)
    l4=Label(top,text=None,bg='black',fg='#c3ff00', font=(tit_font,15), anchor = 'center')
    l4.place(x=550,y=250)
    l=Label(top,text="REGISTER HERE!!",bg='black',fg='#c3ff00',font=(tit_font,25), anchor='center')
    l.pack()
    def but(x,y,text,fcolor,bcolor,cmd):
        def submit():
            usn_val = usn.get()
            pass_val = pas.get()
            email_val = email.get()
            if usn_val=='':
                l4.config(text="Enter ID properly")
            elif len(pass_val)<8:
                l4.config(text="Minimum password length is 8")
            elif re.findall(em,email_val)==[]:
                l4.config(text="Enter email-id")
            else:
                new=(usn_val.upper(),email_val,pass_val)
                try:
                    cur.execute("insert into reg_teacher(t_id,email,password) values {}".format(new))
                    top.destroy()
                    global j,l,fin
                    j=0
                    l=[]
                    fin=''
                    top.after(1000,splash('Teacher Registering.....','#c3ff00'))
                except:
                    l4.config(text="Account already exists please login")
        def nothing(val):
            if val=='submit':
                submit()
            elif val=='log':
                top.destroy()
                global j,l,fin
                j=0
                l=[]
                fin=''
                top.after(1000,splash('Loading Teacher Login Page.....','#c3ff00'))
            else:
                top.destroy()
                starting2()
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:nothing(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(600,280,'Register','black','#c3ff00','submit')
    but(600,420,'Login','black','#f0fc00','log')
    but(600,560,'Back','black','#facd02','back')
    l1.place(x=350,y=100)
    usn.place(x=500,y=100)
    l2.place(x=350,y=150)
    pas.place(x=500,y=150)
    l3.place(x=350,y=200)
    email.place(x=500,y=200)
    top.mainloop()
#------------------------------
def logging1():
    log = Tk()
    log.config(bg='black')
    #log.state('zoomed')
    log.attributes('-fullscreen', True)
    log.title("Login Here")
    l=Label(log,text="LOG IN HERE!!",bg='black',fg='#66ffd9',font=(tit_font,25), anchor='center')
    l.pack()
    l1=Label(log,text="USN:", bg='black',fg='#66ffd9',font=(tit_font,15), anchor = 'center')
    l1.place(x=350,y=100)
    usn = Entry(log,font=(tit_font,15),width=30)
    usn.place(x=500,y=100)
    l2=Label(log,text="Password: ",bg='black',fg='#66ffd9',font=(tit_font,15), anchor = 'center')
    l2.place(x=350,y=160)
    pas = Entry(log,show='*',font=(tit_font,15),width=30)
    pas.place(x=500,y=160)
    l3=Label(log,text=None,bg='black',fg='#66ffd9', font=(tit_font,15), anchor = 'center')
    l3.place(x=550,y=220)
    def forg():
        global j,l,fin
        j=0
        l=[]
        fin=''
        log.after(1000,splash('Enter USN.....','#00ffea'))
    def something():
        usn_val = usn.get()
        pass_val = pas.get()
        new=(usn_val.upper(),pass_val)
        global usnn
        usnn=usn_val.upper()
        try:
            cur.execute("select password from reg_student where usn={};".format("\"{}\"".format(usn_val)))
            a=cur.fetchall()
            if a[0][0]==pass_val:
                log.destroy()
                global j,l,fin
                j=0
                l=[]
                fin=''
                log.after(1000,splash('Student Logging in.....','#00ffea'))
            else:
                l3.config(text="Enter password correctly")
        except:
            l3.config(text='Enter valid credentials')
    def another(val):
        if val=='submit':
            something()
        elif val=='forg':
            log.destroy()
            forg()
        else:
            log.destroy()
            one()
    def but(x,y,text,fcolor,bcolor,cmd):
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(log,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:another(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(550,280,'Login','black','#02fac8','submit')
    but(550,400,'Forgot Password','black','#02cdfa','forg')
    but(550,520,'Back','black','#03a1fc','back')
    log.mainloop()
#-------------------------
def logging2():
    log = Tk()
    log.config(bg='black')
    #log.state('zoomed')
    log.attributes('-fullscreen', True)
    log.title("Login Here")
    l=Label(log,text="LOG IN HERE!!",bg='black',fg='#ffff80',font=(tit_font,25), anchor='center')
    l1=Label(log,text="ID:",bg='black',fg='#ffff80', font=(tit_font,15), anchor = 'center')
    usn = Entry(log,bg='#c3ff00', font=(tit_font,15),width=30)
    l2=Label(log,text="Password: ",bg='black',fg='#ffff80', font=(tit_font,15), anchor = 'center')
    pas = Entry(log,bg='#c3ff00', font=(tit_font,15),show='*', width=30)
    l3=Label(log,text=None,bg='black',fg='#ffff80', font=(tit_font,15), anchor = 'center')
    l3.place(x=550,y=220)
    def forg():
        global j,l,fin
        j=0
        l=[]
        fin=''
        log.after(1000,splash('Enter ID.....','#f0fc00'))
    def something():
        usn_val = usn.get()
        pass_val = pas.get()
        new=(usn_val.upper(),pass_val)
        global usnn
        usnn=usn_val.upper()
        try:
            cur.execute("select password from reg_teacher where t_id={};".format("\"{}\"".format(usn_val)))
            a=cur.fetchall()
            if a[0][0]==pass_val:
                l3.config(text="successfully logged in")
                log.destroy()
                global j,l,fin
                j=0
                l=[]
                fin=''
                log.after(1000,splash('Teacher Logging in.....','#f0fc00'))
            else:
                l3.config(text="Enter password correctly")
        except:
            l3.config(text='Enter valid credentials')
    def another(val):
            if val=='submit':
                something()
            elif val=='forg':
                log.destroy()
                forg()
            else:
                log.destroy()
                one()
    def but(x,y,text,fcolor,bcolor,cmd):
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(log,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:another(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(550,280,'Login','black','#c3ff00','submit')
    but(550,400,'Forgot Password','black','#f0fc00','forg')
    but(550,520,'Back','black','#facd02','back')
    l.pack()
    l1.place(x=350,y=100)
    usn.place(x=500,y=100)
    l2.place(x=350,y=160)
    pas.place(x=500,y=160)
    log.mainloop()
#--------------------------------
def start1(value):
    global no
    no=value
    top = Tk()
    top.config(bg='black')
    #top.state('zoomed')
    top.attributes('-fullscreen',True)
    k=''
    l6=Label(top,text=None,bg='black',fg='#66ffd9', font=(tit_font,15), anchor = 'center')
    l6.place(x=600,y=320)
    def but(x,y,text,fcolor,bcolor,cmd):
        def chec(val):
            if val=='submit':
                submit()
            else:
                top.destroy()
                logging1()
        def submit():
            name_val = name.get()
            sem_val = sem.get()
            branch_val = branch.get()
            phone_val = Phone.get()
            cur.execute("select email from reg_student where usn={}".format("\"{}\"".format(no)))
            some=cur.fetchall()
            email_val = some[0][0]
            new=(no.upper(),name_val,sem_val,branch_val.upper(),phone_val,email_val)
            if name_val=='':
                l6.config(text='Please enter the Name')
            elif branch_val=='':
                l6.config(text='Please enter the branch')
            elif phone_val=='' or len(phone_val)<10 or len(phone_val)>10:
                l6.config(text='Enter the 10 digits of phone number')
            elif sem_val=='' or sem_val not in '12345678':
                if sem_val!='' and sem_val not in '12345678':
                    l6.config(text='Enter a valid Semester')
                elif sem_val=='':
                    l6.config(text='Please enter your Semester')
            else:
                try:
                    cur.execute("insert into info_student(usn, name,sem, branch, phone, email) values {}".format(new))
                    try:
                        card(name_val,no.upper(),branch_val,phone_val,"student")
                        top.destroy()
                        global j,l,fin
                        j=0
                        l=[]
                        fin=''
                        try:
                            top.after(1000,splash('Student ID card created','#00ffea'))
                        except:
                            pass
                    except:
                        l6.config(text="Check if your photo exists")
                except:
                    try:
                        cur.execute("update info_student set name={}, branch={}, phone={}, email={} where usn={}".format("\"{}\"".format(name_val),"\"{}\"".format(branch_val),"\"{}\"".format(phone_val),"\"{}\"".format(email_val),"\"{}\"".format(no)))
                        try:
                            card(name_val,no.upper(),branch_val,phone_val,'student')
                            top.destroy()
                            j=0
                            l=[]
                            fin=''
                            try:
                                top.after(1000,splash('Student ID card created','#00ffea'))
                            except:
                                pass
                        except:
                            l6.config(text="Check if your photo exists")
                    except:
                        l6.config(text="Enter a valid branch")
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:chec(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    top.title("Id card Generator")
    l1=Label(top,text="Name:",bg='black',fg='#66ffd9',font=(tit_font,14), anchor = 'center')
    name=Entry(top, font=(tit_font,14), width=50)
    l3=Label(top,text="Branch: ",bg='black',fg='#66ffd9', font=(tit_font,14), anchor = 'center')
    branch = Entry(top,font=(tit_font,14), width=50)
    l4=Label(top,text="Phone no: ",bg='black',fg='#66ffd9', font=(tit_font,14), anchor = 'center')
    Phone = Entry(top, font=(tit_font,14), width=50)
    l5=Label(top,text="Sem: ",bg='black',fg='#66ffd9', font=(tit_font,14), anchor = 'center')
    sem = Entry(top,font=(tit_font,14), width=50)
    but(600,350,'SUBMIT','black','#66ffd9','submit')
    but(600,500,'Back','black','#66ffd9','back')
    l1.place(x=310,y=100)
    name.place(x=450,y=100)
    l3.place(x=310,y=150)
    branch.place(x=450,y=150)
    l4.place(x=310,y=200)
    Phone.place(x=450,y=200)
    l5.place(x=310,y=250)
    sem.place(x=450,y=250)
    top.mainloop()
#--------------------------
def start2(value):
    global no
    no=value
    top = Tk()
    top.config(bg='black')
    #top.state('zoomed')
    top.attributes('-fullscreen',True)
    k=''
    l6=Label(top,text=None,bg='black',fg='#cccc00', font=(tit_font,15), anchor = 'center')
    l6.place(x=600,y=300)
    def but(x,y,text,fcolor,bcolor,cmd):
        def chec(val):
            if val=='submit':
                submit()
            else:
                top.destroy()
                logging2()
        def submit():
            name_val = name.get()
            branch_val = branch.get()
            phone_val = Phone.get()
            cur.execute("select email from reg_teacher where t_id={}".format("\"{}\"".format(no)))
            some=cur.fetchall()
            email_val = some[0][0]
            new=(no.upper(),name_val,branch_val,phone_val,email_val)
            if name_val=='':
                l6.config(text='Please enter the Name')
            elif branch_val=='':
                l6.config(text='Please enter the branch')
            elif phone_val=='' or len(phone_val)<10 or len(phone_val)>10:
                l6.config(text='Enter the 10 digits of phone number')
            else:
                try:
                    cur.execute("insert into info_teacher(id, name, branch, phone, email) values {}".format(new))
                    try:
                        card(name_val,no.upper(),branch_val,phone_val,'teacher')
                        top.destroy()
                        global j,l,fin
                        j=0
                        l=[]
                        fin=''
                        try:
                            top.after(1000,splash('Teacher ID card created','#00ffea'))
                        except:
                            pass
                    except:
                        l6.config(text="Check if your photo exists")
                except:
                    cur.execute("update info_teacher set name={}, branch={}, phone={}, email={} where id={}".format("\"{}\"".format(name_val),"\"{}\"".format(branch_val),"\"{}\"".format(phone_val),"\"{}\"".format(email_val),"\"{}\"".format(no)))
                    try:
                        card(name_val,no.upper(),branch_val,phone_val,'teacher')
                        top.destroy()
                        j=0
                        l=[]
                        fin=''
                        try:
                            top.after(1000,splash('Teacher ID card created','#00ffea'))
                        except:
                            pass
                    except:
                        l6.config(text="Check if your photo exists")
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:chec(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    top.title("Id card Generator")
    l1=Label(top,text="Name:",bg='black',fg='#cccc00',font=(tit_font,14), anchor = 'center')
    name=Entry(top, font=(tit_font,14), width=30)
    l3=Label(top,text="Branch: ",bg='black',fg='#cccc00', font=(tit_font,14), anchor = 'center')
    branch = Entry(top,font=(tit_font,14), width=30)
    l4=Label(top,text="Phone no: ",bg='black',fg='#cccc00', font=(tit_font,14), anchor = 'center')
    Phone = Entry(top, font=(tit_font,14), width=30)
    but(600,350,'SUBMIT','black','#cccc00','submit')
    but(600,500,'Back','black','#cccc00','back')
    l1.place(x=310,y=100)
    name.place(x=500,y=100)
    l3.place(x=310,y=150)
    branch.place(x=500,y=150)
    l4.place(x=310,y=200)
    Phone.place(x=500,y=200)
    top.mainloop()
#--------------------------------
def forgot(cho,fg,an,some):
    def checks(val):
        if val=='submit':
            submit()
        else:
            if cho=='student':
                top.destroy()
                logging1()
            else:
                top.destroy()
                logging2()
    def submit():
        def new():
            def changepass():
                def setting():
                    pas_val = pas.get()
                    if len(pas_val)>=8:
                        cur.execute("update {} set password={} where {}={};".format(table,"\"{}\"".format(pas_val),some,"\"{}\"".format(usnn)))
                        top.destroy()
                        if choice=="student":
                            logging1()
                        else:
                            logging2()
                    else:
                        l2.config(text='Enter 8 digit password')
                top=Tk()
                top.title("Changing Password")
                #top.state("zoomed")
                top.attributes('-fullscreen',True)
                top.config(bg='black')
                l1 = Label(top,text="Enter new Password:",bg='black',fg=f, font=(tit_font,15), anchor = 'center')
                pas = Entry(top,font=(tit_font,15),width=50)
                l2 = Label(top,text=None,bg='black',fg=f, font=(tit_font,15), anchor = 'center')
                def but(x,y,text,fcolor,bcolor):
                    def on_enter(e):
                        butt['background']=fcolor
                        butt['foreground']=bcolor
                    def on_leave(e):
                        butt['background']=bcolor
                        butt['foreground']=fcolor
                    butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:setting())
                    butt.bind('<Enter>',on_enter)
                    butt.bind('<Leave>',on_leave)
                    butt.place(x=x,y=y)
                but(500,280,"Set Password",'black',f)
                l1.place(x=190,y=100)
                pas.place(x=400,y=100)
                l2.place(x=500,y=200)
                top.mainloop()
            def confirming():
                otp_val = otpp.get()
                if otp_val==str(otp):
                    top.destroy()
                    changepass()
                else:
                    global count
                    if count>0:                        
                        l2.config(text='Wrong OTP, More {} chance left'.format(count))
                        count-=1
                    else:
                        if an=='reg_student':
                            top.destroy()
                            logging1()
                        else:
                            logging2()
            global count
            count=3
            top=Tk()
            top.title("Entering OTP")
            #top.state("zoomed")
            top.attributes('-fullscreen',True)
            top.config(bg='black')
            l1 = Label(top,text="OTP:",bg='black',fg=f, font=(tit_font,15), anchor = 'center')
            otpp = Entry(top,font=(tit_font,15),width=50)
            l2 = Label(top,text=None,bg='black',fg=f, font=(tit_font,15), anchor = 'center')
            l2.place(x=400,y=200)
            def but(x,y,text,fcolor,bcolor):
                def on_enter(e):
                    butt['background']=fcolor
                    butt['foreground']=bcolor
                def on_leave(e):
                    butt['background']=bcolor
                    butt['foreground']=fcolor
                butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:confirming())
                butt.bind('<Enter>',on_enter)
                butt.bind('<Leave>',on_leave)
                butt.place(x=x,y=y)
            but(550,280,"Confirm",'black',f)
            l1.place(x=310,y=150)
            otpp.place(x=400,y=150)
            top.mainloop()
        global otp
        global usnn
        otp=random.randint(1000,10000)
        x=usn.get()
        usnn=x.upper()
        try:
            cur.execute("select email from {} where {}={};".format(table,some,"\"{}\"".format(x)))
            m=cur.fetchall()
            yag.send(m[0][0],"Reset Password",str(otp)+" is your otp for new password")
            top.destroy()
            new()
        except:
            l6.config(text='Check if your account exists!')
    global choice,f,table
    choice=cho
    f=fg
    table=an
    top=Tk()
    #top.state("zoomed")
    top.attributes('-fullscreen',True)
    top.config(bg='black')
    top.title("Forgot password")
    l1 = Label(top,text="{}:".format(some.upper()),bg='black',fg=f, font=(tit_font,15), anchor = 'center')
    usn = Entry(top,font=(tit_font,15),width=30)
    l6=Label(top,text=None,bg='black',fg=f,font=(tit_font,15),anchor='center')
    def but(x,y,text,fcolor,bcolor,cmd):
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:checks(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(550,280,"SEND",'black',f,'submit')
    but(550,480,"Back",'black',f,'back')
    l1.place(x=350,y=100)
    usn.place(x=500,y=100)
    l6.place(x=500,y=200)
    top.mainloop()
#----------------------------------
def card(name,usn,branch,phone,part):
    global usnn1,pa,bran
    usnn1=usn
    pa=part
    bran=branch
    img=Image.open(r"F:\5th sem dbms mini project\{}_template.png".format(part))
    img_edit = ImageDraw.Draw(img)
    img_edit.text((550,1165), name,font=tit_font,fill=0)
    img_edit.text((550,1345), usn,font=tit_font,fill=0)
    img_edit.text((550,1525), branch,font=tit_font,fill=0)
    img_edit.text((550,1675), phone,font=tit_font,fill=0)
    img.save(r"F:\5th sem dbms mini project\id cards\{}\{}.png".format(part,usn))
    new()
def new():
    img1 = Image.open(r"F:\5th sem dbms mini project\id cards\{}\{}.png".format(pa,usnn1))
    img1copy = img1.copy()
    img2 = Image.open(r"F:\5th sem dbms mini project\{}\{}.jpg".format(pa+" pictures",usnn1))
    photo=img2.copy()
    photo=photo.resize((500,600))
    img1copy.paste(photo, (600, 450))
    img3 = Image.open(r"F:\5th sem dbms mini project\qr_code.jpeg")
    img3=img3.resize((400,400))
    img1copy.paste(img3,(600,1800))
    img1copy.save(r"F:\5th sem dbms mini project\id cards\{}\{}.png".format(pa,usnn1))
one()
