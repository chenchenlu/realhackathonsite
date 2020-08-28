from flask import Flask, redirect, url_for, render_template, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

from flask_wtf import FlaskForm

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'whatthefrick'


class ReusableForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=['GET', 'POST'])
def send():
    # dropdown_list = ['The Slope Benches','Class of 1927 Bench']
    form= ReusableForm()
    if form.validate_on_submit:
        return render_template('persons.html',form=form)
    return render_template("index.html",form=form)

@app.route("/testsignup")
def signup():
    form= ReusableForm()
    return render_template("testsignup.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)