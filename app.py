# from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for
import os
from second_order_markov_chain import MarkovChain
from pymongo import MongoClient

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/markov')
client = MongoClient(host=host)
db = client.get_default_database()

favorites = db.favorites


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    words_list = read_file('sample_book.txt')
    markov_chain = MarkovChain(words_list=words_list)

    length = 10
    if request.args.get('sentence length'):
        length = int(request.args.get('sentence_length'))

    if request.args.get('favorite') is not None:
        favorites.insert_one(
                {'sentence': markov_chain.sentence,
                 'likes': 0
                })


    sentence = markov_chain.sentence_gen(length=length)
    favorites_list = favorites.find()
    print(favorites_list)

    return render_template('index.html', sentence=sentence, favorites=favorites_list)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
