

from salarie import Employee
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmb

# import rightfram as r
# import leftfram as l





class Mainwindow:
    def __init__(self, window):
        self.window = window
        self.window.title('salaire')
        self.window.geometry('1166x720')
        self.window.minsize(height=780,width=1570)
        self.window.state('zoomed')
        #######################  topframe   ####################################
        self.topfram = Frame(self.window, bg='#1b9ea4', height=100)
        self.topfram.pack(fill=X)
        self.titre = Label(self.topfram, text='Salaire Net', bg='#1b9ea4', fg='white', font=('tachona', 50), pady=30)
        self.titre.pack()
        #######################  mainfarame = leftframe + rightframe   ####################################

        self.mainrfram = Frame(self.window, bg='red')
        self.mainrfram.pack(fill=BOTH,expand=True)
        ##############################################################################
        
        #######################  leftframe= 6 entry boxes + 3 buttons  ####################################
        self.leftfram = Frame(self.mainrfram,width=20, bg='#44838e')
        self.leftfram.pack(side=LEFT,fill=Y)
        
        
        self.topleft = Frame(self.leftfram, bg='#44838e',pady=40)
        self.topleft.pack()


        self.name=StringVar()
        self.lastname=StringVar()
        self.cin=StringVar()
        self.email=StringVar()
        self.salaire=StringVar()
        self.chs=StringVar()

        self.namefarme = Frame(self.topleft,padx=50,pady=20, bg='#44838e')
        self.namefarme.pack()
        self.ln=Label(self.namefarme,text='Nom             ',fg='white', bg='#44838e',font=('tachona', 20))
        self.ln.grid(row=0,column=0)
        self.nom = Entry(self.namefarme,font=('tachona',20),textvariable=self.name)
        self.nom.grid(row=0,column=1)


        self.prenomfarme = Frame(self.topleft,padx=50,pady=20, bg='#44838e')
        self.prenomfarme.pack()
        self.lp = Label(self.prenomfarme, text='Prenom        ',fg='white', bg='#44838e',font=('tachona', 20))
        self.lp.grid(row=0, column=0)
        self.p = Entry(self.prenomfarme,font=('tachona',20),textvariable=self.lastname)
        self.p.grid(row=0, column=1)





        self.cinfarme = Frame(self.topleft, padx=50, pady=20, bg='#44838e')
        self.cinfarme.pack()
        self.lc = Label(self.cinfarme, text='CIN              ',fg='white', bg='#44838e',font=('tachona', 20))
        self.lc.grid(row=0, column=0)
        self.c = Entry(self.cinfarme, font=('tachona', 20),textvariable=self.cin)
        self.c.grid(row=0, column=1)


        self.emailfarme = Frame(self.topleft,padx=50,pady=20, bg='#44838e')
        self.emailfarme.pack()
        self.le = Label(self.emailfarme, text='Email           ',fg='white', bg='#44838e',font=('tachona', 20))
        self.le.grid(row=0, column=0)
        self.e = Entry(self.emailfarme,font=('tachona',20),textvariable=self.email)
        self.e.grid(row=0, column=1)



        self.sfarme = Frame(self.topleft,padx=50,pady=20, bg='#44838e')
        self.sfarme.pack()
        self.ls = Label(self.sfarme, text='Salaire         ',fg='white', bg='#44838e',font=('tachona', 20))
        self.ls.grid(row=0, column=0)
        self.s = Entry(self.sfarme,font=('tachona',20),textvariable=self.salaire)
        self.s.grid(row=0, column=1)


        self.sbfarme = Frame(self.topleft,padx=50,pady=20, bg='#44838e')
        self.sbfarme.pack()
        self.lsb = Label(self.sbfarme, text='charge social',fg='white', bg='#44838e',font=('tachona', 20))
        self.lsb.grid(row=0, column=0)
        self.sb = Entry(self.sbfarme,font=('tachona',20),textvariable=self.chs)
        self.sb.grid(row=0, column=1)


        self.btnfram = Frame(self.leftfram, bg='#44838e')
        self.btnfram.pack(fill=X)

        self.afram = Frame(self.btnfram, bg='#44838e',padx=4)
        self.afram.grid(row=0,column=0)

        self.mfram = Frame(self.btnfram, bg='#44838e',padx=4)
        self.mfram.grid(row=0,column=1)

        self.delfram = Frame(self.btnfram, bg='#44838e',padx=4,pady=20)
        self.delfram.grid(row=0,column=2)

        self.ab=Button(self.afram,text='Ajouter',command=self.add,fg='white', bg='#1b9ea4',font=('tachona', 20),padx=20)
        self.ab.pack()
        self.mb=Button(self.mfram,text=' Modifier  ',fg='white', bg='#1b9ea4',font=('tachona', 20),command=self.modifier,padx=20)
        self.mb.pack(side=LEFT)
        self.delb=Button(self.delfram,text='Supprimer',command=self.supprime,fg='white', bg='#1b9ea4',font=('tachona', 20),padx=20)
        self.delb.pack(side=RIGHT)
        #############################################################################
        
        #######################  rightframe = treeview + verifier(entryboxe + button) + about(lable)   ####################################
        self.rightfram = Frame(self.mainrfram,width=20, bg='#44838e')
        self.rightfram.pack(side=RIGHT,fill=Y)
        
        
        self.righttop = Frame(self.rightfram, bg='#44838e',pady=20)
        self.righttop.pack()
        ##verifier######
        self.verifram = Frame(self.righttop,padx=4,pady=30, bg='#44838e')
        self.verifram.pack(fill=X)
        self.vb=Button(self.verifram,text='Verifier',command=self.verifier,fg='white', bg='#1b9ea4',font=('tachona', 20),padx=20)
        self.vb.grid(row=0,column=1)
        self.vr = Entry(self.verifram,font=('tachona',34),width=35)
        self.vr.grid(row=0,column=0)
        self.tblfram = Frame(self.righttop,padx=4,pady=20, bg='#44838e')
        self.tblfram.pack(fill=X)
        #treeview#
        self.table=ttk.Treeview(self.tblfram,columns=("n","p","c","e","s","cs","sn"),show='headings', height=16)
        self.table.pack()
        self.table.heading("n", text="NOM")
        self.table.heading("p", text="PRENOM")
        self.table.heading("c", text="CIN")
        self.table.heading("e", text="EMAIL")
        self.table.heading("s", text="SALAIRE")
        self.table.heading("cs", text="CHARGE SOCIALE")
        self.table.heading("sn", text="SALAIRE NET")
        self.table.column('n',width=130)
        self.table.column('p',width=150)
        self.table.column('c',width=100)
        self.table.column('e',width=300)
        self.table.column('s',width=100)
        self.table.column('cs',width=150)
        self.table.column('sn',width=100)
        ###############################################################################
        
        
        self.read()
        self.table.bind("<ButtonRelease>",self.affich)
        
        #######################  about   ####################################
        self.labout = Label(self.tblfram, text='about : This app was developed and designed by Mohammed Fares.',fg='white', bg='#44838e',font=('tachona', 20),pady=70)
        self.labout.pack()
        
        
    def read(self):#to read from database
        afch=Employee()
        l=afch.afficher()
        self.table.delete(*self.table.get_children())
        for i in l:
            self.table.insert('','end',iid=i[2],values=i)
    def verifier(self):#to search in employee.txt
        r=Employee()
        self.table.delete(*self.table.get_children())
        self.table.insert('','end',values=r.recherche(self.vr.get()))
        


    def add(self):#to add to employee.txt

        if (len(self.nom.get())==0 or len(self.p.get())==0 or len(self.c.get())==0 or len(self.e.get())==0 or len(self.s.get())==0 or len(self.sb.get())==0):
            tmb.showerror('error','required data')
        else:
            try:
                int(self.s.get())
                int(self.sb.get())
                ajte = Employee(self.nom,self.p,self.c,self.e,self.s,self.sb) 
                if ajte.already_exist():
                    tmb.showinfo('deja','vu')
                else:
                    ajte.ajout()
                    self.read()
                    tmb.showinfo('succesfully added','data inserted')
                    self.rest()
            except ValueError:
                tmb.showerror('error','salaire must be int')
    def rest(self):
        self.nom.delete(0,'end')
        self.p.delete(0,'end')
        self.c.delete(0,'end')
        self.e.delete(0,'end')
        self.s.delete(0,'end')
        self.sb.delete(0,'end')
    def affich(self,ev):
        self.data=self.table.focus()
        alldata=self.table.item(self.data)
        val=alldata['values']
        self.name.set(val[0])
        self.lastname.set(val[1])
        self.cin.set(val[2])
        self.email.set(val[3])
        self.salaire.set(val[4])
        self.chs.set(val[5])
    def supprime(self):#to delete from employee.txt
        r=Employee()
        r.remove(self.data)
        self.read()
        tmb.showinfo('supprime')
        self.rest()
    def modifier(self):#to update employee.txt

        m=Employee()
        m.modifier(self.data,self.name.get(),self.lastname.get(),self.email.get(),int(self.salaire.get()),int(self.chs.get()),int(self.s.get())-int(self.sb.get()),self.cin.get())
        self.read()
        tmb.showinfo('modifier')
        self.rest()


        

        
def page():
    window = Tk()
    Mainwindow(window)
    window.mainloop()


if __name__ == '__main__':
    page()