import math

import vsearch
from flask import Flask, redirect, render_template, request, session

import Chapter10.checkerDecorator as check
from Chapter5.DBcm import UseDatabase

app = Flask(__name__)
app.config['dbconfigs'] = {
    "host": "127.0.0.1",
    "user": "websearch",
    "password": "search",
    "database": "vsearchlogdb"
}


def get_hash(val: str) -> str:
    """Creates a custom hash for provided value"""
    return ''.join(sorted(str(int(math.fabs(len(val) * 24))) + 'KBpy2CAeCiVYRt9Q8qyN'))


@app.route('/register', methods = ['POST', 'GET'])
def reg() -> 'html':
    title = 'Sign Up'
    return render_template('Register.html', the_title = title)


@app.route('/createAnotherAsshole', methods = ['POST', 'GET'])
def create_account():
    username = request.form['username']
    pass_hash = get_hash(request.form['password'])

    _sql_register = """insert into users 
                        (username, password_hash)
                        values
                        (%s, %s)"""

    _sql_check_user = """select username
                            from users
                            where username = '%s'"""

    with UseDatabase(app.config['dbconfigs']) as cursor:
        cursor.execute(_sql_check_user, username)
        is_user_exists = cursor.fetchall()
        if is_user_exists.count() > 0:
            cursor.execute(_sql_register, username, pass_hash)

    return redirect('/login')


@app.route('/')
@app.route('/login')
def do_login() -> 'html':
    title = 'Sign In'
    if 'logged_in' not in session:
        return render_template('Login.html', the_title = title)
    return redirect('/search4')


@app.route('/sendFuckingForm', methods = ['POST', 'GET'])
def auth():
    username = request.form['username']
    pass_hash = get_hash(request.form['password'])

    _sql_authenticate = """select username
                    from users
                    where username = '%s' AND password_hash = '%s'"""
    with UseDatabase(app.config['dbconfigs']) as cursor:
        cursor.execute(_sql_authenticate, username, pass_hash)
        print(username)
        print(pass_hash)
        print(cursor.fetchone())
        print(cursor.fetchone() == username)
        is_authenticate = cursor.fetchone() == username

    if is_authenticate:
        session['logged_in'] = True
        return redirect('/search4')
    return redirect('/register')


@app.route('/entry')
def landing_page() -> 'html':
    return render_template('Entry.html', the_title = 'WebsearchApp')


@app.route('/logout')  # how this function can be invoked from browser
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


def log_request(req: 'flask_request', res: str) -> None:
    _sqlInsert = """insert into logs
    (phrase, letters, ip, user_agent, results)
    values
    (%s, %s, %s, %s, %s)"""

    with UseDatabase(app.config['dbconfigs']) as cursor:
        cursor.execute(_sqlInsert, (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res))  # such way of execute SQL queries should be safe enough to avoid SQL
        # injections


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
@check.check_logged_in
def view_log() -> 'html':
    titles = ('Phrase', 'Letters', 'IP', 'User agent', 'Result')
    _sql_select = """select phrase, letters, ip, user_agent, results
                    from logs"""
    with UseDatabase(app.config['dbconfigs']) as cursor:
        cursor.execute(_sql_select)
        content = cursor.fetchall()
    return render_template('ViewLog.html', the_title = 'Logging', the_row_titles = titles, the_data = content)


if __name__ == '__main__':
    app.run(debug = True)
