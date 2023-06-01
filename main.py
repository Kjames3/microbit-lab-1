MyNumber = 0
MyString = "Sup!"
MyAge = 22
def on_forever():
    global MyNumber
    global MyString
    global MyAge   
    MyNumber = 10
    basic.show_number(MyNumber)
    MyNumber += 5
    basic.show_number(MyNumber)
    basic.show_string(MyString)
basic.forever(on_forever)
