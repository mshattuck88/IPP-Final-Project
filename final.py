# Setup -- import Flask and giphypop
from flask import Flask, render_template, request
app = Flask(__name__)
import giphypop
import os

# Set up an index page
@app.route('/')
def index():
    return render_template('index.html')

# Set up a results page that will use giphypop to find requested gifs and display error message if no gif is requested
@app.route('/results')
def results():
    try:
        gif = request.values.get('gif')
        g = giphypop.Giphy()
        results = g.search(gif)
        if len(list(results)) > 0:
            git = request.values.get('gif')
            g = giphypop.Giphy()
            results = g.search(gif)
            return render_template('results.html', gif=gif, results=results)
        else:
            error = "No results found. Please try your search again."
            return render_template('index.html', error=error)
    except AssertionError:
        error = "No search term. Please try your search again."
        return render_template('index.html', error=error)

# Set up an about page
@app.route('/about')
def about():
    return render_template('about.html')

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
