from pydoc import html

import vsearch
from flask import Flask, render_template, request, escape

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    with open('websearch.log', 'a') as logFile:
        print(req.form, req.remote_addr, req.user_agent, res, file=logFile, sep='|')


@app.route('/search4', methods=['POST'])  # indicates URL where this function will be invoked and methods that are allowed for this URL
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Results of your request'
    # gets arguments from html form. Form related with function via action attribute in form (it should be same as URL in function's decorator)
    result = str(vsearch.search4letters(phrase, letters))
    # renders template Result.html from the templates folder with provided arguments
    log_request(request, result)
    return render_template('Results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=result)


@app.route('/viewlog')
def view_log() -> 'html':
    content = []
    with open('websearch.log') as log:
        for line in log:
            content.append([])
            for item in line.split('|'):
                content[-1].append(escape(item))
    return str(content)


@app.route('/')
@app.route('/entry')
def landing_page() -> 'html':
    return render_template('Entry.html', the_title='WebsearchApp')


if __name__ == '__main__':
    app.run(debug=True)
