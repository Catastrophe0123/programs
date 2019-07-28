import PySimpleGUI as s

#layout = [[s.Text("TODO LIST ") , s.InputText("", key = "in")] , [s.Text(" ",key = "name", auto_size_text=False)],
 #         [s.Button("ok")] ,[ s.Exit() ]]
lis = []
#f = open("F:\\Navaneeth\College stuff\\asssignments and projects\programming\PySimpleGUI\\file.txt","w+")


def readFile(lis):
    with open("F:\\Navaneeth\College stuff\\asssignments and projects\programming\PySimpleGUI\\file.txt","r") \
            as f:
        if(lis == []):
            return lis
        lis = f.read().splitlines()
        print(lis)
    return lis

def writeToFile():
    with open("F:\\Navaneeth\College stuff\\asssignments and projects\programming\PySimpleGUI\\file.txt","w") \
            as f:
        for i in range(len(lis)):
            f.write(lis[i])
            f.write("\n")

lis = readFile(lis)
print("lis after reading : ",lis)
layout = [[s.Text("TODO LIST ")],[s.Text("New Entry : "),s.InputText("",key = "entry")],
          [s.Listbox(values=lis,key = "list",size=(60,6), enable_events=True)],
          [s.CalendarButton("Choose Date", target="dateDisp", key='date'),s.InputText("",key = "dateDisp",do_not_clear=False)],
          [s.Button("add"),s.Button("delete"),s.Button("prioritize"),s.Exit()],
          [s.Text("",auto_size_text=False,key = "tell")]]

window = s.Window("my first SGUI ",layout)

while True:
    event, entries = window.Read()
    print(event, entries)
    print("selected item " , entries["list"])
    print(lis, "before add ")

    if event is None or event == "Exit":
        break

    elif (event == "add"):
        print(entries["entry"],entries["dateDisp"])
        x = entries["entry"]+" "+entries["dateDisp"]
        lis.append(x)
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("item added")
        print(lis , " after add ")
        writeToFile()

    elif( event == "delete"):
        print(lis)
        print(''.join(entries["list"]), "will be deleted : ") #converting list to string
        lis.remove(''.join(entries["list"]))
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("item deleted")
        writeToFile()

    elif( event == "prioritize"):
        x = ""
        x = ''.join(entries["list"])
        lis.insert(0, lis.pop(lis.index(x)))
        print(lis)
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("item prioritized")
        writeToFile()

window.Close()

#calendar : https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Calendar.py

'''import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[sg.T('Calendar Test')],
          [sg.In('', size=(20,1), key='input')],
          [sg.CalendarButton('Choose Date', target='input', key='date')],
          [sg.Ok(key=1)]]

window = sg.Window('Calendar', grab_anywhere=False).Layout(layout)
event,values = window.Read()
sg.Popup(values['input'])
'''
