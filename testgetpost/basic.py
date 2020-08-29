from flask import *
from formtest import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

@app.route('/signup')
def basic():
    form = SignUpForm()
    return render_template("def.html")

if __name__ == '__main__':
    app.debug = True
    app.run()