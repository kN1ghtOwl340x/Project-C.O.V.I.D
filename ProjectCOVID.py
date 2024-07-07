import mysql.connector as mycon
import time
from clrprint import *
import os
import pickle as pie
import csv
from mysql.connector import Error

try:
    path1='C:/Users/Public/'
    path2='Project Covid'
    path=os.path.join(path1,path2)
    os.mkdir(path)

except FileExistsError as exception:
    print()

try:
    path3='C:/Users/Public/Project Covid'
    path4='Biodata'
    path=os.path.join(path3,path4)
    os.mkdir(path)

except FileExistsError as exception:
    print()





password=input('Enter your MySQL client password: ')

clrprint("███████████                          ███                     █████         █████████        ███████       █████   █████    █████    ██████████",clr='r')
time.sleep(0.025)
clrprint("░███░░░░░███                        ░░░                     ░░███         ███░░░░░███     ███░░░░░███    ░░███   ░░███    ░░███    ░░███░░░░███ ",clr='r')
time.sleep(0.025)
clrprint("░███    ░███ ████████   ██████      █████  ██████   ██████  ███████      ███     ░░░     ███     ░░███    ░███    ░███     ░███     ░███   ░░███",clr='r')
time.sleep(0.025)
clrprint("░██████████ ░░███░░███ ███░░███    ░░███  ███░░███ ███░░███░░░███░      ░███            ░███      ░███    ░███    ░███     ░███     ░███    ░███",clr='r')
time.sleep(0.025)
clrprint("░███░░░░░░   ░███ ░░░ ░███ ░███     ░███ ░███████ ░███ ░░░   ░███       ░███            ░███      ░███    ░░███   ███      ░███     ░███    ░███",clr='r')
time.sleep(0.025)
clrprint("░███         ░███     ░███ ░███     ░███ ░███░░░  ░███  ███  ░███ ███   ░░███     ███   ░░███     ███      ░░░█████░       ░███     ░███    ███ ",clr='r')
time.sleep(0.025)
clrprint("█████        █████    ░░██████      ░███ ░░██████ ░░██████   ░░█████     ░░█████████  ██ ░░░███████░   ██    ░░███      ██ █████ ██ ██████████  ",clr='r')
time.sleep(0.025)
clrprint("░░░░        ░░░░░      ░░░░░░       ░███  ░░░░░░   ░░░░░░     ░░░░░       ░░░░░░░░░  ░░    ░░░░░░░    ░░      ░░░      ░░ ░░░░░ ░░ ░░░░░░░░░░   ",clr='r')
time.sleep(0.025)
clrprint("                                ███ ░███                                                                                                        ",clr='r')
time.sleep(0.025)
clrprint("                               ░░██████                                                                                                         ",clr='r')
time.sleep(0.025)
clrprint("                            ░░░░░░                                                                                                          ",clr='r')
time.sleep(0.025)
clrprint()
clrprint()
time.sleep(0.025)
clrprint("___       ___              ___              ___  ___     __      ___       __                     __   __       ",clr='p')
time.sleep(0.025)
clrprint(" |  |__| |__     |  | |     |  |  |\/|  /\   |  |__     |__) \ /  |  |__| /  \ |\ | __  |\/| \ / /__` /  \ |    ",clr='p')
time.sleep(0.025)
clrprint(" |  |  | |___    \__/ |___  |  |  |  | /~~\  |  |___    |     |   |  |  | \__/ | \|     |  |  |  .__/ \__X |___ ",clr='p')
time.sleep(0.025)
clrprint()                                                                                                            
clrprint(" __       ___       __        __   ___           ___  ___  __   ___       __   ___                              ",clr='p')
time.sleep(0.025)
clrprint("|  \  /\   |   /\  |__)  /\  /__` |__     | |\ |  |  |__  |__) |__   /\  /  ` |__                               ",clr='p')
time.sleep(0.025)
clrprint("|__/ /~~\  |  /~~\ |__) /~~\ .__/ |___    | | \|  |  |___ |  \ |    /~~\ \__, |___                              ",clr='p')
time.sleep(0.025)

                                                                                                               
clrprint()




def menu():

    
    clrprint("What do you want to do with the databases in your system?")
    clrprint("1) Add Data to a database\n2) Update your databases with new attributes and/or modify them\n3) Just see the data inside the databases.",clr='b')
    clrprint("4) Delete Data from your databases",clr='b')
    clrprint("5) BACK",clr='b')
    choice=int(clrinput("Enter the serial number of the option  you want to use: ",clr='y'))
    if choice==1:
        add_data()
    elif choice==2:
        update_data()
    elif choice==3:
        display_data()
    elif choice==4:
        delete_data()
    elif choice==5:
        return None
    else:
        clrprint("Invalid Choice",clr='r')

