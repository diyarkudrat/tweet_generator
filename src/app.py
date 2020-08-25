from flask import Flask, render_template, request, jsonify
import os
from second_order_markov_chain import MarkovChain, cleanup_text_file
from pymongo import MongoClient
from utils import cleanup

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/markov')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()

favorited = db.favorited
album_covers = db.album_covers



app = Flask(__name__)


words_list = cleanup_text_file('chance_lyrics.txt')
markov_chain = MarkovChain(words_list=words_list)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.args.get('favorite') is not None:
        favorited.insert_one(
                            {'sentence': markov_chain.sentence,
                            })

    length = 10
    if request.args.get('sentence length'):
        length = int(request.args.get('sentence length'))


    sentence = markov_chain.sentence_gen(length=length)

    favorited_list = favorited.find()

    return render_template('index.html', sentence=sentence, favorited=favorited_list)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
