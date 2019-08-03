import sqlite3 as a
db = a.connect("todo")

def createTable():
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS todolist(event TEXT, date TEXT, priority TEXT,
     completed TEXT DEFAULT 0)''')
    print(cursor.fetchall())
    db.commit()
    cursor.close()

def readTable():
    cursor = db.cursor()
    cursor.execute('''select event, date, priority from todolist where completed = 0''')
    #cursor.execute('''select event, date, priority from todolist where completed = 0''')
    lst = cursor.fetchall()
    print(lst)
    y = ""
    lst1 = []
    for k in lst:
        y=''
        for i in k:
            for j in i:
                y+= j
            y += " "
        lst1.append(y.strip())
    db.commit()
    cursor.close()
    return lst1

def readCompleted():
    cursor = db.cursor()
    cursor.execute("select event, date, priority from todolist where completed = 1")
    lst = cursor.fetchall()
    y = ""
    lst1 = []
    for k in lst:
        y=''
        for i in k:
            for j in i:
                y+= j
            y += " "
        lst1.append(y.strip())
    db.commit()
    cursor.close()
    return lst1

def deleteTable():
    cursor = db.cursor()
    cursor.execute("delete from todolist")
    db.commit()
    cursor.close()

def addEvent(lst):
    cursor = db.cursor()
    y= ''
    #lst = ['qwe 123 1', 'qswe 123 12']
    for i in range(len(lst)):
        y  =''
        y = lst[i].split()
        print("y = ",y)
    cursor.execute('insert into todolist(event,date,priority) values(?,?,?)',(y[0],y[1],y[3]))
    cursor.execute('select event, date, priority from todolist')
    print("inter " ,cursor.fetchall())
    db.commit()
    cursor.close()

def deleteEvent(x):
    #x is string-  event
    cursor = db.cursor()
    y=''
    y = x.split()
    print(" y is : ",y)
    print(type(y))
    cursor.execute('delete from todolist where event = ?',(y[0],))
    db.commit()
    cursor.close()

def completedEvent(x):
    cursor = db.cursor()
    print("x is : ",x)
    y = ''
    y = x.split()[0]
    #update tablename set event =  where id =
    cursor.execute('update todolist set completed = \'1\' where event = ? ',(y,))
    cursor.execute('select * from todolist')
    print("completed check : ", cursor.fetchall())
    db.commit()
    cursor.close()
