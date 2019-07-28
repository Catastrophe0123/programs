import PySimpleGUI as s

lis = []

def readFile(lis):
    with open("F:\\Navaneeth\College stuff\\asssignments and projects\programming\PySimpleGUI\\file.txt","r") \
            as f:
        if(lis == []):
            return lis
        lis = f.read().splitlines()
    return lis

def writeToFile():
    with open("F:\\Navaneeth\College stuff\\asssignments and projects\programming\PySimpleGUI\\file.txt","w") \
            as f:
        for i in range(len(lis)):
            f.write(lis[i])
            f.write("\n")

lis = readFile(lis)
layout = [[s.Text("TODO LIST ")],[s.Text("New Entry : "),s.InputText("",key = "entry")],
          [s.Listbox(values=lis,key = "list",size=(60,6), enable_events=True)],
          [s.CalendarButton("Choose Date", target="dateDisp", key='date'),s.InputText("",key = "dateDisp",do_not_clear=False)],
          [s.Button("add"),s.Button("delete"),s.Button("prioritize"),s.Exit()],
          [s.Text("",auto_size_text=False,key = "tell")]]

window = s.Window("my first SGUI ",layout)

while True:
    event, entries = window.Read()

    if event is None or event == "Exit":
        break

    elif (event == "add"):
        x = entries["entry"]+" "+entries["dateDisp"]
        lis.append(x)
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("item added")
        writeToFile()

    elif( event == "delete"):
        lis.remove(''.join(entries["list"]))
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("item deleted")
        writeToFile()

    elif( event == "prioritize"):
        x = ""
        x = ''.join(entries["list"])
        lis.insert(0, lis.pop(lis.index(x)))
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("item prioritized")
        writeToFile()

window.Close()
