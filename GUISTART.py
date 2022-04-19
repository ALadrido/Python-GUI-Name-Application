from guizero import App, Text, TextBox, PushButton, Slider, Picture

def say_my_name():
    welcome_message.value = my_name.value

def change_text_size(slider_value):
    welcome_message.size = slider_value

#APPSTART
app = App(title = "Hello World")
welcome_message = Text(app, text = "Welcome!", font = "Comfortaa", size=30, color = "purple")
my_name = TextBox(app)
my_name.width = 35
update_text = PushButton(app, text = "Update", command = say_my_name)
text_size = Slider(app, command = change_text_size, start = 10, end = 100)
#my_turtle = Picture(app, image ="cat.png", height=320, width=285)


app.display()