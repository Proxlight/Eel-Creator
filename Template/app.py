import eel
eel.init('web')

@eel.expose
def function1(data1,data2,data3):
    print(data1,data2,data3)
    
eel.start('index.html', size=(1000, 600))