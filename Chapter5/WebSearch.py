import vsearch
from flask import Flask, render_template, request

from Chapter5.DBcm import UseDatabase

app = Flask(__name__)
app.config['dbconfigs'] = {
    "host": "127.0.0.1",
    "user": "websearch",
    "password": "search",
    "database": "vsearchlogdb"
}


def log_request(req: 'flask_request', res: str) -> None:
    _sqlInsert = """insert into logs
    (phrase, letters, ip, user_agent, results)
    values
    (%s, %s, %s, %s, %s)"""

    with UseDatabase(app.config['dbconfigs']) as cursor:
        cursor.execute(_sqlInsert, (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res))


@app.route('/search4', methods = ['POST'])  # indicates URL where this function will be invoked and methods that are allowed for this URL
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Results of your request'
    # gets arguments from html form. Form related with function via action attribute in form (it should be same as URL in function's decorator)
    result = str(vsearch.search4letters(phrase, letters))
    # renders template Result.html from the templates folder with provided arguments
    log_request(request, result)
    return render_template('Results.html', the_title = title, the_phrase = phrase, the_letters = letters, the_results = result)


@app.route('/viewlog')
def view_log() -> 'html':
    titles = ('Phrase', 'Letters', 'IP', 'User agent', 'Result')
    _sql_select = """select phrase, letters, ip, user_agent, results
                    from logs"""
    with UseDatabase(app.config['dbconfigs']) as cursor:
        cursor.execute(_sql_select)
        content = cursor.fetchall()
    return render_template('ViewLog.html', the_title = 'Logging', the_row_titles = titles, the_data = content)


@app.route('/')
@app.route('/entry')
def landing_page() -> 'html':
    return render_template('Entry.html', the_title = 'WebsearchApp')


if __name__ == '__main__':
    app.run(debug = True)
