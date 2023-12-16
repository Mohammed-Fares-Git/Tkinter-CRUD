
class Employee:
    def __init__(self,n=None,p=None,c=None,e=None,s=None,cs=None):
        self.__nom=n
        self.__prenom=p
        self.__cin=c
        self.__email=e
        self.__salaire=s
        self.__chargesocial=cs
        
    def ajout(self):
        with open('employee.txt','a') as f:
            f.write(str(self.__nom.get()).lower().capitalize()+"\n")
            f.write(str(self.__prenom.get()).lower().capitalize()+"\n")
            f.write(str(self.__cin.get()).upper()+"\n")
            f.write(str(self.__email.get()).lower()+"\n")
            f.write(str(self.__salaire.get())+"\n")
            f.write(str(self.__chargesocial.get())+"\n")
            f.write(str(int(self.__salaire.get()) - int(self.__chargesocial.get()))+"\n")
    def afficher(self):
        liste_clients=[]
        with open('employee.txt',"r") as file:
            nbc=int(len(file.readlines())/7)
        with open('employee.txt',"r") as file:
            for i in range(nbc):
                l=[]
                l.append(file.readline().strip())
                l.append(file.readline().strip())
                l.append(file.readline().strip())
                l.append(file.readline().strip())
                l.append(file.readline().strip())
                l.append(file.readline().strip())
                l.append(file.readline().strip())
                liste_clients.append(l)
        return liste_clients        
    def already_exist(self):
        l=self.afficher()
        for i in l:
            if self.__cin.get()==i[2] or self.__email.get()==i[3]:
                return True
                break
    def recherche(self,id):
        l=self.afficher()
        for i in l:
            if id==i[2]:
                return i
                break
    def modifier(self,id,n,p,e,s,cs,sn,cin="00000"):
        l=self.afficher()
        i=self.recherche(id)
        l.remove(i)
        i[0]=str(n).lower().capitalize()
        i[1]=str(p).lower().capitalize()
        i[2] = str(cin).upper()
        i[3]=str(e).lower()
        i[4]=s
        i[5]=cs
        i[6]=sn
        l.append(i)
        self.necrire(l)
        
    def remove(self,id):
        l=self.afficher()
        l.remove(self.recherche(id))
        self.necrire(l)

    def necrire(self,l):
        with open('employee.txt','w') as f:
            for i in l:
                for j in i:
                    f.write(str(j)+'\n')


        



