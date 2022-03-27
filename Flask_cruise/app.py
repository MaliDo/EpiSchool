from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    title = "Welcome aboard!"
    
    text = """It is a wonderful day to start your cruise. Now choose your suite!"""

    choices = [
        ('first_class',"1st Class"),
        ('second_class',"2nd Class")
    ]

    return render_template('home.html', title=title, text=text, choices=choices)

@app.route("/first_class")
def first_class():
    title = "First class cabin"
    
    text = """Do you want a window in your cabin?"""

    choices = [
        ('completed',"Yes (Outside)"),
        ('completed',"No (Inside)")
    ]

    return render_template('first_class.html', title=title, text=text, choices=choices)

@app.route("/second_class")
def second_class():
    title = "Second class cabin"
    
    text = """Do you want a window in your cabin?"""

    choices = [
        ('completed',"Yes (Outside)"),
        ('completed',"No (Inside)")
    ]

    return render_template('second_class.html', title=title, text=text, choices=choices)

@app.route("/completed")
def completed():
    title = "Booking completed!"
    
    text = """Thank you for your choice!"""

    return render_template('completed.html', title=title, text=text)