def display_data():
    
    clrprint('The Databases available in your system are....')
    mydb=mycon.connect(host='localhost',user='root',passwd=password)
    mycursor=mydb.cursor()
    mycursor.execute('show databases')
    dblist=[]
    templist=[]
    w=''
    q=''
    no=1
    for i in mycursor:
        clrprint(no,') ',i[0],clr='b')
        templist=i[0]
        dblist.append(templist)
        no+=1
    dbname=clrinput('Enter the name of the database you want to use: ',clr='y')
    for j in dblist:
        if dbname==j:
            clrprint('The following tables are present in the database ',dbname)
            mydb=mycon.connect(host='localhost',user='root',passwd=password,database=dbname)
            mycursor=mydb.cursor()
            mycursor.execute('show tables')
            no=1
            tablelist=[]
            for i in mycursor:
                clrprint(no,') ',i[0],clr='b')
                tablename=i[0]
                tablelist.append(tablename)
                no+=1
            f=clrinput('Enter the name of the table you want to use: ',clr='y')
            for l in tablelist:
                clrprint('What do you want to do with table:',clr='b')
                clrprint('1) See all the data inside it',clr='b')
                clrprint('2) See data of specific number of rows',clr='b')
                clrprint('3) See data of rows with conditions',clr='b')
                clrprint('4) See data of specific cloumn',clr='b')
                clrprint('5) See data of specific column with conditions',clr='b')
                clrprint('6) See table discription',clr='b')
                g=int(clrinput('Enter option number: ',clr='y'))

                #1) See all the data inside it
                if g==1:
                    mydb=mycon.connect(host='localhost',user='root',passwd=password,database=dbname)
                    mycursor=mydb.cursor()
                    mycursor.execute('select * from '+f)
                    col=mycon.connect(host='localhost',user='root',passwd=password,database=dbname)
                    colhead=col.cursor()
                    colhead.execute('desc '+f)
                    heading=[]
                    for qwe in colhead:
                        heading.append(qwe[0])
                    columnhead=tuple(heading)
                    clrprint(columnhead,clr='p')
                    results=mycursor.fetchall()
                    for m in results:
                        clrprint(m,clr='g')

                    #2) See data of specific number of rows'
                elif g==2:
                    x=int(clrinput('How many rows you want to see:  '))
                    my=mycon.connect(host='localhost',user='root',passwd=password,database=dbname)
                    mycurs=my.cursor()
                    mycurs.execute('select * from '+f)
                    col=mycon.connect(host='localhost',user='root',passwd=password,database=dbname)
                    colhead=col.cursor()
                    colhead.execute('desc '+f)
                    headin=[]
                    for qw in colhead:
                        headin.append(qw[0])
                    columnhea=tuple(headin)
                    clrprint(columnhea,clr='p')
                    results=mycurs.fetchmany(x)
                    for n in results:
                        clrprint(n,clr='g')

                  #3) See data of rows with conditions      
                elif g==3:
                    col=mycon.connect(host='localhost',user='root',passwd=password,database=dbname)
                    colhead=col.cursor()
                    colhead.execute('desc '+f)
                    headi=[]
                    clrprint('The available columns are:')
                    for ert in colhead:
                        headi.append(ert[0])
                        clrprint(ert[0],clr='b')
                    columnhe=tuple(headi)
                    y=int(clrinput('How many conditions: ',clr='y'))
                    for z in range(0,y):
                        u=clrinput('Enter conditons : ',clr='y')
                        w=w+u+' and '
                    lis=list(w)
                    for az in range(0,len(lis)-5):
                        q=q+lis[az]
                    my=mycon.connect(host='localhost',user='root',passwd=password,database=dbname)
                    mycurs=my.cursor()
                    mycurs.execute('select * from '+f+' where '+q)
                    clrprint(columnhe,clr='p')
                    results=mycurs.fetchall()
                    for th in results:
                        clrprint(th,clr='g')
                    break

                #4) See data of specific cloumn
                elif g==4:
                    clrprint('The available columns are: ')
                    my=mycon.connect(host='localhost',user='root',passwd=password,database=dbname)
                    mycurs=my.cursor()
                    col=mycon.connect(host='localhost',user='root',passwd=password,database=dbname)
                    colhead=col.cursor()
                    colhead.execute('desc '+f)
                    headis=[]
                    for qw in colhead:
                        headis.append(qw[0])
                    columnh=tuple(headis)
                    clrprint(columnh,clr='p')
                    collm=''
                    jik=''
                    sdc=int(clrinput('Enter number of columns you want to select:'))
                    for ol in range(0,sdc):
                        ccol=clrinput('Enter column name: ',clr='y')
                        collm=collm+ccol+','
                    lis1=list(collm)
                    for dsf in range(0,len(lis1)-1):
                        jik=jik+lis1[dsf]
                    spl=jik.split(',')
                    tspl=tuple(spl)
                    clrprint(tspl,clr='p')
                    mycurs.execute("select "+jik+" from "+f)
                    for answ in mycurs:
                        clrprint(answ,clr='g')

                #5) See data of specific column with conditions
                elif g==5:
                    clrprint('The available columns are: ')
                    my=mycon.connect(host='localhost',user='root',passwd=password,database=dbname)
                    mycurs=my.cursor()
                    col=mycon.connect(host='localhost',user='root',passwd=password,database=dbname)
                    colhead=col.cursor()
                    colhead.execute('desc '+f)
                    headisj=[]
                    for qwdf in colhead:
                        headisj.append(qwdf[0])
                    columnhj=tuple(headisj)
                    clrprint(columnhj,clr='p')
                    collm=''
                    jik=''
                    sdc=int(clrinput('Enter number of columns you want to select:',clr='y'))
                    for ol in range(0,sdc):
                        ccol=clrinput('Enter column name: ',clr='y')
                        collm=collm+ccol+','
                    lis1=list(collm)
                    for dsf in range(0,len(lis1)-1):
                        jik=jik+lis1[dsf]
                    spl=jik.split(',')
                    tspl=tuple(spl)
                    y=int(clrinput('How many conditions: ',clr='y'))
                    for z in range(0,y):
                        u=clrinput('Enter conditons : ',clr='y')
                        w=w+u+' and '
                    lis=list(w)
                    for az in range(0,len(lis)-5):
                        q=q+lis[az]
                    mycurs.execute('select '+jik+' from '+f+" where "+q)
                    clrprint(tspl,clr='p')
                    for i in mycurs:
                        clrprint(i,clr='g')

                #6) See table discription
                elif g==6:
                    my=mycon.connect(host='localhost',user='root',passwd=password,database=dbname)
                    mycurs=my.cursor()
                    mycurs.execute('desc '+f)
                    clrprint('The discription of table is: ')
                    for i in mycurs:
                        clrprint(i,clr='r')
                break
            break
        
    else:
        clrprint('Database Not Available.',clr='r')
        
