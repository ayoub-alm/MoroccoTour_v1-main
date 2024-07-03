from flask import Flask, render_template

from models import storage
from models.cities import City
from models.places import Place

app = Flask(__name__,
            static_folder='web_dynamic/static',
            template_folder='web_dynamic/templates')


@app.route('/')
def index():
    cities = storage.all(City).values()
    places = storage.all(Place).values()
    return render_template('index.html', cities=cities, places=places)


@app.route('/show-destination')
def show():
    return render_template('show-destination.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/landing-page')
def landing_page():
    return render_template('landing_page.html')


if __name__ == '__main__':
    app.run(debug=True)
