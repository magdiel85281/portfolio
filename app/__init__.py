from flask import Flask, render_template, request, url_for, redirect, flash, session
from datetime import datetime
from content_management import Content
from dbconnect import connection
from wtforms import Form, TextField, validators
import gc
import secrets
# from mysql import escape_string as thwart

app = Flask(__name__)
TOPIC_DICT = Content()

sec = secrets.token_urlsafe(32)
app.secret_key = sec


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


class RegistrationForm(Form):
    contact_name = TextField('Name', [validators.Length(min=4, max=50)])
    email = TextField('Email Address', [validators.Length(min=6, max=50)])
    message = TextField('Message', [validators.Length(max=1200)])


@app.route('/contact_1/', methods=['GET', 'POST'])
def contact_page():
    try:
        form = RegistrationForm(request.form)

        if request.method == 'POST' and form.validate():
            contact_name = form.contact_name.data
            email = form.email.data
            message = form.message.data
            tstamp = datetime.now()

            c, conn = connection()
            c.execute("INSERT INTO contacts (name, email, message, date) VALUES (%s, %s, %s, %s)", 
                (contact_name, email, message, tstamp))
            conn.commit()

            flash('Message submitted!')
            c.close()
            conn.close()

            gc.collect()

            session['logged_in'] = True
            session['contact_name'] = contact_name

            return redirect(url_for('dashboard'))

        return render_template('send_message.html', form=form)

    except Exception as e:
        return (str(e))


@app.route('/contact/', methods=['POST'])
def contact():
    contact_name = request.form['ContactName']
    contact_email = request.form['ContactEmail']
    contact_message = request.form['ContactMessage']
    tstamp = datetime.now()

    print(contact_name, contact_email, contact_message)

    c, conn = connection()
    c.execute("INSERT INTO contacts (name, email, message, date) VALUES (%s, %s, %s, %s)", 
        (contact_name, contact_email, contact_message, tstamp))
    conn.commit()
    
    c.close()
    conn.close()
    gc.collect()

    flash('Message submitted!')
    return render_template('main.html')

if __name__ == '__main__':
    app.run()

    # debug mode
    # app.run(host='0.0.0.0', port=5000, debug=True)