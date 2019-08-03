import PySimpleGUI as s
import sqlite

sqlite.createTable()
lis = []
completed = []
lis = sqlite.readTable()
completed = sqlite.readCompleted()
layout = [[s.Text("TODO LIST ",pad= ((250,100),(0,0)))],[s.Text("New Entry : "),s.InputText("",key = "entry")],
          [s.Listbox(values=lis,key = "list",size=(40,6), enable_events=True) , s.Listbox(values=completed,key = "complete",size=(40,6), enable_events=True)],
          [s.CalendarButton("Choose Date", target="dateDisp", key='date'),s.InputText("",key = "dateDisp", disabled=True ,do_not_clear=False)],
          [s.Slider(range=(5,1,-1),default_value=5,orientation="horizontal",key="priority")],
          [s.Button("add"),s.Button("delete"),s.Button("prioritize"),s.Button("completed"),s.Exit()],
          [s.Text("", auto_size_text=False, key="tell")]]

window = s.Window("my first GUI ", layout)

while True:
    event, entries = window.Read()
    print(event, entries)
    if event is None or event == "Exit":
        break

    elif (event == "add"):
        if(entries["dateDisp"] == ""):
            window.Element("tell").Update("Please input a date")
            continue
        x = entries["entry"]+" "+entries["dateDisp"]+" "+str(int(entries["priority"]))
        lis.append(x)
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("item added")
        sqlite.addEvent(lis) #working

    elif( event == "delete"):
        print("delete pass argument :  :ASD sad :",''.join(entries["list"]))
        lis.remove(''.join(entries["list"]))
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("item deleted")
        sqlite.deleteEvent(''.join(entries["list"])) #working

    elif( event == "prioritize"):
        for i in range(len(lis)):
            min = i
            for j in range(i+1, len(lis)):
                if(lis[min][-1] > lis[j][-1]):
                    min = j
            lis[i],lis[min] = lis[min],lis[i]
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("prioritized")
        #sqlite.writeToFile(lis) #working

    elif( event == "completed"):
        lis.remove(''.join(entries["list"]))
        completed.append(''.join(entries["list"]))
        window.FindElement("list").Update(lis)
        window.FindElement("complete").Update(completed)
        window.Element("tell").Update("item completed")
        sqlite.completedEvent(''.join(entries["list"])) #working



window.Close()
