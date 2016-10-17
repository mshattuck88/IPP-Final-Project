# Setup -- import Flask and giphypop
from flask import Flask, render_template, request
app = Flask(__name__)
import giphypop

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    g = giphypop.Giphy()
    gif = request.values.get('gif')
    results = g.search(gif)
    for result in results:
        media_url = result.media_url
        result_url = result.url
    return render_template('results.html', gif=gif, results=results, media_url=media_url, result_url=result_url)

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)