def add_data():
    
    clrprint('1) Create a new database.',clr='b')
    clrprint('2) Add data in existing database.',clr='b')
    x=int(clrinput('Enter your choice (enter option number): ',clr='y'))


    if x==1:
        try:
            myd=mycon.connect(host='localhost',user='root',passwd=password)
            mycurso=myd.cursor()
            z=clrinput('What name do you want to give the database: ',clr='y')
            mycurso.execute('show databases')
            if z in mycurso:
                clrprint('Database of the same name is already present.',clr='r')
                

            else:
                mycurso.execute('create database '+z)
                clrprint('Database created.',clr='g')
                clrprint('1) Do you want to add values in the created database.',clr='b')
                clrprint('2) Do you want to stop adding the data.',clr='b')
                y=int(clrinput('Enter option number: ',clr='y'))
                
                if y==1:
                    my=mycon.connect(host='localhost',user='root',passwd=password,database=z)
                    mycurs=my.cursor()
                    q=clrinput('Enter the name of the table: ',clr='y')
                    t=''
                    w=int(clrinput('Enter the number of columns you want to add in table: ',clr='y'))
                    for e in range(1,w+1):
                        p=str(e)
                        r=clrinput('Enter information of column '+p+': ',clr='y')
                        t=t+r+','
                        o=''
                    for u in range(0,len(t)-1):
                        o=o+t[u]
                    mycurs.execute('Create table '+q+'('+o+')')
                    c=o.split(',')
                    n=''
                    for v in range(0,len(c)):
                        b=c[v].split()
                        n=n+b[0]+','
                    Q=''
                    for m in range(0,len(n)-1):
                        Q=Q+n[m]
                    clrprint('Table created.',clr='g')
                    clrprint('1) Do you want to add values of row in the created table.',clr='b')
                    clrprint('2) Do you want to stop adding data.',clr='b')
                    a=int(clrinput('Enter your choice :',clr='y'))
                    f=tuple(o.split(','))
                    if a==1:
                        s=int(clrinput('Enter how many rows of value do you want to add: ',clr='y'))
                        for d in range(1,s+1):
                            clrprint('For row number ',d,' enter value: ',clr='y')
                            h=''
                            for g in range(0,len(f)):
                                j=clrinput('Enter data for column \''+f[g]+'\': ',clr='y')
                                j="'"+j+"'"
                                h=h+j+','
                            l=''
                            for k in range(0,len(h)-1):
                                l=l+h[k]
                            mycurs.execute("Insert into "+q+"("+Q+")  values ("+l+")")
                            my.commit()
                        clrprint('Values inserted.',clr='g')
                    elif a==2:
                        clrprint('Data addition operation terminated',clr='g')
                    else:
                        clrprint('Inavlid option',clr='r')
                elif y==2:
                    clrprint('Data addition operation terminated',clr='g')
                else:
                    clrprint('Invalid option.',clr='r')

        except mycon.Error as error:
            print("Failed to add data {}".format(error))

                
    elif x==2:
        mydb=mycon.connect(host='localhost',user='root',passwd=password)
        mycursor=mydb.cursor()
        mycursor.execute('show databases')
        no=1
        a=[]
        for i in mycursor:
            clrprint(no,') ',i[0])
            b=i[0]
            a.append(b)
            no+=1
        W=clrinput('In which database do you want to add the data: ',clr='y')
        for w in a:
            if W==w:
                try:
                    my=mycon.connect(host='localhost',user='root',passwd=password,database=W)
                    mycurs=my.cursor()
                    clrprint('1) Do you want to add data in a new table.',clr='b')
                    clrprint('2) Do you want to add data in an existing table.',clr='b')
                    e=int(clrinput('Enter your option number :',clr='y'))
                    if e==1:
                        q=clrinput('Enter the name of the table: ',clr='y')
                        t=''
                        w=int(clrinput('Enter the number of columns you want to add in table: ',clr='y'))
                        for WE in range(1,w+1):
                            p=str(WE)
                            r=clrinput('Enter information of column '+p+': ',clr='y')
                            t=t+r+','
                        o=''
                        for u in range(0,len(t)-1):
                            o=o+t[u]
                        mycurs.execute('Create table '+q+'('+o+')')
                        c=o.split(',')
                        n=''
                        for v in range(0,len(c)):
                            b=c[v].split()
                            n=n+b[0]+','
                        Q=''
                        for m in range(0,len(n)-1):
                            Q=Q+n[m]
                        clrprint('Table created.',clr='g')
                        clrprint('1) Do you want to add values of row in the created table.',clr='b')
                        clrprint('2) Do you want to stop adding data.',clr='b')
                        a=int(clrinput('Enter your choice :',clr='y'))
                        f=tuple(o.split(','))
                        if a==1:
                            s=int(clrinput('Enter how many rows of value do you want to add: ',clr='y'))
                            for d in range(1,s+1):
                                clrprint('For row number ',d,' enter value: ',clr='p')
                                h=''
                                for g in range(0,len(f)):
                                    j=clrinput('Enter data for column \''+f[g]+'\': ',clr='y')
                                    j="'"+j+"'"
                                    h=h+j+','
                                l=''
                                for k in range(0,len(h)-1):
                                    l=l+h[k]
                                mycurs.execute("Insert into "+q+"("+Q+")  values ("+l+")")
                                my.commit()
                            clrprint('Values inserted.',clr='g')
                    elif e==2:
                        myd=mycon.connect(host='localhost',user='root',passwd=password,database=W)
                        mycurso=myd.cursor()
                        mycurso.execute('show tables')
                        non=1
                        aa=[]
                        for i in mycurso:
                            clrprint(non,') ',i[0],clr='b')
                            bb=i[0]
                            aa.append(bb)
                            no+=1
                        E=clrinput('Enter the name of the table you want to add the data in: ',clr='y')
                        mycurso.execute('desc '+E)
                        Y=[]
                        I=''
                        clrprint('The columns in table ',E,' are: ')
                        for T in mycurso:
                            I=I+T[0]+','
                            clrprint(T[0]+','+str(T[1]),clr='p')
                        o=''
                        for u in range(0,len(I)-1):
                            o=o+I[u]
                        c=o.split(',')
                        n=''
                        for v in range(0,len(c)):
                            b=c[v].split()
                            n=n+b[0]+','
                        Q=''
                        for m in range(0,len(n)-1):
                            Q=Q+n[m]
                        f=tuple(o.split(','))            
                        s=int(clrinput('Enter how many rows of value do you want to add: ',clr='y'))
                        for d in range(1,s+1):
                            clrprint('For row number ',d,' enter value: ',clr='y')
                            h=''
                            for g in range(0,len(f)):
                                j=clrinput('Enter data for column \''+f[g]+'\': ',clr='y')
                                j="'"+j+"'"
                                h=h+j+','
                            l=''
                            for k in range(0,len(h)-1):
                                l=l+h[k]
                            mycurso.execute("insert into "+E+"("+Q+")  values ("+l+")")
                            myd.commit()
                        clrprint('Values inserted.',clr='g')

                except mycon.Error as error:
                    print("Failed to add data {}".format(error))

                        
    else:
        clrprint('Invalid option',clr='r')
    
                                                                                                                                          
