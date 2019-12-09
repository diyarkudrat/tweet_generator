# from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for
import os
from sampling import main_sample, prob_word, get_count, sentence
from markov_chain import MarkovChain
from histogram import histogram_dict, read_file
from pymongo import MongoClient

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/csmarkov')

client = MongoClient(host=host)
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()


app = Flask(__name__)


@app.route('/')
def index():
    words_list = read_file('sample_book.txt')

    markov_chain = MarkovChain(words_list=words_list)


    # ' '.join(sentence(count, total, histogram))
    return markov_chain.sentence_gen()
    return render_template('index.html', markov_chain=markov_chain)


if __name__ == '__main__':
    app.run(debug=True)
