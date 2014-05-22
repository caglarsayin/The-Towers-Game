import random
from Tkinter import IntVar
from itertools import permutations
__author__="caglar"
__date__ ="$Nov 20, 2010 9:11:04 PM$"

if __name__ == "__main__":
    print "Hello World"

class Hints:

    def __init__(self):
        self.hintsup=[]
        self.hintsdown=[]
        self.hintsright=[]
        self.hintsleft=[]
        self.huplabel=[]
        self.hdownlabel=[]
        self.hrightlabel=[]
        self.hleftlabel=[]

class Box:

    def __init__(self):
        self.value = 0
        self.posiblty = []
        self.entry = IntVar()

class Puzzle:
    def __init__(self):
        self.boxes=list()
        self.hint=Hints()
        self.size=int()
    def clean(self):
        self.boxes=list()
        self.hint=Hints()
        self.size=int()

    def generate(self):
        temp=int()
        for i in range(self.size):
            self.boxes.append(list())
            for j in range(self.size):
                self.boxes[i].append(Box())
                self.boxes[i][j].value=((self.size+i+j)%self.size)+1
        for i in range(random.randrange(0,self.size*self.size*self.size*self.size)):
            x=random.randrange(0,self.size)
            y=random.randrange(0,self.size)
            for ii in range(self.size):
                temp=self.boxes[x][ii]
                self.boxes[x][ii]=self.boxes[y][ii]
                self.boxes[y][ii]=temp
            x=random.randrange(0,self.size)
            y=random.randrange(0,self.size)
            for ii in range(self.size):
                temp=self.boxes[ii][x]
                self.boxes[ii][x]=self.boxes[ii][y]
                self.boxes[ii][y]=temp

        self.hinter()
    def hinter(self):
        self.printval()

        for i in range(self.size):#hintup
            x=0
            count=0
            for j in range(self.size):
                if(self.boxes[i][j].value>x):
                    #print "for up x is ", x , "smaller than" , self.boxes[i][j].value
                    x=self.boxes[i][j].value
                    count=count+1
            self.hint.hintsup.append(count)
        for j in range(self.size):#hintleft
            x=0
            count=0
            for i in range(self.size-1,-1,-1):
                if(self.boxes[i][j].value>x):
                    #print "for left x is ", x , "smaller than" , self.boxes[i][j].value
                    x=self.boxes[i][j].value
                    count=count+1
            self.hint.hintsleft.append(count)

        for i in range(self.size):#hintdown
            x=0
            count=0
            for j in range(self.size-1,-1,-1):
                if(self.boxes[i][j].value>x):
                    #print "for down x is ", x , "smaller than" , self.boxes[i][j].value
                    x=self.boxes[i][j].value
                    count=count+1
            self.hint.hintsdown.append(count)

        for j in range(self.size):#hintright
            x=0
            count=0
            for i in range(self.size):
                if(self.boxes[i][j].value>x):
                    #print "for right x is ", x , "smaller than" , self.boxes[i][j].value
                    x=self.boxes[i][j].value
                    count=count+1
            self.hint.hintsright.append(count)

    def checker(self):
        doubt =0
        for j in range(self.size):#hintup
            x=0
            count=0
            for i in range(self.size):
                if(self.boxes[i][j].value>x):
                    x=self.boxes[i][j].value
                    count=count+1
            if(self.hint.hintsup[j]==count):
                doubt=doubt+1
            #print "doubt = %d count = %d %d = hint" %(doubt,count,self.hint.hintsup[j])
        if (doubt<self.size):#to make it rapid
            return 0
        for i in range(self.size):#hintleft
            x=0
            count=0
            for j in range(self.size-1,-1,-1):
                if(self.boxes[i][j].value>x):
                    x=self.boxes[i][j].value
                    count=count+1

            if(self.hint.hintsleft[i]==count):
                doubt=doubt+1
            #print "doubt = %d count = %d %d = hint" %(doubt,count,self.hint.hintsleft[j])
        for j in range(self.size):#hintdown
            x=0
            count=0
            for i in range(self.size-1,-1,-1):
                if(self.boxes[i][j].value>x):
                    x=self.boxes[i][j].value
                    count=count+1
            if(self.hint.hintsdown[j]==count):
                doubt=doubt+1
            #print "doubt = %d count = %d %d = hint" %(doubt,count,self.hint.hintsdown[j])
        for i in range(self.size):#hintright
            x=0
            count=0
            for j in range(self.size):
                if(self.boxes[i][j].value>x):
                    x=self.boxes[i][j].value
                    count=count+1
            if(self.hint.hintsright[i]==count):
                doubt=doubt+1
            #print "doubt = %d count = %d %d = hint" %(doubt,count,self.hint.hintsright[j])
        result=0
        if(self.size*4==doubt):
            result=1
        return result

    def printval(self):
        print ""
        for i in range(self.size):#hint hesaplama
            for j in range(self.size):
                print self.boxes[j][i].value,
            print ""

    def ProbMapper(self):
        print "it will be writen in the future"

    def solver(self):
        sample=list()
        sample2=list()
        for i in range(self.size):#sample hazirliyor
            sample.append(list())
            sample2.append(list())
            for j in range(self.size):
                sample[i].append(Box())
                sample2[i].append(Box())
                sample[i][j]=((self.size+i+j)%self.size)+1
        perm=range(self.size)
        perm=permutations(perm)
        perm=list(perm)
        for k in range(len(perm)):
            for i in range(self.size):
                for j in range(self.size):
                    sample2[perm[k][i]][j].value=sample[i][j]

            for t in range(len(perm)):
                for i in range(self.size):
                    for j in range(self.size):
                        self.boxes[j][perm[t][i]].value=sample2[j][i].value
                if(self.checker()==1):
                    self.printval()
                    return 1
        return 0
