# from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for
import os
from sampling import main_sample, prob_word, get_count, sentence
from histogram import histogram_dict


app = Flask(__name__)


@app.route('/')
def index():
    text_file = 'fish.txt'
    histogram = histogram_dict(text_file)
    count = get_count(histogram)

    words_from_text = read_file('fish.txt')
    total = len(words_from_text)

    print(sentence(histogram, count, total))



if __name__ == '__main__':
    app.run(debug=True)
