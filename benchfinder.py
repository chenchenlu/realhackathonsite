from flask import Flask, redirect, url_for, render_template, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import folium
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

start_coords = [42.4453,-76.482661]
fg=folium.Map(location=start_coords, zoom_start=17)

for lt,ln,nm,ws in zip(LAT,LON,name,directions):
 	fg.add_child(folium.Marker(location=[lt,ln],popup="<b>Name  : </b>"+nm + "<br><b>Directions: </b><a href="+ws+">click here</a>",icon=folium.Icon(color='green')))

class ReusableForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Submit')

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