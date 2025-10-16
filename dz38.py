from flask import Flask, render_template_string

app = Flask(__name__)

menu = {
    'Главная': '/',
    'О нас': '/about',
    'Контакты': '/contacts'
}

@app.route('/')
def home():
    return render_template_string("""
    <h1>Главная страница</h1>
    <ul>
        {% for name, url in menu.items() %}
        <li><a href="{{ url }}">{{ name }}</a></li>
        {% endfor %}
    </ul>
    """, menu=menu)

@app.route('/about')
def about():
    return render_template_string("""
    <h1>О нас</h1>
    <p>Здесь описание компании или проекта.</p>
    <ul>
        {% for name, url in menu.items() %}
        <li><a href="{{ url }}">{{ name }}</a></li>
        {% endfor %}
    </ul>
    """, menu=menu)

@app.route('/contacts')
def contacts():
    return render_template_string("""
    <h1>Контакты</h1>
    <p>Телефон: 8-800-555-35-35<br>Почта: info@example.com</p>
    <ul>
        {% for name, url in menu.items() %}
        <li><a href="{{ url }}">{{ name }}</a></li>
        {% endfor %}
    </ul>
    """, menu=menu)

if __name__ == "__main__":
    app.run(debug=True)
