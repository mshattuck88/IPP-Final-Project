# Setup -- import Flask and giphypop
from flask import Flask, render_template, request
app = Flask(__name__)
import giphypop

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    gif = request.values.get('gif')
    return render_template('results.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)