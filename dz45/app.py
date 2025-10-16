from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    task = "Домашнее задание выполнено!!!"
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Домашнее задание</title>
    </head>
    <body>
        <h1>Страница с домашним заданием</h1>
        <p>{{ message }}</p>
    </body>
    </html>
    """, message=task)

if __name__ == "__main__":
    app.run(debug=True)
