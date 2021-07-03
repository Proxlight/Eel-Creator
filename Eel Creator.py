import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

# Example
createFolder('./web/')
fin=open("index.html","r")
fout=open(".//web//main.js","a+")
fpy=open("app.py","a+")
count_Button=0
count_textbox=0


fpy.write('''import eel
eel.init('web')
''')



for line in fin :
    words=line.split()
    for i in words:
        if i==('''type="button"''') or i==('''type="submit"'''):
            count_Button+=1
            fpy.write('''
@eel.expose
def function'''+ str(count_Button) +'''(data'''+ str(count_Button)+ '''):
    pass
    ''')
            fout.write('''
function function'''+ str(count_Button) +'''() {
	eel.function'''+ str(count_Button) +'''(data'''+ str(count_Button) +''')(setImage)
}''')
        elif i == ('''type="text"''') or i==('''type="password"'''):
            count_textbox+=1
            fout.write('''\nvar data'''+ str(count_textbox) +''' = document.getElementById("data").value''')

fpy.write('''
eel.start('index.html', size=(1000, 600))'''
)