import mysql.connector
import vsearch
from flask import Flask, escape, render_template, request

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    dbconfig = {
        "host": "127.0.0.1",
        "user": "websearch",
        "password": "search",
        "database": "vsearchlogdb"
    }

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()

    _sqlInsert = """insert into logs
    (phrase, letters, ip, user_agent, results)
    values
    (%s, %s, %s, %s, %s)"""

    cursor.execute(_sqlInsert, (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res))
    conn.commit()
    cursor.close()
    conn.close()


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
    titles = ('Form Data', 'IP', 'User agent', 'Result')
    content = []
    with open('websearch.log') as log:
        for line in log:
            content.append([])
            for item in line.split('|'):
                content[-1].append(escape(item))
    return render_template('ViewLog.html', the_title = 'Logging', the_row_titles = titles, the_data = content)


@app.route('/')
@app.route('/entry')
def landing_page() -> 'html':
    return render_template('Entry.html', the_title = 'WebsearchApp')


if __name__ == '__main__':
    app.run(debug = True)