def update_data():
    
    clrprint('1. Do you want to update the data.',clr='b')
    clrprint('2. Do you want to alter the data.',clr='b')
    q=int(clrinput('Enter option number: ',clr='y'))
    if q==1:
        e=1
        r=[]
        mydb=mycon.connect(host='localhost',user='root',passwd=password)
        mycursor=mydb.cursor()
        mycursor.execute('show databases')
        clrprint('Data of which database you want to update: ')
        for w in mycursor:
            clrprint(e,') ',w[0],clr='b')
            r.append(w[0])
            e+=1
        t=clrinput('Enter database name: ',clr='y')
        for y in r:
            if t==y:
                clrprint('Data of which table do you want to update: ')
                myd=mycon.connect(host='localhost',user='root',passwd=password,database=t)
                mycurso=myd.cursor()
                mycurso.execute('show tables')
                u=1
                i=[]
                for o in mycurso:
                    clrprint(u,') ',o[0],clr='b')
                    i.append(o[0])
                    u+=1
                p=clrinput('Enter the name of table you want to update: ',clr='y')
                for a in i:
                    if p==a:
                        mycurso.execute('desc '+p)
                        f=[]
                        for d in mycurso:
                            f.append(d[0])
                        g=tuple(f)
                        clrprint(g,clr='p')
                        mycurso.execute('select * from '+p)
                        for s in mycurso:
                            clrprint(s,clr='g')
                        h=int(clrinput('Data of how many columns you want to change: ',clr='y'))
                        l=''
                        for j in range(1,h+1):
                            W=str(j)
                            k=clrinput('Enter the name of column '+W+' and what value do you want to give it: ',clr='y')
                            l=l+k+','
                        x=''
                        for z in range(0,len(l)-1):
                            x=x+l[z]
                        c=int(clrinput('How many conditions do you want to give: ',clr='y'))
                        n=''
                        for v in range(1,c+1):
                            R=str(v)
                            b=clrinput('Enter condition number '+R+': ',clr='y')
                            n=n+b+','
                        Q=''
                        for m in range(0,len(n)-1):
                            Q=Q+n[m]
                        mycurso.execute('update '+p+' set '+x+' where '+Q)
                        myd.commit()
                        clrprint('Table updated.',clr='g')
                        break
                else:
                    clrprint('Table not available.',clr='r')
                    break
                break
        else:
            clrprint('Database not available',clr='r')
            
    elif q==2:
        e=1
        r=[]
        mydb=mycon.connect(host='localhost',user='root',passwd=password)
        mycursor=mydb.cursor()
        mycursor.execute('show databases')
        clrprint('Data of which database you want to alter: ')
        for w in mycursor:
            clrprint(e,') ',w[0],clr='b')
            r.append(w[0])
            e+=1
        t=clrinput('Enter database name: ',clr='y')
        for y in r:
            if t==y:
                clrprint('Data of which table do you want to alter: ')
                myd=mycon.connect(host='localhost',user='root',passwd=password,database=t)
                mycurso=myd.cursor()
                mycurso.execute('show tables')
                u=1
                i=[]
                for o in mycurso:
                    clrprint(u,') ',o[0],clr='b')
                    i.append(o[0])
                    u+=1
                p=clrinput('Enter the name of table you want to alter: ',clr='y')
                for a in i:
                    if p==a:
                        mycurso.execute('desc '+p)
                        f=[]
                        for d in mycurso:
                            f.append(d[0])
                        g=tuple(f)
                        clrprint(g,clr='p')
                        mycurso.execute('select * from '+p)
                        for s in mycurso:
                            clrprint(s,clr='g')
                        clrprint('1) Do you want to change the column name.',clr='b')
                        clrprint('2) Do you to change the datatype of a column.',clr='b')
                        clrprint('3) Do you want to add a new column.',clr='b')
                        h=int(clrinput('Enter your choice: ',clr='y'))
                        if h==1:
                            j=clrinput('Enter the name of the column you want to change: ',clr='y')
                            for k in g:
                                if j==k:
                                    l=clrinput('Enter what name do you want to give: ',clr='y')
                                    mycurso.execute('alter table '+p+' rename column '+j+' to '+l)
                                    myd.commit()
                                    clrprint('Name changed.',clr='g')
                                    break
                            else:
                                clrprint('Column not available.',clr='r')
                            
                        elif h==2:
                            mycurso.execute('desc '+p)
                            x=''
                            clrprint('The columns with their current datatypes are: ')
                            for c in mycurso:
                                x=c[0]+' '+str(c[1])+' '+c[3]
                                clrprint(x,clr='b')
                            j=clrinput('Enter the name of the column you want to change: ',clr='y')
                            for k in g:
                                if j==k:
                                    l=clrinput('What data type do you want to give: ',clr='y')
                                    mycurso.execute('alter table '+p+' modify '+j+' '+l)
                                    myd.commit()
                                    clrprint('Datatype changed.',clr='g')
                                    break
                            else:
                                clrprint('Column not available.',clr='r')

                        elif h==3:
                            j=clrinput('Enter the name of the column you want to add: ',clr='y')
                            for k in g:
                                if j==k:
                                    clrprint('Column already present',clr='r')
                                    break
                            else:
                                l=clrinput('Enter what datatype do you want to give: ',clr='y')
                                mycurso.execute('alter table '+p+' add '+j+' '+l)
                                myd.commit()
                                clrprint('Column added.',clr='g')
                        else:
                            clrprint('Option not available.',clr='r')

                        break
                else:
                    clrprint('Table not available.',clr='r')
                    break
                break
        else:
            clrprint('Database not available.',clr='r')
                
    else:
        clrprint('Option not available.',clr='r')                                                                                                         


