from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
   return """
   <!DOCTYPE html>
   <html lang="ru">
      <head>
          <meta charset="UTF-8">
          <title>Новостной сайт</title>
      </head>
      <body>
        <h1>Скоро тут будут новости</h1>
        <p>Следите за обновлениями</p>
      </body>
   </html>
   """


@app.route('/news')
def news():
   return 'Новости'


@app.route('/news_detail/<int:id>')
def news_detail(id):
   return f'Новость {id}'


@app.route('/category/<name>')
def category_detail(name):
   return f'Категория {name}'


if __name__ == '__main__':
   app.run(debug=True)