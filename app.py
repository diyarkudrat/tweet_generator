# from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for
import os
from sampling import main_sample, prob_word, get_count, sentence
from histogram import histogram_dict, read_file



app = Flask(__name__)


@app.route('/')
def index():
    text_file = read_file('histo_sample_song.txt')
    histogram = histogram_dict(text_file)
    count = get_count(histogram_dict(text_file))
    total = len(text_file)

    ' '.join(sentence(count, total, histogram))
    return sentence(count, total, histogram)


if __name__ == '__main__':
    app.run(debug=True)