def delete_data():
    
    clrprint('1) Do you want to drop a database.',clr='b')
    clrprint('2) Do you want to drop a table.',clr='b')
    clrprint('3) Do you want to delete the content of a table.',clr='b')
    q=int(clrinput('Enter your choice: ',clr='y'))
    mydb=mycon.connect(host='localhost',user='root',passwd=password)
    mycursor=mydb.cursor()
    mycursor.execute('show databases')
    if q==1:
        e=1
        t=[]
        for w in mycursor:
            clrprint(e,') ',w[0],clr='b')
            t.append(w[0])
            e+=1
        r=clrinput('Which database do you want to drop: ',clr='y')
        for y in t:
            if r==y:
                mycursor.execute('Drop database '+r)
                mydb.commit()
                clrprint('Database dropped.',clr='g')
                break
        else:
            clrprint('Database not avaiable.',clr='r')
    elif q==2:
        e=1
        t=[]
        for w in mycursor:
            clrprint(e,') ',w[0],clr='b')
            t.append(w[0])
            e+=1
        r=clrinput('Table of which database do you want to drop: ',clr='y')
        for y in t:
            if r==y:
                myd=mycon.connect(host='localhost',user='root',passwd=password,database=r)
                mycurso=myd.cursor()
                mycurso.execute('show tables')
                i=1
                o=[]
                for u in mycurso:
                    clrprint(i,') ',u[0],clr='b')
                    o.append(u[0])
                    i+=1
                p=clrinput('Enter which table do you want to drop: ',clr='y')
                for a in o:
                    if p==a:
                        mycurso.execute('Drop table '+p)
                        myd.commit()
                        clrprint('Table dropped.',clr='g')
                        break
                else:
                    clrprint('Table not available.',clr='r')
                break
        else:
            clrprint('Database not avaiable.',clr='r')

        

    elif q==3:
        e=1
        t=[]
        for w in mycursor:
            clrprint(e,') ',w[0],clr='b')
            t.append(w[0])
            e+=1
        r=clrinput('Data of table of which database do you want to delete: ',clr='y')
        for y in t:
            if r==y:
                myd=mycon.connect(host='localhost',user='root',passwd=password,database=r)
                mycurso=myd.cursor()
                mycurso.execute('show tables')
                i=1
                o=[]
                for u in mycurso:
                    clrprint(i,') ',u[0],clr='b')
                    o.append(u[0])
                    i+=1
                p=clrinput('Data of which table do you want to delete: ',clr='y')
                for a in o:
                    if p==a:
                        clrprint('1) Do you to delete the whole content of table.',clr='b')
                        clrprint('2) Do you to specific rows of the table.',clr='b')
                        h=int(clrinput('Enter your choice: ',clr='y'))
                        if h==2:
                            mycurso.execute('desc '+p)
                            s=[]
                            for f in mycurso:
                                s.append(f[0])
                            d=tuple(s)
                            clrprint(d,clr='p')
                            mycurso.execute('Select * from '+p)
                            for g in mycurso:
                                clrprint(g,clr='g')
                            j=int(clrinput('Enter no of conditions: ',clr='y'))
                            x=''
                            for k in range(1,j+1):
                                z=str(k)
                                l=clrinput('Enter condition number '+z+': ',clr='y')
                                x=x+l+' or '
                            v=''
                            for c in range(0,len(x)-4):
                                v=v+x[c]
                            mycurso.execute('delete from '+p+' where '+v)
                            myd.commit()
                            clrprint('Data deleted.',clr='g')
                        if h==1:
                            mycurso.execute('delete from '+p)
                            myd.commit()
                            clrprint('Data deleted.',clr='g')
                        else:
                            clrprint('Option not available.',clr='r')
                            
                        
                        break
                else:
                    clrprint('Table not available.',clr='r')
                break
        else:
            clrprint('Database not available.',clr='r')

        




    else:
        clrprint('Option not available.',clr='r')
    

