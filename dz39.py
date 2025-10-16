from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menu.db'
db = SQLAlchemy(app)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(50))

# Первый запуск: создать базу и заполнить меню
@app.before_first_request
def setup():
    db.create_all()
    if Menu.query.count() == 0:
        db.session.add_all([
            Menu(name='Главная', url='/'),
            Menu(name='О нас', url='/about'),
            Menu(name='Контакты', url='/contacts')
        ])
        db.session.commit()

@app.route('/')
def home():
    menu = Menu.query.all()
    return render_template_string("""
        <h1>Главная страница</h1>
        <ul>
            {% for item in menu %}
            <li><a href="{{ item.url }}">{{ item.name }}</a></li>
            {% endfor %}
        </ul>
        """, menu=menu)

@app.route('/about')
def about():
    menu = Menu.query.all()
    return render_template_string("""
        <h1>О нас</h1>
        <ul>
            {% for item in menu %}
            <li><a href="{{ item.url }}">{{ item.name }}</a></li>
            {% endfor %}
        </ul>
        """, menu=menu)

@app.route('/contacts')
def contacts():
    menu = Menu.query.all()
    return render_template_string("""
        <h1>Контакты</h1>
        <ul>
            {% for item in menu %}
            <li><a href="{{ item.url }}">{{ item.name }}</a></li>
            {% endfor %}
        </ul>
        """, menu=menu)

if __name__ == "__main__":
    app.run(debug=True)
