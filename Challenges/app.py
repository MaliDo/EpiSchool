from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    title = "Challenges"
    return render_template("home.html", title=title)

@app.route("/fizzbuzz/")
def fizzbuzz():
    title = "FizzBuzz"
    return render_template("fizzbuzz.html", title=title)

@app.route("/fizzbuzz/<int:count_to>")
def count(count_to):
    title = "FizzBuzz - Count"
    l1 = range(1, (count_to + 1))
    return render_template("fizzbuzz_count.html", title=title, l1=l1, count_to=count_to)

@app.route("/words/")
def words():
    title = "Words"
    return render_template("words.html", title=title)

@app.route("/words/<string:word>")
def l_words(word):
    title = "Words - List"
    f = open('words.txt')
    word_list = f.read().splitlines()
    return render_template("l_words.html", title=title, word_list=word_list, word=word, list=list, sorted=sorted, len=len, set=set)