def file():
    try:
        q=0
        clrprint("1) Do you want to create a new file.\n2) Do you want to add values in an existing file.\n3) Do you want to retrieve information from a certain file.\n4) BACK",clr='b')
        try:
            q=int(clrinput('Enter your option: ',clr='y'))
        except:
            print("Invalid Input")
        if q==1:
            clrprint('1) Do you want to create a text file.\n2) Do you want to create a binary file.\n3) Do you want to create a Microsoft Excel file.',clr='b')
            option=int(clrinput('Enter your choice: ',clr='y'))

            if option==1:
                qwe=clrinput('What name do you want to give the file: ',clr='y')
                w="C:\\Users\\Public\\Project Covid\\"+qwe
                f1=open(w+'.txt',"w+")
                clrprint('File created.',clr='g')
                clrprint('1) Do you want add value in the created file.\n2) Do you want to stop.',clr='b')
                e=int(clrinput('Enter your choice: ',clr='y'))

                if e==1:
                    r=int(clrinput("How many lines do you want to add: ",clr='y'))

                    for t in range(1,r+1):
                        u=str(t)
                        y=clrinput("Enter data for line "+u+': ',clr='y')
                        f1.write(y+'\n')
                    clrprint('Data added',clr='g')
                    f1.close()
                elif e==2:
                    clrprint('Addition of data executed.',clr='g')
                    f1.close()



            elif option==2:
                qwe=clrinput('What name do you want to give the file: ',clr='y')
                w="C:\\Users\\Public\\Project Covid\\"+qwe
                f1=open(w+'.log',"w+b")
                clrprint('File created.',clr='g')
                clrprint('1) Do you want add value in the created file.\n2) Do you want to stop.',clr='b')
                e=int(clrinput('Enter your choice: ',clr='y'))

                if e==1:
                    r=int(clrinput("How many lines do you want to add: ",clr='y'))

                    for t in range(1,r+1):
                        u=str(t)
                        y=clrinput("Enter data for line "+u+': ',clr='y')
                        pie.dump(y,f1)
                    clrprint('Data added',clr='g')
                    f1.close()
                elif e==2:
                    clrprint('Addition of data executed.',clr='g')
                    f1.close()



            elif option==3:
                qwe=clrinput('What name do you want to give the file: ',clr='y')
                w="C:\\Users\\Public\\Project Covid\\"+qwe
                f1=open(w+'.csv',"w+")
                csvwriter=csv.writer(f1,lineterminator='\r')
                clrprint('File created.',clr='g')
                clrprint('1) Do you want add value in the created file.\n2) Do you want to stop.',clr='b')
                e=int(clrinput('Enter your choice: ',clr='y'))

                if e==1:
                    r=[]
                    
                    y=int(clrinput('Enter the number of columns you want to add: ',clr='y'))
                    for u in range(1,y+1):
                        i=str(u)
                        o=clrinput('Enter the name of columns '+i+': ',clr='y')
                        r.append(o)
                    csvwriter.writerow(r)
                    
                    p=int(clrinput('Enter the number of rows you want to add: ',clr='y'))
                    for a in range(1,p+1):
                        t=[]
                        clrprint('For row number ',a,' enter value: ',clr='y')
                        for s in range(0,len(r)):
                            d=clrinput('Enter value for \''+r[s]+'\': ')
                            t.append(d)
                        csvwriter.writerow(t)
                    clrprint('Data added.',clr='g')
                f1.close()
                    
                
            else:
                clrprint('Invalid Option',clr='r')


        elif q==3:
            clrprint('From which file do you want to retrieve data: ',clr='b')
            location=os.listdir("C:\\Users\\Public\\Project Covid")
            location.remove('Biodata')
            for i in location:
                clrprint(i)
            qwe=clrinput('Enter file name: ',clr='y')
            w="C:\\Users\\Public\\Project Covid\\"+qwe
            m=w.split('.')

            
            if 'txt'in m:
                f1=open(w,"r")
                clrprint('1) Do you want to retrieve all the data.\n2) Do you want to retrieve data till certain line\n3) Do you want to retrive data till some number of element.',clr='b')

                e=int(clrinput('Enter your choice: ',clr='y'))

                if e==1:
                    f2=f1.read()
                    clrprint('The data is....')
                    clrprint(f2,clr='g')

                elif e==3:
                    r=int(clrinput('How many element you want to see: ',clr='y'))
                    f2=f1.read(r)
                    clrprint('The data is....')
                    clrprint(f2,clr='g')

                elif e==2:
                    r=int(clrinput('Enter number of lines: ',clr='y'))
                    f2=f1.readlines()
                    clrprint('The data is.....')
                    for t in range(0,r):
                        clrprint(f2[t],clr='g')

                else:
                    clrprint('Invalid option.',clr='r')
                f1.close()


            elif 'log' in m:
                f1=open(w,"rb")
                clrprint('1) Do you want to retrieve all the data.\n2) Do you want to retrieve data till certain line.',clr='b')
                t=int(clrinput('Enter your choice: ',clr='y'))
                
                if t==1:
                    clrprint('The data is.....')
                    for r in range(0,len(f1.read())):
                        try:
                            f2=pie.load(f1)
                            clrprint(f2,clr='g')
                        except Exception as e:
                            break
                elif t==2:
                    y=int(clrinput('Enter number of lines: ',clr='y'))
                    clrprint('The data is.....')
                    for r in range(0,y):
                        try:
                            f2=pie.load(f1)
                            clrprint(f2,clr='g')
                        except Exception as e:
                            break
                else:
                    clrprint('Invalid option',clr='r')
                f1.close()
                

            elif 'csv' in m:
                f1=open(w,'r')
                reader=csv.reader(f1)
                clrprint('The data is.....')

                t=[]
                
                for i in reader:
                    t.append(i)

                clrprint(t[0],clr='p')
                for o in range(1,len(t)):
                    clrprint(t[o],clr='g')
                f1.close()

        elif q==2:
            clrprint('In which file do you want to data: ',clr='b')
            location=os.listdir("C:\\Users\\Public\\Project Covid")
            location.remove('Biodata')
            for i in location:
                clrprint(i)
            qwe=clrinput('Enter file name: ',clr='y')
            w="C:\\Users\\Public\\Project Covid\\"+qwe
            m=w.split('.')

            if 'txt' in m:
                f1=open(w,'a+')
                r=int(clrinput("How many lines do you want to add: ",clr='y'))

                for t in range(1,r+1):
                    u=str(t)
                    y=clrinput("Enter data for line "+u+': ',clr='y')
                    f1.write(y+'\n')
                clrprint('Data added.',clr='g')
                f1.close()

            elif 'log' in m:
                f1=open(w,'a+b')
                
                r=int(clrinput("How many lines do you want to add: ",clr='y'))

                for t in range(1,r+1):
                    u=str(t)
                    y=clrinput("Enter data for line "+u+': ',clr='y')
                    pie.dump(y,f1)
                clrprint('Data added.',clr='g')
                f1.close()

            else:
                clrprint('Value can\'t be added in the file or file not present.',clr='r')

        elif q==4:
            return None
        else:
            clrprint('Invalid Option.',clr='r')
    except ValueError as error:
        print(' {}'.format(error))

