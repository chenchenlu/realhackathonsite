from flask import Flask, redirect, url_for, render_template, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField
import folium
import collections
import pandas
from flask_wtf import FlaskForm
#lol ok this is creative
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'whatthefrick'
data=pandas.read_csv('Benches_Coordinates.csv')
#okay
LAT=list(data['Latitude'])
LON=list(data['Longitude'])
name=list(data['Name'])
directions=list(data['Directions'])
LIST_BENCHES=name
url = 'https://photos.app.goo.gl/vAkBHxzFRJ9WG7W18'
iconBench= folium.features.CustomIcon(url, icon_size=(50,50))

start_coords = [42.4453,-76.482661]
fg=folium.Map(location=start_coords, zoom_start=17)


for lt,ln,nm,ws in zip(LAT,LON,name,directions):
 	fg.add_child(folium.Marker(location=[lt,ln],popup="<b>Name  : </b>"+nm + "<br><b>Directions: </b><a href="+ws+">click here</a>",icon=iconBench))

class ReusableForm(FlaskForm):
    username = StringField('Number of People Going')
    submit = SubmitField('Submit')
    benches = SelectField(label='Benches', choices=[(bench, bench) for bench in LIST_BENCHES])

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/')
def index():
    return fg._repr_html_()


@app.route('/density')
def density():
    return render_template("density.html")

@app.route('/cumap')
def mapdisplay():
    return fg._repr_html_()

@app.route('/send', methods=['GET', 'POST'])
def send():
    form= ReusableForm()

    if form.validate_on_submit():
         return "<h2> Persons going: {0} {1}".format(form.username.data, form.benches.data)
    return render_template("persons.html",form=form)

@app.route("/testsignup")
def signup():
    form= ReusableForm()
    return render_template("testsignup.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)