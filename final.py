# Setup -- import Flask and giphypop
from flask import Flask, render_template, request
app = Flask(__name__)
import giphypop
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    try:
        gif = request.values.get('gif')
        g = giphypop.Giphy()
        results = g.search(gif)
        return render_template('results.html', gif=gif, results=results)
    except AssertionError:
        error = "Please try your search again."
        return render_template('index.html', error=error)

@app.route('/about')
def about():
    return render_template('about.html')

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)