def qwerty():

    try:
        sql=mycon.connect(host='localhost',user='root',passwd=password)
        curs=sql.cursor()

        
        curs.execute('create database Employee')
        sql.commit()

        

    except mycon.Error as error:
        clrprint()

    try:
        conn = mycon.connect(host='localhost',database='EMPLOYEE', user='root', passwd=password)
        cur=conn.cursor()
        cur.execute('create table employee(emp_id int,name varchar(20),photo longblob,biodatafile longblob)')
        conn.commit()

    except mycon.Error as error:
        clrprint()
        
    



    
    # Convert digital data to binary format
    def ConversionToBinary(filename):
        with open(filename, 'rb') as file:
            BinaryFile = file.read()
        return BinaryFile

    def addblob(emp_id, name, photo, biodatafile):
        clrprint("Inserting BLOB into Employee Table",clr='y')
        try:
            connection = mycon.connect(host='localhost',database='EMPLOYEE', user='root', passwd=password)
            cursor = connection.cursor()
            query = """ INSERT INTO Employee(emp_id, name, photo, biodatafile) VALUES (%s,%s,%s,%s)"""

            empPic = ConversionToBinary(photo)
            file = ConversionToBinary(biodatafile)
            insert_blob_query = (emp_id, name, empPic, file)
            result = cursor.execute(query, insert_blob_query)
            connection.commit()
            clrprint("Image and file inserted successfully as a BLOB into Employee table", result,clr='g')

        except mycon.Error as error:
            clrprint("Failed inserting BLOB data into MySQL table {}".format(error),clr='r')
        if connection.is_connected():
            cursor.close()
            connection.close()
            



    # Convert binary data to normal format and write it on Disk
    

    def getblob(emp_id):
        clrprint("Reading BLOB data from Employee table",clr='y')

        try:
            connection = mycon.connect(host='localhost', database='EMPLOYEE', user='root', passwd=password)
            cursor = connection.cursor()
            alpha=str(emp_id)
            beta="Select * from employee where emp_id='"+alpha+"'"
            query = beta

            
            cursor.execute(query)
            record = cursor.fetchall()
            for i in record:
                clrprint("Id = ", i[0],clr='b' )
                clrprint("Name = ", i[1],clr='b')
                image = i[2]
                file = i[3]
                
                clrprint("Stored employee image and bio-data on disk.",clr='g')
                clrprint("Data saved in folder C:\\Users\\Public\\Project Covid\\Biodata ",clr='g')
                with open("C:\\Users\\Public\\Project Covid\\Biodata\\Photo.png", 'wb') as f1:
                    f1.write(image)

                with open('C:\\Users\\Public\\Project Covid\\Biodata\\Biodata.log','wb') as f2:
                    f2.write(file)
                

        except mycon.Error as error:
            clrprint("Failed to read BLOB data from MySQL table {}".format(error),clr='r')
        if connection.is_connected():
                cursor.close()
                connection.close()
                
            
    
    # main
    try:
        clrprint("This is an option provided for small businesses to manage their employee details as a file with their pictures.")
        clrprint("You will be able to add images and biodata of your employees directly into the Employee table.")
        clrprint("(1)To insert biodata and pictures into the Employee table",clr='b')
        clrprint("(2)To retrieve biodata and pictures from the Employee table",clr='b')
        choice=int(clrinput("Enter your choice : ",clr='y'))

        if choice==1:
            emp_id=int(clrinput("Enter Employee ID : ",clr='y'))
            name=clrinput("Enter name of employee : ",clr='y')
            empPic=clrinput("Enter the complete location of the employee's image on your disk : ",clr='y')
            file=clrinput("Enter the complete location of the file containing the employee's biodata : ",clr='y')
            addblob(emp_id,name,empPic,file)

        elif choice==2:
            emp_id=int(clrinput("Enter the id of the employee whose image and biodata you want to retrieve: ",clr='y'))
            getblob(emp_id)
        else:
            clrprint("INVALID OPTION",clr='r')
    except ValueError as error:
        print(' {}'.format(error))


