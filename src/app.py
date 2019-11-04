from flask import Flask
# from histogram import histogram_dict
from sampling import main_sample, prob_word, get_count
from histogram import histogram_dict


app = Flask(__name__)


@app.route('/')
def index():
    text_file = 'fish.txt'
    return prob_word(histogram_dict(text_file), get_count(histogram_dict(text_file)))


if __name__ == '__main__':
    app.run(debug=True)
