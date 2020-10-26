from flask import Flask, render_template
from content_management import Content


app = Flask(__name__)
TOPIC_DICT = Content()


@app.route('/')
def homepage():
    return render_template('main.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html', TOPIC_DICT=TOPIC_DICT)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.route('/fake/')
def fakeit():
    try:
        return render_template('dashboard.html', TOPIC_DICT=gibberish)
    except Exception as e:
        return render_template('500.html', error=e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
