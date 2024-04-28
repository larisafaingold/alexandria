#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, TextAreaField

app = Flask(__name__)

class ConfigForm(Form):
    config = TextAreaField('Config')

@app.route('/', methods=['GET', 'POST'])
def home():

    form = ConfigForm(request.form)

    if request.method == 'POST' and form.validate():
        config = form.config.data

        return(redirect(url_for('home')))

    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)