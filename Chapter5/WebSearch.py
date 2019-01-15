from pydoc import html

import vsearch
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/search4', methods = ['POST'])  # indicates URL where this function will be invoked and methods that are allowed for this URL
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Results of your request'
    result = str(vsearch.search4letters(phrase, letters))  # gets arguments from html form. Form related with function via action attribute in form (it should be same as URL in function's decorator)
    return render_template('Results.html', the_title = title, the_phrase = phrase, the_letters = letters, the_results = result)  # renders template Result.html from the templates folder with
    # provided arguments


@app.route('/')
@app.route('/entry')
def landing_page() -> 'html':
    return render_template('Entry.html', the_title = 'WebsearchApp')


app.run(debug = True)
