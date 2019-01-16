from random import random, randint, choice
from tkinter import *
class Player(object):
    def __init__(self,name='no_name',canPlay=True):
        self.name = name
        self.canplay = canPlay
    def here(self):
        self.canplay = True
    def gone(self):
        self.canplay = False
    def ishere(self):
        return self.canplay

class Team(object):
    def __init__(self,name,roster=[]):
        self.name = name
        self.roster = roster
    def setName(self,newName='team0'):
        self.name = newName
    def show(self,other):
        try:
            assert(type(other)==Team)
            if len(self.roster) >= len(other.roster):
                rStr = ''
                for n in range(len(self.roster)):
                    if n >= len(other.roster):
                        rStr += '{0:10d} || {1:10d}'.format(self.roster[n],' ')
                        pass
                    rStr += '{0:10d} || {1:10d}'.format(self.roster[n],other.roster[n])
            elif len(self.roster) < len(other.roster):
                rStr = ''
                for n in range(len(other.roster)):
                    if n >= len(self.roster):
                        rStr += '{0:10d} || {1:10d}'.format(' ',other.roster[n])
                        pass
                    rStr += '{0:10d} || {1:10d}'.format(self.roster[n],other.roster[n])
            print(rStr)
        except AssertionError:
            print("Can't show a team versus something not a team")
            return
    def __repr__(self):
        rStr = str(self.roster.pop(0).name)
        for i in self.roster:
            rStr += ', {0:10d}'.format(i.name)
        return rStr
    def __add__(self,other):
        if type(other) == Player:
            self.roster += other
            print("Player {0:10d} added to {1}.\n{1} new roster: {2}".format(other.name,self.name,self.roster))
        elif type(other) == Team:
            self.roster += other.roster
            print("Teams {0:15d} and {1:15d} merged under name {2:15d}.\nRoster of team {2}:".format(self.name,other.name,self.name[:int(len(self.name))/2]+other.name[int(len(other.name))/2:]))
            self.setName(self.name[:int(len(self.name))/2]+other.name[int(len(other.name))/2:])
        elif type(other) == list:
            self.roster += other
            print("Players added to {0}.\n {0} new roster: {1}".format(self.name,self.roster))
        else:
            raise TypeError
            

def main():
    root = Tk()
    pool = Team('pool',[])
    def makeTeams():
        lst = pool.roster
        lstT1 = []
        for n in range(int(len(lst)/2)):
            lstT1 = lst.pop(n)
        T1 = Team('Team 1',lstT1)
        T2 = Team('Team 2',lst) #LEFT OFF HERE, making teams and figuring out the addPlayer func
    def addPlayer():
        pName = str(ePname.get())
        lPName = pName.split(',')
        pool += lPname
    lPname = Label(root,text="Names, separated by commas")
    lT1 = Label(root,text="Team 1")
    lT2 = Label(root,text="Team 2")
    lbT1 = Listbox(root,bg='white',fg='blue')
    lbT2 = Listbox(root,bg='white',fg='red')
    btnMakeTeams = Button(root,text="Make Teams",command=makeTeams)
    btnAddPlayer = Button(root,text="Add Player(s)",command=addPlayer)
    ePname = Entry(root,bg='white')

if __name__ == '__main__':
    main()
    