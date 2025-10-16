from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menu.db'
db = SQLAlchemy(app)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(50))

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)

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
    if Page.query.count() == 0:
        db.session.add_all([
            Page(url='/', title='Главная страница', content='<b>Добро пожаловать!</b>'),
            Page(url='/about', title='О нас', content='Здесь описание компании или проекта.'),
            Page(url='/contacts', title='Контакты', content='Телефон: 8-800-555-35-35<br>Почта: info@example.com')
        ])
        db.session.commit()

def render_page(url):
    menu = Menu.query.all()
    page = Page.query.filter_by(url=url).first()
    return render_template_string("""
        <h1>{{ page.title }}</h1>
        <div>{{ page.content|safe }}</div>
        <ul>
            {% for item in menu %}
            <li><a href="{{ item.url }}">{{ item.name }}</a></li>
            {% endfor %}
        </ul>
    """, menu=menu, page=page)

@app.route('/')
def home():
    return render_page('/')

@app.route('/about')
def about():
    return render_page('/about')

@app.route('/contacts')
def contacts():
    return render_page('/contacts')

if __name__ == "__main__":
    app.run(debug=True)
