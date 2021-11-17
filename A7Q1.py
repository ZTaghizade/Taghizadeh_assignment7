import random
boys=[]
girls=[]
while(True):
    print("""MENU:
Enter the number of sellection:
1.Add new boy
2.Add new girl
3.Married
4.EXIT""")
    n=input()
    n=int(n)
    if(n>3):
        break
    elif(n==1):
        bname=input("Name: ")
        if(bname not in boys):
            boys.append(bname)
    elif(n==2):
        gname=input("Name: ")
        if(gname not in girls):
            girls.append(gname)
    elif(n==3):
        i=0
        result=[]
        brang=[]
        grang=[]
        j=0
        if(len(boys)!=0 and len(girls)!=0):
            if(len(boys)>len(girls)):
                ran=len(girls)
            else:
                ran=len(boys)
            while(j<ran):
                b=random.randint(0,len(boys)-1)
                g=random.randint(0,len(girls)-1)
                if((b not in brang) and (g not in grang)):
                    result.append([])
                    result[i].append(boys[b])
                    result[i].append(girls[g])
                    brang.append(b)
                    grang.append(g)
                    i+=1
                    j+=1
            print(result)