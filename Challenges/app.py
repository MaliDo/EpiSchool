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
    l = []
    for item in word_list:
        if sorted(word.upper()) == sorted(item):
            l.append(item)
    return render_template("l_words.html", title=title, word_list=word_list, word=word, l=l)

@app.route("/words/dictionary/")
def dict():
    title = "Dictionary"
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return render_template("dict.html", title=title, alph=alph)

@app.route("/words/dictionary/<string:word>")
def dict_l(word):
    title = "Dictionary"
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    l = []
    f = open('words.txt')
    word_list = f.read().splitlines()
    is_real_word = word.upper() in word_list
    for i in alph:
        l.append(word + i)
    matching_words = []
    for x in word_list:
        y = str(x[0:len(word)])
        if str(word.upper()) == y:
            matching_words.append(x)
    # next_words = []
    # real_next_words = []
    # for z in l:
    #     for i in alph:
    #         next_words.append(z+i)
    # for n in next_words:
    #     for m in word_list:
    #         if str(n.upper()) == str(m[0:len(n)]):
    #             real_next_words.append(n)
    return render_template("dict_l.html", title=title, alph=alph, word=word, l=l, word_list=word_list, matching_words=matching_words, x=x, len=len, y=y, is_real_word=is_real_word, i=i)

    # next_words=next_words, real_next_words=real_next_words