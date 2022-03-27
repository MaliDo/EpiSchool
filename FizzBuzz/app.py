from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    title = "FizzBuzz"
    return render_template("main.html", title=title)


@app.route("/fizzbuzz/<int:count_to>")
def count(count_to):
    title = "FizzBuzz - Count"
    l1 = range(1, (count_to + 1))
    return render_template("fizzbuzz.html", title=title, l1=l1, count_to=count_to)