trip=True
while trip==True:
    clrprint('1) Do you want to use MySQL.\n2) Do you want to use filehandling.\n3) Do you want to add/see information regarding a person.\n4) EXIT',clr='b')
    tycoon=int(clrinput('Enter your choice: ',clr='y'))

    if tycoon==1:
        y=True
        menu()
        while y==True:
                
            trip2=clrinput("Do you want to repeat the program?Type Y/N :")
            affirmative=['y','Y',"YES","yes","Yes"]
            if trip2 in  affirmative:
                menu()
            else:                
                y=False
                    
    elif tycoon==2:
        y=True
        file()
        while y==True:
            trip2=clrinput("Do you want to repeat the program?Type Y/N :")
            affirmative=['y','Y',"YES","yes","Yes"]
            if trip2 in  affirmative:
                file()
            else:
                y=False

    elif tycoon==3:
        y=True
        qwerty()
        while y==True:
                
            trip2=clrinput("Do you want to repeat the program?Type Y/N :")
            affirmative=['y','Y',"YES","yes","Yes"]
            if trip2 in  affirmative:
                qwerty()
            else:                
                y=False
        
        
    elif tycoon==4:
        clrprint("                ___                    __   ___     __           ",clr='p')
        clrprint("|__|  /\  \  / |__      /\     |\ | | /  ` |__     |  \  /\  \ / ",clr='p')
        clrprint("|  | /~~\  \/  |___    /~~\    | \| | \__, |___    |__/ /~~\  |  ",clr='p')
        clrprint("Please close this window")
        trip=False

    else:
        clrprint('Invalid Option.',clr='r')          
    
