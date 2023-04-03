from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Главная страница"


@app.route('/news')
def news():
    return 'Новости'


@app.route('/news_detail/1')
def new_detail1():
    return "Новость1"


@app.route('/news_detail/2')
def new_detail2():
    return "Новость2"


if __name__ == '__main__':
    app.run(debug=True)
