class franction:
    def __init__(self,a,b,c,d):
        self.sa=int(a)
        self.mb=int(b)
        self.sc=int(c)
        self.md=int(d)
    def sum(self):
        print("11111")
        if(self.mb==self.md):
            res=self.sa+self.sc
            res=str(res)
            mdst=str(self.md)
            return(res+"/"+mdst)
        else:
            sres=(self.sa*self.md)+(self.sc*self.mb)
            mres=self.mb*self.md
            sres=str(sres)
            mres=str(mres)
            return(sres+"/"+mres)
    def sub(self):
        if(self.mb==self.md):
            res=self.sa-self.sc
            res=str(res)
            mdst=str(self.md)
            return(res+"/"+mdst)
        else:
            sres=(self.sa*self.md)-(self.sc*self.mb)
            mres=self.mb*self.md
            sres=str(sres)
            mres=str(mres)
            return(sres+"/"+mres)
    def mul(self):
        sres=self.sa*self.sc
        mres=self.mb*self.md
        sres=str(sres)
        mres=str(mres)
        return(sres+"/"+mres)
    def div(self):
        sres=self.sa*self.md
        mres=self.mb*self.sc
        sres=str(sres)
        mres=str(mres)
        return(sres+"/"+mres)
while(True):
    a=0
    b=1
    c=0
    d=1
    franc1=input("first franction: ").split("/")
    a=franc1[0]
    if(b!=1):
        b=int(franc1[1])
    franc2=input("first franction: ").split("/")
    c=franc2[0]
    if(d!=1):
        d=int(franc2[1])
    ob=franction(a,b,c,d)
    print("""Enter the number of your sellection:
1.SUM
2.SUB
3.MUL
4.DIV
5.EXIT""")
    n=input()
    n=int(n)
    if(n>4):
        break
    elif(b==0 or d==0):
        print("Denominator can't be '0'")
    elif(n==1):
        ans=franction.sum(ob)
        print(ans)
    elif(n==2):
        print(franction.sub(ob))
    elif(n==3):
        print(franction.mul(ob))
    elif(n==4):
        print(franction.div(ob))