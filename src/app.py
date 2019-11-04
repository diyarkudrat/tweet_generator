from flask import Flask
# from histogram import histogram_dict
from sampling import main_sample, prob_word, get_count
from histogram import histogram_dict


app = Flask(__name__)


@app.route('/')
def index():
    text_file = 'fish.txt'
    histogram = histogram_dict(text_file)
    count = get_count(histogram_dict(text_file))

    return prob_word(histogram, count)


if __name__ == '__main__':
    app.run(debug=True)
